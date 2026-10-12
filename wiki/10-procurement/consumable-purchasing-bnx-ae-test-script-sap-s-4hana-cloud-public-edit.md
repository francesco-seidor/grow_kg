---
id: 10-procurement/consumable-purchasing-bnx-ae-test-script-sap-s-4hana-cloud-public-edit
title: Consumable Purchasing (BNX_AE) Test Script - SAP S/4HANA Cloud Public Edition (BNX_S4CLD2608_BPD_EN_AE)
description: "SAP test script for scope item BNX_AE (Consumable Purchasing, UAE): PR, PO, approval, goods receipt, supplier invoice, invoicing plan, retention; release 2608."
cluster: 10-procurement
tags: [kb/procurement, topic/requisitioning-and-consumable-purchasing]
aliases: [BNX_S4CLD2608_BPD_EN_AE]
keywords: [Requisitioning and Consumable Purchasing, consumable purchasing, purchase requisition, purchase order, purchase order approval, flexible workflow, goods receipt, supplier invoice, multiple account assignment, invoicing plan]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BNX_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1294
topic: 10-procurement/requisitioning-and-consumable-purchasing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Consumable Purchasing (BNX_AE) Test Script - SAP S/4HANA Cloud Public Edition (BNX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BNX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Requisitioning and Consumable Purchasing** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Consumable Purchasing (BNX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862539)

[2 Prerequisites 4](#_Toc232862540)

[2.1 Additional Manual Configuration 4](#_Toc232862541)

[2.2 System Access 4](#_Toc232862542)

[2.3 Roles 4](#_Toc232862543)

[2.4 Master Data and Organizational Data 5](#_Toc232862544)

[2.5 Business Conditions 6](#_Toc232862545)

[2.6 Preliminary Steps 7](#_Toc232862546)

[2.6.1 Activate Flexible Workflow for Purchase Order 7](#_Toc232862547)

[2.6.1.1 Check Flexible Workflow for Purchase Order Approval 7](#_Toc232862548)

[2.6.1.2 Configure Flexible Workflow for Purchase Order 8](#_Toc232862549)

[2.6.2 Create Purchasing Info Record (Optional) 9](#_Toc232862550)

[2.6.3 Activate Flexible Workflow for Supplier Invoice 12](#_Toc232862551)

[2.6.3.1 Activate Flexible Workflow for Supplier Invoice 12](#_Toc232862552)

[2.6.3.2 Check Workflow for Supplier Invoice 14](#_Toc232862553)

[2.6.3.3 Update Cost Center for User Responsible 14](#_Toc232862554)

[2.6.3.4 Update Profit Center for User Responsible 15](#_Toc232862555)

[2.6.4 Edit User-Specific Parameters for Supplier Invoices (Optional) 16](#_Toc232862556)

[2.6.5 Create Purchase Contract 17](#_Toc232862557)

[2.6.6 Maintain Retention Scenario in PO 18](#_Toc232862558)

[3 Overview Table 21](#_Toc232862559)

[4 Test Procedures 23](#_Toc232862560)

[4.1 Create Purchase Requisition 23](#_Toc232862561)

[4.2 Convert Purchase Requisition to Purchase Order 26](#_Toc232862562)

[4.3 Create Purchase Order 27](#_Toc232862563)

[4.4 Execute Mass Changes to Purchase Orders (Optional) 29](#_Toc232862564)

[4.5 Redistribute Workload (Optional) 31](#_Toc232862565)

[4.6 Change Purchase Order (Optional) 32](#_Toc232862566)

[4.7 Approve Purchase Order (Optional) 33](#_Toc232862567)

[4.8 Monitor Purchase Order Items (Optional) 34](#_Toc232862568)

[4.9 Post Goods Receipt 35](#_Toc232862569)

[4.10 Preview Goods Receipt Slip (Optional) 36](#_Toc232862570)

[4.11 Monitor Purchase Order Items by Account Assignment (Optional) 37](#_Toc232862571)

[4.12 Create Supplier Invoice 38](#_Toc232862572)

[4.12.1 Option A: Create Supplier Invoice with PO/GR relation 39](#_Toc232862573)

[4.12.2 Option A: Release Completed Supplier Invoice (Optional) 41](#_Toc232862574)

[4.12.3 Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction) (Optional) 43](#_Toc232862575)

[4.12.4 Option B: Print Complaint Letter in case of Invoice Reduction (Only relevant for SAP S/4HANA Cloud Public Edition) 45](#_Toc232862576)

[4.13 Release Blocked Supplier Invoice (Optional) 46](#_Toc232862577)

[4.14 Multiple Account Assignment for consumable purchasing 46](#_Toc232862578)

[4.14.1 Create Purchase Order 46](#_Toc232862579)

[4.14.2 Post Goods Receipt 48](#_Toc232862580)

[4.14.3 Create Supplier Invoice 49](#_Toc232862581)

[4.15 Invoicing Plan for Consumable Purchasing 51](#_Toc232862582)

[4.15.1 Create Purchase Order for Invoicing Plan 51](#_Toc232862583)

[4.15.2 Create Invoice Plan Settlement 53](#_Toc232862584)

[4.16 Update Invoicing Plans (Optional) 54](#_Toc232862585)

[4.17 Retention Scenario in PO 55](#_Toc232862586)

[5 Appendix 61](#_Toc232862587)

[5.1 Process Integration 61](#_Toc232862588)

[5.2 Succeeding Processes 61](#_Toc232862589)

[5.3 Setup Mail Notification for Supplier Invoice Workflow 61](#_Toc232862590)

[5.4 Setup Mail Notification for Supplier Invoice Workflow with Factory Calendar 63](#_Toc232862591)

[5.5 Retention Process 64](#_Toc232862592)

[5.5.1 Prerequisites 64](#_Toc232862593)

[5.5.2 Create Purchase Order with Retention 64](#_Toc232862594)

[5.5.3 Post Goods Receipt 65](#_Toc232862595)

[5.5.4 Create Supplier Invoice 66](#_Toc232862596)

## Purpose

Overview

This scope item contains the creation and approval of purchase orders for consumables. Alternatively, the process can also be triggered via a purchase requisition, which can then be converted to a purchase order. Subsequently, the goods receipt and invoice processes are triggered.

Both standard and limit items can be procured with this scope item. As the value of the consumable goods is directly expended to an account assignment category, no inventory is provided.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a82f9de36679cf6b7f175a7ad0c837d5)

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT | Divisional Accounting | SAP_BR_DIVISION_ACCOUNTANT |  |

### Master Data and Organizational Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Production Plant 3310 |  |
| Supplier | 33300001 | Consumable material supplierNote To send form print outs by e-mail instead of using the print functionality, ensure that you have maintained a valid e-mail address in the vendor master data. |  |
| Purchase organization | 3310 | Purch. Org. 3310 |  |
| Material | NS0001 | Note You can use material with or without material numbers for purchase. |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Activate Flexible Workflow for Purchase Order

##### Check Flexible Workflow for Purchase Order Approval

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

##### Configure Flexible Workflow for Purchase Order

Pupose

In this procedure, you configure your release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make the following entries:Name: Test Workflow for Purchase OrderSelect Start Conditions, and in the Start Conditions area, make the following entries:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10 ,Currency: AED .In the Steps area, choose Create and make the following entries:Step Type : Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER )Step to be completed by： One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Create Purchasing Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If the info record for the material and supplier mentioned in this step already exists in the system, you can skip this step. Otherwise, complete the following procedure for each material mentioned below. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Organization: 3310Purchasing Info Record Category: StandardSupplier: 33300001Material: NS0001Plant: 3310Purchasing Group: 001Material Group: YBMM01 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: Vendor Location | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 1Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 10Pricing Unit: 1Unit of Measure: PCCurrency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create your data | Choose Create. | The purchasing info record is created. |  |

#### Activate Flexible Workflow for Supplier Invoice

##### Activate Flexible Workflow for Supplier Invoice

Context

In this procedure, you activate flexible workflow for supplier invoice.

If you want to use the flexible workflow to approve the supplier invoice, you have to process the step: Activate Flexible Workflow for Supplier Invoice.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Supplier Invoice, choose configuration with name Incoming Invoice from search result, then choose Configure on the right of configuration steps with name Activate Flexible Workflow for Supplier Invoices. | The Change View "Activate Flexible Workflow for Supplier Invoices": Detail screen displays. |  |
| 5 | Active Flexible Workflow for Supplier Invoices | Select checkbox Payment Block: Flexible Workflow is Active,Select checkbox Release Completed Invoice: Flexible Workflow is ActiveSelect checkbox Check Authorizations for Flexible Workflow Steps (Optional)Choose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Supplier Invoices.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Activate Flexible Workflow for Supplier Invoices": Detail screen displays. |  |
| 3 | Active Flexible Workflow for Supplier Invoices | Select checkbox Payment Block: Flexible Workflow is Active,Select checkbox Release Completed Invoice: Flexible Workflow is ActiveSelect checkbox Check Authorizations for Flexible Workflow Steps (Optional)Choose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |  |

Result

The Scenario based workflow is activated for Supplier Invoices.

##### Check Workflow for Supplier Invoice

Purpose

In this procedure, you make sure Workflow for Supplier Invoice is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Workflows for Supplier Invoices (F2873). | The Manage Workflows screen displays. |  |
| 3 | Check Workflow for Parked Invoice as Complete | In Workflows dropdown list, choose Workflow for Parked Invoice as Complete, make sure workflow Release completed invoice is in active status. If not, select it and choose Activate.Note Choose the line and go to the Workflow Details screen. Go to the Step Sequence tab, and check the column Recipients in Step Sequence defines the user who handles invoice in the particular step, for example Creator of Purchase Order, cost center responsible or profit center responsible. If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to business role of the user. This action is also required for other invoice workflow. | The Workflow Item is activated. |  |
| 4 | Check Workflow for Blocked Invoice | In Workflows dropdown list, choose Workflow for Blocked Invoice, make sure workflow Release blocked Invoice by Accounting Responsibles is in active status. If not, select it and choose Activate. | The Workflow Item is activated. |  |

##### Update Cost Center for User Responsible

Purpose

In this procedure, you configure your release conditions for Invoice Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Cost Centers - Old Version (F1443A) | The Manage Cost Centers screen is displayed. |  |
| 3 | Filter Cost Center | Cost Center: e.g. 33101101Choose Go, select cost center in search results by clicking on the chevron > then choose Edit. | Cost Center detail information screen is displayed. |  |
| 4 | Input User Responsible | In General Information section,User Responsible: Select from F4. For example, search short description for purchasing_manager to get the user ID.Person Responsible: For example purchasing_manager |  |  |
| 5 | Save Data | Choose Save. | Cost center is saved. |  |

##### Update Profit Center for User Responsible

Purpose

If precondition Account assignment category Profit Center is used in workflow, you need to update your profit center user responsible for Invoice workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Profit Centers - Old Version (F3516). | The Manage Profit Centers screen is displayed. |  |
| 3 | Filter Profit Center | On Manage Profit Centers screen, input Profit CenterYB600Choose Go, select profit center in search results by clicking on the chevron >, then choose Edit. | Profit center detail information screen is displayed. |  |
| 4 | Input User Responsible | In General tab,User Responsible: Select from F4. For example: search short description for *purchasing_manager* to get the user ID.Responsible Person: For example Purchasing_Manager |  |  |
| 5 | Save Data | Choose Save. | Profit center is saved. |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Edit Supplier Invoice Settings (F3813) | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice, it will take effective immediately. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

#### Create Purchase Contract

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Enter Contract Header and General Information | Choose Create and make the following entries:Contract Type: Choose CMK Qty Contract-PSEValid From: Start date of the contractValid To: Today + 12 monthsPurchasing Organization: For example, 3310Purchasing Group: For example, 001Company Code: 3310Supplier: 33300001 |  |  |
| 4 | Enter Contract Item details | In the Item tab, choose Create and and choose > to go to Purchase Contract Item screen. Make the following entries:Account Assignment Category: UMaterial: NS0001Plant: For example, 3310Enter the following values in Quantity and Price section:Target Quantity: <Enter total quantity 50000 PC>Net price: <10>AEDper PCChoose Apply. |  |  |
| 5 | Create Contract | Choose Create. | The purchase contract is created. |  |

#### Maintain Retention Scenario in PO

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Set Local Version | Choose Set Local Version.In the Set Local Version dialog box, select United Arab Emirates (AE) from the dropdown list and choose Set Local Version. | The country/region version is set to United Arab Emirates. |  |
| 4 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 5 | Assign Special G/L account to Recon Account | Search SSCUI 100297 and open | The app opens. |  |
| 6 | Maintain seletion criteria | Maintain selection criteria as following.Area = Fincial AccountingSubarea = Accounts Receivable and Accounts PayableProcess: Define Alternative Reconciliation Accounts for Special G/L TransactionsChart of Acccounts = YCOAChoose Step 2 then maintain selection parameters as following.Account Type = K (Vendors)Special G/L = H |  |  |
| 7 | Configure | Choose "step 3" then: In Account Assignments section, assign Special G/L account to Recon Account.Choose Add and then enter the corresponding account number.For example,Recon. Acct : 21100000Special G/L account : 21200000Choose Review.Choose Save then confirm the configure setting. | New entry is created. |  |
| 8 | Set tax reduction in original document | Search SSCUI 103276 and open | The app opens. |  |
| 9 | Configure | Choose Position. Enter the Company Code = 3310.Choose the entry 1 Tax reduction in original document from the dropdown for field Tax for invoice reduction.Choose Save. | Existing entry is modified. |  |
| 10 | Set tax code with reduction | Search SSCUI 105912 and open | The app opens. |  |
| 11 | Configure | Enter Country/Region Key = AE.Choose New Entries then enter the following:For example,VAT: V2Tax Reduct: X (Selected)Choose Save. | New entry is created. |  |
| 12 | Assign Procedure Type and Tax Code to Compmay Code | Search SSCUI 104113 and open. | The app opens. |  |
| 13 | Configure | Choose New Entries then enter the following:For example,Company Code : 3310Procedure Type : RT RetentionTax Code : V2Choose Save. | New entry is created. |  |
| 14 | Log on | Log on to the SAP Fiori launchpad as a GL_ACCOUNTANT. |  |  |
| 15 | Access App | Open app Manage G/L Account Master Data | The app opens. |  |
| 16 | Maintain Tax Category for G/L account | Maintain selection criteria.For example,Company Code : 3310G/L account : 21720200In Control Data tab, enter * in Tax Category field.Posting Without Tax Allowed: Selected | Data saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | APP | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition](#unique_21) [page ] 23 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Manage Purchase Requisitions Professional: initial screen appears. |
| [Convert Purchase Requisition to Purchase Order](#unique_22) [page ] 26 | Purchaser | Process Purchase Requisitions (F1048A) | A list of Requisitions is displayed. |
| [Create Purchase Order](#unique_23) [page ] 27 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order for consumable material is created. |
| [Execute Mass Changes to Purchase Orders (Optional)](#unique_24) [page ] 29 | Purchaser | Mass Changes to Purchase Orders (F2593) | Purchase Order can be changed in bulk. |
| [Redistribute Workload (Optional)](#unique_25) [page ] 31 | Purchaser | Redistribute Workload (F2504) | Purchase Order for purchase group is changed. |
| [Change Purchase Order (Optional)](#unique_26) [page ] 32 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order for consumable material is changed. |
| [Approve Purchase Order (Optional)](#unique_27) [page ] 33 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase Order for consumable material is approved |
| [Monitor Purchase Order Items (Optional)](#unique_28) [page ] 34 | Purchaser | Monitor Purchase Order Items (F2358) |  |
| [Post Goods Receipt](#unique_29) [page ] 35 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipts are posted |
| [Preview Goods Receipt Slip (Optional)](#unique_30) [page ] 36 | Warehouse Clerk | Material Documents Overview (F1077) | A Good Receipt Slip is created in a PDF format |
| [Monitor Purchase Order Items by Account Assignment (Optional)](#unique_31) [page ] 37 | Accounts Payable Accountant | Purchase Order Items by Account Assignment (F2420) |  |
| [Create Supplier Invoice](#unique_32) [page ] 38 |  |  |  |
| [Option A: Create Supplier Invoice with PO/GR relation](#unique_33) [page ] 39 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is posted |
| [Option A: Release Completed Supplier Invoice (Optional)](#unique_34) [page ] 41 | Purchasing Manager | My Inbox - All Items (F0862) | The invoice is released. |
| [Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction) (Optional)](#unique_35) [page ] 43 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is posted |
| [Option B: Print Complaint Letter in case of Invoice Reduction (Only relevant for SAP S/4HANA Cloud Public Edition)](#unique_36) [page ] 45 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Complaint letter is printed |
| [Release Blocked Supplier Invoice (Optional)](#unique_37) [page ] 46 | Purchasing Manager | My Inbox - All Items (F0862) | The invoice is released. |
| Multiple Account Assignment for consumable purchasing |  |  |  |
| [Create Purchase Order](#unique_38) [page ] 46 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order with the multiple account assignment is created. |
| [Post Goods Receipt](#unique_39) [page ] 48 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipts are posted |
| [Create Supplier Invoice](#unique_40) [page ] 49 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is created |
| Invoicing Plan for Consumable Purchasing |  |  |  |
| [Create Purchase Order for Invoicing Plan](#unique_41) [page ] 51 | Purchaser | Create Purchase Order - Advanced (ME21N) | The Create Purchase Order screen is displayed. |
| [Create Invoice Plan Settlement](#unique_42) [page ] 53 | Accounts Payable Accountant | Create Invoicing Plan Settlement (MRIS) | The Create Supplier Invoices screen is displayed. |

## Test Procedures

### Create Purchase Requisition

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229) . | The Manage Purchase Requisitions Professional: initial screen appears. |  |
| 3 | Create New Purchase Requisition | Choose Create. | The Purchase Requisition screen appears. |  |
| 4 | Enter Document Type | Enter Document Type: Pur. Requisition (NB).Choose Automatic Source Determination. |  |  |
| 5 | Case 1: Purchase with Material Master | In the Items section, choose Create then choose Material to add new items to Purchase RequisitionsEnter the following values in General Information section:Item Category: StandardMaterial: NS0001Plant: 3310Account Assignment Category: K (Cost Center)Note Account Assignment Category P for account assignments to projects is also supported. In case budget availability control for a project is active you may run into warning / error messages along the requisition process in case budget thresholds are exceeded. For further details on the budget availability control for projects you can refer to (1NT) - Project Financial Control test script (component responsible: PPM-CNT).Enter the following values in Quantity and Date section:Quantity:1Delivery Date: default valueRequisition Date: default valueRelease Date: default valueChoose Account Assignment section.Make the following entries: G/L Account: for example, 51600000 for materials with a material number, The G/L account will be determined automatically.Go to the section Account Assignment and click on the corresponding line to go to Account Assignment screen, and enter Cost Center: 33101101 in the appearing screen.WBS Element: <WBS Element>Note If Account Assignment Category is P, enter your created WBS in test script (1NT) Project Financial Control and (35F) Capital Investment Project Management. For further support or issue reporting, you can create an incident under PPM-CNT component.Choose Apply.Choose Contact Information section.Make the following entries:Purchasing Organization: 3310Purchase Group: 001Choose Source of Supply section: Agreement/Item:46xxxxxxxxx/00xxIf the source does not automatically determine, then you can choose Assign Source of Supply. On the Select Source Of Supply screen, choose the contract which is created in the Preliminary step.On the Purchase Requisition Item screen, choose Apply. | The Add Purchase Requisition Item screen appears. |  |
|  | Case 2: Purchase for Limit Item (N/A for Brazil) | In the Limit Items area on Purchase Requisition screen, choose Create.Choose Material and enter the following values:Item Description: for example, LimitFixed Supplier: 33300001Expected Value: 100 AEDOverall Limit: 105AEDProduct Type Group: Material (1)Plant: 3310Acct Assignment Cat.: Cost center (K)Material Group: YBMM00 and choose Enter.Go to the section Requisition Period and enter the following values:Start Date:<Today>End Date: For example: <Today+12 month>Requisition Date:<Default Date>Release Date: <Today>65100000 is for material group YBMM00. The G/L account will be determined automatically.Go to the section Account Assignment and click on the corresponding line to go to Account Assignment screen, and enter Cost Center:33101101 in the appearing screen.Choose Apply.Go to the section Contact Information and enter the following values:Purchasing Organization: 3310Purchasing Group: 001On the Purchase Requisition Limit Item screen, choose Apply |  |  |
| 6 | Create your entries | Choose Create.Choose Create to confirm the popup message. | A purchase requisition is created. |  |

Result

The Purchase Requisition is created.

### Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to convert assigned purchase requisitions to purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Purchase Requisitions (F1048A) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of requisitions is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the purchase requisition number and choose Go.Note Purchase requisition can also be generated from scope item 4RF - Project Control – Resourcing and Procurement. And if you encounter any account assignment P related issues, you can create an incident under PPM-CNT component. | The purchase requisition is shown depending on material. |  |
| 4 | Prepare the Purchase Order | Choose Show More per Row button on the side of Create RFQ. Check whether the purchase requisition is assigned of source of supply and choose Create Purchase Order. | The Purchase Order Preview screen is displayed. |  |
| 5 | Create the Purchase Order | Select the Purchase Order. Make the following entries:Purchase Order Type: Standard PO.Choose Order. | The purchase order is created. |  |
| 6 | Back to Manage Purchase Requisition | In the dialog box, choose OK. | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |

Result

The Purchase Requisition is converted to Purchase Order.

### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to formalize a specific requirement for a material from the vendor by creating a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Orders screen displays. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The New Purchase Order screen displays. |  |
| 4 | Enter Purchase Order data | Make the following entries:In the Basic Data area:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300001Currency: AEDPurchasing Group: 001Purch. Organization: 3310Company Code: 3310Choose tab Notes on the head level. Choose > or < to search for Header text. On the Header text column, enter the free text:xxx for testing. |  |  |
|  | Case 1: Purchase material without material number | In the Items area:Choose Create and make the following values:Short Text: Enter appropriate description, for example, <office supplies>Material Group: YBMM00Plant: 3310Order Quantity: <XX PC >Net Order Price: <XX>Note If you want the purchase order to be assigned to an approver, then choose a quantity and total net amount of purchase order is greater than 500 AED for Purchasing Groups 003Choose the item and go to the Purchase order Item screen and enter the following values:Item Category: StandardAcct Assignment Cat.: Cost centerGo to the Tax area:Tax Code: <Input Tax Code>Choose Account Assignment.65100000 for material without material number. The G/L account will be determined automatically.Go to the section Account Assignment and click on the corresponding line to go to Purchase Order Item Account Assignment screen, and enter Cost Center:33101101 in the appearing screen.Choose Apply and go back to Purchase order screen. |  |  |
|  | Case 2: Purchase for Limit item | In the Limit Items area:Choose Create and enter the following values:Short Text: for example, <Limit>Expected Value: 100AEDOverall Limit: 105AEDAcct Assignment Cat.: Cost center (K)Product Type Group: Material (1)Plant: 3310Choose the item and go to the Purchase Order Limit Item screen and enter the following values:Material Group: YBMM00 and choose Enter.Go to the Tax area:Tax Code: <Input Tax Code>G/L Account: for example, 65100000 for material without material number. The G/L account will be determined automatically.Go to the section Account Assignment and click on the corresponding line to go to Purchase Order Item Account Assignment screen, and enter Cost Center:33101101 in the appearing screen.Choose Apply. |  |  |
| 5 | Save Purchase order | After choose Apply to go back to Purchase order screen. Choose Order to save the purchase order. | The Purchase Order is created. |  |

|  |
| --- |
| Note If you do not know who should approve the purchase orders you created, then you can use App Manage Purchase Orders to display the created purchase order: Go to the Approval Details tab and check the approvers listed in section Approval Details. |

### Execute Mass Changes to Purchase Orders (Optional)

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Mass Changes to Purchase Orders (F2593) . | The Mass Changes to Purchase Orders screen displays. |  |
| 3 | Search for Purchase Orders Items | Set values to some filters to search Purchase Orders. For example:Material GroupPurchasing OrganizationPurchasing GroupPlantThen choose GO. | The search results show the details with the respective filter Criteria.By Default, all the Purchase Orders items are selected for Mass Change operation. |  |
| 4 | Select Purchase Order | Select several POs by clicking the checkbox beside the purchase order number. | Purchase Order has been selected. |  |
| 5 | Choose Mass Edit | After selecting an individual purchase order, then choose Mass Edit. |  |  |
| 6 | Apply Mass Changes | Set new values in the given desired fields:For example: Terms of Payment: <Replace Field Value> 0003.Choose Apply Mass Changes . Choose Apply to confirm the Apply Mass Changes screen. Choose Close to close the Success screen. | New values will be set to desired fields for selected Purchase Orders/Items. |  |
| 7 | Check Application Jobs | Choose Monitor Mass Changes.On Monitor Mass Changes screen, enter the Created At with Today and remove Created By filter as blank. Choose Go and then choose Mass Change Jobs tab. Navigate to the selected Mass Change Job by clicking on the Chevron (>) or by directly clicking on the Mass Change Job line. | It will navigate to Monitor Mass Changes screen.Verify if the job is successful for the selected Purchase Orders. |  |

### Redistribute Workload (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this test script, the relevant Purchasing Document would be listed. By choosing Purchasing Document/Documents, the Reassign Purchasing Group button will be enabled . Thereafter, the user may select the Respective Purchasing Group from the list of respective Purchasing group by choosing F4. The user can then choose Simulate, this shall list the possibility whether the Purchasing Group would be changed or not for the selected Purchasing document. Then the User can confirm (either Cancel or OK or Save ) to get it updated accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Redistribute Workload (F2504). | The Redistribute Workload screen displays. |  |
| 3 | Search Purchasing Document Entry / Entries | Set values to some filters to search purchasing documents for which you want to redistribute workload, then choose GO.For example:Creation DateDocument NumberDocument TypePurchasing OrganizationPurchasing GroupDocument Category | The search results show the purchasing documents details with the respective filter Criteria. |  |
| 4 | Reassign Purchasing Group | Select Purchasing Document Entry / Entries you want to redistribute workloadChoose Reassign Purchasing Group and select a Purchasing Group from the list. | The Reassign Purchasing Group dialog box displays and new Purchasing Group can be selected. |  |
| 5 | Simulate | Choose Simulate.Note If all the purchase documents have error in Simulation and Purchasing Group cannot be updated for the documents (For example purchase documents already have follow-on document or get locked), you need to choose Cancel and go back to the previous step to select different purchase documents. | This shall list the simulation messages as to whether the Reassignment is feasible or not. |  |
| 6 | Save the Reassignment | Choose Save to save the Reassignment when the simulation shows the Reassignment is feasible. | The Purchasing Group shall get reassigned accordingly with system message Purchasing Group has been assigned to documents. |  |
| 7 | Check Application Jobs Change Log | Choose Change Log. | It will navigate to Application Logs page containing the list of Job IDs for all Purchase documents.Verify if the job is successful for the selected Purchase documents |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Orders screen displays. A list of Purchase Orders is displayed. If needed, you can enter search criteria to find your purchase order. |  |
| 3 | Select Purchase Order | Choose the line of the purchase order you want to change. | The purchase order is opened in display mode. |  |
| 4 | Change Purchase Order | Choose Edit.Change certain field values of the purchase order.Note Ensure that the total amount of the PO is higher than 500 AED and purchase group is 003, to be available for the next step, Approval | The purchase order values are changed. |  |
| 5 | Save Purchase Order | Choose Order to save the purchase order. | If a message is displayed, you must correct the purchase order. If no message is displayed, the purchase order is complete. |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the total amount of PO is > 500 AED and purchase group is 003, then the PO should be approved. To decide which POs need approval, please refer to Configure Flexible Workflow for Purchase Order in Preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open My Inbox - All Items (F0862) . | A list of already created purchase orders displays. |  |
| 3. | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4. | Check Account Assignment Detail information | Choose > to navigate to the item detail, and navigate to the Account Assignment information on the right side of the screen. | The account assignment information is displayed. |  |
| 5. | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 6. | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

### Monitor Purchase Order Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor each item in purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Monitor Purchase Order Items (F2358) . | The Monitor Purchase Order Items screen displays. The numbers of current overdue PO items are listed. |  |
| 3 | Search for Purchase Orders | The basic filters are available:Display CurrencyPurchase OrderMaterial GroupMaterial, SupplierPlant, and so onMake the below entries accordingly, and then choose Go . | The search results show the details with the respective filter criteria.You can choose Adapt Filters to select filters. |  |
| 4 | Display Purchase Order | Select an individual line item of the Purchase Order to display the PO details. | The Purchase Order Item screen displays. |  |
| 5 | Verify Data | Verify data displayed on the object page. | The data is logically in-sync with the purchase order. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843) . | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search for the Purchase Order | On the Post Goods Receipt for Purchasing Document screen, enter the purchase order number and choose Enter. | The purchase order displays. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted and input delivered quantity. |  |  |
| 6 | Post | Choose Post. | The system message confirms that the goods receipt posted successfully. |  |

### Preview Goods Receipt Slip (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the material document is previewed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Material Documents Overview (F1077) . | The Material Documents Overview displays. |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose Go.Plant: 3310Material Document: xxx | The relevant Material Document items for the material display. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The Material Document Details screen displays. |  |
| 5 | Check Goods Receipts Details | Check the General Information, and the Material Document Items. | In the General Data section, the correct Posting Date, Document Date, and the Delivery Note display. |  |
| 6 | Select the Material Document Item | Choose the material document item you want to preview by choosing the row . | A new screen with the General Information and Output Management displays. |  |
| 7 | Preview the Material document | In the Output Management section, choose Display Document in the Preview column after selecting Show Details on output type level. | The Goods Receipt Slip is opened in PDF format. |  |
| 8 | Back to Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

### Monitor Purchase Order Items by Account Assignment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor each item in Purchase orders based on account assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Purchase Order Items by Account Assignment (F2420) . | The Purchase Order Items by Account Assignment screen displays. |  |
| 3 | Search for Purchase Orders | All basic filters are displayed:Purchase OrderAcct Assignment CategoryCost CenterWBS ElementAssetSupplierPlantPurchasing OrganizationPurchasing GroupSelect your filtering requirement from the available filters and then choose Go. | The search results show the details with the respective filter criteria.By default data is filtered by Cost Center.You can choose Adapt Filters to list filters to add adapt filters.This app only displays the purchase order which status is open. |  |
| 4 | Display Purchase Order | Select an individual line item of the Purchase Order Item and choose Details by choosing > at the right side of the row. | The Purchase Order Item screen displays. |  |
| 5 | Verify data displayed | Verify data displayed on the screen. | The data matches the data of the purchase order. |  |
| 6 | Return to the main screen | Choose Back (<) to return to the main screen. | Return to the main screen. |  |

### Create Supplier Invoice

Context

In this activity, you create the supplier invoice. You have the following two options to create the supplier invoice:

- Option A: Create Supplier Invoice with PO/GR relation.
- Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction)

You can choose either option A or option B to execute the supplier invoice creation. For more information, see the next two tasks.

|  |
| --- |
| Note Only choose option A or B (not both). |

#### Option A: Create Supplier Invoice with PO/GR relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation. You have two options to create the supplier invoice:

Choose Option A: Create Supplier Invoice with PO/GR relation.

Choose Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction)

You can choose either option A or option B to execute the supplier invoice creation with PO/GR relation. For more information, see the next two tasks.

|  |
| --- |
| Note Only choose either option A or B (not both). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:33300001In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:33300001Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Exchange Rate should be changed from USD in EUR according to the customizing settings. The Exchange Rate is changeable |  |
| 4 | Enter Purchase Order References | In Purchasing Document References section, add the references.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items, which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | If the invoice item is Limit, then enter the Amount is < 105 AED Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Block invoice on item level (Optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Choose Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Choose Back to Supplier Invoice. | The item is blocked with a blocking reason. |  |
| 9 | Check the balance | Calculate the tax by choosing Propose Tax. Check the balance to make sure that the balance is zero. | The balance should be zero. |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. Choose Back. | The Supplier Invoice is complete to post. |  |
| 11 | Post Invoice or Save as completed invoice | Optional A: Choose Post. When you choose Post, then you have to process the step: [Release Blocked Supplier Invoice (Optional)](#unique_37) [page ] 46.Optional B: Choose Save as Completed, then you have to process the step: [Option A: Release Completed Supplier Invoice (Optional)](#unique_34) [page ] 41.Note If Invoice triggers Workflow for Parked Invoice as Complete, Approval Details tab will be shown in supplier invoice with workflow steps and processor.Note Only choose option A or B (not both). You can choose Park to park the invoice first. After that, you can edit the created supplier invoice to choose Save as Completed. | The system message is shown. |  |

#### Option A: Release Completed Supplier Invoice (Optional)

Purpose

In this activity, if the system displays message Price too high (tolerance limit of XXX exceeded) when you run Save As Completed, please choose Option A, otherwise choose Option B.

|  |
| --- |
| Note Only choose either option A or B. |

Table 2: Option A

| No. | Workflow sequence | Business Role |
| --- | --- | --- |
| 1 | Release by purchaser | PurchaserNote If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to the business role of the user. This action is also required for other invoice workflow. |
| 2 | Release by Cost Center Responsible | Approver is set in preliminary step [Update Cost Center for User Responsible](#unique_15) [page ] 14. |
| 3 | Release by Profit Center Responsible | Approver is set in preliminary step [Update Profit Center for User Responsible](#unique_16) [page ] 15. |

Table 3: Option B

| No. | Workflow sequence | Business Role |
| --- | --- | --- |
| 1 | Release by Cost Center Responsible | Approver is set in preliminary step [Update Cost Center for User Responsible](#unique_15) [page ] 14. |
| 2 | Release by Profit Center Responsible | Approver is set in preliminary step [Update Profit Center for User Responsible](#unique_16) [page ] 15. |

Procedure

Once the completed supplier invoice is released, you could check details on the Approval Details Tab of the corresponding supplier invoice via APP Supplier Invoices List.

For more information, see below procedure:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as approver set in preliminary step. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open My Inbox - All Items (F0862) . | The My Inbox screen displays. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice displays. |  |
| 4 | Approve Supplier Invoice | On the Release Completed Invoice XXXXXXXX screen, select the Release button at the bottom of the screen.On the Submit Decision screen, add note if necessary and select Submit button. | Task successfully processed. |  |

#### Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction) (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with invoice reduction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | Make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: XXX(Invoice (overall) amount (incl. Tax) of the (fictive) invoice)Currency:AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoicing Party: 33300001 | The Create Supplier Invoices screen is displayed. |  |
| 4 | Enter Purchase Order References | In Purchasing Document Reference section, add the references.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Reduce Invoice | Choose the item to navigate to the details screen.Choose the Reduce invoice button in the bottom.On the Reduce Invoice dialog box, make the following entries:Amount from Supplier: XX (Larger than amount in PO)Quantity from Supplr.: XX (Larger than quantity in PO)Choose OK to close the dialog box and choose Back to Supplier Invoice.If the Payment Terms is 0002 or 0003 in the invoice creation, then you must enter the Baseline Date.Enter the Baseline Date: <the first day of the last month> | Supplier Invoice amount is reduced |  |
| 8 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount, when the tax code value is greater than zero | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify tax code <Input Tax Code> |  |
| 9 | Verify the balance | Verify the Gross Invoice Amount that you entered in step 3, against the items plus tax amount (for invoice reduction item, Amount Acc. Suppl. is used for calculation)If tax code you selected is zero tax, you do not have any tax amount. | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose Simulate .You can check the simulation results in the Simulation Overview and Simulation Details area. | The supplier invoice is simulated. |  |
| 11 | Post Invoice | Choose Post . | The invoice is posted. |  |

#### Option B: Print Complaint Letter in case of Invoice Reduction (Only relevant for SAP S/4HANA Cloud Public Edition)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you want to output these messages you have to start the output manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant . | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Supplier Invoices List (F1060A) . | The Supplier Invoice List screen displays. |  |
| 3. | Search for Supplier Invoice | Make the following entry and choose Go button.Invoicing Document No.: XXXXXXXX (created in above step) | The relevant supplier invoice is displayed. |  |
| 4 | Complaint Letter Overview | Choose Invoice item by clicking on the row of the invoice to go to Supplier Invoice detail screen. Go to the Output section and choose Show More per Row, and choose Display Document. | The complaint letter opens as a PDF file. |  |
| 5 | Print Complaint Letter | On the Display page, you can select Print from menu by clicking right mouse. | The output items are sent to the printer queue. |  |

### Release Blocked Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the blocked supplier invoice is released, you could check details on the Approval Details Tab of the corresponding supplier invoice via APP Supplier Invoices List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an approver set in preliminary step, cost center responsible | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open My Inbox - All Items (F0862) . | The My Inbox screen displays. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice displays. |  |
| 4 | Release Supplier Invoice | On the Release of Blocked Invoice XXXXXXXX screen, select the Release button at the bottom of the screen.On the Submit Decision screen, add note if necessary and select Submit button. | Task successfully processed. |  |

### Multiple Account Assignment for consumable purchasing

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create the purchase order with the multiple account assignment function.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The New Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order data | Enter the following values:Basic Data:Supplier: 33300001Company Code: 3310Purchasing Org: 3310Purchasing Group: 001Currency: AEDEnter the following data for each item:Items – choose Create.Purchase material without material number:Short Text: Enter appropriate description, for example, office suppliesMaterial Group: for example, YBMM00Plant: 3310Order Quantity: XX PCNet Order Price :XX |  |  |
| 5 | EnterAccount Assignment data | Click on your item to Purchase Order Item screen.Item Category: StandardAcct Assignment Cat.: Cost centerTax Code: for example,<Input Tax Code>Choose Account AssignmentMake following data:G/L Account: for example, 65100000 for material without material number. The G/L account be determined automatically.Choose Create to add another account assignment line.Note If you do not find Distribution (%) column and Cost Center column on Account Assignment Tab, then you have to choose Settings to select Distribution (%) and Cost Center on the View Settings screen. After that, you should choose OK to confirm the View Settings screen.Choose the Account Assgmt No. 1 itemEnter Cost Center:33101101 and Distribution (%) : for example: for example:20Choose the Account Assgmt No. 2Enter Cost Center:33101401 and Distribution (%) : for example: for example: 80 |  |  |
| 6 | Save Purchase Order | Choose Apply to go back to Purchase Order screen. Choose Order to save the purchase order. | The Purchase Order created. |  |

|  |
| --- |
| Note If Scope Item 2I3 (Predictive Commitments Management) has been activated for controlling area from a chosen fiscal year in the system, then you can display commitments by App Manage Purchase Orders. Once the PO is approved, you can navigate to Item tab and choose Display Commitments in App Manage Purchase Orders. You can check the commitment amount of the Purchase Order Item. |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843) . | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search for the Purchase Order | On the Post Goods Receipt for Purchasing Document screen, enter the purchase order number and choose Enter. | The purchase order displays. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted and input delivered quantity. |  |  |
| 6 | Post | Choose Post. | The system message confirms that the goods receipt posted successfully. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries. screen displays.Transaction: InvoiceCompany Code: 3310Reference: <xxx>(reference invoice number from invoicing party)Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Invoice Party:33300001 | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document screen section, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling Agreement | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items and delivery costs items which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order).Note You can choose invoice item to display multiple account assignment detail in next screen. | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the differences are within the defined tolerance), the Supplier Invoice is complete to post.Check the Gross Invoice Amount against the items plus tax amount (If tax code you selected is zero tax, you do not have any tax amount.) | The Supplier Invoice is complete to simulate. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. |  |

### Invoicing Plan for Consumable Purchasing

#### Create Purchase Order for Invoicing Plan

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced(ME21N) . | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300003In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group:002Company Code: 3310In Items section,Material: NS0001Item Category: StandardAcct Assignment Cat.: Cost centerPlant: 3310Storage Location: 331APO Quantity: 100Net Price: 10AEDGo to Delivery Tab and deselect Goods Receipt.Go to Invoice Tab and enter Tax Code<Input Tax Code>.GR-Bsd IV: DeselectTax Date: <Default Value>ERS: Select | The Create Purchase Order screen is displayed. |  |
| 4 | Enter Cost Center | Go to Account Assignment Tab and enter Cost Center:33101202Choose Enter. |  |  |
| 5 | Enter Invoicing Plan data | On the Invoice tab, choose Invoicing PlanChoose 10 Sample periodic invoice plan on screen Specify Invoicing Plan.Choose Continue.If the warning message pops up, then choose Enter to confirm it.In Advance: SelectStart date: TodayEnd date: Last Day of the Current YearChoose Back(F3) to go to the Create Purchase Order screen. |  |  |
| 6 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

#### Create Invoice Plan Settlement

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Invoicing Plan Settlement (MRIS) | The Invoicing Plan Settlement with Logistics Invoice Verification screen opens. |  |
| 3 | Enter Data for Invoice Plan Settlement | Make the following entries and choose the Run (F8) button.Company Code:3310Plant: 3310Supplier: 33300003Purchasing Document : PO number which is created in step Create Purchase Order for Invoicing PlanTax Date: Default ValueTest Run: Deselect | The relevant Purchase Orders are shown. |  |
| 4 | Write Down Invoice Document Number | The invoice document is created. Write down its number as it is needed. | The invoice document is created. |  |
| 5 | Back to SAP Fiori Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

### Update Invoicing Plans (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can generate further invoicing plan dates for purchase orders. If you have assigned a periodic invoicing plan to a purchase order item but have not initially defined invoicing dates covering the entire validity period of the purchase order, you can generate further dates in due course. The Horizon field (HORIZ) lets you define how far in the future dates should be generated. For example: you have an invoicing plan that runs over 5 years. However, you only want to create the commitments for one year in advance. Solution: You enter a horizon of one year from the current date. When you now regularly run Transaction MLRP, it generates dates up to a year into the future. Also, the commitments are created only for these dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Update Invoicing Plans - Purchase Order (MLRP) . | The Updating Invoicing Plans - Purchase Order screen displays. |  |
| 3 | Enter Data for Updating Invoicing Plan | Make the following entries and choose Run (F8).Purchasing Order: PO number which is created in step Create Purchase Order for Invoicing PlanLog: select | The relevant Purchase Orders are entered. |  |
| 4 | Get the Log | Get the log for the updating invoicing plans. | The log for the updating invoicing plans has been created. |  |
| 5 | Back to SAP Fiori Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

### Retention Scenario in PO

Purpose

The procedure below consists of:

- Raising a Purchase Order with a retention clause of 10%
- Receiving the goods
- Receiving the supplier’s invoice for the full purchase order value which leads to the creation of two documents: one for the invoice and one for the retention
- Paying the supplier’s invoice with the retention deducted
- Converting the retention to a supplier’s liability and accounting for the VAT on the retention
- Paying the supplier’s retention

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2. | Access App | Open Create Purchase Order - Advanced (ME21N) . | The Create Purchase Order screen displays. |  |
| 3 | Enter Purchase Order Data | Enter all the necessary data.PO Type: Standard PO (NB)Supplier: 33300001Doc. Date: <current date>On the tab Org. Data, make the following entries and choose Enter:Company Code: 3310Purchasing Organization:3310Purchasing Group:001On the tab Delivery/Invoice, make the following entries and choose Enter:Currency: AEDPayment Terms: 0004On the tab Payment Processing, make the following entries and choose Enter:Retention: Applicable (Item Level)Under the Items section make the following entries:Material: TG0011PO Quantity:<quantity>Net Price: <price>Plant: 3310Stor. Location: 331ANavigate to the Invoice tab of the selected item. The following entries display:Inv. Receipt: <selected>GR-Bsd IV: <selected>Tax Code: V2Retention %: 10 | The Purchase Order screen is displayed. |  |
| 4. | Verify Purchase Order for completeness and Save Purchase Order | Choose Check to check the Purchase Order for completeness.If no messages are raised, press Save. | A new Purchase Order is created if no error is displayed in the dialog box. |  |
| 5. | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 6. | Access App | Open Post Goods Receipt for Purchasing Document. | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 7 | Enter Purchase Order | Enter the Purchase Order ID and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 8 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: xxxPrinting: Individual slip |  |  |
| 9 | Select Item | From the Items section, select the goods receipt item to be posted. | You can see that the Post button is activated. |  |
| 10 | Post | Choose Post. | The system displays the message material document xxx posted. |  |
| 11 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 12 | Access App | Open Create Supplier Invoice - Advanced. | The Enter Vendor Invoice: Company Code3310 screen is displayed. |  |
| 13 | Enter General Data | Enter the following information:Transaction: InvoiceInvoice Date: <invoice date>Posting Date: <posting date>Reference: <supplier invoice reference>Gross Invoice Amount: <invoice amount + VAT>Currency: AEDCalculate Tax: <selected>Tax Code: V2 | The General Data is populated. |  |
| 14 | Enter Payment Data | On the Payment tab, enter the following information:Pyt Terms: 0004BaselineDt: <invoice date> |  |  |
| 15 | Enter Purchase Order References | Under the PO Reference tab, make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO Number> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 16 | Enter Retention Due Date | Under the Basic Data tab, enter the following information:Retention Due: <Due Date for Retention> | The due date by which the retention must be released.Make sure Retention Due date should be after Baseline due date. |  |
| 17 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated.Since there is a retention on this invoice, a message with the amount of retention is displayed. |  |
| 18 | Post Invoice | Choose Post. | The invoice is posted.Two documents are created:One document for the supplier invoice full amount with the VAT calculation based on the base amount – the retention amountOne document for the retention amount |  |
| 19 | Supplier Payment | Follow the steps as described in scope item J60_AE Accounts Payable under section Payment Run to pay the outstanding invoice to supplier minus the retention. | The outstanding supplier invoice has been paid with the retention deducted. |  |
| 20 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 21 | Access App | Open Clear Outgoing Payment. | The Clear Outgoing Payment screen is displayed. |  |
| 22 | Select Clear Open Item | Click Clear Open Items button. | The criteria screen is displayed. |  |
| 23 | Mainatain Selection Criteria | Enter the following information:Company Code: 3310Supplier: 33300001 | The Clear Outgoing Payment screen is displayed. |  |
| 24 | Maintain Document Header | Enter the following information:Journal Entry Date: <retention end date>Journal Entry Type: KACompany Code: 3310Posting Date: <retention end date>Currency: AEDReference: <supplier invoice number of original invoice> |  |  |
| 25 | Maintain Open Item Selection | Select Select More.Enter the following information:Company Code: 3310Account Type: SupplierAccount ID: 33300001Line Item Type: Special G/L TransactionsSpecial G/L: H | The Open Items list is displayed |  |
| 26 | Select Open Item | Select the special retention open document to be cleared and click Clear button. |  |  |
| 27 | Maintain First Line Item | The first line item corresponds to the retention amount including VAT that must now be paid to the supplier.Click Post on Account tab.Enter the following:Account Type: SupplierCompany Code : 3310Supplier: 33300001Credit Amount : <retention amount + VAT> | The retention amount including VAT to be paid to the supplier is maintained. |  |
| 28 | Maintain Second Line Item | The second line item corresponds to an offsetting entry for the vendor posting created in the first line item.Click Post to G/L Account tab.Enter the following:Account Type : G/L accountCompany Code : 3310G/L Account: 21720200Debit Amount: <retention amount + VAT>Tax Code: V2 | The offsetting entry is maintained. |  |
| 29 | Maintain Third Line Item | The third line item corresponds to an offsetting entry for the retention posting made to the special G/L indicator H that will be cleared in the next step.In Post to G/L Account tab, click Add.Enter the following:Account Type : G/L accountCompany Code : 3310G/L Account: 21720200Credit Amount: <retention amount w/o VAT> | The offsetting entry is maintained. |  |
| 30 | Simulate Posting | Click Simulate. | The document shall be made of 5 line items:Line 1: posting on supplier’s account the retention amount + VATLine 2: posting on offsetting account the retention amount with Tax Code V2Line 3: posting on offsetting account the retention amount without Tax CodeLine 4: posting with clearing on the supplier’s account (special G/L account H) the retention amountLine 5: posting on Input VAT account VAT amount + Tax Code V2 |  |
| 31 | Post Document | Press Post. | A new document for the retention amount + VAT to be paid to the supplier is posted. |  |
| 32 | Supplier Retention Payment | Follow the steps as described in scope item J60_AE Accounts Payable under section Payment Run to pay the outstanding invoice to supplier retention. | The outstanding supplier retention has been paid. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 4:

| Process | Business Condition |
| --- | --- |
| Real-Time Reporting and Monitoring for Procurement(1JI) | The Procurement Overview page provides the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reportsThe Global Filter helps the Purchaser to filter the Procurement Overview page to view all information according to specific suppliers, material groups, purchasing groups and more.Using contextual navigation, the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or get more detailed information in the corresponding KPI drill-downs. |
| Accounts Payable (J60) | Outgoing Payment |

### Setup Mail Notification for Supplier Invoice Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Copy the predelivered email template to the exactly named custom template.

Procedure

|  |
| --- |
| Note Please check email address has already maintained for the approver. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Extensibility Specialist role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Email Templates - Deprecated (F1306) . | The templates displays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_CRT_NOTIFY_RECIPIENTS.Choose email template then choose Copy then make bellow entries:Email Template: For example, YY1_00800251_CRT_ALLName: Release of Supplier InvoiceChoose Copy.Note For Release Blocked Invoice workflow, the custom template must follow these naming pattern:YY1_00800251_CRT_10 or YY1_00800251_CRT_ALL(Both work the same way, as there is only one relevant node in the workflow)For Parked Invoice as Complete workflow, the custom template must follow these naming pattern:YY1_00800303_CRT_19 Email is triggered in case of work item to approve invoiceYY1_00800303_CRT_30 Email is triggered in case of work item to rework invoiceYY1_00800303_CRT_ALL Email is triggered in case of work item to approve or rework invoice | Email Template copied. |  |
| 4 | Adjust the text of the mail template | Choose Custom tab.Choose Email template, for example YY1_00800251_CRT_ALL then go to Email Template screen. | Custom Email Template opened. |  |
| 5 | Choose Language | Choose Language, for example English. Then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request then choose Save. | The Email Template adjusted. |  |

### Setup Mail Notification for Supplier Invoice Workflow with Factory Calendar

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Copy the predelivered email template to the exactly named custom template.

After finishing this step, in app Manage Workflows for Supplier Invoices (F2873), you will be able to add a deadline based on workday(s) in the Deadlilnes section when executing action Mark Step as Overdue or action Send Mail Notification. You can select any Email template created in app Maintain Email Templates - Deprecated (F1306) for action Send Mail Notification.

Procedure

|  |
| --- |
| Note Please check if email address has already been maintained for the approver. |

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fall/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Email Templates - Deprecated (F1306) | The templates displays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (X), search Template: MRM_WF_DEADLINE.Choose email template then choose Copy then make bellow entries:Email Template: for example, YY1_ MRM_WF_DEADLINEName: Supplier Invoice NotificationChoose Copy. | Email template is copied. |  |
| 4 | Adjust the Text of the Mail Template | Choose Custom tab.Choose Email template, for example YY1_ MRM_WF_DEADLINE then go to Email Template screen. | Custom Email Template is opened. |  |
| 5 | Choose Language | Choose Language, for example English. Then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request then choose Save. | The Email Template is adjusted. |  |

### Retention Process

#### Prerequisites

This section summarizes the prerequisites for conducting the test.

Additional Manual Configuration

Before you can test this process, you need to check below additional configuration steps.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step Name | Mandatory | ID | Expected Result | Component |
| --- | --- | --- | --- | --- |
| 1.Automatic Account Determination | Mandatory | 100297 | The special G/L Account for Account type K and Special G/L H must be maintained. | FI-CNT-GL |
| 2.Define Default Due Date for Retention | Optional | 105914 | Warranty Duration for Retention per Date Category can be maintained if necessary. | MM-IV-LIV-CRE |
| 3.Define Tax Handling for Retention | Optional | 105912 | Tax Code and Tax Reduction can be added if necessary. | MM-IV-LIV-CRE |
| 4.Define Control Parameters for Retention | Optional | 105913 | DueDateReq and SGL can be maintained if necessary. | MM-IV-LIV-CRE |

#### Create Purchase Order with Retention

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) . | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300001In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group:001Company Code: 3310In Header section, on the Payment Processing tab, make the following entries:Retention: Applicable (Header Level)Retention:10%In Items section,Material: NS0001Item Category: StandardAcct Assignment Cat.: Cost centerPlant: 3310Storage Location: 331APO Quantity: 100Net Price: 10AEDGo to Delivery Tab and deselect Goods Receipt.Go to Invoice Tab and enter Tax Code<Input Tax Code>.Retention:10%GR-Bsd IV: SelectTax Date: <Default Value> | The Create Purchase Order screen is displayed. |  |
| 4 | Enter Cost Center | Go to Account Assignment Tab and enter Cost Center:10101202Choose Enter. |  |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843) . | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search for the Purchase Order | On the Post Goods Receipt for Purchasing Document screen, enter the purchase order number and choose Enter. | The purchase order displays. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. |  |  |
| 6 | Post | Choose Post. | The system message confirms that the goods receipt posted successfully. |  |

#### Create Supplier Invoice

Purpose

In this activity, you create the supplier invoice with PO/GR relation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoice - Advanced screen is displayed. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, enter below data:Company Code: 3310Transaction: InvoiceInvoice Date: <Today>Posting Date: <Today>Retention Due Date: < Today + 30 >Gross Invoice Amount: <xxx>Currency: AEDReference: <xxx>(reference invoice number from invoicing party) | The data is entered. |  |
| 4 | Enter Purchase Order References | In PO References tab, add the references. Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items, which refer to the entered purchase order document. |  |
| 6 | Check the balance | Calculate the tax by choosing Calculate Tax. Check the balance to make sure that the balance is zero. | The balance should be zero. |  |
| 7 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. Choose Back. | The supplier Invoice is complete to post. |  |
| 8 | Post Invoice | Choose Post.Note If you got message No special G/L acct defined for acct type K sp. G/L ind. H recon.acct…, please check if the special GL account has been maintained via SSCUI Automatic Account Determination mentioned in section [Prerequisites](#unique_51) [page ] 64. If you still have issues, please create a ticket to component FI-CNT-GL. | The system message is shown. |  |
| 9 | Check Accounting Document | Choose the invoice number xxxxxxxxxx/xxxx just created.Choose Journal Entries. Two accounting documents was posted.Select the second Accounting Document.Choose Display Document. You can see the details of the accounting document. | Two accounting document can be displayed. |  |

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
> Flagged while digesting this document, not verified: PO approval threshold: the flexible workflow configuration example uses total net amount greater than 10 AED for purchasing group 003, while the Create PO, Change PO and Approve PO steps say approval applies above 500 AED for purchasing group 003.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Option A/B labels are overloaded: in Create Supplier Invoice step 11, 'Optional A' (Post) leads to Release Blocked Invoice and 'Optional B' (Save as Completed) leads to 'Option A: Release Completed Supplier Invoice', while the invoice creation options A/B mean without/with invoice reduction and the release tables use Option A/B for two workflow sequences.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-requisitioning-18j-ae-sap-s-4hana-cloud-public-edition-705]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BNX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 109,226 chars in the whole document
