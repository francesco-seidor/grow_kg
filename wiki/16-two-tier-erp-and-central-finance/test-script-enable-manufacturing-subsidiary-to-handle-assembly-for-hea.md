---
id: 16-two-tier-erp-and-central-finance/test-script-enable-manufacturing-subsidiary-to-handle-assembly-for-hea
title: "Test Script: Enable Manufacturing Subsidiary to Handle Assembly for Headquarter (2WL_AE) (2WL_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2WL: subsidiary performs make-to-order assembly for headquarters, from sales order to invoice."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/subsidiary-assembly-for-hq]
aliases: [2WL_S4CLD2608_BPD_EN_AE]
keywords: [Manufacturing Subsidiary Assembly for Headquarters, assembly processing, subcontracting, make-to-order production, test script prerequisites, material requirements planning, production orders, outbound delivery, billing documents, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2WL_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-885
topic: 16-two-tier-erp-and-central-finance/subsidiary-assembly-for-hq
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Enable Manufacturing Subsidiary to Handle Assembly for Headquarter (2WL_AE) (2WL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2WL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Manufacturing Subsidiary Assembly for Headquarters** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Enable Manufacturing Subsidiary to Handle Assembly for Headquarter (2WL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851059)

[2 Prerequisites 4](#_Toc232851060)

[2.1 System Access 4](#_Toc232851061)

[2.2 Roles 4](#_Toc232851062)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851063)

[2.4 Business Conditions 7](#_Toc232851064)

[2.5 Integration Set-up 7](#_Toc232851065)

[2.6 Preliminary Steps 8](#_Toc232851066)

[2.6.1 In the Headquarter System 8](#_Toc232851067)

[2.6.1.1 Post Initial Stock for Raw Materials 8](#_Toc232851068)

[2.6.1.2 Create Info Record for Semi-Finished Material 9](#_Toc232851069)

[2.6.2 In the Subsidiary System 11](#_Toc232851070)

[2.6.2.1 Create Info Record for Raw Materials 11](#_Toc232851071)

[3 Overview Table 14](#_Toc232851072)

[4 Test Procedures 16](#_Toc232851073)

[4.1 Display Sales Order and Order Confirmation (Optional) 16](#_Toc232851074)

[4.2 Material Requirements Planning 18](#_Toc232851075)

[4.3 Monitor Material Coverage 19](#_Toc232851076)

[4.4 Convert Purchase Requisition to Purchase Order 21](#_Toc232851077)

[4.5 Approve Purchase Orders (Optional) 22](#_Toc232851078)

[4.6 Goods Issue from Headquarter 23](#_Toc232851079)

[4.7 Post Goods Receipt 24](#_Toc232851080)

[4.8 Convert Planned Order to Production Order 25](#_Toc232851081)

[4.9 Release Production Order 26](#_Toc232851082)

[4.10 Material Staging into Production Storage Location 28](#_Toc232851083)

[4.11 Pick Components for Production 29](#_Toc232851084)

[4.12 Confirm Assembly Activities 30](#_Toc232851085)

[4.13 Post Goods Receipt for Production Order 31](#_Toc232851086)

[4.14 Create Delivery 32](#_Toc232851087)

[4.15 Execute Picking 33](#_Toc232851088)

[4.16 Post Goods Issue for Delivery 34](#_Toc232851089)

[4.17 Send Advance Shipping Notification 35](#_Toc232851090)

[4.18 Post Goods Receipt at Headquarter 36](#_Toc232851091)

[4.19 Create Billing Document 37](#_Toc232851092)

[4.20 Send Invoice 39](#_Toc232851093)

[4.21 Review Supplier Invoice at Headquarter (Optional) 40](#_Toc232851094)

[5 Appendix 41](#_Toc232851095)

[5.1 Succeeding Processes 41](#_Toc232851096)

## Purpose

In this two tier scenario, the manufacturing subsidiary handles the assembly processing for headquarters.

Overview

This scope item runs a Make-to-Order scenario (assembly processing) at a subsidiary. A sales order is automatically uploaded to the subsidiary system when a subcontracting purchase order is created in the headquarters system. The receipt of the sales order is electronically confirmed to headquarters. Components are issued manually from the headquarter and received at subsidiary with zero price. The delivery process occurs after the ordered goods are produced by the manufacturing subsidiary. The process includes the electronic sending of an advance shipping notification to the headquarters. Afterwards, the billing process runs at the subsidiary, and an electronic invoice is sent to the headquarters.

To realize end to end process, some additional test steps for reference that exclusively happens at headquarter are provided. Headquarter system roles are not included in the Roles section.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

The process to be tested in this test script is for the Subsidiary side of a 2-tier scenario. Integration between Subsidiary system (S/4HANA Cloud, representing the supplier side) and Headquarters system (representing the buyer side) shall be set up in advance. You will be able to process the test steps ONLY after the corresponding buyer system has sent the required messages.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SG35 |  | SEMI35 – Assembly Unit 1 (2T) |
| Material | RM35 |  | RAW35 – Assembly Component 1 (2T) |
| Material | RM36 |  | RAW36 – Assembly Component 2 (2T) |
| Plant | 3310 |  | Plant 1 AE |
| Storage Location | 331A |  | Std. storage for finished products |
| Storage Location | 331B |  | Std. storage for production |
| Storage Location | 331C |  | Raw mat. sto. loc. |
| Customer | 33101011 |  | Domestic UAE Customer 11 |
| Supplier | 33100088 |  | Domestic AE Supplier 88 |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |
| Shipping Point | 3310 |  |  |

Bill of Material SG35

This overview shows the bill of material structure of SG35 and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| SG35 | 0 | SEMI | PC | Semifinished Good for MT0 processing |  |
| RM35 | 1 | RAW | PC | External procured |  |
| RM36 | 1 | RAW | PC | External procured |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNR | Create Product Master of Type "Raw Material" |
| BNS | Create Product Master of Type "Semi-Finished Good" |
| BND | Create Customer Master |

### Business Conditions

Before this scope item can be tested, the business conditions about BNU and BNZ must be met.

The business processes described in this Test Script refer to steps from some other scope items (BJE and 2EL). Thus you must also have fulfilled business conditions for such referred scope items before you are able to start going through this one:

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the steps described in the master data script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the master data script. Posting Period is up to date. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | All relevant steps described in the Business Conditions are completed. |
| 2EL - Integration of Sales with External Buyers | All relevant steps described in the Business Conditions are completed. |
| 2EJ – Integration of Procurement with External Suppliers | All relevant steps described in the Business Conditions are completed. |
| BMY – Subcontracting | All relevant steps described in the Business Conditions are completed. |

### Integration Set-up

To execute this activity, process the following scope items step up guide by using the master data from this document (see the following table):

|  |
| --- |
| Steps to process from set-up guide of Integration of SAP S/4HANA Cloud Public Edition Sales with Procurement – 2EL |
| Cloud-to-Cloud Integration (Section 2) |

|  |
| --- |
| Steps to process from set-up guide of Integration of SAP S/4HANA Cloud Public Edition Procurement with Suppliers – 2EJ |
| Cloud-to-Cloud Integration (Section 2) |

| Master Data | Sample Value |
| --- | --- |
| Customer | 3310 1011 |
| Supplier | 3310 0088 |

### Preliminary Steps

#### In the Headquarter System

##### Post Initial Stock for Raw Materials

Purpose

In a real business case, the materials are usually purchased from external vendors. In this case, the process is covered by standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | TheManage Stock screen displays. |  |
| 3 | Search Material | Make the following entries, and press Enter:Material: RM35Plant: Plant 1 AE3310 | The stock overview for the material is displayed. |  |
| 4 | Add Initial Stock | Choose the Unrestricted-Use Stock icon for the raw material storage location 331C.On the Manage Stock dialog box, make the following entries, and choose Post:Stock Change: Initial EntryQuantity: 1000Document date: <Current Date>Posting date: <Current Date> | The stock is added and the system displays a confirmation message. |  |
| 5 | Add Initial Stock of Another Material | Repeat the steps 2 to 4 for Material: RM36. | The stock is added and the system displays a confirmation message. |  |

##### Create Info Record for Semi-Finished Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a purchasing info record for a semi-finished material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchasing Info Records (F1982) app. | The Manage Purchasing Info Records is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: SubcontractingPurchasing Organization: 3310Supplier: 33100088Material: SG35Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days:10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: 100Select the following checkboxes:Goods-Receipt-Based Invoice VerificationAutomatic Sourcing | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 6.17Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

#### In the Subsidiary System

##### Create Info Record for Raw Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create purchasing info records for raw materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchasing Info Records (F1982) app. | The Manage Purchasing Info Records is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33100088Material: RM35Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days:10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note When the Time Dependent Tax (TDT) is activated through SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in SSCUI.When the Registration for Indirect Taxation Abroad (RITA) is activated, tax registration country is maintained for company code in SSCUI 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as a default value, but you can change to the valid country ID that is maintained in SSCUI accordingly.Order Unit: PCStandard Order Quantity: 100Select the following checkboxes:Goods-Receipt-Based Invoice VerificationAutomatic Sourcing | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: .59Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | The purchasing info record is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Display Sales Order and Order Confirmation (Optional)](#unique_12) [page ] 16 | Internal Sales Representative | Display Sales Orders - VA03 (VA03) | Sales order is displayed and an Order Confirmation is sent to Headquarters. |
| [Material Requirements Planning](#unique_13) [page ] 18 | Production Planner | Schedule MRP Runs (F1339) | MRP run executed for the sales order created earlier. |
| [Monitor Material Coverage](#unique_14) [page ] 19 | Production Planner | Manage Material Coverage - New Version (F0251A) | The Monitor Material Coverage- Net and Individual Segments screen displays. |
| [Convert Purchase Requisition to Purchase Order](#unique_15) [page ] 21 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase order is created for the purchase requisition. |
| [Approve Purchase Orders (Optional)](#unique_16) [page ] 22 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase Manager approves the Purchase Order. |
| [Goods Issue from Headquarter](#unique_17) [page ] 23 | Purchaser | Display Subcontracting Stocks by Supplier (ME2ON) | Goods (raw materials) are issued from Headquarter to Subsidiary. |
| [Post Goods Receipt](#unique_18) [page ] 24 | Warehouse Clerk | Post Goods Movement (MIGO) | Post the goods receipt for the Raw Material against the subcontracting PO. |
| [Convert Planned Order to Production Order](#unique_19) [page ] 25 | Production Planner | Manage Material Coverage - New Version (F0251A) | Planned order is converted into production order. |
| [Release Production Order](#unique_20) [page ] 26 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The production order is released. |
| [Material Staging into Production Storage Location](#unique_21) [page ] 28 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | Materials needed are staged for final assembly. |
| [Pick Components for Production](#unique_22) [page ] 29 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | The Picking List: Initial Screen displays. |
| [Confirm Assembly Activities](#unique_23) [page ] 30 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Production Operator confirms the production operations. |
| [Post Goods Receipt for Production Order](#unique_24) [page ] 31 | Warehouse Clerk | Post Goods Movement (MIGO) | The Post Goods Receipt for Order screen displays. |
| [Create Delivery](#unique_25) [page ] 32 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | Outbound delivery is created. |
| [Execute Picking](#unique_26) [page ] 33 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. |
| [Post Goods Issue for Delivery](#unique_27) [page ] 34 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Shipping Specialist makes the Goods Issue for the delivery. |
| [Send Advance Shipping Notification](#unique_28) [page ] 35 | Shipping Specialist | Display Outbound Delivery (VL03N) | ASN is sent to Headquarters |
| [Post Goods Receipt at Headquarter](#unique_29) [page ] 36 | Warehouse Clerk | Post Goods Movement (MIGO) | Headquarter receives the assembly material. |
| [Create Billing Document](#unique_30) [page ] 37 | Billing Clerk | Create Billing Documents - VF04 (VF04) | Billing Clerk creates the Billing Document. |
| [Send Invoice](#unique_31) [page ] 39 | Billing Clerk | Manage Billing Documents (F0797) | Invoice is sent to Headquarters |
| [Review Supplier Invoice at Headquarter (Optional)](#unique_32) [page ] 40 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Headquarter receives and reviews the Supplier invoice. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Display Sales Order and Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you see newly created sales order and order confirmation in SAP S/4HANA supplier system. A Sales Order is automatically created from PO and an Order Confirmation is automatically sent to the Buyer system.

|  |
| --- |
| Note Subcontracting Purchase Order (PO) gets created in opposite system (buyer) and sent to the SAP S/4HANA system (subsidiary as supplier side). For details, see the Create Purchase Order test procedure in the Subcontracting (BMY) test script. |

Procedure

In this activity, you see newly created sales order and order confirmation

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Internal Sales Representative. |  |  |
| 2 | Open Display Sales Order | Open Display Sales Orders - VA03 (VA03). | The Display Sales Document screen appears. |  |
| 3 | Enter search criteria | Enter PO number from the previous step in the Purchase Order No. field and choose Search. Then choose the entry with purchase order number in the dialog box.. |  |  |
| 4 | Display sales order | Sales order is displayed with correct data. Make a note of the sales order ID. | You can see all the sales order details. |  |
| 5 | Display Order Confirmation | On the Display Standard Order xxx: Overview screen, choose More > Extras > Output > Header > Edit | Output display screen appears |  |
| 6 | Check status for Outputs | On the Display Standard Order xxx: Output screen, check Status for outputs with Output Type ORDER_CONFIRMATION or ORDER_CONFIRMATION_CHANGE and Channel EDI | Successfully outputs sent displayed as Completed. |  |

In this activity, you see how subcontracting purchase order is created at Headquarter (optional)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order Advanced | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order Data | Enter all of the necessary data.Order type: NB Standard POSupplier: 3310 0088In Header section, on the Org. Data tab:Purch. Org.: 3310Purch. Group: 001Company Code: 3310In Item Overview section:Item Category: LMaterial: SG35Plant: 3310Storage Location: 331AQuantity: xNet Price: xIn Item Detail section, on Confirmations tab:Conf. Control: Confirmations | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Subcontracting Purchase Order is created.Purchase Order Number is displayed. |  |

Result

In this step, you display the sales order and order confirmation.

### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To execute this activity, process the following steps using the master data from this document (see also the following table):

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Schedule MRP Runs (F1339) app. | The Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create.On the New Job screen, make the following entries:Job Template: Material Requirements Planning (MRP)Job Name: MRP for SG35Choose Step 2.In the Scheduling Options section:Select the Start Immediately checkbox.Choose Define Recurrence Pattern.On the Scheduling Information dialog box, in the Recurrence Pattern field, select Single Run, and then choose OK.Choose Step 3.Choose Step 4.In the Parameter section:In the Plant field, enter 3310.In the Material field, enter SG35.Select the Changed BOM Components checkbox.In the Planning Mode field, enter 1 (default).Choose Check.Tip To locate the Check button, scroll down and check on the left-bottom side of the screen.Choose Schedule. | The new job is created and the Application Jobs screen is displayed again. |  |

Result

In this step, you start the MRP run for the sales order created earlier.

### Monitor Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the MRP has performed, you can display the Semi finished Good (SG35) with in the stock and requirements list in the App Monitor Material Coverage Net / Individual Segments.

|  |
| --- |
| Note Requirements planning has been carried out. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Material Coverage - New Version (F0251A). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Check Default Area of Responsibility | On the top right of the screen, choose your profile icon and then choose MRP Setting. On the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, ensure that the AOR Status toggle is set to AOR is Assigned for the following plant.Plant 1 AE 3310Tip For the other plant entries, the AOR Status toggle should be set to AOR is Unassigned. |  |  |
| 4 | Select Material | Mark the checkbox of the following materials, and then choose Manage Materials in bottom right.Material: SG35, RM35, RM36 | The Material screen and Material Details screen display. |  |
| 5 | Review Stock / Requirement List | Select the corresponding material on the Material screen on the left | The detailed Stock / Requirement List displays |  |
| 6 | View the report | Results for SG35: An individual Planned Order is created for the Sales OrderResults for RM35: An individual Purchase Requisition is created for the Sales OrderResults for RM36: An individual Purchase Requisition is created for the Sales OrderNote Note the Purchase Requisition numbers for the Raw materials (RM35 and RM36). These Purchase Requisitions are required for the [Convert Purchase Requisition to Purchase Order](#unique_15) [page ] 21 test procedure. |  |  |
| 7 | Back | Choose Back. |  |  |

### Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase order for consumables. This activity is only required if you do not convert an existing purchase requisition as described in Assign Purchase Requisition / Create Subcontract Order.

|  |
| --- |
| Note You can store purchase order data as template for frequently used data. To save the data to a template, choose Save as Template. To load data from a template, choose Load from Template. Use the tile Monitor Stock / Requirements List to check purchase requisition number for RM35 and RM36 |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori LaunchPad using the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Create Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Enter Purchase Order data | Enter the following data and choose Enter:Order type: Standard POSupplier : 33100088In the area of Header / Org. Data:Purchasing Org:3310Purchasing Group :001Company Code:3310In the area of Document Overview, Select Purchase Requisition under selection variant.In the area of Purchase Requisitions, enter the following materials and choose ExecuteMaterial: RM35 and RM36Select the listed purchase requisition and choose Adopt.In Item Detail section, Choose Item 10 (RM35)on the Invoice tab:Invoice Receipt: Uncheck the invoice receipt check boxIn Item Detail section, Choose Item 20 (RM36)on the Invoice tab:Invoice Receipt: Uncheck the invoice receipt check box | All data is entered. The Item Detail screen displays.Selected purchase requisitions is copied to item overview screen |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. |  |

### Approve Purchase Orders (Optional)

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
| Note Only POs with a value higher than 500.00 USD can be released in this transaction. POs with a value under this amount required not to be released. For POs under this amount, this step can be skipped. The above created purchase order have zero value, so we may not trigger approval based on value. Release should be configured with other parameters |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to Fiori Launch Pad as Purchasing Manager. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Approve Purchase Order | Open My Inbox - All Items (F0862). | A list of already created Purchase Orders is displayed. |  |
| 3 | Check Purchase Order Status | Search for Purchase Order with Need Approval Status. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase order in left of the screen and click Approve in bottom right. | The Submit Decision dialog box is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to Fiori Launch Pad | Choose the Home button to go back to the Fiori Launch pad. | The Fiori Launch Pad is displayed. |  |

### Goods Issue from Headquarter

Purpose

In this activity, Goods Issue is posted in the headquarter and communicated to subsidiary. For details, see the Transfer Posting test procedure in the Subcontracting (BMY) test script.

Procedure

This step is manual process and communication between HQ and Subsidiary is done email or phone.

In this procedure, you can post goods issue against the subcontracting purchase order

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log On to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Subcontracting Stocks by Supplier (ME2ON). | The app name screen displays. |  |
| 3 | Subcontracting Cockpit | Enter the following data:Supplier: 33100088Assembly: SG35With Reqts from SC Requisns: checkW.Ext.Receipts from Requisns: checkWith Ext.Receipts from POs: checkChooseExecute. |  |  |
| 4 | Subcontracting Cockpit | Expand the Components column for the following materials:Material: RM35 and RM36Find the line items with your purchase order number. Use Ctrl to select both lines.Select Morethen Post Goods Issue.If there is no storage location then post goods issue ends with error.In the Create Goods Issue screen maintain the followingStorage Location:331CSelect the items and choose create document. |  |  |

### Post Goods Receipt

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
| Note Goods Issue against the subcontracting purchase order must have been created in the headquarter system (buyer side). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log On to Fiori Launch Pad as Warehouse Clerk role. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Post Goods Movement tile | Open Post Goods Movement (MIGO). | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Order screen, make the following entries and choose Enter:Goods Receipt : SelectPurchasing Order : SelectOrder number: Purchase Order numberGR goods receipt: 101 | The items of the selected Purchase Order display. |  |
| 4 | Choose the Quantity tab and confirm the quantity | Confirm the quantity. |  |  |
| 5 | Select Item ok Indicator | Select the Item OK checkbox. |  |  |
| 6 | Post | Choose Post | The system displays the message Material document 5000000XX 201X posted. |  |

### Convert Planned Order to Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, planned order is converted into production order.

|  |
| --- |
| Note Planned order for assembly semi finished good (SG35) is generated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select the Material | Make the following entry, and choose Go:Material: SG35Choose the row corresponding to the material SG35, and navigate inside the material details.Note Ensure that you choose the row with the correct customer order in the Individual Segment column. | The Manage Material Coverage screen displays. |  |
| 4 | Convert Planned Order to Production Order | Choose Convert from the Actions drop-down menu for the generated planned order.In the Convert Planned Order dialog box, choose OK. | The production order is created. |  |

Result

A production order for the semi finished good SG35 has been created. Make a note of the production order.

### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the production order.

|  |
| --- |
| Note The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Production Orders (F2336). | The Manage Production Orders screen displays. |  |
| 3 | Check Default Area of Responsibility (supervisor) | On the Manage Production Orders screen, make the following entries:Check Default Area of Responsibility (supervisor).Select the user from the top left corner and choose App settings then Area of Responsibility Production Supervisor. Check whether only this entry is displayed:Plant 1 AE (3310)MTO w/o VC Val. (YB4) | If no entry Plant 1 AE (3310) in the Area of Responsibility(Supervisor) screen, choose add to select it and then choose OK.For other plant entries in the Area of Responsibility (Supervisor) screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Production Order | On the Manage Production Orders screen, enter the following search condition as filter.Choose Adapt Filters to display more selection filter. Choose More filters under Material and Plant. Check the checkbox for Material and Plant and choose Go. Choose OK. The Material and Plant fields are then added to filter bar.Status: CreatedMaterial: SG35Plant: 3310 (Production plant)Choose Go to execute.Choose the filtered production order entry. | The Manage Production Orders screen displays. |  |
| 5 | Execute Release | Choose Release on the top right corner. | Order is released. |  |

Result

The production order for Semi finished Good (SG35) is released.

### Material Staging into Production Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you stage materials for production. In case there is sufficient stock available on the production storage location no line items are generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.Staging Types: SLoc.Level (Activate checkbox).Plant: 3310Selection Horizon for Remts: <date in the future - after scheduled start date>Select the Production/Process order tab.Production Order: <Production Order Number> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | Select the required line items from the left-hand margin and choose Replenishment proposal from the top of the screen. |  |  |
| 5 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment elements. |  |  |
| 6 | Enter Replenishment Storage Location | On the bottom half of the split screen, select the lines and enter the replenishment storage location (331C). |  |  |
| 7 | Select Stage | Choose Stage in the middle of the screen. |  |  |
| 8 | Save | Choose Save. |  |  |

Result

Missing materials are transferred to the shop floor from the designated storage area.

### Pick Components for Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The released production order is now ready for picking. Only those materials that are not in the service stock at the assembly aisle are to be picked. For picking, the operator selects the specific picking list that can be called up directly with the production order number. The operator has a series of further selection options to allow for optimal worklist selection.

|  |
| --- |
| Note Ensure that sufficient material is present on stock. Use the tile Monitor Stock / Requirements List to check the stock. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter relevant search criteria | Make the following entries and choose Execute.Profile: 000002Production Order: <Your Production Order number> | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. | A list of all the selected reservations is displayed. |  |
| 5 | Post | Choose Post to post the goods movements. |  |  |

### Confirm Assembly Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process shows the processing status of orders, different operations, and individual capacities. It is an instrument for controlling orders. This scope item uses time event confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Perform Work screen, make the following entries and press Enter:Order: Production Order Number you notedOperation: for example, operation 0010 |  |  |
| 4 | Enter fields in Quantities Section | In the Quantities section, make the following entries:Yield: <enter the amount you want to Confirm> |  |  |
| 5 | Enter fields in Activities Section | In the Activities section, make the following entries:Setup: <enter the setup time you want to confirm for this operation>Machine : <enter the machine time you want to confirm for this operation>Labor: <enter the labor time you want to confirm for this operation> |  |  |
| 6 | Save your entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created. If you would like to make partial confirmation, you can choose Post. |  |
| 7 | Repeat steps | Go back and repeat steps 3 to 6 for operation number 0020, 0030 and save your entries. |  |  |

Result

The final confirmation for the production order has been done.

### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to post the goods receipt for the production order

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). | The Goods Receipt Order – User name screen displays. |  |
| 3 | Enter Details | Make the following entries and press Enter.Action: Goods ReceiptReference: OrderOrder: <Production Order Number> (From previous step)Move Type: 101Plant: 3310Storage Location: 331A | Previous settings might be changed by other processes. Check if the value in the Action field is Goods Receipt and the value in the Reference field should be Order. If not, maintain the same. |  |
| 4 | Check | Set Item OK indicator and choose Check. |  |  |
| 5 | Post | Choose Post. |  |  |

Result

Semi finished Goods (SG35) were received.

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Deliveriy With Order Reference screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point:3310Selection Date: <Sales order creation date +5 or Sales order Schedule line dateOrder: <Sales order number created previously>Choose Continue. |  |  |
| 4 | Create Delivery | Choose Save. | Creation of a delivery is triggered. |  |

Result

You successfully created the outbound delivery for the sales order. Make a note of the Delivery number.

### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area, where goods that are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Shipping Specialist. | The SAP Fiori launchpad screen displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries – VL06O screen displays. |  |
| 3 | Choose For Picking | Choose For Picking. |  |  |
| 4 | Enter shipping point | Make the following entries and choose Execute.Shipping point: 3310Select the Only Picking without WM option.Picking Date: <Current Date + 1>Choose Execute. |  |  |
| 5 | Change outbound delivery | From Day’s Workload for Picking, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | Enter a quantity equal to the delivery quantity in the Picked Qty field for picking related items. |  |  |
| 7 | Choose Enter | Press Enter. |  |  |
| 8 | Save | Choose Save. | The delivery gets picked. |  |

### Post Goods Issue for Delivery

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
| 1 | Log on | Log onto the SAP Fiori launchpad as Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and then choose Execute:Shipping Point: 3310 |  |  |
| 4 | Post goods issue | Mark the relevant delivery and choose Post Goods Issue. Select the current date from the dialog box. | The goods issue is posted. |  |

### Send Advance Shipping Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

ASN is automatically sent to the Buyer system.

|  |
| --- |
| Note Goods issues must be available in the SAP S/4HANA system (supplier side). |

Procedure

This step is automatically generated.

You can do the optional output check, to verify, whether the confirmation is delivered.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Display Outbound Delivery | Enter your Delivery number and choose Continue.From the Delivery xxxxxxxx Display: Overview screen, choose More > Extras > Delivery Output > Output control |  |  |
| 4 | Check Status for Outputs | Check Status for outputs with Output Type DELIVERY_NOTE and Channel EDI . Successfully sent outputs are displayed as Completed |  |  |

Result

ASN is sent to the Buyer system.

### Post Goods Receipt at Headquarter

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the inbound delivery at Headquarter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Warehouse Clerk role. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Post Goods Movement tile | Open Post Goods Movement (MIGO). | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Order screen, make the following entries and choose Enter:Goods Receipt : SelectInbound Delivery: SelectInbound Delivery Number: Inbound Delivery NumberGR goods receipt: 101Note To get the Inbound Delivery Number, open the Display Purchase Order - Advanced (ME23N) app, search for the purchase order created in the headquarter system, and check the Confirmations tab. | The items of the selected Purchase Order display. |  |
| 4 | Choose the Quantity tab and confirm the quantity | Confirm the quantity. |  |  |
| 5 | Select Item Ok Indicator | Select the Item OK check box. |  |  |
| 6 | Post | Choose Post | The goods receipt is posted and the system displays the confirmation message. |  |

Result

Goods Receipt is posted against the inbound delivery at Headquarter.

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create billing document against the outbound delivery.

|  |
| --- |
| Note Goods receipt against the Inbound delivery should be created in opposite system (buyer). As the billing document creation in the SAP S/4HANA system (subsidiary as supplier side) triggers a supplier invoice to the opposite system which requires goods receipt. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open the Open the Create Billing Documents app. | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.You must set the following settings to ON.Set billing date and type before billingCreate separate billing document for each item of billing due listAutomatically post billing documentsDisplay billing documents after creationChoose delivery items to the billed and select quantitiesChoose OK. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if required. | Sales documents are displayed in the results. |  |
| 5 | Choose Individual Billing Document | Select a row of sales document created previously and choose Create Billing Documents. | The Create Billing Documents window is displayed. |  |
| 6 | Maintain Billing Date | Choose the billing type F2 Invoice (F2) and maintain billing date, for example, the current date. Choose OK and then Save. | The new billing document is created. |  |
| 7 | Display Billing Document after Creation | The billing document appears automatically. | The system generates an invoice for billing. |  |

Result

Billing document is generated for the sales document.

### Send Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, Supplier Invoice is automatically sent to Headquarter.

Procedure

This step is automatically generated.

You can do the optional output check, to verify, whether the confirmation is delivered.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 3 | Display billing document | Input the Billing document number and press Enter.Select the billing document item, and choose Display. | Billing Document displayed |  |
| 4 | Display Output and check status | On the Billing Document screen, chose the last assignment block - Output Itemscheck Status for outputs with Output Type BILLING_DOCUMENT and Channel EDI. Successfully sent outputs are displayed as Completed |  |  |

Result

Invoice is sent to the Buyer system.

### Review Supplier Invoice at Headquarter (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, a supplier invoice is displayed at Headquarter. These test steps are processed only when the corresponding supplier system sends an invoice

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Supplier Invoice List | Open Supplier Invoices List (F1060A). | The Supplier Invoice List screen is displayed. |  |
| 3 | Search for Supplier Invoice | Enter the following details and choose Go.Reference: <Billing document number created in [Create Billing Document](#unique_30) [page ] 37>Select the invoice in the search results to review the details. |  |  |

Result

Supplier Invoice is displayed at the Headquarter system.

## Appendix

### Succeeding Processes

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Complete the following activities:Posting a Customer Invoice in AccountingOverdue ReceivablesDisplay Customer BalancesManage Customer Line Items |

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

## Connections
- part-of :: [[_cluster]]
- see-also :: [[12-production-and-manufacturing/make-to-order-production-semifinished-goods-planning-and-assembly-1bm]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2WL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 62,938 chars in the whole document
