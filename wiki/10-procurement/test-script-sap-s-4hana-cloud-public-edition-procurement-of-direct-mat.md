---
id: 10-procurement/test-script-sap-s-4hana-cloud-public-edition-procurement-of-direct-mat
title: Test Script SAP S/4HANA Cloud Public Edition - Procurement of Direct Materials (J45_AE) (J45_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item J45: direct-material procurement from requisition to PO, goods receipt, invoice, plus optional variants."
cluster: 10-procurement
tags: [kb/procurement, topic/direct-material-procurement]
aliases: [J45_S4CLD2608_BPD_EN_AE]
keywords: [Direct Material Procurement, direct materials procurement, purchase orders, purchase requisitions, automatic purchase order creation, goods receipt, supplier invoices, purchase order workflow, down payments, cash discount situations]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J45_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1301
topic: 10-procurement/direct-material-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Procurement of Direct Materials (J45_AE) (J45_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J45_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Direct Material Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 01-09-26 |
| --- | --- |
|  | Procurement of Direct Materials (J45_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc239512757)

[2 Prerequisites 6](#_Toc239512758)

[2.1 System Access 6](#_Toc239512759)

[2.2 Roles 6](#_Toc239512760)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc239512761)

[2.4 Additional Manual Configuration 9](#_Toc239512762)

[2.5 Business Conditions 9](#_Toc239512763)

[2.6 Preliminary Steps 9](#_Toc239512764)

[2.6.1 Maintain HSN/SAC Code 9](#_Toc239512765)

[2.6.2 Open New MM Period 10](#_Toc239512766)

[2.6.3 Create Purchasing Info Record (Optional) 10](#_Toc239512767)

[2.6.4 Create Purchase Requisition 13](#_Toc239512768)

[2.6.5 Check Flexible Workflow for Purchase Order Approval 14](#_Toc239512769)

[2.6.6 Configure Flexible Workflow for Purchase Order 16](#_Toc239512770)

[2.6.7 Manage Conditions to Restart Flexible Workflow 17](#_Toc239512771)

[2.6.8 Create Ready-to-Use Situation Type for Cash Discount at Risk (Optional) 18](#_Toc239512772)

[2.6.9 Create Team and Responsibilities (Optional) 19](#_Toc239512773)

[2.6.10 Master Data Update for Automatic Purchase Order Creation from Purchase Requisition 20](#_Toc239512774)

[2.6.10.1 Change Material Master Data - Purchasing Data 20](#_Toc239512775)

[2.6.10.2 Change Supplier Master Data - Purchasing Organization Data 22](#_Toc239512776)

[2.6.10.3 Generate Source List 23](#_Toc239512777)

[2.6.11 Edit User-Specific Parameters for Supplier Invoices (Optional) 24](#_Toc239512778)

[3 Overview Table 26](#_Toc239512779)

[4 Test Procedures 29](#_Toc239512780)

[4.1 Procurement of Stock Material 29](#_Toc239512781)

[4.1.1 Convert Purchase Requisitions to Purchase Orders 29](#_Toc239512782)

[4.1.2 Create Purchase Order 30](#_Toc239512783)

[4.1.3 Approve Purchase Order (Optional) 33](#_Toc239512784)

[4.1.4 Preview Purchase Order (Optional) 34](#_Toc239512785)

[4.1.5 Change Purchase Order (Optional) 35](#_Toc239512786)

[4.1.6 Monitor Purchase Order Items (Optional) 36](#_Toc239512787)

[4.1.7 Execute Mass Changes to Purchase Orders (Optional) 37](#_Toc239512788)

[4.1.8 Create Supplier Confirmation (Optional) 38](#_Toc239512789)

[4.1.8.1 Create Purchase Order with Confirmation (Optional) 39](#_Toc239512790)

[4.1.8.2 Create Supplier Confirmation (Optional) 40](#_Toc239512791)

[4.1.8.3 Approve Supplier Confirmation (Optional) 42](#_Toc239512792)

[4.1.8.4 Manage Supplier Confirmation (Optional) 42](#_Toc239512793)

[4.1.9 Post Goods Receipt 44](#_Toc239512794)

[4.1.10 Preview Goods Receipt Slip and Label (Optional) 45](#_Toc239512795)

[4.1.11 Check Goods Receipt Details (Optional) 46](#_Toc239512796)

[4.1.12 Reverse Goods Receipt (Optional) 47](#_Toc239512797)

[4.1.13 Analyze Stock Overview (Optional) 48](#_Toc239512798)

[4.1.14 Analyze Material Document (Optional) 49](#_Toc239512799)

[4.1.15 Manage Stock (Optional) 50](#_Toc239512800)

[4.1.16 Create Supplier Invoice 51](#_Toc239512801)

[4.1.16.1 Option A: Create Supplier Invoice with PO/GR Relation 51](#_Toc239512802)

[4.1.16.2 Option A: Create Supplier Invoice for Custom Duty (Optional) 53](#_Toc239512803)

[4.1.16.3 Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction) (Optional) 55](#_Toc239512804)

[4.1.16.4 Option B: Print Complaint Letter in case of Invoice Reduction (Only relevant for SAP S/4HANA Cloud Public Edition) 57](#_Toc239512805)

[4.1.16.5 Create Supplier Invoice without PO/GR (Optional) 58](#_Toc239512806)

[4.1.17 Detect Critical Cash Discount Situations (Optional) 60](#_Toc239512807)

[4.1.18 React to Critical Cash Discount Situations (Optional) 60](#_Toc239512808)

[4.1.19 Create Credit Memo (Optional) 62](#_Toc239512809)

[4.1.20 Check Supplier Invoice List (Optional) 64](#_Toc239512810)

[4.1.21 Approve Supplier Invoice (Optional) 65](#_Toc239512811)

[4.1.22 Reverse Invoice (Optional) 66](#_Toc239512812)

[4.1.23 Clear GR / IR (Optional) 67](#_Toc239512813)

[4.1.24 Cancel Journal Entry (Optional) 68](#_Toc239512814)

[4.1.25 Monitor Down Payment process 69](#_Toc239512815)

[4.1.25.1 Create Purchase Order Manually for Down Payment 69](#_Toc239512816)

[4.1.25.2 Monitor Down Payments (Optional) 70](#_Toc239512817)

[4.1.25.3 Create Down Payment Request 71](#_Toc239512818)

[4.1.25.4 Create Down Payment 73](#_Toc239512819)

[4.1.25.5 Post Goods Receipt 75](#_Toc239512820)

[4.1.25.6 Create Supplier Invoice for Down Payment (Optional) 76](#_Toc239512821)

[4.2 Automatic Purchase Order Creation from Purchase Requisition 77](#_Toc239512822)

[4.2.1 Create Purchase Requisition 77](#_Toc239512823)

[4.2.2 Automatic Conversion of Purchase Requisition to Purchase Order 79](#_Toc239512824)

[4.2.3 Post Goods Receipt 80](#_Toc239512825)

[4.2.4 Create Supplier Invoice 81](#_Toc239512826)

[5 Appendix 84](#_Toc239512827)

[5.1 Process Integration 84](#_Toc239512828)

[5.1.1 Succeeding Processes 84](#_Toc239512829)

[5.1.2 Goods Receipt Blocked Stock 84](#_Toc239512830)

[5.1.2.1 Post Goods Receipt Blocked Stock 84](#_Toc239512831)

[5.1.2.2 Release Goods Receipt Blocked Stock 85](#_Toc239512832)

[5.1.3 Setup Mail Notification for Purchase Order Workflow 87](#_Toc239512833)

[5.1.4 Setup Mail Notification for Purchase Order Deadline 88](#_Toc239512834)

[5.1.5 Configure Deadline in Manage Workflows for Purchase Orders 89](#_Toc239512835)

[5.1.6 Free Goods Purchasing 91](#_Toc239512836)

[5.1.6.1 Change Material Master Data – For Free Goods 91](#_Toc239512837)

[5.1.6.2 Change Supplier Master Data - For Free Goods 92](#_Toc239512838)

[5.1.6.3 Create Purchasing Info Record 93](#_Toc239512839)

[5.1.6.4 Create Purchase Order Manually for Free Goods 95](#_Toc239512840)

[5.1.7 Quantity Optimization for Purchase Order 96](#_Toc239512841)

[5.1.7.1 Setup a Static Rounding Profile 96](#_Toc239512842)

[5.1.7.2 Maintain a Rounding Profile in the Purchasing Info Record 100](#_Toc239512843)

[5.1.7.3 Create Purchase Order with Quantity Optimization 103](#_Toc239512844)

[5.1.7.4 Simulate Quantity Optimizing 105](#_Toc239512845)

[5.1.8 Rework Flexible Workflow for Purchase Orders 106](#_Toc239512846)

[5.1.8.1 Activate Inquiry Workflow for Purchase Orders 106](#_Toc239512847)

[5.1.8.2 Configure Rework Flexible Workflow for Purchase Orders 108](#_Toc239512848)

[5.1.8.3 Rework Purchase Order 109](#_Toc239512849)

[5.1.9 Dunning Reminder for Purchase Orders 109](#_Toc239512850)

[5.1.9.1 Output Parameter Determination for Purchase Orders Dunning Reminder 110](#_Toc239512851)

[5.1.9.2 Create Purchase Order for Dunning Reminder 112](#_Toc239512852)

[5.1.9.3 Dunning Reminder on Purchase Orders Advanced 113](#_Toc239512853)

[5.1.9.4 Schedule Dunning Reminder Output for Purchase Orders (Optional) 114](#_Toc239512854)

[5.1.10 Custom Attributes in Task Cards for Purchase Order Workflow (Optional) 116](#_Toc239512855)

[5.1.10.1 Maintain CDS Based Custom Attributes for Purchase Order Workflow (Optional) 116](#_Toc239512856)

[5.1.10.2 Approve Purchase Order through Task Cards (Optional) 124](#_Toc239512857)

[5.1.11 Purchase Order Workflow Review 125](#_Toc239512858)

[5.1.11.1 Configure Purchase Order Flexible Workflow for Review 125](#_Toc239512859)

[5.1.11.2 Review Purchase Order Items (Optional) 126](#_Toc239512860)

[5.1.12 Ad-hoc Approver in Purchase Order Workflow 127](#_Toc239512861)

[5.1.12.1 Configure Flexible Workflow for Purchase Orders 127](#_Toc239512862)

[5.1.12.2 Create Purchase Order to Add Ad-hoc Workflow Steps 128](#_Toc239512863)

[5.1.12.3 Approve Purchase Order 131](#_Toc239512864)

[5.1.13 Output Channel External Output Management for Purchase Order 131](#_Toc239512865)

[5.1.13.1 Manage Output Queues for External Output Management 132](#_Toc239512866)

[5.1.13.2 Output Parameter Determination for Purchase Orders External Output Management Channel 133](#_Toc239512867)

[5.1.13.3 Create Purchase Order External Output Management Channel 135](#_Toc239512868)

[5.1.13.4 Create Purchase Order External Output Management Channel for Dunning Reminder 136](#_Toc239512869)

[5.1.13.5 Dunning Reminder on Purchase Order for External Output Management 137](#_Toc239512870)

[5.2 Relevant Features 139](#_Toc239512871)

## Purpose

Overview

This purchasing process uses purchase requisitions that are generated either by the Material Requirements Planning (MRP) process or manually by a requester. The conversion from a purchase requisition to a purchase order can either be done manually (in case adoptions are necessary) or automatically (applicable for large volumes). Alternatively, the purchase orders can be generated manually.

The purchase order can be subject to approval before being issued to a supplier. Goods are shipped from the supplier and the goods receipt is created with reference to the corresponding purchase order. Subsequently the invoicing process is triggered. The user can monitor the progress throughout the entire procurement process and can initiate reactive actions if needed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/J45_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Standard storage 1 | Shop floor w/o lean WM |
| Storage Location | 331B | Standard storage 2 | Shop floor w/o lean WM |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001/002 | Group 001/Group 002 | depending on material |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Supplier | 33300003 | Domestic UAE Supplier 3 |  |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/47fe5fb3ea8515cab641f87fe7fb7145)

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |
| 31N - Situation Handling | You install this scope item for the situation handling steps. |

### Preliminary Steps

#### Maintain HSN/SAC Code

Purpose

In this procedure, you maintain HSN/SAC Code for each material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to Fiori Launchpad as a Master Data Specialist - Product Data . | The Fiori launchpad is displayed. |  |
| 2 | Open the Fiori App | Open Change Material (MM02) . | The Monitor Material Coverage screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Continue.Material: TG0011 | The Change Material TG0011 screen is displayed. |  |
| 4 | Select View(s) | On the Select View(s) screen, make the following entries:International Trade: Import: selectChoose Org. Levels:Plant:3310.Choose Continue. |  |  |
| 5 | Maintain HSN/SAC | In the Control code field, press F4.Country Key : AEChoose Find.Control Code: Select one control code from the list: 02 01 10 00 For example. Choose Copy.Choose Save. | Material XXX changed. |  |

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period:

Closing MM Period and Opening New Posting Period

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
| Note If the Info Record for the material TG0011 and suppliers (33300001, 33300002 and 33300003) already exists in the system, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: TG0011Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 31.12.9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Tax Rate Valid From: Select value from F4 helpNote If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 10Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12.31.9999Amount: 10Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create your data | Choose Create. | The purchasing info record is created. |  |

|  |
| --- |
| Note TG0011 and Supplier 33300002, its net price is 35AED. |

|  |
| --- |
| Note Repeat the above step to create the Info Record for Material TG0011 and Supplier 33300003, its purchase group is 001, and its net price is 25AED. Repeat the above steps and for step 7, don’t select No Evaluated Receipt Settlement. |

#### Create Purchase Requisition

Purpose

Purchase Requisition can be created via MRP run (refer to J44 - Material Requirements Planning ) or they can be created manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229) . | The Manage Purchase Requisitions - Professional screen displays. |  |
| 3 | Create New Purchase Requisition | Choose Create. | The Purchase Requisition screen displays. |  |
| 4 | Enter Document Type | From the Document Type drop-down, select Pur. Requisition (NB). |  |  |
| 5 | Add Item | In the Items section, choose Create then choose Material. | The Purchase Requisition screen displays. |  |
| 6 | Enter detail data | Enter the following values in the General Information section:Item Category: StandardMaterial: TG0011Plant: 3310Enter the following values in the Quantity and Date section:Quantity:10Delivery Date: default valueRequisition Date: default valueRelease Date: default valueEnter the following values in the Contact Information section:Requirement Tracking Number: For example, TestTrackPurchasing Organization:3310Purchasing Group:001 or 002Choose Apply. And you automatically go back to the Purchase Requisition screen. |  |  |
| 7 | Create your entries | Choose Create.Choose Create to confirm the popup message. | A purchase requisition is created. |  |

Result

The Purchase Requisition is created.

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
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Manage Conditions to Restart Flexible Workflow

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

#### Create Ready-to-Use Situation Type for Cash Discount at Risk (Optional)

Purpose

In this procedure, you create ready-to-use situation type for cash discount at risk.

|  |
| --- |
| Note Please make sure 31N is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Business Process Specialist role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Copy standard template | Choose Situation Templates tab and choose Go to display standard situation templates.Choose situation template with ID: MM_CASHDISCOUNTATRISK and choose Copy. | The Situation Type screen displays. |  |
| 4 | Create custom Situation Type | On the Situation Type screen, make the following entries:ID: Z_MM_CASHDISCOUNTATRISK (for example).Name: Cash Discount at Risk;Display Sequence: HighGo to section Conditions and make sure that Processing Order 1 is set as Open, and Send Notification is selected.On the Used Filters section, remove all values for Criteria Cash Discnt Due Date, and ensure it is blank.Go to section Batch Job Scheduling and make the following entries:Time Zone: Any Data (select a time zone from input help based on your location)Start Batch Job At: Any DataGo to section Situation Display.Message Details: <default value>Go to section Notifications and do the following:Aggregate Notifications: Select.Resend Notifications: Select.Go to section Recipients.Filter by Member Function: Select Operational Purchasing from the dropdown list.Go to section Situation Monitoring and select Monitor Instances. |  |  |
| 5 | Save Situation Type | Choose Create. | The Situation Type is created. |  |
| 6 | Enable Situation Type | From the Enable Situation Type dialog box, select Yes. | The Situation Type is enabled. |  |

#### Create Team and Responsibilities (Optional)

Purpose

In this procedure, you create team and responsibilities for Cash Discount at Risk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412) . | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create team and responsibilities | Choose Create and make following entries:Name: Z_MM_CASHDISCOUNTATRISKGlobal ID: Z_MM_CASHDISCOUNTATRISKDescription: for Cash Discount at RiskStatus: EnabledType: OPPURGo to Team Owners area, the default team owner value will display. If the default team owner does not display, then choose Create, and make the following entries:Business Partner: Select from F4 help help. For example: search Last Name for *Bpc_expert* to get the user ID.Go to Team Members area, choose Create, and make the following entry:Business Partner: Select from F4 help. For example: search Last Name for *APAccountant* to get the user ID.Choose OK.Functions: Select OP_PURCH from F4 help |  |  |
| 4 | Save Team | Choose Create. | The team is created. |  |

#### Master Data Update for Automatic Purchase Order Creation from Purchase Requisition

|  |
| --- |
| Note If you want to perform the step [Automatic Purchase Order Creation from Purchase Requisition](#unique_18) [page ] 77, run these Preliminary steps. |

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

The following procedure provides instructions for changing material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Master Data Specialist - Product Data role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Change Material (MM02). | The Change Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | On the Change Material screen, make the following entries:Material: for example, TG0011Choose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Choose Views | On the Select View(s) screen, choose Purchasing and Continue. | The Organizational Levels displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, make the following entries:Plant: <Plant>, for example, 3310Choose Continue. | The Change Material XXXXX (Material general) displays. |  |
| 6 | Select Autom.PO | Scroll down to the General Data section and select the following:Autom.PO: <selected> | Autom.PO is selected. |  |
| 7 | Save your data | Choose Save. | The material master data is updated. |  |

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
| 3 | Enter Business Partner | Make the following entry and choose Enter:Find: Business PartnerBy: Supplier NumberSupplier Number: for example,33300001Choose Start. The Supplier row displays.Double-click the Supplier Partner row. | The Supplier information screen displays. |  |
| 4 | Switch to Change mode | Ensure you are in Change mode. Otherwise, select Switch Between Display and Change. | The Change mode screen displays. |  |
| 5 | Change BP role | In the Change in BP role field, choose the following value: Supplier (defined) |  |  |
| 6 | Open Purchasing Organization Data | Choose the Purchasing tab at the top of the screen. | The Purchasing Organization sub section screen displays. |  |
| 7 | Enter Purchasing Data | Choose Switch Organization.Make the following entry and choose Enter:Purch. Organization: <Purchasing Organization>, for example, 3310 |  |  |
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
| 4 | Enter General Information | Go to General Information area and make the following entries:MaterialTG0011Plant: : for example, <Plant>, for example, 3310Choose Generate. |  |  |
| 5 | Search these Sources for the Material and Plant | On the Generated Sources sceen, make the following entries:Valid From: <Current Date>Valid To: <31.12.9999>Choose Go, | The Sources are displayed. |  |
| 6 | Choose Sources | Go to Sources (X) area.Choose all lines of items.Choose Replace Existing.If you have warning message, choose OK. |  |  |
| 7 | Choose a fixed Source | Go to Supplier 33300001 and make the following entry:Status: Fixed Status (Fixed) | The Supplier has been assigned to Fixed Supplier. |  |
| 8 | Save your Data | Choose Create. | The Source List is created. |  |

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

Table 2: Procurement of Stock Material

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Convert Purchase Requisitions to Purchase Orders](#unique_24) [page ] 29 | Purchaser | Process Purchase Requisitions (F1048A) | A list of Requisitions is displayed. |
| [Create Purchase Order](#unique_25) [page ] 30 | Purchaser | Manage Purchase Orders (F0842A) | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. |
| [Approve Purchase Order (Optional)](#unique_26) [page ] 33 | Purchasing Manager | My Inbox - All Items (F0862) | A list of already created Purchase Orders is displayed. |
| [Preview Purchase Order (Optional)](#unique_27) [page ] 34 | Purchaser | Manage Purchase Orders (F0842A) | The Manage Purchase Orders screen is displayed.A list of already created Purchase Orders is displayed. |
| [Change Purchase Order (Optional)](#unique_28) [page ] 35 | Purchaser | Manage Purchase Orders (F0842A) | The Manage Purchase Orders screen is displayed.A list of already created Purchase Orders is displayed. |
| [Monitor Purchase Order Items (Optional)](#unique_29) [page ] 36 | Purchaser | Monitor Purchase Order Items (F2358) | The Monitor Purchase Order Items screen is displayed also, the numbers of current overdue PO items are listed. |
| [Execute Mass Changes to Purchase Orders (Optional)](#unique_30) [page ] 37 | Purchaser | Mass Changes to Purchase Orders (F2593) | The Mass Changes to Purchase Orders screen is displayed. |
| [Post Goods Receipt](#unique_31) [page ] 44 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchase Order screen is displayed. |
| [Preview Goods Receipt Slip and Label (Optional)](#unique_32) [page ] 45 | Warehouse Clerk | Material Documents Overview (F1077) | The Material Documents Overview is displayed. |
| [Check Goods Receipt Details (Optional)](#unique_33) [page ] 46 | Warehouse Clerk | Material Documents Overview (F1077) | The Material Documents Overview is displayed. |
| [Reverse Goods Receipt (Optional)](#unique_34) [page ] 47 | Warehouse Clerk | Material Documents Overview (F1077) | The Material Documents Overview is displayed. |
| [Analyze Stock Overview (Optional)](#unique_35) [page ] 48 | Inventory Manager | Stock - Single Material (F1076) | The Stock Single Material screen is displayed. |
| [Analyze Material Document (Optional)](#unique_36) [page ] 49 | Inventory Manager | Material Documents Overview (F1077) | The Material Document Overview screen displayed. |
| [Manage Stock (Optional)](#unique_37) [page ] 50 | Inventory Manager | Manage Stock (F1062) | The Manage Stock screen is displayed. |
| [Create Supplier Invoice](#unique_38) [page ] 51 |  |  |  |
| [Option A: Create Supplier Invoice with PO/GR Relation](#unique_39) [page ] 51 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoices screen is displayed. |
| [Option A: Create Supplier Invoice for Custom Duty (Optional)](#unique_40) [page ] 53 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The supplier invoice for Custom Duty is created. |
| [Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction) (Optional)](#unique_41) [page ] 55 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoices screen is displayed. |
| [Option B: Print Complaint Letter in case of Invoice Reduction (Only relevant for SAP S/4HANA Cloud Public Edition)](#unique_42) [page ] 57(Cloud) | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoice List screen is displayed. |
| [Create Supplier Invoice without PO/GR (Optional)](#unique_43) [page ] 58 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoice screen is displayed. |
| [Detect Critical Cash Discount Situations (Optional)](#unique_44) [page ] 60 |  |  |  |
| [React to Critical Cash Discount Situations (Optional)](#unique_45) [page ] 60 | Accounts Payable Accountant | Supplier Invoices List (F1060A) |  |
| [Create Credit Memo (Optional)](#unique_46) [page ] 62 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Credit Memo is created |
| [Check Supplier Invoice List (Optional)](#unique_47) [page ] 64 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoices list screen is displayed. |
| [Approve Supplier Invoice (Optional)](#unique_48) [page ] 65 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoices list screen is displayed. |
| [Reverse Invoice (Optional)](#unique_49) [page ] 66 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoices list screen is displayed. |
| [Clear GR / IR (Optional)](#unique_50) [page ] 67 | Accounts Payable Accountant | Clear GR/IR Clearing Account (MR11) | The Clear GR / IR Clearing Account screen opens |
| [Cancel Journal Entry (Optional)](#unique_51) [page ] 68 | Accounts Payable Accountant | Display/Cancel Account Maintenance Document (MR11SHOW) | The Display / Cancel Account Maintenance Document screen opens |
| Monitor Down Payment process |  |  |  |
| [Create Purchase Order Manually for Down Payment](#unique_52) [page ] 69 | Purchaser | Create Purchase Order - Advanced (ME21N) | The Create Purchase Order screen is displayed. |
| [Monitor Down Payments (Optional)](#unique_53) [page ] 70 | Accounts Payable Accountant | Monitor Purchase Order Down Payments (F2877) | The Monitor Purchase Order Down Payments screen displays. |
| [Create Down Payment Request](#unique_54) [page ] 71 | Accounts Payable Accountant | Monitor Purchase Order Down Payments (F2877) | The Monitor Purchase Order Down Payments screen displays. |
| [Create Down Payment](#unique_55) [page ] 73 | Accounts Payable Accountant | Post Outgoing Payments (F1612) | The Monitor Purchase Order Down Payments screen displays. |
| [Post Goods Receipt](#unique_56) [page ] 75 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchase Order screen is displayed. |
| [Create Supplier Invoice for Down Payment (Optional)](#unique_57) [page ] 76 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) . | The Create Supplier Invoices screen is displayed. |
| [Automatic Purchase Order Creation from Purchase Requisition](#unique_18) [page ] 77 |  |  |  |
| [Create Purchase Requisition](#unique_58) [page ] 77 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Manage Purchase Requisitions - Professional screen is displayed. |
| [Automatic Conversion of Purchase Requisition to Purchase Order](#unique_59) [page ] 79 | Purchaser | Schedule Purchasing Jobs - Advanced (F1702) | The Application Jobs screen is displayed. |
| [Post Goods Receipt](#unique_60) [page ] 80 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchasing Document screen is displayed. |
| [Create Supplier Invoice](#unique_61) [page ] 81 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoices screen is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Procurement of Stock Material

#### Convert Purchase Requisitions to Purchase Orders

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
| 2 | Access App | Open Process Purchase Requisitions (F1048A) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | Process Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the purchase requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | Choose Show More per Row button on the side of Create RFQ. If the purchase requisition has been assigned the source, then you don't need to assign source again for this step. If the Purchase Requisition hasn't been assigned the source, choose Quick Edit, and then enter a source. | The assignment of one source to the requisition is done. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order. | The Purchase Order Preview screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchasing Doc. Type: Standard PO.Choose Order. | The purchase order is created. |  |
| 8 | Back to Process Purchase Requisition | Click on Back to go to Process Purchase Requisitions (F1048A). | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |

#### Create Purchase Order

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
| 4 | Enter Purchase Order Data | Enter all of the necessary data.On the General Information tab, make the following entries:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300001Company Code: 3310Purchasing Organization: 3310Purchasing Group: 001Currency: AEDOn the Delivery and Invoice tab, make the following entries and choose Enter:Payment Terms: 0003Go to Supplier Contact Data tab, the Supplier Address, Telephone, Fax, Contact Person are shown.On the Notes tab, choose > or < to search for Header Text. On the Header text column, enter the free text: xxx for testing.On the Items tab, from the Purchase Order Items screen, choose Create and make the following entries:Material: TG0011Plant: 3310Order Quantity: <quantity>Net Order Price: <price>Navigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.On the General Information tab, make the following entry:Storage Location: 331AGo to the Delivery Address tab and then navigate to the Address field. Click on the F4 value help to select the Address Number, and then choose Enter.Note This step is optional. If there is no appropriate Address Number in the system for usage, please skip this step.From the Purchase Order Item section, choose Process Flow tab.The following entries display:Goods Receipt: yesInvoice Receipt: <selected>Verify Goods-Receipt-Based Invoice Verification is selected.On the tab Tax, check the following entries:Tax Code: <Default Value>Tax Date: <Default Value>On the Schedule Lines tab, make the following entry:Delivery date: <a date in the future>From the Purchase Order Item section, choose Attachments tab.Select Doc. Type to Upload: For External UseChoose Upload to upload an attachment.Note If you want your purchase order to be assigned to an approver, choose a quantity and total net amount of purchase order higher than 500AED (for Purchase Groups = 003) | The Purchase Order screen is displayed. |  |
| 5 | Add Custom duty | From the Purchase Order Item section, choose the Pricing tab.Choose Add pricing elements (+) icon at the bottom of the Pricing Elements panel.Enter Condition Types: TAE1(AE Import Cust. Duty) for custom duty and choose Enter.Enter the following values:Condition type: TAE1Price Element Amount: 5%Choose Add, then the custom duty condition will be inserted into the Pricing Element panel.Choose Apply to go back to the Purchaser Order screen. |  |  |
| 6 | Add Freight Cost | From the Purchase Order Item section, choose the Pricing tab.Choose Create.In the Add Price Element section, enter one of the following three condition types for freight and choose Enter:FGW1 (Freight / Gr. Weight 1), freight is calculated based on gross weight.FQU1 (Freight / Quantity 1), freight is calculated based on quantity.FVA1 (Freight / Value 1), freight is a fixed value.If you use FQU1 as an example, enter the following values:Condition type: FQU1Amount16 AED Per PCChoose Add, then the freight cost condition will be inserted into the Pricing Element panel.Choose Apply to go back Purchaser Order screen. |  |  |
| 7 | Generate Output Preview (Optional) | Click the Output Preview button on the header of the purchase order and select the output option as required.Note The Output Preview button is only avaliable when your purchase order is in status Draft, In Approval, Not Yet Sent, or Output Error. | An output preview in PDF format is generated. |  |
| 8 | Verify Purchase Order for Completeness and Save Purchase Order | Choose Order to save the Purchase Order. | A new Purchase Order is created if no error is displayed in the dialog box. |  |
| 9 | Check the Purchase Order | Open the created purchase order in display mode and check if the values are displayed as text (code). | The relevant values are displayed as text and code. |  |
| 10 | Check the 6 Column Facet in the Tab | Click on the tab (General Information, Delivery and Invoice, Supplier Contact Data). | The tab (General Information,Delivery and Invoice, Supplier Contact Data) will be having the 6 column facet. |  |

|  |
| --- |
| Note If you do not know who should approve the purchase orders you created, then you can use App Manage Purchase Orders to display the created purchase order: Go to the Approval Details tab and check the approvers listed in section Approval Details. |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO > 500 AED and purchase group is 003, then the purchase orders should be approved. To decide which POs need approval, please refer to [Configure Flexible Workflow for Purchase Order](#unique_13) [page ] 16 in Preliminary step.

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
| 4 | Preview the Purchase Order | Go to the Output Management tab. In the Output Management section, choose Show More per Row and choose Display Document.Note When the Relevant and Merge are both selected for the document type SL1 and channel print in SSCUI: 103542 (Define Output Settings for Document Type), you upload the attachments of SL1 document type in Attachments Tab at the item level in App: Manage Purchase Orders, then the output should contain the Attachments as Document along with PO output.At the Output line item, the number of attachments for the Line item should match the number of attachments we attached. | The Purchase Order is opened in PDF format. |  |

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
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to change and use the little arrow on the right side to enter the PO detail, then choose Edit. | The Purchase Order screen is shown.The Purchase order is opened in change mode. |  |
| 4 | Change Purchase Order | Change certain field values of the Purchase Order. | The Purchase Order values are changed. |  |
| 5 | Check Purchase Order for completeness | Choose Order. | The Purchase Order is complete. |  |
| 6 | Messages (Optional) | Choose Messages (if possible). | If a message is displayed, you must correct the Purchase Order. If no message is displayed, the Purchase Order is complete. |  |
| 7 | Save Purchase Order | Choose Order to save the Purchase Order. | The Purchase Order has been saved. The system displays a success message Purchase order has been saved. |  |

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

#### Create Supplier Confirmation (Optional)

The steps below are sourced from 2TX. Before proceeding, ensure that 2TX is activated in your system.

##### Create Purchase Order with Confirmation (Optional)

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
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Purchaser role. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders(F0842A). | The Manage Purchase Order screen is displayed |  |
| 3 | Enter Purchase Order data | Choose Create, and enter all of the necessary data.In General Information section:Supplier: 33300001Currency: AEDPurchasing Organization: 3310Purchasing Group:003Company Code: 3310In Items section, choose Create button and make the following entries:Material: TG0011Plant: 3310Storage Location: 331AQuantity: xNet Price: xClick this item, then choose Supplier Confirmation Control tab:Confirmation Control: ConfirmationsChoose Schedule Lines tab:Delivery Date: <Today>Choose Apply. | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Order and when the purchase order number is displayed, write it down and record the delivery date for further use. | A new purchase order is created. Purchase order number is displayed. |  |

##### Create Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a supplier confirmation for stock material directly. Before processing this step, you must first complete the "Create Purchase Order with Confirmation" step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Purchaser role. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Confirmations(F5039). | The Manage Supplier Confirmation screen is displayed |  |
| 3 | Choose Create | Choose Create. | The Supplier Confirmation screen is displayed. |  |
| 4 | Enter Reference Purchase Order | Enter Reference Purchase Order that was created on step (Option A: Create Purchase Order with Confirmation) | The purchase order number is entered. |  |
| 5 | Enter Supplier Reference | Enter Supplier Reference: 10300001 | The Supplier is entered. |  |
| 6 | Choose Create | Choose Create in Confirmation Item |  |  |
| 7 | Create Supplier Confirmation Item | Enter all of the necessary data in screen Supplier Confirmation Item.Supplier Reference: 10300001Item: 10Confirmed Net Order Price: <Default Value>Note If you want to enter the confirmed Net Order price, you can use the SSCUI 101718 (Set Up Confirmation Control) to click the Price for confirmation Category AB.Confirmed Price Unit: <Default Value> | The Supplier Confirmation Item is entered. |  |
| 8 | Create Confirmation Line Data | Choose Create to enter the following values in tab: Confirmation LineDelivery Date: TodayConfirmed Quantity: <same as PO quantity> | The Confirmation Line Data is entered. |  |
| 9 | Choose Apply | Choose Apply. |  |  |
| 10 | Create Supplier Comments | Go to the Section Item Notes, and click Create to drop down and select Supplier Comments in Supplier Confirmation Item.Enter some comments （For example, Test for supplier confirmation）in the popup screen.Choose Create in the popup screen. | Supplier Comments are now created and visible. |  |
| 11 | Choose Create | Choose Create. |  |  |
| 12 | Choose Save | Choose Save to confirm the warning message. | The supplier confirmation is created. |  |

##### Approve Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the supplier is 10300003 and purchase group is 003, then supplier confirmation should be approved. To decide which supplier confirmation need approval, please refer to the scope item 2TX (Direct Procurement with Inbound Delivery) prerequisite step: Manage Workflows for Supplier Confirmations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Purchasing Manager. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items(F0862). | A list of existing Purchase Documents are displayed. |  |
| 3 | Search for Supplier Confirmation Status | Make the following entry and choose Enter.Search: <Supplier Confirmation number> | The Supplier Confirmation is displayed. |  |
| 4 | Approve Supplier Confirmation | Select the Supplier Confirmation on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary and then choose Submit. | The Supplier Confirmation is approved. |  |

##### Manage Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manage Supplier Confirmation is used in the procurement process to track and manage responses from suppliers regarding purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Confirmations(F5039). | The Manage Supplier Confirmation screen is displayed |  |
| 3 | Search for Supplier Confirmations | The basic filters are displayed.Purchase Order, Supplier, Created By, and so on.Make the above entries accordingly, then choose Go. | The Supplier Confirmation screen is displayed. |  |
| 4 | Check the Supplier Confirmation Processing Status | Select the supplier confirmation and check its Processing Status. | The purchase order number is entered. |  |
| 5 | Click the navigation to view Confirmation details | Click the navigation icon (>) to view the supplier confirmation’s General information. |  |  |
| 6 | Go to Confirmation Item | Go to the tab Confirmation Item and choose the Confirmation Item and click the navigation icon (>) |  |  |
| 7 | Review Confirmation Item | On the Supplier Confirmation Item screen, you can review the following entries:Delivery Date: <Default Value>Confirmed Quantity: <Default Value> | You have reviewed the supplier confirmation item. |  |

|  |
| --- |
| Note If you want to post goods receipt for a purchase order with confirmation, you can follow the 2TX steps: Create Inbound Deliveries and Post Goods Receipt for Inbound Delivery. |

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
| 3 | Enter Purchase Order | Enter the Purchase Order ID created in the step [Convert Purchase Requisitions to Purchase Orders](#unique_24) [page ] 29 or the step [Create Purchase Order](#unique_25) [page ] 30 and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: xxxPrinting: Individual slip |  |  |
| 5 | Select Item | From the Items section, select the goods receipt item to be posted.Choose Storage Location (for example) 331A.Note Select an item with a quantity of two or more pieces. | You can see that the Post button is activated. |  |
| 6 | Post | Choose Post. | The system displays the message Material Document xxx posted. |  |

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
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose the Go button.Plant: 3310Material Document: Material document number, in previous step | The relevant Material Document item displays. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The Material Document screen displays. |  |
| 5 | Check Goods Receipt Details | Check the General Information, Attachments, Item, Document Flow and Process Flow. | In the General Information section, you can see the Posting Date, Document Date. |  |
| 6 | Select the Material Document Item | In the Items section, select the row of material document item that you want to preview. | The Material Document Item screen displays. |  |
| 7 | Preview the Material Document Goods Receipt Slip | In the Output Management section, choose Show More per Row, and choose Display Document icon in the item of which Output Type is GOODS_RECEIPT_PO_SLIP. | The Goods Receipt Slip is opened in PDF format. |  |
| 8 | Preview the Material Document Goods Receipt Label | In the Output Management section, choose Show More per Row, and choose Display Document icon in the item of which Output Type is GOODS_RECEIPT_LABEL. | The Goods Receipt Label is opened in PDF format. |  |
| 9 | Back to Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

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
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose Go:Plant: 3310Material Document: xxx | On the Material Documents Overview screen, the relevant Material Documents / Material Document items are shown. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The list of the Material Documents is displayed.The Goods Receipts Details are shown. |  |
| 5 | Check Goods Receipts Details | Check the General Information, and the Material Document Items. | In the General Data section, the correct Posting Date, Document Date, and the Delivery Note are shown. |  |
| 6 | Display Document Flow | Switch to the section Process Flow. | The Process Flow shows the Purchase Order and the Material Document as a flow chart. |  |
| 7 | Back to Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Reverse Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the goods receipt posted in the previous chapter is reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Material Documents Overview (F1077) . | The Material Documents Overview is displayed. |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose the Go button.Plant: 3310Material Document:xxx | The relevant Material Documents / Material Document items are shown. |  |
| 4 | Select Material Document for Goods Receipt | Select your Goods Receipt by choosing the relevant row. | The list of the Material Documents is displayed.The Goods Receipts Details are shown. |  |
| 5 | Choose Reverse | Choose Reverse. | The Reverse Goods Receipt dialog box is displayed. |  |
| 6 | Post Reverse | Select the items you want to reverse in the pop up screen, then choose OK. |  |  |

#### Analyze Stock Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the stock overview is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Stock - Single Material (F1076) . | The Stock Single Material screen is displayed. |  |
| 3 | Enter Material | Enter the following entry in the Material field.Select the material from the interactive value help.Material: TG0011 | The Stock Overview for the Material is shown. |  |
| 4 | Change View | You need to choose the icon Chart View in order to change to a graphical view. | A Bar Chart for the stock by Plant / Storage Location is displayed. |  |
| 5 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Analyze Material Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the material document is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Material Documents Overview (F1077) . | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Material Documents | Enter the following entries in the data fields.Select the Go button.Plant: 3310Material: TG0011 | The relevant Material Document items for the material are shown. |  |
| 4 | Analyze Material Document | Select your Material Document by choosing the according row. | The Material Document Details are shown. |  |
| 5 | Check Material Document Details | Check the General Information and the Material Document Items. | The Status of the Material Document is correct; in the section General Data the correct Posting Date, Document Date and the Delivery Note are shown. |  |
| 6 | Back to Launch Pad | Select the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Manage Stock (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Materials must be scrapped as they are damaged and they should not appear any longer in the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Stock (F1062) . | The Manage Stock screen is displayed. |  |
| 3 | Open Stock Overview | Enter the following data in the fields.Plant: 3310Material: TG0011 | The Manage Stock screen is displayed.The Stock Overview of the Material is shown. |  |
| 4 | Select stock | Select the icon beside the stock that you want to scrap. | The Manage Stock dialog box opens. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Scrap Items | Enter the following data in the following data fields and choose the Post button.Stock Change:ScrappingCost Center: for example, R & DReason Code: for example, : QualityQuantity: x | The system displays X document has been created: Material Document xxx. |  |

#### Create Supplier Invoice

##### Option A: Create Supplier Invoice with PO/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation. You have two options to create the supplier invoice:

Option A: Create Supplier Invoice with PO/GR relation.

Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction)

You can choose either option A or option B to execute the supplier invoice creation with PO/GR relation. For more information, see the next two tasks.

|  |
| --- |
| Note Only choose either option A or B (not both). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:33300001For now, if you move the mouse to the Invoicing Party in the header of the supplier invoice, then click the Invoicing Party, the Company Date with Address and Contact Details are displayed.In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from AED to USD.)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:33300001Select See More at header area, make the following entries.Exchange Rate: <XXX> | The exchange rate should be changed to AED according to the customizing settings.The exchange rate is changeable. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References section, add the references.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order: <xxx> | All items of the referenced purchase order are added to the Invoice Items section. |  |
| 5 | Add Notes (Optional) | Enter notes under the Note tab if you want to add more detailed long text for the supplier invoice. |  |  |
| 6 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 7 | Check the Invoice Items Data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 8 | Check Tax Code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 9 | Block Invoice on Item Level (Optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Click Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Click Back to supplier invoice. | The item is blocked with a blocking reason. |  |
| 10 | Check the Balance | Calculate tax by choosing Propose Tax. Check the balance (difference between the calculated amount and the gross amount you entered in step 3). | The balance should be zero, or is within the defined tolerance. |  |
| 11 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier invoice is simulated. |  |
| 12 | Post Invoice | Choose Post. | The invoice is posted. The system displays the relevant message. |  |

##### Option A: Create Supplier Invoice for Custom Duty (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice for Custom Duty. This an optional step only needed when you created a PO with custom duty previously. Procedure

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | START CLOUD ONLY STEPLog on to the SAP Fiori launchpad as an Accounts Payable Accountant.END CLOUD ONLY STEPSTART on-premise ONLY STEPLog on to the SAP Fiori launchpad as an Accounts Payable Accountant - Procurement.END on-premise ONLY STEP | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | Make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:33300002 |  |  |
| 4 | Enter Purchase Order References | In Purchase Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items for Import Cust. Duty. | You may see material items and Import Cust. Duty, which refer to the entered purchase order document. Check if items for custom duty have an item text. |  |
| 6 | Check the Invoice Items data | Enter following data in item:Amount: <XXX>Quantity: 1 PCTax Code: Select a proper tax code for import custom duty | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items. |  |
| 8 | Check the balance | Calculate the tax by choosing Propose Tax. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

##### Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction) (Optional)

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

##### Option B: Print Complaint Letter in case of Invoice Reduction (Only relevant for SAP S/4HANA Cloud Public Edition)

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

##### Create Supplier Invoice without PO/GR (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice without purchase order reference. Follow below procedure to create an individual invoice. If need to mass upload supplier invoice, please refer to scope item Accounts Payable (J60).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | In section General Information, make the following entries:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: xxxCurrency: AEDInvoice Date: TodayPosting Date: TodayReference: xxx(reference invoice number from invoicing party) |  |  |
| 4 | Enter Invoicing Party | Make the following entries.General DataInvoicing Party: 33300001 |  |  |
| 5 | Enter G/L Account Item | Choose Add G/L Account Item.Make the following entries.Debit/Credit: DebitG/L Account: 65008300Amount: xxx | A new row for a GL/ Account Item displays with entry fields for the side of the Account, the G/L Account, and the Amount. |  |
| 6 | Enter G/L Account Item details | Expand Show Details.Make the following entries.Cost Center 33101201Tax Code:If there is no tax, specify tax code <Input Tax Code> | Details for a GL/ Account Item display with entry fields for the cost center and the tax code. |  |
| 7 | Simulate Supplier Invoice and Check Messages | Choose the Simulate button.If there are no differences(or if the value is within the defined tolerance), the Supplier Invoice is complete to post.Check the Gross Invoice Amount against the items plus tax amount(if tax code is,<Input Tax Code> you do not have any tax amount) | Invoice is consistent.In case that an error message is displayed, a correction of the entries is necessary |  |
| 8 | Post Invoice | Select the Post button to post the Supplier Invoice. | The Invoice is posted. |  |

#### Detect Critical Cash Discount Situations (Optional)

The system automatically detects critical situations, which could lead to the loss of the cash discount. The detection process is automatically triggered by the system on a regular basis and indicates critical cash discount situations to the accounts payable accountant, using the notification functionality on the home screen. This enables the accounts payable accountant to proactively react to situations, where the cash discount is at risk. Therefore, negative financial effects to the business of the company can be avoided.

#### React to Critical Cash Discount Situations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, supplier invoices with payment block are displayed. Blocked for Payment is a dynamic link which is visible only in invoice header when the invoice is blocked for payment. The Tab contains data relevant for explaining the block situation and its possible resolution e.g. Actions to contact supplier/purchaser, Block related statistics etc.

Situation and Notification will be triggered according to Selection Criteria set in preliminary steps. System automatically detects cash discount situations by daily job, and indicates critical situations using the notification functionality on the home screen. This enables Team Member to proactively react to potential cash discount overdue and avoid negative implications to the business processes of the company.

|  |
| --- |
| Note You must perform step Create Ready-to-Use Situation Type for Cash Discount at Risk and Create Team and Responsibilities before testing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Supplier Invoices List (F1060A) . | The Supplier Invoice List screen displays. |  |
| 3 | Search for Supplier Invoices | Make the following entries and choose Go.Invoice Document No.: invoice created above (The Payment Status of Invoice is Blokced for Payment, and the Payment Terms is 0002/0003 in Invoice). | The relevant supplier invoice is displayed |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select an Invoice Document by clicking the entire row.If the invoice is blocked for payment, choose Blocked for Payment link to go to Payment status page. You can check the information below:InformationThe system shows: This Invoice is blocked for payment.ActionsContact Supplier: Supplier contact information.Contact Purchaser: Purchaser contact information.Blocked Invoice ItemsShowing blocking reason on line item level.Invoice TimelineShowing dates, such as invoice document date, invoice posting date, invoice payment due date, cash discount deadline if there is any discount)Statistics of SupplierBlocked Invoices Amount by Reason:Shows amount of invoices blocked for the supplier and particular company codeBlocked Invoices Count by Reason:Shows count of invoices blocked for the supplier and particular company codePayment Blocked by Reason:Shows percentage of block reasons/occurrences | The Payment block tab is displayed. |  |
| 5 | Check Supplier Invoices with Cash Discount Notification | Choose the Notifications icon at top right of screen.Choose notification, for example:X Supplier Invoices are blocked for payment.Cash Discount at Risk due to invoice pay | The X supplier invoices which at cash discount risk are displayed in Supplier Invoices List. |  |
| 6 | Check Situation Message in Supplier Invoice | Select one invoice in the above list to go to Supplier Invoice page. If notification is triggered for invoice, Situations tab will be added in supplier invoice. You can choose Close Situation and pick a reason for closing this situation. | Situation Message is shown and closed. |  |

#### Create Credit Memo (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the credit memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | In section General Data, make the following entries:Transaction: Credit MemoCompany Code: 3310Gross Invoice Amount: Invoice amountCurrency: AEDInvoice Date: TodayPosting Date: TodayReference: xxxInvoicing Party: 33300001 |  |  |
| 4 | Enter Purchase Order References | In Purchasing Document References section, add the references.Make the following entries (use a PO you created previously).Reference: Purchase OrderPurchase Order: xxx | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create credit memo for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Add Amount and Quantity | Check the Items that you want to post, and enter the following field entries.Amount: xxxQuantity: xxxThen choose the Check button at the bottom right of the screen. | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax | In the section Tax, check if the Tax Amount equals the sum of Amount multiplied by Tax Code value of the selected items in Step 6 | The section tax is displayed. |  |
| 8 | Simulate Credit memo and Check Messages | Choose the Simulate button.If there are no differences(or if the value is within the defined tolerance), the Supplier Invoice is complete to post.Check the Gross Invoice Amount against the items plus tax amount(if tax code is,<Input Tax Code> you do not have any tax amount) | Invoice is consistent.In case that an error message is displayed, a correction of the entries is necessary |  |
| 9 | Post Credit Memo | Select the Post button to post the Credit Memo | The Invoice is posted. The system displays the message Invoice xxx posted. |  |

Result

The supplier Invoice is complete to post.

#### Check Supplier Invoice List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, all supplier invoices are displayed.

Payment block tab is a dynamic tab which is visible only in case the invoices blocked for payment (based on payment block status in FI Module)

The Tab contains data relevant for explaining the block situation and its possible resolution e.g. Actions to contact supplier/purchaser, Block related statistics etc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Supplier Invoices List (F1060A) . | The Supplier Invoices list screen is displayed. |  |
| 3 | Search for Supplier Invoices | On the Supplier Invoice List screen, make the following entries and choose the Go button.Invoicing Party: 33300001 | The relevant Supplier Invoices are shown, grouped by status Posted, Reversal and Reversed. |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select an Invoice Document by clicking the entire row.If the invoice is blocked for payment, you check below information by choosing Blocked for Payment.InformationShowing ‘This Invoice is blocked for payment.’ActionsContact Supplier: Supplier contact information.Contact Purchaser: Purchaser contact information.Blocked Invoice ItemsShowing blocking reason on line item level.TimelineShowing dates with focus on cash discount deadline (e.g. invoice document date, invoice posting date, cash discount deadline date if there is any discount)Charts with statistics1st chart shows the amounts of invoices blocked for the supplier and particular company code2nd chart shows count of invoices blocked for the supplier and particular company code3rd chart shows the percentage of block reasons/occurrences | The invoice document is displayed. |  |

#### Approve Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a supplier invoice is approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Supplier Invoices List (F1060A) . | The Supplier Invoices list screen is displayed. |  |
| 3 | Filter Supplier Invoice List | Fill in search criteria fields or leave them blank, and choose Go. | The Supplier Invoices list is displayed. |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select an Invoice Document by clicking the entire row, which is blocked for payment. | The invoice document is displayed. |  |
| 5 | Release the Invoice | Choose Release. | The invoice is released. |  |
| 6 | Back to SAP Fiori Launch Pad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Reverse Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a supplier invoice is reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Supplier Invoices List (F1060A) . | The Supplier Invoices list screen is displayed. |  |
| 3 | Search for Supplier Invoices | On the Supplier Invoice List screen, make the following entries and choose the Go button.Invoicing Party: 33300001 | The relevant Supplier Invoices are shown, grouped by status Posted and Reversal. |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select the invoice created in the previous step by clicking on the row to display the invoice. | The invoice document is displayed. |  |
| 5 | Reverse the Invoice | Choose Reverse. | The Reverse Invoice dialog box opens. |  |
| 6 | Enter Reason for Reversal | Reason for Reversal: <Default Value>Posting Date: <Today>Choose OK. | The Invoice is reversed. |  |
| 7 | Back to SAP Fiori Launch Pad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Clear GR / IR (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, one or more postings are cleared.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | OpenClear GR/IR Clearing Account (MR11). | The Maintain GR/IR Clearing Account screen opens. |  |
| 3 | Search for Purchasing Documents | Make the following entries and choose the Execute (F8) button.Company Code:3310Plant: 3310Purchase Order Date to: <today> | The relevant Purchase Orders are shown. |  |
| 4 | Post Clearing | If Purchase Orders exist that need clearing, select one and choose Post Clearing (Ctrl + F12). | The clearing document is created. |  |
| 5 | Write down Clearing Document Number | The clearing document is created. Write down its number as it is needed for the next step. |  |  |
| 6 | Back to SAP Fiori Launch Pad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Cancel Journal Entry (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the GR / IR clearing posting is reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display/Cancel Account Maintenance Document (MR11SHOW) . | The Display / Cancel Account Maintenance Document screen opens |  |
| 3 | Search for Accounting Maintenance Document | Make the following entries and choose the Overview (Enter) (F9) .Acct Maint.Document / fiscal year <Journal Entry> / <Fiscal year> from previous step | The accounting maintenance document is displayed.The Display / Cancel Account Maintenance Document screen is displayed. |  |
| 4 | Reverse Journal Entry | Select the line item created in the previous step and choose the Reverse Document. | The Reversal Document Post Date screen opens. |  |
| 5 | Reverse Journal Entry | In the Reversal Document Posting Date window, the original date is default in Posting Data field, you can manually choose another date via F4 button or choose Current Date, then choose Reverse (Shift+F1). . | The Accounting Maintenance Document is reversed. The reversal document number is displayed. |  |
| 6 | Back to the SAP Fiori launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Monitor Down Payment process

##### Create Purchase Order Manually for Down Payment

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) . | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300003In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group: 002Company Code: 3310In Items section,Material: TG0011Plant: 3310Storage Location: 331APO Quantity: 100Net Price: XAEDGo to Invoice Tab and enter Tax Code<Input Tax Code>.Tax Date: <Default Value>DP Category: Mandatory Down PaymentERS: deselectChoose Enter.Down Payment %: 10DP Date: the last day of this Month | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

##### Monitor Down Payments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can monitor down payment for purchase orders.

Prerequisite

The Purchase Orders for down payment exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Monitor Purchase Order Down Payments (F2877) . | The Monitor Purchase Order Down Payments screen displays. |  |
| 3 | Search for Purchase Orders | Enter the following filters values for the PO Down Payments.Display Currency: AEDSupplier: 33300003Choose Go. | The down payment PO has been searched. |  |
| 4 | Display Down Payment PO | Check the Down Payment Purchase Order for the detail information as Down Payment %, Amount, Release Amount, PO/items, etc. |  |  |

##### Create Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A down payment request is created.

Prerequisite

The Purchase Orders for down payment exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Monitor Purchase Order Down Payments (F2877) . | The Monitor Purchase Order Down Payments screen displays. |  |
| 3 | Search for Purchase Orders | Enter the following filters values for the PO Down Payments.Display Currency: AEDSupplier: 33300003Choose Go. | The down payment PO has been searched. |  |
| 4 | Access the SAP Fiori App | Highlight the PO which is created in step [Create Purchase Order Manually for Down Payment](#unique_52) [page ] 69.Choose Create Down Payment Request to open Manage Supplier Down Payment Requests screen. | The Manage Suppliers Down Payment Requests screen displays. |  |
| 5 | Header | Choose > and make the following entries:Company Code: 3310Journal Entry date: Today’s datePosting date: Today’s dateJournal Entry Type: KZTransaction Currency: AED |  |  |
| 6 | Items | Make the following entries:Supplier: 33300003Trg. Spec. G/L Ind: A (Default value, do not change)Amount: <PO total amount * 10%>AEDPurchasing Document: <Default Value>Purchasing Doc. Item: <Default Value>Tax Code: <Default Value>Tax Amount:<Default Value>Due On: <Default Value> |  |  |
| 7 | Post | Choose Post. | The Success screen is displayed showing the journal entry XXX posted. |  |
| 8 | Other | Select the desired action in the Success screen:DisplayGo Back |  |  |

##### Create Down Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A payment for a down payment request is generated.

|  |
| --- |
| Note Actually, this step refers to the chapter Post Outgoing Payment in the Accounts Payable (J60) scope item. Please make sure the down payment has not been blocked in any payment run and payment proposal. |

Prerequisite

A down payment request has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments screen displays. |  |
| 3 | Enter Payment Data | Make the following entries and choose Show Items.In the General Information section:Company Code: 3310Posting Date: today's dateJournal Entry Date: today's dateValue Date: today's dateReference (optional): referenceJournal Entry Type: KZIn the Bank Data section:G/L Account: 11001000House Bank / Account: AEBK1/AEAC1Amount / Currency: <PO total amount * 10% >AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / Code Currency: OptionalIn the Open Item Selection section:Account Type/Account ID: Supplier33300003 | A list of open items is displayed in the Open Items section. |  |
| 4 | Select More | To display only the special G/L transactions, click Additional Options and choose the Select More button, deselect all entries in Line Item Type field and select:Line Item Type: Special G/L TransactionsChoose OK. | Document with special G/L transactions are displayed. |  |
| 5 | Select/Deselect | Select a downpayment which is created in previous step, and in the Clear column, choose Clear. | The downpayment to pay is transferred to the Items to be Cleared section. |  |
| 6 | Post | Choose Post. | The Success screen is displayed showing the journal entry number is successfully posted. |  |

##### Post Goods Receipt

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

##### Create Supplier Invoice for Down Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Purchase Order for down payment has been created successfully in step: [Create Purchase Order Manually for Down Payment](#unique_52) [page ] 69.

Down payment has been posted successfully in step: [Create Down Payment](#unique_55) [page ] 73.

Purpose

The invoice verification is done in this activity and you can do the down payment clearing.

|  |
| --- |
| Note If purchase order is not for the down payment and down payment didn’t post for the purchase order successfully, please skip this step directly. Please make sure the down payment has not been blocked in any payment proposal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice - Advanced (MIRO) . | The Create Supplier Invoice Advanced screen is displayed. |  |
| 3 | Enter General Data | Make the following entries and choose Enter:Company Code: 3310Transaction: InvoiceInvoice date: TodayPosting Date:TodayAmount: value in POCalculate Tax: XReference: <xxx>(reference invoice number from invoicing party)Tax code: same with tax code in PO: <Input Tax Code>Text: <enter text value> |  |  |
| 4 | Enter Purchase Order References | References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: PO number which is created in step [Create Purchase Order Manually for Down Payment](#unique_52) [page ] 69. Choose Enter. Choose Continue if there is a dialog about Information appears which relevant Down Payment. |  |  |
| 5 | Check the Purchase Order Items data | Check the Amount, the Quantity, and the Tax Code. |  |  |
| 6 | Choose Down Payment Clearing (Optional) | Down Payment Clearing and on the Choose Down Payment Clearing screen.Amount Entered: same with Available AmountChoose Copy |  |  |
| 7 | Simulate Supplier Invoice and Check Messages | Take the amount of the items as input for the Amount field in the Basic Data section. Make sure the invoice balance is 0. | The Supplier Invoice is simulated. |  |
| 8 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

### Automatic Purchase Order Creation from Purchase Requisition

|  |
| --- |
| Note When you perform the following steps Automatic Purchase Order Creation from Purchase Requisition, you have to run Master Data update on the Preliminary Step:[Master Data Update for Automatic Purchase Order Creation from Purchase Requisition](#unique_17) [page ] 20 |

#### Create Purchase Requisition

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen displays. |  |
| 3 | Create Purchase Requisition | Choose Create. | The Purchase Requisition screen displays. |  |
| 4 | Enter Document Type | Enter Document Type: Pur. Requisition (NB). |  |  |
| 5 | Add Item | Automatic Source Determination: <selected>In the Items section, choose Create then choose Material to add new items to Purchase Requisitions. | The Purchase Requisition Item screen appears. |  |
| 6 | Enter Detail Data | Enter the following values in General Information section:Item Category: StandardMaterial: TG0011Plant: 3310Enter the following values in Quantity and Date section:Quantity: 10Delivery Date: default valueRequisition Date: default valueRelease Date: default valueEnter the following values in Contact Information section:Purchasing Organization: 3310, and choose Enter.Purchasing Group: 002, and choose Enter.Go to Source of Supply area and make sure one source has been assigned.Choose Apply.Choose Apply and you will automatically go back to the Purchase Requisition screen. |  |  |
| 7 | Save your entries | Choose Create to confirm the popup message. | The purchase requisition is created. |  |

Result

The Purchase Requisition is created.

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
| 4 | Define a Job | On the New Job: Automatic Creation of Purchase Orders from Requisitions screen, make the following entries:Choose 1 Template Selection and go to 1. Template Selection area to make the following entries:Job Template: <Job Template>, for example, Automatic Creation of Purchase Orders from RequisitionsJob Name: <Job Name>, for example, Automatic Creation of Purchase Orders from RequisitionsChoose Step 2 and go to 2. Scheduling Options area to make the following entries:Start Immediately : <selected>Start: <Current Time>Note If the job needs to be run on a regular basis, choose Define Recurrence Pattern.Choose Step 3 and go to 3. Parameters area to make the following entries:Per Requisition:<selected>Per Company Code: <selected>Per Contract: <selected>Note Set Parameter settings according to your needs.Choose Schedule. | The job is created. |  |
| 5 | Convert Purchase Requisition to Purchase Order | On the Application Jobs screen.Go to Jobs (X) area and check the status until it changes to Finished. | The Job automatically converts Purchase Requisition to Purchase Order. |  |
| 6 | Check Result | Choose Result.Choose Preview. | The Purchase Order is created. |  |

|  |
| --- |
| Note You may go to the Fiori Launchpad main screen. On the Fiori Launchpad main screen, choose Search button on the top. Choose Purchase Order from the drop-down box, and enter the Purchase Order number in the field Search In: Purchase Orders. Select the Purchase Order you want to display on the Search screen. |

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
| 3 | Search for Purchase Order | Open Purchasing Document Search. | A list of Purchasing Documents displays. |  |
| 4 | Select Purchase Order | Select your purchase order (if not in the PO, the storage location must be specified). | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 5 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: xxx | The Post Goods Receipt screen displays. |  |
| 6 | Select Item | Select the items for which a goods receipt is to be posted.Choose Storage Location (for example) 331A. |  |  |
| 7 | Post | Choose Post. | The system displays the message Material Document <Document No> posted. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 12345678Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Baseline Date: <Today> (in Payment tab)Invoice Party: 33300001 | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items and delivery costs items which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Purchase Order Items Data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.Check the Gross Invoice Amount against the items plus tax amount (if tax code is <Input Tax Code> , you do not have any tax amount) | The supplier invoice is complete to simulate. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. 51xxxxxxxx has been created. |  |

## Appendix

### Process Integration

The process to be test in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Description |
| --- | --- |
| Accounts Payable- (J60) | Outgoing Payment |

#### Goods Receipt Blocked Stock

Purpose

If you wish to accept goods from a supplier conditionally (for example, because a certificate is missing) you initially post the goods to the non-valuated Goods Receipt Blocked stock upon receipt. When the conditions for the acceptance of the delivery have been fulfilled, you release the Goods Receipt Blocked stock to Unrestricted-use stock, Quality Inspection stock or Blocked stock. The valuation and updating of the stock data does not take place until the material is released.

Prerequisite Process

Before you proceed to test this function, please follow the above detailed process in Step Create Purchase Order. Please note that if Purchase Order needs to be approved, please process the optional Step Approve Purchase Order.

##### Post Goods Receipt Blocked Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can post the goods to the non-valuated Goods Receipt blocked stock upon receipt.

|  |
| --- |
| Caution If the Goods-Receipt-Based Invoice Verification has been selected in PO creation, then you have to use App: Post Goods Movement to run this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search for Purchase Order | Search for Purchaser Order number and choose Enter. |  |  |
| 4 | Select Item | Select the items for which a goods receipt is to be posted. Check the checkbox on the beginning of the item row. |  |  |
| 5 | Post to Goods Receipt Blocked Stock | Enter the number of items to be posted to GR blocked stock in Delivered field. Choose a storage location in Storage Location field.For example:Delivered: 1 PCStorage Location: 331AChoose Goods Receipt Blocked Stock from Stock Type drop down list.Choose Post. | System displays Material Document XXX posted. |  |

##### Release Goods Receipt Blocked Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can release the Goods Receipt Blocked Stock to Unrestricted used stock, stock in Quality Inspection, or Blocked stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search for Purchase Order | Search for Purchaser Order number and choose Enter. |  |  |
| 4 | Release Goods Receipt Blocked Stock | Enter the number of items to be released from GR blocked stock in Delivered field. Choose a storage location in Storage Location field.For example:Delivered: 1 PCStorage Location: 331AChoose Stock Type from the drop down list:GR Blocked Stock to Unrestricted – UseNote You can also select other stock type if you would like to release stock to Quality Inspection Stock or Blocked StockChoose Post. | System displays Material Document XXX posted. |  |

#### Setup Mail Notification for Purchase Order Workflow

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Extensibility Specialist role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Email Templates - Deprecated (F1306) . | The templates displays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_CRT_NOTIFY_RECIPIENTS.Choose email template, choose Copy and then make below entries:Email Template: _00800238_CRT_ALLName: Workflow for Release of Purchase OrderChoose Copy.Note Following templates are available for purchase order workflow:Workflow for Release of Purchase Order:00800238_CRT_ALL00800238_CRT_19 | Email Template copied. |  |
| 4 | Adjust the text of the mail template | Choose Custom tab.Choose Email template, for example YY1__00800238_CRT_ALL then go to Email Template screen. | Custom Email Template opened. |  |
| 5 | Choose Language | Choose Language, for example English. Then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request then choose Save. | The Email Template adjusted. |  |

#### Setup Mail Notification for Purchase Order Deadline

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Extensibility Specialist role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Email Templates - Deprecated (F1306) . | The templates displays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (X), search Template: MMPUR_PO_WFL_DEADLINE_EMAIL.Choose email template then choose Copy then make below entries:Prefix: YY1_Email Template: MMPUR_PO_WFL_DEADLINE_EMAILName: Email Notification for Purchase Order DeadlineChoose Copy. | Email Template copied. |  |
| 4 | Adjust the text of the mail template | Choose Custom tab.Choose Email template, for example YY1_MMPUR_PO_WFL_DEADLINE_EMAIL then go to Email Template screen. | Custom Email Template opened. |  |
| 5 | Choose Language | Choose Language, for example English. Then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request then choose Save. | The Email Template adjusted. |  |
| 6 | Display the Show Data Fields (Optional) | Click Show Data Fields to get the fields available to configure in the email template | The Show Data Fields displayed. |  |

#### Configure Deadline in Manage Workflows for Purchase Orders

Purpose

In order to implement the email notifications for deadline purchase order, and inform the approvers about the PO's overdue for approval, then the deadline should be configured in Purchase Order Workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872) . | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the STEP area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients. | The Workflow for Purchase Order is configured. |  |
| 4 | Setup Deadlines | Go to Deadlines section, choose Create, and make the following entries:If step is not completed by: The below timeline after start of the approval workflow.- < for example 2> Minute(s)Execute the following action: Send mail notificationE-Mail Template: Email Notification for Purchase Order DeadlineGo to Recipients, and make the following entries:Assignment By: UserUser: Select User from value help (for example: Employee ID PURCHASING_MANAGER)Note This recipients user: for example PURCHASING_MANAGER should assign the email address.Choose Create.Choose Save . |  |  |
| 5 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Free Goods Purchasing

##### Change Material Master Data – For Free Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for changing material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Master Data Specialist - Product Data role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Change Material (MM02). | The Change Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | On the Change Material screen, make the following entries:Material: for example, TG0012Choose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Choose Views | On the Select View(s) screen, choose Purchasing and Continue. | The Organizational Levels displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, make the following entries:Plant: <Plant>, for example, 3310Choose Continue. | The Change Material XXXXX (Material general) displays. |  |
| 6 | Select Autom.PO | Scroll down to the General Data section and select the following:Qual.f.FreeGoodsDis.: <2> | Autom.PO is selected. |  |
| 7 | Save your data | Choose Save. | The material master data is updated. |  |

##### Change Supplier Master Data - For Free Goods

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
| 2 | Access App | Choose Maintain Business Partner (BP) . | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Find: Business PartnerBy: Supplier NumberSupplier Number: for example, 33300003Choose Start. The Supplier row displays.Double-click the Supplier Partner row. | The Supplier information screen displays. |  |
| 4 | Switch to Change mode | Ensure you are in Change mode. Otherwise, select Switch Between Display and Change. | The Change mode screen displays. |  |
| 5 | Change BP role | In the Change in BP role field, choose the following value:Supplier (defined) |  |  |
| 6 | Open Purchasing Organization Data | Choose the Purchasing tab at the top of the screen. | The Purchasing Organization sub section screen displays. |  |
| 7 | Enter Purchasing Data | Choose Switch Organization.Make the following entry and choose Enter:Purch. Organization: <Purchasing Organization>, for example, 3310 |  |  |
| 8 | Select Grant Free Goods checkbox | From the Purchasing Data section, scroll down to the Control Data section, make the following entry:Grant Free Goods: <selected> | The Grant Free Goods checkbox is selected. |  |
| 9 | Save your data | Choose Save. | The Supplier change is saved. |  |

##### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create purchasing info record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Manage Purchasing Info Records screen is displayed. |  |
| 3 | Create New Purchasing Info Record for header data | On Create Info Record: Initial Screen, make the following entries and choose Enter.Supplier: 33300003Material: TG0012Plant: 3310Purchasing Organization: 3310Standard Info category: select | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Purch.Org. Data | ● Delivery Time in Days: 3● Purch.Group: 001● Tol. Underdl.: 10.0● Tol. Overdl.: 10%● Tax Code: <Input Tax Code>● Order Unit: PC● Standard Order Quantity: 10● Net Price: 30● Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.● Incoterm Location 1: VENDOR | Purchase Organization data for Purchasing Info Record is added. |  |
| 5 | Maintain Free Goods | Choose Conditions to go to next screen.Highlight Condition Type PPR0 with price.Choose Free Goods (Ctrl+F1), and make the following entries:Supplier: 33300003Material: TG0012Plant: 3310Purchasing Organization: 3310Valid From: TodayValid To: 12/31/9999Infotype: 0Order Unit: PCMin Qty: 100For: 10Add. qnty: 1Calc.Rule: 1Choose Enter. | The Free Goods condition has been maintained. |  |
| 6 | Save your data | Choose Save twice. | The purchasing info record is saved. |  |

##### Create Purchase Order Manually for Free Goods

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
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) . | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300003In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group:002Company Code: 3310In Items section,Material: TG0012Plant: 3310Storage Location: 331AQuantity: 200Net Price: X AEDChoose Enter.After choosing Enter in PO creation, the result as per the free goods scheme qty 20 PC becomes free automatically in second line item.Go to Invoice Tab and enter Tax Code<Input Tax Code>.Tax Date: <Default Value> | The Create Purchase Order Screen is shown. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

#### Quantity Optimization for Purchase Order

##### Setup a Static Rounding Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for setup a static Rounding Profile

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Select the Application Area | On the Configure Your Solution: Realize Phase screen, enter the following search criteria:Application Area: LogisticsSub Application Area: Quantity OptimizationChoose Enter | A list of items appears. |  |
| 5 | Select Item | Select the item and choose > to go to the screen Quantity Optimizing and Allowed Logistics Unit of Measure | The item is selected and go to the next screen. |  |
| 6 | Select Configuration Step | Choose Configure for Step Name Maintain Rounding Profile, ID:104713 | The SSC UI screen opens. |  |
| 7 | Create a static Rounding Profile | Enter an ID for your rounding profile and choose "Create statically F6" (Static)For example:Rounding Profile: ZT01Plant: 3310Note Rounding profile can be setup plant-dependent or independent. Plant-dependent profiles will be chosen prior to plant independent within the application context. | The system navigates you to the next screen Create Static Rounding Profile. |  |
| 8 | Define Rounding Profile Values | Enter a description and profile values as the following:For example:Rounding Profile Description: Rounding up to full 5Thres. ValueRound. Value1561011151620212526303135364041454650Note With this rounding logic, any input quantity will be round up to the next possible "full 5". E.g. an input quantity of 16, 17, 18, 19 or 20 matches the threshold value 16,000. The rounding up value in all cases will be 20,000 - ie. the next possible "full 5".The system logic will also be able to handle bigger input values even they are not explicitly specific here. That is, if e.g. the current input quantity in the PO item is e,g, 78, the system will be able to round it up to 80 based on the internal algorithm. | Your Rounding Profile is successfully defined. |  |
| 9 | Save rounding Profile | Choose Save to save rounding profile. | The rounding profile has been saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Maintain Rounding Profile | Go to the Configuration app and search for the following activity: Maintain Rounding Profile.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create static Rounding Profile | Enter an ID for your rounding profile and choose "Create statically F6" (Static)For example:Rounding Profile: ZT01Plant: 3310Note Rounding profile can be setup plant-dependent or independent. Plant-dependent profiles will be chosen prior to plant independent within the application context. |  |  |
| 4 | Define Rounding Profile values | Enter a description and profile values as the following:For example:Rounding Profile Description: Rounding up to full 5Thres. ValueRound. Value1561011151620212526303135364041454650Note With this rounding logic, any input quantity will be round up to the next possible "full 5". E.g. an input quantity of 16, 17, 18, 19 or 20 matches the threshold value 16,000. The rounding up value in all cases will be 20,000 - ie. the next possible "full 5".The system logic will also be able to handle bigger input values even they are not explicitly specific here. That is, if e.g. the current input quantity in the PO item is e,g, 78, the system will be able to round it up to 80 based on the internal algorithm. |  |  |
| 5 | Save Rounding Profile | Choose Save to save rounding profile. | The rounding profile has been saved. |  |

|  |
| --- |
| Note If you encounter setup rounding profile issues, you can create an incident under LO-RFM-MD-QO component. |

Result

The static rounding profile ZT01 has been created.

##### Maintain a Rounding Profile in the Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for maintaining the Rounding Profile in the purchasing info record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Search existed Purchasing Info Record | Make the following entries:Purchasing Info Record Category: StandardSupplier: 33300002Material: TG0012Plant: 3310Choose Go.If the Purchasing Info Records is not created at plant level, then you can process the Case 1 (Create Purchasing Info Records).If the purchasing Info Records is created at plant level, then you can process the Case 2: Change Purchasing Info Records. | The purchasing info record can be searched. |  |
| Case 1: Create Purchasing Info Records |  |  |  |  |
| 1 | Open New Purchasing Info Record | Choose Create | The Purchasing Info Record Screen is displayed. |  |
| 2 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300002Material: TG0012Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 3 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 31.12.9999 | General Information is added. |  |
| 4 | Enter Purchasing Data | Make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 5 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Tax Rate Valid From: Select value from F4 helpOrder Unit: PCStandard Order Quantity: 10Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data is added. |  |
| 6 | Enter the Rounding Profile | Make the following entries (for example):Round Profile: ZT01Note The value help behind the field will show all existing rounding profiles. Choose the rounding profile you have created in the previous configuration step | The rounding profile has been added in purchasing info record |  |
| 7 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12.31.9999Amount: 30.00Pricing Unit: 1Currency: Plant: AEDChoose Apply. | Condition Data is added |  |
| 8 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 9 | Create your data | Choose Create. | The purchasing info record is created. |  |
| Case 2: Change Purchasing Info Records |  |  |  |  |
| 1 | Open Existed Purchasing Info Record | Choose this existed Purchasing Info Record, and choose > to go to the next screen. | Go to the purchasing info record screen. |  |
| 2 | Choose Edit | Choose Edit | The purchasing info record can be edited. |  |
| 3 | Enter the Rounding Profile | Go to Tab Delivery and Quantity , and make the following entries (for example):Round Profile: ZT01Note The value help behind the field will show all existing rounding profiles. Choose the rounding profile you have created in the previous configuration step. | The rounding profile has been added in purchasing info record. |  |
| 4 | Save your data | Choose Save. | The purchasing info record is saved. |  |

##### Create Purchase Order with Quantity Optimization

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
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) . | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300002In Header section, on the Org. Data tab, make the following entries:Purchasing Org.: 3310Purchasing Group:002Company Code: 3310In Items section,Material: TG0012Plant: 3310Storage Location: 331AQuantity: <7>Note After quantity <7> was entered as item quantity, the system will automatically round it up to 10 as per the logic in the used rounding profile.Respectively other quanties will be rounded up to full 5 as per the rounding profile's logic.In addition, there will be an info message displayed in the message try (left lowert screen corner).In the message window section General information you will see a message Order quantity violates rounding rules (See long text).Once you navigate to the long text you see more details on what the system automatically adjusted. In this example the action Rounding via static rounding profile will be shown as measure taken by the system.Net Price: XAEDChoose Enter.Go to Invoice Tab and enter Tax Code <Input Tax Code> .Tax Date: <Default Value> | The Create Purchase Order Screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

|  |
| --- |
| Note Once you have entered a PO Quantity which is then automatically rounded up, the item will not be subject to a 2nd rounding again if you again change the quantity which needed to be rounded as well. Or in other words, the rounding automatism is only triggered once for a PO item. If you need to restart, you need to remove the item and enter it again to have one attempt for executing the quantity optimization. |

##### Simulate Quantity Optimizing

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
| 2 | Access App | Open Simulate Quantity Optimizing (WLB8). | The selection screen for Simulating Quantity Optimizing opens |  |
| 3 | Make Your Selection | In the Selection screen, make the following entries:Application Rel. XCalling Application: A Standard Purchase OrderChoose Continue. | The selection screen for Application-Dependent Simulation: Standard Purchase Order opens. |  |
| 4 | Enter the simulate data | In the selection screen make the following entries:Material: TG0012Vendor: 33300002Supplying Plant: <leave empty>Purch. Organization: 3310Receiving Plant: 3310Item Category: StandardInput Quantity: 7Input UoM: PCNote You can play with the Quantity, e.g. you may use different quantities to be rounded, even those which are not explicitly defined in the Rounding Profile. The system will extrapolate the rounded quantity.Start the simulaiton by pressing the "Execute" action button | The Rounded Quantity will display the rounding result (here: 10 PC).That is, based on the rounding profile ZT01, the input quantity of 7 PC was rounded up to 10 PC. |  |

|  |
| --- |
| Note If you encounter simulate Quantity Optimizing issues, you can create an incident under LO-RFM-MD-QO component. |

#### Rework Flexible Workflow for Purchase Orders

##### Activate Inquiry Workflow for Purchase Orders

Purpose

In this procedure, you activate the Inquiry Workflow for Purchase Orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Activate Inquiry Workflow for Purchase Orders | On the Configure Your Solution: Realize Phase screen, search Activate Inquiry Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Inquiry Workflow for Purchase Orders. | The Purchase Order Processing screen is displayed. |  |
| 5 | Activate Inquiry Workflow for Purchase Orders | Choose the Change State to change Switch State from OFF to On. | The Inquiry Workflow for Purchase Orders is activated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Activate Inquiry Workflow for Purchase Orders | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Activate Inquiry Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Purchase Order Processing screen displays. |  |
| 3 | Activate Inquiry Workflow for Purchase Orders | Choose the Change State to change Switch State from OFF to On. | The Inquiry Workflow for Purchase Orders is activated. |  |

Result

The Inquiry Workflow for Purchase Orders is activated.

##### Configure Rework Flexible Workflow for Purchase Orders

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Rework Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Reworkable Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Exception Handling:Rework Requested:Required Action: Rework Purchase OrderRecipients: Default: <Role: Determined automatically>Action result: Repeat stepNote Action result should be (after rework):● Continue Workflow: Current Workflow shall move to next step● Repeat Step: repeat the current step of current workflow● Restart workflow: restart the workflowChoose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

##### Rework Purchase Order

Procedure

You can ignore this step if you did not set up the Steps [Configure Rework Flexible Workflow for Purchase Orders](#unique_86) [page ] 108.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of already created Purchase Orders is displayed. |  |
| 3 | Rework Purchase Order | Select the Purchase Order from the left screen and choose Request Rework at the bottom right of the screen.Enter the rework reason in the Submit Decision dialog then choose Submit. | The Purchase Order is requested rework. |  |
| 4 | Back to SAP Fiori launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

After this step, the Purchase Order should be edited by the creator with the rework reason.

#### Dunning Reminder for Purchase Orders

With Dunning Reminder for Purchase Order, one can create and send goods delivery reminders to your business partners to remind them of overdue delivery dates. You can print your Dunning Reminder with unfulfilled quantities and overdue dates.

##### Output Parameter Determination for Purchase Orders Dunning Reminder

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the perquisition step for the purchase order dunning reminder steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Administrator role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination. | The Output Parameter Determination screen displays. |  |
| 3 | Create Output Type for Dunning Reminder | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Output Type.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Dispatch Time : 1 (Immediately)Choose ActivateChoose Yes to Confirm Activation screen. | Output type Purchase Order Dunning is created. |  |
| 4 | Create Receiver for Dunning Reminder | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Receiver.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Role: LFExclusive Indicator: -(false)Choose Activate | The Receiver for Dunning Reminder is created. |  |
| 5 | Create Channel for Dunning Reminder | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step: Channel.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Role: LFChannel : PRINT(Printout)Exclusive Indicator: -(false)Choose Activate. | The channel for dunning reminder is created. |  |
| 6 | Create Printer Settings for Dunning Reminder | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step: Printer Settings.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Role: LFPurchasing Org.: BlankPrint Queue: DEFAULTNumber of Copies: 1Choose Activate. | The printer settings for dunning reminder is created. |  |
| 7 | Create Form Template for Dunning Reminder | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step: Form Template.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Role: LFOutput Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Channel: PRINT(Printout)Sender Ctry/Reg.: BlankForm Template: MM_PUR_PO_DUNNING_REMINDERChoose Activate. | The form template for dunning reminder is created. |  |
| 8 | Create Output Relevance for Dunning Reminder | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Output Relevance.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Relevance Indicator : X(true)Choose Activate | The Output Relevance for Dunning Reminder is created. |  |

##### Create Purchase Order for Dunning Reminder

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N) . | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300001In Header section, on the Org. Data tab, make the following entries:Purchasing Organization: 3310Purchasing Group:002Company Code: 3310In Items section,Material: TG0011Plant: 3310Storage Location: 331AQuantity: 100Deliv.Date: TodayNet Price: XAEDGo to Invoice Tab and enter Tax Code V0 .Tax Date: <Default Value>Go to Delivery Tab and enter the following entries:1st Rem./Exped. : 3-2nd Rem./Exped. : 2-3rd Rem./Exped. : 1- | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

##### Dunning Reminder on Purchase Orders Advanced

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note If you encounter issues for this step, you can create an incident under MM-PUR-GF-OC component. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Dunning Reminder on Purchase Order - Advanced (ME91FF) | The Dunning Reminder on Purchase Order Advanced screen displays |  |
| 3 | Define Purchasing Document Data | On the Dunning Reminder on Purchase Order -Advanced screen, make the following entries:Purchasing document: <use a PO you created previously>Choose Execute. | The Purchasing Document Data has been defined. |  |
| 4 | Choose Purchase Order | On the Purchase Order: Dunning Reminders screen, select this purchase order.Choose Generate Messages . | The dunning reminder output gets the generated. |  |
| 5 | Check Message Status | The Message Status is changed to Output Generated. | Message Status has been changed. |  |
| 6 | Preview the PO Dunning Reminder document | Choose Message Details to navigate to the Purchase Order Output screen.Choose the Output Type with Purchase Order Dunning , and choose Display Document to preview the Dunning Document.Close the PDF document. | The Purchase Order dunning reminder document is opened in PDF format. |  |
| 7 | Choose Back | Choose Back |  |  |
| 8 | Choose Save | On the Purchase Order: Dunning Reminders screen, choose Save . |  |  |

##### Schedule Dunning Reminder Output for Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note If you encounter issues for this step, you can create an incident under MM-FIO-PUR-PO-OM component. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Schedule Dunning Reminder output for Purchase Orders (F7083) | The Application Jobs screen displays |  |
| 3 | Create Job | Choose Create. | The New Job screen displays. |  |
| 4 | Define a Job | On the New Job: Schedule Dunning Reminder output for Purchase Orders screen,go to 1. Template Selection area, make the following entries:Job Template: <Job Template>, for example, Schedule Dunning Reminder output for Purchase OrdersJob Name: <Job Name>, for example, Schedule Dunning Reminder output for Purchase OrdersChoose Step 2 and go to 2. Scheduling Options area and make the following entries:Start Immediately : <selected>Job Start: <Current Time>Choose Step 3 and go to 3. Parameters area and make the following entries:Purchasing document: <use a PO you created previously>Document Type: <NB>Set Parameter settings according to your needs.Choose Schedule. | The job is created. |  |
| 5 | Dunning Reminder output for Purchase Orders created | On the Application Jobs screen.Go to Jobs (X) area and check the status until it changes to Finished. |  |  |
| 6 | Check Result | Click on Logs to navigate to the job log. |  |  |

#### Custom Attributes in Task Cards for Purchase Order Workflow (Optional)

Purpose

The requirement is to enable the Custom attributes along with workflow task data in task card and in My Inbox with Multi Select mode. Custom attributes allow to expose business-relevant data along with workflow task data. They are usually relevant for taking a decision regarding the task and can be prominently exposed in the Inbox of the user that is processing it.

|  |
| --- |
| Note When you process this step, make sure that you have processed the step Check Flexible Workflow for Purchase Order Approval and Configure Flexible Workflow for Purchase Order in the Preliminary Steps. |

##### Maintain CDS Based Custom Attributes for Purchase Order Workflow (Optional)

Purpose

Custom attributes allow the exposure of business-relevant data along with the workflow task data. They are usually relevant for taking a decision regarding the task and can be exposed in the Inbox of the user processing it. Here you can configure a CDS Entity and a CDS Entity Element for the purchase order Flexible Workflow Scenario. During creation of a task instance the configured CDS Entity Element will be used to retrieve the value displayed to the task processor.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Maintain CDS Based Custom Attributes | On the Configure Your Solution: Realize Phase screen, search Maintain CDS Based Custom Attributes , then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Output Control screen, choose Configure on the line of configuration step with name Maintain CDS Based Custom Attributes . | The Maintain CDS Based Custom Attributes screen is displayed. |  |
| 5 | Create Custom Attributes (Company Code) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < COMPANYCODE >• Active: Select• Description: <Company Code>• Rank: 60● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choose COMPANYCODEChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:4>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Company Code has been created for PO flexible workflow. |  |
| 6 | Create Custom Attributes (Purchase Order Creator) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < CREATEDBYUSER>• Active: Select• Description: <Purchase Order Creator >• Rank: 40● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choose CREATEDBYUSERChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:12>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Purchase Order Creator has been created for PO flexible workflow. |  |
| 7 | Create Custom Attributes (Purchase Order Date) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASEORDERDATE>• Active: Select• Description: <Purchase Order Date>• Rank: 50● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASEORDERDATEChoose Enter.● XSD Type: <Default Value:xs:date>● XSD Length: <Default Value:8>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:D Date (YYYYMMDD)>Choose Save. | The custom attribute Purchase Order Date has been created for PO flexible workflow. |  |
| 8 | Create Custom Attributes (Purchase Order Net Value) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASEORDERNETAMOUNT>• Active: Select• Description: <Purchase Order Net Value>• Rank: 100● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASEORDERNETAMOUNTChoose Enter.● XSD Type: <Default Value:xs:decimal>● XSD Length: <Default Value:23>● XSD Decimals: <Default Value:2>● ABAP type: <Default Value:P Packed number>Choose Save. | The custom attribute Purchase Order Net Value has been created for PO flexible workflow. |  |
| 9 | Create Custom Attributes (Purchase Group) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASINGGROUP>• Active: Select• Description: <Purchase Group>• Rank: 70● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASINGGROUPChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:3>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Purchase Group has been created for PO flexible workflow. |  |
| 10 | Create Custom Attributes (Purchasing Organization) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASINGORGANIZATION>• Active: Select• Description: <Purchasing Organization>• Rank: 80● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASINGORGANIZATIONChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:4>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Purchasing Organization has been created for PO flexible workflow. |  |
| 11 | Create Custom Attributes (Supplier) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < Supplier>• Active: Select• Description: <Supplier Details>• Rank: 90● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to chooseSUPPLIERChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:10>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Supplier has been created for PO flexible workflow. |  |
| 12 | Choose Back | Choose Back to return to the previous screen. |  |  |
| 13 | Choose Save. | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Maintain CDS Based Custom Attributes | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Maintain CDS Based Custom Attributes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain CDS Based Custom Attributes screen displays. |  |
| 3 | Create Custom Attributes (Company Code) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < COMPANYCODE >• Active: Select• Description: <Company Code>• Rank: 60● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choose COMPANYCODEChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:4>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Company Code has been created for PO flexible workflow. |  |
| 4 | Create Custom Attributes (Purchase Order Creator) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < CREATEDBYUSER>• Active: Select• Description: <Purchase Order Creator >• Rank: 40● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choose CREATEDBYUSERChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:12>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Purchase Order Creator has been created for PO flexible workflow. |  |
| 5 | Create Custom Attributes (Purchase Order Date) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASEORDERDATE>• Active: Select• Description: <Purchase Order Date>• Rank: 50● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASEORDERDATEChoose Enter.● XSD Type: <Default Value:xs:date>● XSD Length: <Default Value:8>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:D Date (YYYYMMDD)>Choose Save. | The custom attribute Purchase Order Date has been created for PO flexible workflow. |  |
| 6 | Create Custom Attributes (Purchase Order Net Value) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASEORDERNETAMOUNT>• Active: Select• Description: <Purchase Order Net Value>• Rank: 100● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASEORDERNETAMOUNTChoose Enter.● XSD Type: <Default Value:xs:decimal>● XSD Length: <Default Value:23>● XSD Decimals: <Default Value:2>● ABAP type: <Default Value:P Packed number>Choose Save. | The custom attribute Purchase Order Net Value has been created for PO flexible workflow. |  |
| 7 | Create Custom Attributes (Purchase Group) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASINGGROUP>• Active: Select• Description: <Purchase Group>• Rank: 70● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASINGGROUPChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:3>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Purchase Group has been created for PO flexible workflow. |  |
| 8 | Create Custom Attributes (Purchasing Organization) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < PURCHASINGORGANIZATION>• Active: Select• Description: <Purchasing Organization>• Rank: 80● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to choosePURCHASINGORGANIZATIONChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:4>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Purchasing Organization has been created for PO flexible workflow. |  |
| 9 | Create Custom Attributes (Supplier) for PO Flexible Workflow | Click New Entries, and enter the following entries:● Task/FlexWorkflow: WS00800238● Step ID: 19● Name of Attribute: < Supplier>• Active: Select• Description: <Supplier Details>• Rank: 90● CDS Entity: C_PURORDWORKFLOWTASKCARD● CDS Entity Element: use F4 to chooseSUPPLIERChoose Enter.● XSD Type: <Default Value:xs:string>● XSD Length: <Default Value:10>● XSD Decimals: <Default Value:0>● ABAP type: <Default Value:C Character String>Choose Save. | The custom attribute Supplier has been created for PO flexible workflow. |  |
| 10 | Choose Back | Choose Back to return to the previous screen. |  |  |
| 11 | Choose Save. | Choose Save. |  |  |

##### Approve Purchase Order through Task Cards (Optional)

Purpose

|  |
| --- |
| Note After completing step Maintain CDS based custom attributes for purchase order workflow (Optional), you can process this setup, and the step: Maintain CDS based custom attributes for purchase order workflow (Optional) is a prerequisite for this step. You can ignore this step if you did not set up the Steps:Maintain CDS based custom attributes for purchase order workflow (Optional). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of existing Purchase Orders is displayed. |  |
| 3 | Click Multi Select button | Click on Multi-Select button on left panel.Select Task Type is Release of Purchase Order. If the Select Task Type pop up screen is not displayed, then you can ignore this step. | The Task Summary has been displayed on the right panel. All the custom attributes should be displayed in table view on right panel along with task based custom attributes.Sequence should be based on ranking maintained in SSCUI 106664 (Maintain CDS Based Custom Attributes). |  |
| 4 | Select the Purchase Order | Select the purchase order that you want to approve. | The purchase order has been selected for approval. |  |
| 5 | Choose Approve | Choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 6 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

#### Purchase Order Workflow Review

##### Configure Purchase Order Flexible Workflow for Review

Purpose

In this procedure, you can configure the step Purchase Order Flexible Workflow for Reviewer. For all the purchase order workflow scenarios, along with approvers, reviewers also can be configured separately, and monitor the progress of the workflows during the entire workflow process. Reviewers do not have an option to approve/reject/rework the work items to be reviewed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entry:Workflow Name: <Test Workflow for Purchase Order>In section Start Conditions, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 50,000Currency: AEDIn the Steps area, choose Create and make the following entry:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Create.In the Review Steps area, choose Create and make the following entries:Step Type: Review Workflow of Purchase OrderAssignment By: UserUser: Select user from value help (with employee ID), for example, PURCHASER.Choose OK.Choose Create.Choose Save. | The workflow for purchase order is configured. |  |
| 4 | Activate Workflow Item | Select the workflow item you just created, and choose Activate.Note Make sure the default workflow Automatic Release of Purchase Order is activated. | The workflow item is activated. |  |

##### Review Purchase Order Items (Optional)

Purpose

In this procedure, purchase order workflow reviewers can login to system and review purchase order items.

|  |
| --- |
| Note If you did not execute [Configure Purchase Order Flexible Workflow for Review](#unique_96) [page ] 125, you can ignore this step. |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) | A list of existing purchase orders is displayed. |  |
| 3 | Review Purchase Order Items | Review the purchase order items. | Your purchase orders are displayed.After the purchase order workflow completes, the purchase order items would be invisible in the reviewer's My Inbox. |  |

#### Ad-hoc Approver in Purchase Order Workflow

Purpose

The purpose of this case is to implement the ad-hoc approver step in approval details of purchase order in app: Manage Purchase Orders.

##### Configure Flexible Workflow for Purchase Orders

Purpose

In this procedure, you configure the flexible workflow for purchase order approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system.You can translate workflow name and steps name to other languages via app Workflow Content Translation, for example, from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entry:Workflow Name: <Test Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 500,00Currency: AEDIn the Steps area, choose Create and make the following entry:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select user from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | A new workflow item is created. |  |
| 4 | Activate Workflow Item | Select the newly created workflow item, and choose Activate. | The workflow item is activated. |  |

|  |
| --- |
| Note Make sure the default workflow Automatic Release of Purchase Order has been activated. |

##### Create Purchase Order to Add Ad-hoc Workflow Steps

Purpose

In this procedure, you create a purchase order to add ad-hoc workflow steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Workflows screen displays. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. |  |  |
| 4 | Enter Purchase Order Data | Enter all the necessary data.On the General Information tab, make the following entries:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300001Company Code: 3310Purchasing Organization: 3310Purchasing Group: 003Currency: AEDOn the Items tab, from the Purchase Order Items screen, choose Create and make the following entries:Material: TG0011Plant: 3310Order Quantity: <100>Net Order Price: <30>Navigate to the selected item by clicking on the chevron (>) or by directly clicking on the item line.On the General Information tab, make the following entry:Storage Location: 331AFrom the Purchase Order Item section, choose Process Flow tab.The following entries display:Goods Receipt: yesInvoice Receipt: <selected>Verify Goods-Receipt-Based Invoice Verification is selected.On the tab Tax, check the following entry:Tax Code: <Input Tax Code>On the Schedule Lines tab, make the following entry:Delivery date: <a date in the future>Choose Apply. | Purchase order data is maintained. |  |
| 5 | Verify Purchase Order for Completeness and Save Purchase Order | Choose Order to save the purchase order. |  |  |
| 6 | Go to Approve Details to Edit | Navigate to the Approve Details tab, choose Edit to go to the Workflow screen. |  |  |
| 7 | Add the Ad-hoc Approver | Choose Create and make the following entry:Step Type: Release of purchase orderIn the Workflow Steps area, choose Create and make the following entry:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select user from value help (with Employee ID PURCHASER)Choose Create.Note Ensure that the user is assigned the business catalog SAP_MM_BC_PO_ADHOCAPPROVE_PC.Please contact your system administrator for required authorization. | The purchase order data is maintained. |  |
| 8 | Choose Save | Go to the Workflow screen, and choose Save. |  |  |

|  |
| --- |
| NoteThe Edit button is relevant only if the purchase orders are in approval or if the workflow has ended in error.If a purchase order with ad-hoc workflow steps is copied, the copy will not have the ad-hoc steps.The ad-hoc steps do not affect the workflow configuration in the Manage Workflows for Purchase Orders app.Only planned steps can be modified. |

##### Approve Purchase Order

Purpose

In this step, the purchaser manager can approve the purchase order accordingly.

Procedure

| Test Step | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The purchase order displays. |  |
| 4 | Approve Purchase Order | Select the purchase order on the left side of the screen and choose Approve at the bottom right. |  |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary and then choose Submit. | The purchase order is approved with approval reason. |  |

Log on to the SAP Fiori launchpad as a purchaser and repeat the above step to approve other purchase orders.

#### Output Channel External Output Management for Purchase Order

Purpose

The new type of channel External Output Management (EXTOM) is available and supports sending raw data from the standard output process to an external system. This function enables the output channel EXTOM for purchase orders in the Purchase Orders Advanced application. When a purchase order is maintained (created or changed) and is eligible for output management via the EXTOM channel, the output for the EXTOM channel shall be generated.

|  |
| --- |
| Note The output for the EXTOM channel shall be generated, and the Form Data Provider shall read the purchase order data and send the output XML to an external communication arrangement (communication scenario is SAP_COM_0881). When you implement this feature, the communication scenario SAP_COM_0881 should be active and correctly configured in the system. This communication scenario is scope-dependent, with the relevant scope item being 7JD (Integration of External Output Management Solution). If this Scope Item 7JD is not activated in the system, please ignore this step, as it is a prerequisite for this feature. |

##### Manage Output Queues for External Output Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the step to create the output queue for External Output Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Administrator role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Output Queues. |  |  |
| 3 | Create Queue | On the Mange Output Queues screen, choose Create then make bellow entries:Queue: Queue_EXTOMDescription: for EXTOM channelChoose Continue |  |  |
| 4 | Create Queue Settings | On the Mange Output Queues screen, go to the Queue Settings and make bellow entries:Transfer Type: Single TransferQueue Owner: Select from F4 to choose the valueRetention Period (Days) : 30 （For example） |  |  |
| 5 | Choose Create | Choose Create. | The queue has been created successfully. |  |

##### Output Parameter Determination for Purchase Orders External Output Management Channel

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the perquisition step for the purchase order External Output Management channel.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Administrator role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination. | The Output Parameter Determination screen displays. |  |
| 3 | Create External Output Management Channel for purchase order | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Channel.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellowentries:Output Type: PURCHASE_ORDER(Purchase Order)Role : LFChannel : EXTOM(External Output Management)Exclusive Indicator: -(false)Choose Activate |  |  |
| 4 | Create External Output Management Channel for Dunning Reminder | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Channel.On section Maintain Business Rules, choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Role : LFChannel : EXTOM(External Output Management)Exclusive Indicator: -(false)Choose Activate | The External Output Management Channel for Dunning Reminder is created. |  |
| 5 | Create Output Queue Settings for purchase order | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step: Output Queue Settings.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER (Purchase Order)Role : LFPrint Queue: assign Queue name (which is created on the above step)Data Transfer Mode: C(Compressed)Choose Activate. | The Output Queue Settings for Purchase Order is created. |  |
| 6 | Create Output Queue Settings for Dunning Reminder | On section Maintain Business Rules, choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING (Output type for Dunning Reminder)Role : LFPrint Queue: assign Queue name (which is created on the above step)Data Transfer Mode: C(Compressed)Choose Activate. | The Output Queue Settings for Dunning Reminder is created. |  |
| 7 | Create Form Template for Purchase Order | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Form Template.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER(Purchase Order)Role : LFChannel : EXTOM(External Output Management)Form Template: MM_PUR_PURCHASE_ORDERChoose Activate | The Form Template for Purchase Order is created. |  |
| 8 | Create Form Template for Dunning Reminder | On section Maintain Business Rules, choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_DUNNING(Output type for Dunning Reminder)Role : LFChannel : EXTOM(External Output Management)Form Template: MM_PUR_PO_DUNNING_REMINDERChoose Activate | The Form Template for Dunning Reminder is created. |  |

##### Create Purchase Order External Output Management Channel

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
|  | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. |  |  |
|  | Access App | Open Create Purchase Order - Advanced(ME21N). | The Create Purchase Order screen is displayed. |  |
|  | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300001In Header section, on the Org. Data tab, make the following entries:Purchasing Organization: 3310Purchasing Group: 003Company Code: 3310In Items section,Material: TG0011Plant: 3310Storage Location: 331AQuantity: 100Deliv.Date: TodayNet Price: X AEDGo to Invoice Tab and enter Tax Code: <Input Tax Code>.Tax Date: <Default Value> | The Create Purchase Order screen is displayed. |  |
|  | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |
|  | Check the Message Tab | Choose Messages to check if the EXTOM channel exists. | Output status is completed for EXTOM channel with Dispatch Time of 1. |  |

##### Create Purchase Order External Output Management Channel for Dunning Reminder

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
|  | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. |  |  |
|  | Access App | Open Create Purchase Order - Advanced(ME21N). | The Create Purchase Order screen is displayed. |  |
|  | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300001In Header section, on the Org. Data tab, make the following entries:Purchasing Organization: 3310Purchasing Group: 003Company Code: 3310In Items section,Material: TG0011Plant: 3310Storage Location: 331AQuantity: 100Deliv.Date: TodayNet Price: X AEDGo to Invoice Tab and enter Tax Code <Input Tax Code>.Tax Date: <Default Value>Go to Delivery Tab and enter the following entries:1st Rem./Exped. : 3-2nd Rem./Exped. : 2-3rd Rem./Exped. : 1- | The Create Purchase Order screen is displayed. |  |
|  | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

##### Dunning Reminder on Purchase Order for External Output Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note Note If you encounter issues for this step, you can create an incident under MM-PUR-GF-OC component. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
|  | Access App | Open Dunning Reminder on Purchase Order - Advanced(ME91FF) | The Dunning Reminder on Purchase Order Advanced screen displays |  |
|  | Define Purchasing Document Data | On the Dunning Reminder on Purchase Order -Advanced screen, make the following entries:Purchasing document: <use a PO you created previously>Choose Execute. | The Purchasing Document Data has been defined. |  |
|  | Choose Purchase Order | On the Purchase Order: Dunning Reminders screen, select this purchase order.Choose Generate Messages . | The dunning reminder output gets the generated. |  |
|  | Check Message Status | The Message Status is changed to Output Generated. | Message Status has been changed. |  |
|  | Preview the PO Dunning Reminder document | Choose Message Details to navigate to the Purchase Order Output screen.Choose the Output Type with Purchase Order Dunning , and choose Display Document to preview the Dunning Document.Close the PDF document. | The Purchase Order dunning reminder document is opened in PDF format. |  |
|  | Choose Back | Choose Back |  |  |
|  | Choose Save | On the Purchase Order: Dunning Reminders screen, choose Save . | Once you save the generated messages, the output status of type 'PURCHASE_ORDER_DUNNING' with the EXTOM channel is completed. |  |

### Relevant Features

Here are listed some important application functionalities related to Purchase Order outputs, Purchase Reports, and Invoice which are not covered in the above test procedures.

| Function Area | Function | Detailed Information | Comment |
| --- | --- | --- | --- |
| Purchase Order Output | Enable Partner Function (Ordering Address) in Purchase Order Output in WebGUI Create Purchase Order - Advanced (ME21N) | To use SSCUI 102524 Define Partner Schemas, make sure OA (Ordering Address) is maintained in Partner Functions in Procedure.Supplier can have several ordering locations which are captured using the partner function “OA” - Ordering Address in the Partner tab of PO header level in WebGUI Create Purchase Order - Advanced (ME21N). Administrator can use the Fiori App Output Parameter Determination to perform the configurations for the various determination steps for the Rule Purchase Order with Role BA for partner function OA (Ordering Address). When the partner function OA/BA is used, the custom purchase order form should have the address and communication details i.e. telephone, fax and email, of the OA partner function. The PO output document is generated with Supplier Address, Supplier Email ID, Supplier telephone number and supplier fax number of the partner function OA/BA when using Webgui Create Purchase Order - Advanced (ME21N). |  |
| Manage Purchase Orders Application | Enable Partner Functions in Manage Purchase Orders Application | SSCUI: 106258 Enable Partner Functions in Manage Purchase Orders ApplicationIn this step, you can use this SSCUI to enable the Partner tab in the App Manage Purchase OrdersIn a standard system this configuration step is switched off by default. Once the switch is on, you cannot turn it off. |  |
| Purchase Order with DMS Attachments | Enable purchase order with DMS attachments in WebGUI Create Purchase Order - Advanced (ME21N) | 1: SSCUI: 103542 (Define Output Settings for Document Type) to select Relevant and Merge.When Relevant and Merge are both selected for the document type SL1 and channel print in SSCUI: 103542 (Define Output Settings for Document Type), you can upload the attachments of SL1 document type in the Attachments Tab at the header level in the WebGUI Create Purchase Order - Advanced (ME21N). Then the output should contain the Attachments as Document along with purchase order output.2: SSCUI: 105346 (Active HDM for Attachment Object Type) for choose Attachment Object Type: PURCHASEORDERFor the printing of purchase order header attachments, please use SSCUI: 105346 (Active HDM for Attachment Object Type) . On the Activate HDM for Attachment Object Type: Change screen, select Attachment Object Type: PURCHASEORDER and click on Activate. Then, double-click the Activate Document Frameworks on the left side of the SSCUI screen, and ensure that Deactivate is unchecked for the PURCHASEORDER. Also, double-click the Maintain Defaults and Restricted Document Types on the left side of the SSCUI screen, and click the Default for the Document Type SL9, and do not click the Default for the Document Type SL1.3: Create the Purchase Order header Attachments in the WebGUI: Create Purchase Order - Advanced (ME21N)When creating the purchase order, you can go to the tab Document on purchase order head. Click the button Insert Row to add the existing SL1 or SL9 Document. Or you can click the button Create Document to create SL1 or SL9 Document.4: Display the Purchase Order message for the header attachmentsWhen you create the purchase order header attachments, you can click the Message button for your created purchase order. The output should contain the attachments as document along with the PO output. In the output line item, the number of attachments for the line item should match the number of attachments you attached. |  |
| Display Suppliers | WebGUI: Display Suppliers - Purchasing (MKVZ) | To use generic user Purchaser to display suppliers. |  |
| Display Purchasing Documents | WebGUI: Display Purchasing Documents by Supplying Plant (ME2W)WebGUI: Display Purchasing Documents by Material Group (ME2C)WebGUI: Display Purchasing Documents by Tracking Number (ME2B) | To use generic user Purchaser to display purchasing documents |  |
| Enter Supplier Invoice for Background Verification | WebGUI: Enter Supplier Invoice for Background Verification | To create supplier invoice in background. |  |
| Supplier Invoice Verification in Background | WebGUI: Schedule Supplier Invoice Jobs – AdvancedJob Template: Verification in Background | To post supplier invoice in background. |  |
| Invoice Verification: Check for duplicate invoices. | Please refer to note 2721713 - Invoice Verification: Check for duplicate invoices - FAQ for details. | Error message pops up when duplicate invoices are found. |  |
| Purchase Order with partner functions | When you create the purchase order using partner functions in the WebGUI Create Purchase Order - Advanced (ME21N) at the PO header level.Examples of partner functions are:AP/CP (Contact Person)VA/CA (Contract Address)WL/GS (Goods Supplier)ZM/ER (Employee Responsible) | To use SSCUI 102524 Define Partner Schemas, ensure that partner functions CP,CA,GS,ER are maintained in Partner Functions in Procedure 0002 (Standard PO).To use App: Output Parameter Determination to configure output parameter determination for purchase order.On the Output Parameter Determination screen, choose Show Rules for: Purchase Order and separately choose the following Determination Steps:ReceiverChannelPrinter SettingsForm TemplateAdd relevant entries for all partner functions converted values as Role for each determination steps.Role Values:AP (Contact Person)VA (Contract Address)WL (Goods Supplier)ZM (Employee Responsible)To use the WebGUI Create Purchase Order - Advanced (ME21N) to create the purchase order using partner functions at the PO header level.After saving the Purchase Order and clicking on Messages, all the partner functions should be enabled in the output management. |  |

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
> Flagged while digesting this document, not verified: Workflow start-condition amounts differ across sections (example 10 AED, 50,000 AED, 500,00 AED) while the PO approval step states approval applies above 500 AED for purchasing group 003; they are examples but may be inconsistent.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/direct-procurement-with-inbound-delivery-2tx-ae-test-script-sap-s-4han]]
- related-to :: [[10-procurement/test-script-cross-company-purchasing-organization-2r3-ae-854]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J45_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 226,709 chars in the whole document
