---
id: 10-procurement/test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa
title: "Test Script: Scheduling Agreement for Consignment Procurement (2NY_AE) - SAP S/4HANA Cloud Public Edition (2NY_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 2NY (AE): consignment scheduling agreement from requisition to settlement, with roles, apps and sample data."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements, topic/supplier-consignment]
aliases: [2NY_S4CLD2608_BPD_EN_AE]
keywords: [Purchase Scheduling Agreements, scheduling agreements, consignment procurement, test scripts, delivery schedule, purchase requisitions, consignment settlement, flexible workflow, scheduling agreement approval, supplier invoices]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NY_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-838
topic: 10-procurement/scheduling-agreements
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Scheduling Agreement for Consignment Procurement (2NY_AE) - SAP S/4HANA Cloud Public Edition (2NY_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NY_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Scheduling Agreement for Consignment Procurement (2NY_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849679)

[2 Prerequisites 4](#_Toc232849680)

[2.1 System Access 4](#_Toc232849681)

[2.2 Roles 4](#_Toc232849682)

[2.3 Master Data and Organizational Data 5](#_Toc232849683)

[2.4 Business Conditions 6](#_Toc232849684)

[2.5 Preliminary Steps 6](#_Toc232849685)

[2.5.1 Activate Flexible Workflow for Scheduling Agreement Approval 6](#_Toc232849686)

[2.5.2 Configure Flexible Workflow for Scheduling Agreement 8](#_Toc232849687)

[2.5.3 Create Purchasing Info Record 9](#_Toc232849688)

[2.5.4 Edit User-Specific Parameters for Supplier Invoices (Optional) 11](#_Toc232849689)

[3 Overview Table 13](#_Toc232849690)

[4 Test Procedures 15](#_Toc232849691)

[4.1 Create Purchase Requisition 15](#_Toc232849692)

[4.2 Convert Purchase Requisition to Scheduling Agreement 16](#_Toc232849693)

[4.3 Create Scheduling Agreement 17](#_Toc232849694)

[4.4 Approve Scheduling Agreement (Optional) 18](#_Toc232849695)

[4.5 Maintain Delivery Schedule 19](#_Toc232849696)

[4.6 Print Scheduling Agreement 20](#_Toc232849697)

[4.7 Evaluate the Stock/Requirement Situation 21](#_Toc232849698)

[4.8 Post Goods Receipt 23](#_Toc232849699)

[4.9 Transfer Posting from Vendor Consigned Stock to Own Stock 24](#_Toc232849700)

[4.10 Invoice Receipt from Consignment Withdrawal 25](#_Toc232849701)

[4.10.1 Option 1: Create Consignment settlement 25](#_Toc232849702)

[4.10.2 Option 2: Schedule Supplier Invoice Jobs 26](#_Toc232849703)

[4.11 Check Supplier Invoice List (Optional) 28](#_Toc232849704)

[5 Appendix 30](#_Toc232849705)

[5.1 Process Integration 30](#_Toc232849706)

[5.1.1 Succeeding Processes 30](#_Toc232849707)

## Purpose

Overview

The use of scheduling agreements can shorten processing times and reduce paperwork. One delivery schedule can replace many discrete purchase orders or contract release orders.

Delivery of the total quantity of materials specified in a scheduling agreement item is spread over a certain period in a delivery schedule, consisting of lines indicating the individual quantities with their corresponding planned delivery dates.

Your suppliers require shorter lead times. Smaller deliveries are required, which can be spaced out over a longer period. Delivery scheduling enables suppliers to plan and allocate their resources more efficiently.

In consignment processing, the supplier provides materials and delivers these to a consignment store.

The supplier remains the legal owner of the materials until these are withdrawn from the consignment stores.

Once withdrawn, the supplier requires payment.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data and Organizational Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM128 | RAW128,PD,Consignment |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 001 | Group 001 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BF6 | Create Scheduling Agreement - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Activate Flexible Workflow for Scheduling Agreement Approval

Purpose

In this procedure, you activate flexible workflow for Scheduling Agreement approval.

If you want to use the flexible workflow to manually approve the Scheduling Agreement, you have to process the steps: Activate Flexible Workflow for Scheduling Agreement Approval and Configure Flexible Workflow for Scheduling Agreement.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search item Activate Flexible Workflow for Purchase Scheduling Agreements, then click the line Scheduling Agreement Processing.On the Configure Your Solution – Scheduling Agreement Processing screen,In Configuration steps area, choose the Configure button for item Activate Flexible Workflow for Purchase Scheduling Agreements. | The Document Types Scheduling Agreement Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make the following entries and choose Save:Document Type Scenario based workflowLP Scheduling Agreement XLPA SA With Release doc. XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then click Continue. | The Scenario based workflow is active for Scheduling Agreements with Document Type: LP and LPA. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Activate Flexible Workflow for Scheduling Agreements | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Scheduling Agreements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Scheduling Agreement Change screen displays. |  |
| 3 | Activate Flexible Workflow for Scheduling Agreements Approval | Make the following entries and choose Save:Document Type Scenario based workflowLP Scheduling Agreement XLPA SA With Release doc. XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then click Continue. | The Scenario based workflow is active for Scheduling Agreements with Document Type: LP and LPA. |  |

#### Configure Flexible Workflow for Scheduling Agreement

Purpose

In this procedure, you configure your release conditions for scheduling agreement approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type LP has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration role. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Scheduling Agreements (F3044). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make following entries:Name: Test Workflow for Scheduling AgreementIn the Start Conditions area select Purchasing Group of scheduling agreement is with value: 001Choose Create Alternative Preconditions and make the following entries:Choose Document type of scheduling agreement is with value: LP Scheduling AgreementIn the Header area choose the Create button and make following entry:Step Type: Release of Scheduling AgreementIn Recipients area:Assignment By: UserUser: Select the User ID with Employee ID PURCHASING_MANAGER from F4 helpStep to be completed by: One of the recipientsChoose Create.Choose Save. | The workflow for scheduling agreement is configured. |  |
| 4 | Activate Workflow Item | Select the just created workflow item and choose Activate. | The workflow item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Scheduling Agreement has been activated. |

#### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this test script, the info records for the necessary materials must be available as master data. If the Info Record has not been maintained in the system yet, create the required master data. Otherwise you can skip this step.

The purpose of this activity is to create the info records for materials, for example, RM128 and choose a valid supplier (for example, 33300001).

This step is obsolete if the necessary info records are present. Check the info records supplier 33300001, material RM128 and Purchasing Organization 3310. The existing info records for this material are displayed on the screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: ConsignmentPurchasing Organization: 3310Supplier: 33300001Material: RM128Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 1000 | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 165Pricing Unit: 100Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Edit Supplier Invoice Settings (F3813) | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice, it will take effective immediately. For APP Create Supplier Invoice – Advanced, user needs to logout and login again to make it take effective. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition](#unique_12) [page ] 15 | Purchaser | Create Purchase Requisition - Advanced (ME51N) | A Purchase Requisition is created. |
| [Convert Purchase Requisition to Scheduling Agreement](#unique_13) [page ] 16 | Purchaser | Create Scheduling Agreement (ME31L) | A Schedule Agreement is created. |
| [Create Scheduling Agreement](#unique_14) [page ] 17 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Schedule Agreement is created. |
| [Approve Scheduling Agreement (Optional)](#unique_15) [page ] 18 | Purchasing Manager | My Inbox - All Items (F0862) | Schedule Agreements are changed. |
| [Maintain Delivery Schedule](#unique_16) [page ] 19 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Scheduling Agreement is approved. |
| [Print Scheduling Agreement](#unique_17) [page ] 20 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Delivery Schedule is created. |
| [Evaluate the Stock/Requirement Situation](#unique_18) [page ] 21 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | Material delivery scheduling lines are displayed. |
| [Post Goods Receipt](#unique_19) [page ] 23 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted against the scheduling agreement. |
| [Transfer Posting from Vendor Consigned Stock to Own Stock](#unique_20) [page ] 24 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The consignment material is transferred to its own stock. |
| Invoice Receipt from Consignment Withdrawal |  |  |  |
| [Option 1: Create Consignment settlement](#unique_21) [page ] 25 | Accounts Payable Accountant | Create Logistics Consignment and Pipeline Settlement (MRKON) | The Supplier Invoice is posted. |
| [Option 2: Schedule Supplier Invoice Jobs](#unique_22) [page ] 26 | Accounts Payable Accountant | ON PREMISE Schedule Supplier Invoice Jobs - Advanced (F1683) | The Supplier Invoice is posted. |
| [Check Supplier Invoice List (Optional)](#unique_23) [page ] 28 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoice is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Requisition

Purpose

Purchase Requisition can be created via MRP run or they can be created manually. In this procedure, you create a purchase requisition for stock material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad with the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Requisition - Advanced (ME51N) . | The Create Purchase Requisition view displays. |  |
| 3 | Enter Document type Data | Enter the following values:Document Type: RV Outl. Agmt Requisn |  |  |
| 4 | Enter Item Data | Make the following entries in the Item Overview area:Item Category: K(consignment stock)Material: RM128Quantity: 120000Plant: 3310 |  |  |
| 5 | Save | Choose Save at the bottom of the view.Make a note of the purchase requisition number. | A Purchase requisition is created. |  |

Result

Purchase Requisition has been created.

### Convert Purchase Requisition to Scheduling Agreement

Purpose

This activity is used to create the scheduling agreement for the material/supplier combination via converting purchase requisition, for example, material RM128and supplier 33300001, if it has not been maintained yet. If the scheduling agreement is already present in the system you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser . |  |  |
| 2 | Access the App | Open Create Scheduling Agreement (ME31L). | The Create Scheduling Agreement initial Screen view displays. |  |
| 3 | Select Purchase Requisition | On the Create Scheduling Agreement: Initial Screen view, choose Reference to PReq.Then in the Selection of Purchase Requisitions dialog box, enter the purchase requisition no. created before, and choose Continue. | The Selection of Purchase Requisitions dialog box displays. |  |
| 4 | Enter Agreement Data | On the Create Scheduling Agreement: Initial Screen view, enter the following values :Supplier: Create Scheduling Agreement: Initial Screen33300001Agreement type: LPAgreement Date: todayPurchasing Organization: 3310Purchasing Group: 001Plant:3310Storage Location : 331Cand choose Enter.Note If the Item Overview displays instead of the header data, then choose the Header Details button (F6). | The Create Scheduling Agreement Header Data view displays. |  |
| 5 | Enter Validity End Date | On the Create Scheduling Agreement Header Data view, enter the Validity end date, e.g. today + 720 daysand choose Enter. |  |  |
| 6 | Select Purchase Requisition | On the Create Scheduling Agreement: Selection List: Purchase Requisitions view, select the purchase requisition item line and choose Adopt. | The Create Scheduling Agreement Item overview view displays. |  |
| 7 | Enter Item Data | On the Create Scheduling Agreement Item Overview view, check the following entries:Item Category: K (consignment stock)Material: RM128Target Quantity: 120000 |  |  |
| 8 | Save | Choose Save at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

Result

Purchase Requisition has been created.

### Create Scheduling Agreement

Purpose

This activity is used to create the scheduling agreement for the material/supplier combination, for example, material RM128 and supplier 33300001 directly or without reference to any preceding purchasing document like Purchase Requisition, if it has not been maintained yet.

If the scheduling agreement is already present in the system you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser . |  |  |
| 2 | Access the App | Choose Manage Purchase Scheduling Agreements (F2179) . | The Create Scheduling Agreement initial view displays. |  |
| 3 | Enter Header Data | Create a new scheduling agreement with the following data:Agreement type: Scheduling Agreement (LP)Supplier: 33300001Valid Start: <today>Valid End: <MM/DD/YYYY>, for example, today + 720 dayPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310Target Value: 200000 AED |  |  |
| 4 | Add Items to Scheduling Agreement | From the New Scheduling Agreement view, choose the Items facets and select Create. | The New Scheduling Agreement Item view displays. |  |
| 5 | Enter Item Data | On the Items facets view, make the following entries:In the General Information viewItem Category: K (Consignment)Plant: 3310Material: RM128Target Quantity: 120000Choose Apply at the bottom of the view. |  |  |
| 6 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

### Approve Scheduling Agreement (Optional)

Purpose

In this procedure, you release a Scheduling Agreement . If the document type of scheduling agreement is LP and the purchase group is 001, then the scheduling agreement should trigger the approval process

Prerequisite

A Scheduling Agreement must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Purchasing Manager role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of already created Scheduling Agreement s is displayed. |  |
| 3 | Search for Scheduling Agreement Status | Enter the Scheduling Agreement number in the search area, then choose the Search button. | The Scheduling Agreement s without follow-on documents (w/o status Follow-On Documents) have the status In Approval. |  |
| 4 | Release Scheduling Agreement | Select the Scheduling Agreement in left of the screen and choose Release in bottom right. | The Submit Decision screen displays. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Scheduling Agreement is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

### Maintain Delivery Schedule

Purpose

The purpose of this activity is to create the delivery schedule for the scheduling agreement if it has not been maintained while creating the scheduling agreement

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the Fiori launchpad using the role Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier 33300001, Agreement Type LP (Scheduling Agreement), Purchasing Organization 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements . |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement page appears in display mode. |  |
| 5. | Maintain Delivery Schedule | 1. Click on the Edit at the right upper corner on the Manage Scheduling Agreement Header Object page.2. In Items tab, click on the desired item for which delivery schedule needs to be maintained. | The Purchase Scheduling Agreement Item screen displays. |  |
| 6. | Maintain Delivery Schedule | Go to the Schedule Lines section on the Purchase Scheduling Agreement Item screen and choose Create. You will get into the Purchase Scheduling Agreement Item screen to maintain the schedules for the item, make following entries:Date type: <Day format>Delivery Date: Today's dateDelivery Time: 10:00:00Scheduled Quantity: 10Choose Apply twice at the right bottom to add a schedule line. | You will be navigated back to Scheduling Agreement Header object page. |  |
| 7. | Save | Choose Save from the Scheduling Agreement Header object page. | Scheduling agreement will get updated with schedule lines. |  |

### Print Scheduling Agreement

Purpose

The purpose of this activity is to preview the scheduling agreement for the material/supplier combination for the new Scheduling agreement or for the one which is already present in the system

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Logon on to Fiori launchpad as Purchaser . | You will get into Manage Purchase Scheduling Agreements list page. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) app. |  |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier 33300001, Agreement Type LP, purchase org 3310, then choose Go button. Select one item from the search result. | The desired scheduling agree-ment appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode |  |
| 5. | View the output form for scheduling agreement | Goto Output controls facet & view the output settings maintained for the scheduling agreement. Click on the PDF sign to view the output form of scheduling agreement | PDF form for scheduling agreement shall open |  |

### Evaluate the Stock/Requirement Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The requirement planning has generated schedule lines in the scheduling agreement for material RM128. In this procedure you want to monitor the material coverage situation.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Material Planner - External Procurement. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) . | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Monitor Material Coverage screen select the user (on the top right corner),choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE 3310MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings. In the MRP Settings dialog box, check Check Material Coverage - Old Version (F0251) that if toggle button is ON.Turn it ON if the toggle button is OFF. | If the toggle button is ON, in following steps, it will be navigated to Check Material Coverage - Old Version (F0251).If the toggle button is OFF, in following steps, it will be navigated to Check Material Coverage - Old Version (F0251).In following steps, we describe the steps when the toggle button is ON. |  |
| 5 | Search for Material | On the Monitor Material Coverage - Net and Individual Segments screen, make the following entries and choose Go.Material: RM128 | The relevant material displays. |  |
| 6 | Select Material | Select the checkbox before the Materials No., and then choose Manage Materials. | The Material screen and Material Details screen display. |  |
| 7 | Review Stock/Requirements List | Select the corresponding material on the left Material screen. | The detailed Stock/Requirements List for each material displays. |  |
| 8 | Open Quickview for MRP Element | On the Material Details screen, click the SchLne XXXX in column MRP Element. | The SchLne XXX you clicked will display on the pop-up. |  |
| 9 | Open Scheduling Agreement | On the Pop-up SchLne XXX screen, choose Display Scheduling Agreement. | The Display Scheduling Agreement: Item Overview screen displays. |  |
| 10 | Display Delivery Schedule | Check the checkbox before the item no., and then choose More > Delivery Schedule . | The Display Scheduling Agreement:Delivery Schedule for Item XXX screen displays.The system displays the scheduled quantity and dates. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt Purchase Order screen appears. |  |
| 3 | Enter Purchase Order | Enter the scheduling agreement number and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted.Enter the delivered quantity and check storage location to be posted.You can click on Cheveron (>) to check the special stock indicator K is set (Supplier Consignment), and then choose Apply. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system is displayed the message 1 material document(s) posted: 5xxxxxxxxx 2xxx. The material is posted to the unrestricted use stock of vendor consignment with storage location 331C and plant 3310 and 33300001. You can display the stock overview in APP Display Stock Overview. |  |

### Transfer Posting from Vendor Consigned Stock to Own Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To consume the consigned inventory, you can either transfer the stock from consigned to the own inventory or issue directly from the consigned inventory (for example in reference to a production order). In this test script, stock is transferred from the consignment stock to the own inventory by transfer posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock – In-Plant screen displays. |  |
| 3 | Open Stock Overview | Enter the following data in the fields:Material: RM128Plant: 3310 | The Stock Overview of the Material is shown. |  |
| 4 | Select stock | Select the icon beside the stock that you want to transfer (Unrestricted-Use Stock, Storage location 331C). | A dialog box opens with Special Stocks, Stock Type, and current Quantity. |  |
| 5 | Select Special Stock | Select item K (Supplier Consignment). |  |  |
| 6 | Select stock | Select the icon beside the stock that you want to transfer (Unrestricted-Use Stock, Storage location 331C) again. | A dialog box opens with Special Stocks, Stock Type, and current Quantity are displayed. |  |
| 7 | Select Special Stock | Select item Unrestricted-Use Stock. | A dialog box opens. The Storage Location, Stock Type, current Quantity, Special Stock Type and Supplier are displayed according to your entries in the previous steps. |  |
| 8 | Transfer Items | Enter the following data in the following data fields. Choose Enter and then choose Post .Document Date: <Today>Posting Date: <Today>Quantity: x PC | The system displaysMaterial document xxx created.The stock has been transferred. |  |

### Invoice Receipt from Consignment Withdrawal

#### Option 1: Create Consignment settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The liabilities should be cleared regularly towards the supplier because of goods issues from the vendor consignment stock. The consignment goods are settled with invoice receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Accounts Payable Accountant . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Logistics Consignment and Pipeline Settlement (MRKON) . | The Consignment and Pipeline Settlement screen displays. |  |
| 3 | Enter parameter | On the selection screen, enter the following values then choose Enter:Company Code: 3310Supplier : 33300001Plant: 3310Material Document: （optional） Enter the material document number created from the last stepConsignment: SelectedPipeline: DeselectedSettle: SelectedTax Date: <Today>Note If RITA is active, the Tax Date will display, which is the key date for calculating tax, please maintain it carefully according to your financial business requirements.Withdrawals Not Settled: Selected |  |  |
| 4 | Execute | Choose Run. | The invoice is posted. |  |
| 5 | View settlement document | On the Logistic Consignment and Pipeline Settlement screen, you can see the invoice document number under column Doc. No.. | The settlement document is created. |  |

#### Option 2: Schedule Supplier Invoice Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Scheduling supplier invoice jobs is especially effective if you create settlement documents periodically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Supplier Invoice Jobs - Advanced (F1683). | The Application Jobs screen is displayed. |  |
| 3 | Create Application Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Execute Consignment settlement | Make the following entries:In the 1. Template Selection section, from the drop-down box of Job Template, choose Logistic Consignment and Pipeline Settlement.Click Step 2. In the Scheduling Options section, make sure that Start Immediately checkbox is checked. Or you can also set the start date and start time.Click Step 3, in the Parameter section, make the following entries:Company Code: for example, 3310Supplier: 33300001Plant: for example, 3310Material Document: Enter the material document number created from the last step.Consignment: SelectedPipeline: DeselectedDisplay: SelectedTax Date: <Today>Note The Tax Date is the key date for calculating tax, please maintain it carefully according to your financial business requirements.Withdrawals Not Settled: SelectedChoose Check. | The system message displays: You can go ahead and schedule the job. |  |
| 5 | Schedule the job without Test Run | Select Settle and then choose Schedule. |  |  |
| 6 | Check the result | In the Application Jobs screen, find the job you created. You may need to wait several minutes and refresh to see the results after the job status becomes finished.Choose Results. | The detailed log is displayed in the Document (ID, XXXXX) screen. You can find the corresponding Document number and FI Document number created. |  |

### Check Supplier Invoice List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can review the document created in the last step and get the generated consignment settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Fiori Launchpad tile | Open the Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the document | On the Supplier Invoices List screen, enter the following values, then choose Go:Invoicing Party : 33300001Company Code: 3310 | Invoices list is displayed. |  |
| 4 | Go to the invoice detailed page | Choose the invoice you created, whose Entry Type is Consignment. | The screen will be navigated to the Supplier Invoice detailed page. |  |
| 5 | Display the document | On the Supplier Invoice screen, go to the Output tab. In the Output Details table, find the line with Output Type of CONSIGNMENT_SETTLEMENT. Choose Display Document in the Preview column. | The document (in this case, Consignment Stock Accounting) is displayed. |  |
| 6 | Download the document | Download the document. | The document is downloaded to your local workspace. |  |
| 7 | Send Documents to Supplier | Send the downloaded document to the supplier as printed document, or by fax or by e-mail or via the Internet.The step is executed offline. | The document is sent to the supplier. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Fiori Overview Pages for Procurement (1JI) | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reports.The Global Filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups and more.Via contextual navigation the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or get more detailed information in the corresponding KPI Drill-Downs. |

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
> Flagged while digesting this document, not verified: The Overview Table's Expected Results appear offset from the procedures: Approve Scheduling Agreement shows 'Schedule Agreements are changed', Maintain Delivery Schedule shows 'A Scheduling Agreement is approved' and Print Scheduling Agreement shows 'A Delivery Schedule is created', which do not match those procedure sections.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Evaluate the Stock/Requirement Situation step 4 states both the ON and OFF positions of the Check Material Coverage - Old Version (F0251) toggle navigate to F0251, so the ON/OFF distinction is contradictory.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/scheduling-agreements-in-procurement-bmr-ae-test-script-sap-s-4hana-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NY_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 48,544 chars in the whole document
