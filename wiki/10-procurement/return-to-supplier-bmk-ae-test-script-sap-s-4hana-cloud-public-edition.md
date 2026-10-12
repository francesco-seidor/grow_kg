---
id: 10-procurement/return-to-supplier-bmk-ae-test-script-sap-s-4hana-cloud-public-edition
title: "Return to Supplier (BMK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BMK_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for the Return to Supplier scope item (BMK_AE, UAE): prerequisites, roles, master data and step-by-step Fiori tests for advanced and basic returns to a supplier."
cluster: 10-procurement
tags: [kb/procurement, topic/return-to-supplier]
aliases: [BMK_S4CLD2608_BPD_EN_AE]
keywords: [Return to Supplier, returns purchase order, advanced returns management, basic return to supplier, outbound delivery, goods issue, supplier credit memo, replacement material, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1289
topic: 10-procurement/return-to-supplier
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Return to Supplier (BMK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BMK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Return to Supplier** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Return to Supplier (BMK_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Return to Supplier (BMK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862323)

[2 Prerequisites 4](#_Toc232862324)

[2.1 System Access 4](#_Toc232862325)

[2.2 Roles 4](#_Toc232862326)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862327)

[2.4 Business Conditions 6](#_Toc232862328)

[2.5 Preliminary Steps 7](#_Toc232862329)

[2.5.1 Return Reason “Wrong material delivered” 7](#_Toc232862330)

[2.5.2 Return Reason “Delivered quantity too high” 7](#_Toc232862331)

[2.5.3 Return Reason “Wrong Trading Good in sales order” 7](#_Toc232862332)

[2.5.4 Return Reason “Quality Inspection Failed” 8](#_Toc232862333)

[2.5.5 Change Supplier Master Data - Returns Supplier 8](#_Toc232862334)

[2.5.6 Create Purchasing Info Record 9](#_Toc232862335)

[2.5.7 Analyse Stock Overview (Optional) 11](#_Toc232862336)

[2.5.8 Transfer Stock (Optional) 12](#_Toc232862337)

[2.5.9 Analyse Stock Overview (Optional) 13](#_Toc232862338)

[3 Overview Table 15](#_Toc232862339)

[4 Test Procedures 17](#_Toc232862340)

[4.1 Part 1: Advanced Returns Management 17](#_Toc232862341)

[4.1.1 Create Returns Purchase Order 17](#_Toc232862342)

[4.1.2 Create Outbound Delivery 18](#_Toc232862343)

[4.1.3 Pick and Post Goods Issue 19](#_Toc232862344)

[4.1.4 Create Credit Memo 20](#_Toc232862345)

[4.1.5 Receive Replacement Material (Optional) 22](#_Toc232862346)

[4.1.6 Post Goods Receipt(Optional) 23](#_Toc232862347)

[4.1.7 Follow-Up Activities For Replacement Material(Optional) 24](#_Toc232862348)

[4.1.8 Check Invoice Document (Optional) 25](#_Toc232862349)

[4.2 Part 2: Basic Return to Supplier 26](#_Toc232862350)

[4.2.1 Create Returns Purchase Order 26](#_Toc232862351)

[4.2.2 Post Goods Issue to Supplier 27](#_Toc232862352)

[4.2.2.1 Goods Issue with Outbound Delivery 28](#_Toc232862353)

[4.2.2.1.1 Create Outbound Delivery 28](#_Toc232862354)

[4.2.2.1.2 Pick and Post Goods Issue 29](#_Toc232862355)

[4.2.3 Monitor Purchase Order Items (Optional) 30](#_Toc232862356)

[4.2.4 Create Credit Memo 31](#_Toc232862357)

[5 Appendix 33](#_Toc232862358)

[5.1 Process Integration 33](#_Toc232862359)

[5.1.1 Succeeding Processes 33](#_Toc232862360)

## Purpose

Overview

The return process begins with the creation of a return purchase order and is followed by the outbound delivery. Subsequently the items are picked and shipped to the supplier. Alternatively, you can also directly post a goods issue. The process is closed with the creation of a credit memo, which transfers the liability to the corresponding supplier.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company was created in your SAP S/4HANA Cloud Public Edition system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use the following master data in the process steps described in this document:

Master data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM12 | RAW12,PD,RepetitiveManuf. |  |
| Material | RM15 | RAW15,PD |  |
| Material | RM19 | RAW19,PD,Batch-Fifo,LeanQM |  |
| Material | RM128 | RAW128,PD,Consignment |  |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage location | 331A | Std. storage 1 |  |
| Storage location | Returns (331R) | Storage Location Returns |  |
| Purchasing org. | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 | Group 001 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Supplier | 33300006 | Domestic UAE Supplier 6 | Note If you want to send form print outs via e-mail instead of using the print functionality make sure that you have maintained a valid e-mail address in the vendor master data.This supplier 33300006 is returns supplier, and the Returns Supplier checkbox should be selected in the Purchasing view for this supplier. |
| Ship-to party | 33100006 | Domestic UAE Customer 6 | Note If you want to send form print-outs via e-mail instead of using the print functionality make sure that you have maintained a valid e-mail address in the customer master data. |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS– MDS |
| BNR | Create Product Master of type "Raw Material" - MDS– MDS |
| BNE | Create Supplier Master - MDS– MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | Material must be available in stock.For trading goods (HAWA) or Raw materials (ROH), perform one of the following activities:Execute the Procurement of Direct Materials(J45) test script |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| 1FM - Quality Management in Procurement | You have completed the step Regular Quality Inspection Process in the Quality Management in Procurement (1FM) test script. |

### Preliminary Steps

#### Return Reason “Wrong material delivered”

During the goods receipt process the warehouse clerk detects that wrong material was delivered. Therefore the material was posted into the blocked stock and moved into the storage location for returns (for example, 331R).

This situation can be the result of test script J45, step Post Goods Receipt for Purchase Order.

#### Return Reason “Delivered quantity too high”

During the goods receipt process the warehouse clerk detects that too much material was delivered. Therefore the additional material was posted into the blocked stock and moved into the storage location for returns (for example, 331R).

This situation can be the result of test script J45, step Post Goods Receipt for Purchase Order.

#### Return Reason “Wrong Trading Good in sales order”

A wrong material number of a trading good was posted into a sales order accidentally. The customer sends the goods back and reminds the delivery of the right ones. The wrong Trading goods must be sent back to the supplier.

This situation can be the result of test script J45, step Post Goods Receipt for Purchase Order.

#### Return Reason “Quality Inspection Failed”

During the goods receipt process, the quality inspection failed. Therefore, the material was posted into return stock with status blocked.

To get a demand for returns to a supplier you can refer to the step Regular Quality Inspection Process in the 1FM - Quality Management in Procurementtest script.

|  |
| --- |
| Note When you refer to the 1FM - Quality Management in Procurement to create the returns purchase order, the item needs to be flagged for returns and Stock Type needs to be Blocked stock on the Delivery tab. |

#### Change Supplier Master Data - Returns Supplier

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
| 1 | Log on | Log on to the SAP Fiori launchpad using the Master Data Specialist - Business Partner Data role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Choose Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Find: Business PartnerBy: Supplier NumberSupplier Number: for example, 33300006Choose Start. The supplier row displays.Double click the Supplier Partner row. | The Supplier Information screen displays. |  |
| 4 | Switch to Change Mode | Ensure you are in Change mode. Otherwise, select Switch Between Display and Change. | The Change Mode screen displays. |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value: Supplier (defined) |  |  |
| 6 | Open Purchasing Organization Data | Choose the Purchasing tab at the top of the screen. | The Purchasing Organization sub section screen displays. |  |
| 7 | Enter Purchasing Data | Choose Switch Organization.Make the following entry and choose Enter:Purch. Organization: <Purchasing Organization>, for example, 3310 |  |  |
| 8 | Select Returns Supplier Checkbox | From the Purchasing Data section, scroll down to the Additional Purchasing Data section, make the following entry:Returns supplier: <selected>Choose Okay (Enter) to confirm the popup screen Customer Default Data | The Returns supplier checkbox is selected. |  |
| 9 | Save Your Data | Choose Save. | The supplier change is saved. |  |

#### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create info records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). |  |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | Go to Header area, make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300006Material: TG12Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Go to Delivery and Quantity area, make the following entries:Delivery Time in Days: <Delivery Time>, for example, 1Under Delivery Tolerance in %: <Under Delivery Tolerance>, for example, 10Over Delivery Tolerance in %: <Over Delivery Tolerance>, for example, 10Tax Code: For example, <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: <Order Unit>, for example, PCStandard Order Quantity: <Standard Order Quantity>, for example, 1Select the following entries if required:Unlimited Delivery: <unselected>Goods-Receipt-Based Invoice Verification: <unselected>No Evaluated Receipt Settlement: < unselected>Order Acknowledgment Requirement: <unselected> | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | Go to the Condition area, choose Create. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>, for example, 15Pricing Unit: <Pricing Unit>, for example, 1Valid To: <Valid to Date>Currency: <Currency>, for example, AED.Choose Apply. | Condition Data is added. |  |
| 7 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

#### Analyse Stock Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check stock/requirements list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad using the Inventory Manager role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen is displayed. |  |
| 3 | Enter material | Make the following entries:Material:TG12Choose Enter. | Reviewing stock requirements helps to determine the timing/urgency and to decide if a normal process to replenish returned items is needed or if a purchase order must be created immediately. |  |

#### Transfer Stock (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to be used if business requirements exist to move inventory (physically and in the system) from a shop floor location or store location to the return goods shipping location. For example, if the storage location filled in the return purchase order is Storage_Location_Returns 331R , return goods must be transferred to the return goods storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad using the Warehouse Clerk role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061). | The stock list is displayed. |  |
| 3 | Input material | Make the following entries and choose Enter.Material: TG12Plant: 3310. |  |  |
| 4 | Choose the source stock | In the line of Std. storage 1 (331A) , choose the icon beside the quantity of Unrestricted-Use Stock. | The icon is highlight.For performing this you should use buttons with arrows near the unrestricted-use stock figures. |  |
| 5 | Choose the destination stock | In the line of Returns (331R), choose the icon beside the quantity of Unrestricted-Use Stock. | Transfer Stock screen is displayed. |  |
| 6 | Input the quantity for material | Input value in the dialog box:Quantity: XXX |  |  |
| 7 | Post | Choose Post. | The material document will be created and its number is displayed. |  |

#### Analyse Stock Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this step to see material in the storage locations of a plant.

Procedure - SAP Fiori

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Inventory Manager role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen is displayed. |  |
| 3 | Enter material | Make the following entry:Material: TG12Choose Enter. | The system displays material including in plant 3310. |  |

## Overview Table

The scope item return to supplier consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Part 1: Advanced Returns Management |  |  |  |
| [Create Returns Purchase Order](#unique_17) [page ] 17 | Purchaser | Create Purchase Order - Advanced (ME21N) | Enh.Ret.to Supplier PO is created. |
| [Create Outbound Delivery](#unique_18) [page ] 18 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | The outbound delivery is posted |
| [Pick and Post Goods Issue](#unique_19) [page ] 19 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Create Credit Memo](#unique_20) [page ] 20 | Accounts Payable Accountant | Create Supplier Invoice (F0859). | Credit memo is posted. |
| [Receive Replacement Material (Optional)](#unique_21) [page ] 22 | Receiving Specialist | Receive Replacement Materials - From Vendor (MSR_VRM_GR) | The replacement material PO is displayed. |
| [Post Goods Receipt(Optional)](#unique_22) [page ] 23 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt for inbound delivery is posted. |
| [Follow-Up Activities For Replacement Material(Optional)](#unique_23) [page ] 24 | Receiving Specialist | My Follow-Up Activities - For Replacement Materials (MSR_VRM_LFU) | The follow up activity for replacement material has been set up. |
| [Check Invoice Document (Optional)](#unique_24) [page ] 25 | Purchaser | Display Purchase Order - Advanced (ME23N) | The invoice document number is shown. |
| Part 2: Basic Return to Supplier |  |  |  |
| [Create Returns Purchase Order](#unique_25) [page ] 26 | Purchaser | Create Purchase Order - Advanced (ME21N) | Returns purchase order is created. |
| Post Goods Issue to Supplier |  |  |  |
| [Create Outbound Delivery](#unique_26) [page ] 28 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | The outbound delivery is created. |
| [Pick and Post Goods Issue](#unique_27) [page ] 29 | Shipping Specialist | Change Outbound Delivery (VL02N) | The outbound delivery is posted. |
| [Monitor Purchase Order Items (Optional)](#unique_28) [page ] 30 | Purchaser | Monitor Purchase Order Items (F2358) |  |
| [Create Credit Memo](#unique_29) [page ] 31 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Credit memo is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note This test script covers two parts. Part 1 is Advanced Returns Management which uses PO document type NB2. Here we offer only goods issue with return delivery.Part 2 is Basic Return to Supplier. |

### Part 1: Advanced Returns Management

#### Create Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how to create a returns purchase order for the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) |  |  |
| 3 | Enter Required Data for Returns Purchase Order | Enter the necessary data:Order type: Enh.Ret.to SupplierSupplier: 33300006Note This supplier 33300006 is a returns supplier. The Returns Supplier checkbox should be checked in the Purchasing view for this supplier.For business partner 33300006 with role supplier (defined), under tab Supplier: General Data, you must assign the following value in section General Data:Customer: 33100006In the Header section, on the Org. Data tab:Purch. Org.: 3310Purch. Group: 001Company Code: 3310In the Item Overview section:Material: TG12Plant: 3310Storage Location: 331RQuantity: 1 |  |  |
| 4 | Save Returns Purchase Order | Choose Save and when the returns purchase order number is displayed, write it down for further use. | Enh.Ret.to Supplier PO is created |  |

#### Create Outbound Delivery

Procedure

|  |
| --- |
| Note When you refer to the 1FM - Quality Management in Procurement to create the return purchase order, the item needs to be flagged for returns and stock type needs to be set to Blocked Stock on the Delivery tab. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the Shipping Specialist role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Purchase Orders, Fast Display screen is displayed. |  |
| 3 | Enter Data for Delivery Creation | In the header area:Shipping Point: 331RDelivery creation dates (From): <delivery creation From date> Delete the default dateDelivery creation dates (To) <delivery creation To date> Delete the default dateCalc Rule: <calculation rule>, for example, 2.Go to the Purchase Orders tab and make the following entries then choose Run(F8):Purchasing Document: Enter a returns purchase order that you created in step: [Create Returns Purchase Order](#unique_17) [page ] 17. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. PO due for delivery is listed. |  |
| 4 | Create Delivery | Select the line of purchase order from the list. Choose Background to create delivery in background. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. |  |
| 5 | Check Delivery Number | Choose Log for delivery creation, on Delivery Creation Log screen, choose Documents(F9), and note down the outbound delivery number shown in Document field. | An outbound delivery is created. |  |

#### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity picks, packs, and ships components to the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the Shipping Specialist role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen is displayed. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, make the following entry and choose Continue(Enter).Outbound Delivery: Enter an outbound delivery that you created in the last step. | The Returns (Pur. Ord.) XXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Enter Picking Data | On the RTS Outbound Dlv.XXXXXXXX: Overview screen, choose the Picking tab, make the following entries:Picked Qty: <picked quantity>Choose Save . | The system shows the message: Returns (Pur.Ord.) xxxxxxxx has been saved. Screen Change Outbound Delivery is displayed again. |  |
| 5 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. | Returns (Pur.Ord.) 8XXXXXXX has been saved. |  |

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If the credit memo is not created, and supplier will deliver the replacement material, then please skip this step and process steps from Receive Replacement Material (Optional) to Check invoice document(Optional). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries:Go to the General Information area:Transaction : Credit MemoCompany Code : 3310Invoice Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
| 4 | Enter Purchasing Document References | Go to the Purchasing Document References area:Reference Document Category :Purchase Order/Scheduling AgreementPurchase Order: <Returns purchase order you created>Choose Enter. |  |  |
| 5 | Check Invoice items | Go to Invoice Items/Standard area and check the Amount, Quantity and Tax Code.Tax code: <same with tax code in PO> |  |  |
| 6 | Enter Gross Invoice amount | Go to the General information area:Gross Invoice Amount: <Total amount in returns PO including tax> |  |  |
| 7 | Post Invoice | Choose Post.Note You can refer to the 2F9-Quality Management for Complaints Against Suppliers scope item. This scope item describes the management of complaints against suppliers, for example, after delivery of a product. | The system message is displayed. |  |

#### Receive Replacement Material (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If the credit memo is created, and supplier will not deliver the replacement material, then please skip the steps from Receive Replacement Material (Optional) to Check invoice document(Optional). The receive replacement material related steps are only optional and not the standard case. |

Purpose

In this activity, you receive the replacement materials from supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Receive Replacement Materials - From Vendor (MSR_VRM_GR). |  |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Returns Purchase Order Type: <NB2>Returns Purchase Order: <enter returns purchase order number> | The Vendor Replacement Material – Document Selection screen displays. |  |
| 4 | Select PO | Expand Supplier/Purchase Order/Item on the left screen, and double click the Item Number, then the data for purchase order on the right screen will show. | The Supplier/Purchase Order/Item has been expanded. The data for Return PO has been shown. |  |
| 5 | Go to Replacement | Go to the Replacement subarea and enter the Replacement Quantity: <1 PC>Note Replacement Quantity must be the same with Quantity for Returns Purchase Order. | The Replacement Quantity has been entered |  |
| 6 | Go to Goods Movement | Go to the Goods Movement subarea and enter in the Receiving Stor.Loc field with value 331A and select S (Block stock) for field Stock Type. | The Receiving Storage Location and Stock Type have been entered. |  |
| 7 | Save | Double click returns purchase order number, and choose Save.When the purchase order for replacement material is displayed, write it down for further use. | Message as follows will be displayed: Replacement purchase order 45XXXXXXXX has been created; see session log for details. |  |
| 8 | Check the Inbound Delivery of Replacement Material Number | On screen: Receive Replacement Materials from Supplier, double click the number of Returns Purchase Order, and choose Menu > Goto > Returns Overview (Shift+F12) , and note down the inbound delivery of replacement material in the Document Number column. | The Inbound Delivery of Replacement Material is automatically created. |  |

#### Post Goods Receipt(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you put away and post goods received for inbound delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Enter:Enter Inbound Delivery Number: XXX | The Change Inbound Delivery XXXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Putaway Qty | Enter Putaway Qty: X | The Putaway Qty has been entered. |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt. | The Goods Receipt is posted.A success message is shown. |  |

#### Follow-Up Activities For Replacement Material(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set follow-up activity for the replacement material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Follow-Up Activities - For Replacement Materials (MSR_VRM_LFU) | The Document Selection of Inbound Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Deliveries without confirmed logistical follow-up activity: SelectedShow all items of selected deliveries: SelectedDelivery: <enter Inbound Delivery number> | The inbound delivery is selected |  |
| 4 | Enter Follow-Up Activity | Go to the Logistical Follow-Up subarea, enter Follow-Up Activity: <0011 Transfer to Free Available Stock > |  |  |
| 5 | Save | Choose Save and Confirm.Choose Continue to confirm the Information screen | Message as follows will be displayed: Logistical follow-up activity has been saved. |  |

#### Check Invoice Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the document in invoice verification that the system has created automatically after the goods receipt for the replacement purchase order has been posted. This document represents a credit memo of value 0 for the returns purchase order and an invoice of value 0 for the replacement purchase order. The document is required to balance the GR/IR clearing account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. |  |  |
| 2 | Access the App | Search for web GUI Display Purchase Order - Advanced (ME23N). | The Display Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order Number | Choose Other Purchase Order and enter the returns purchase order number.Go to Returns tab on head level, and choose Return Overview. | The Returns Overview for Returns Purchase Order XXXXXXXXXX screen displays. |  |
| 4 | Check Invoice | In Document Number column, you can see the number of the document in invoice verification. | The system automatically creates a document in invoice verification that serves both as a credit memo and an invoice with value 0. |  |

### Part 2: Basic Return to Supplier

#### Create Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to create a returns purchase order for the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed. |  |
| 3 | Initial entry for return order | Make the following entries and choose Enter:Order type: Standard POSupplier : 33300006Note This supplier 33300006 is a returns supplier. The Returns Supplier checkbox should be checked in the Purchasing view for this supplier.For business partner 33300006 with role supplier (defined), under tab Supplier: General Data, you must assign the following value in section General Data:Customer: 33100006In the Org. Data tab of the Header section, make the following entries and choose Enter:Company Code: 3310Purch. Org.: 3310Purch. Group: 001In the Item Overview section, make following entries and choose Enter:Material : for example, TG12Quantity : X PCNet. Price :XAEDPlant: 3310Storage Location: 331RReturns Item: <Selected>In the Item Details section, go to Invoice tab and make the following entry and choose Enter:Tax Code: <Input Tax Code> | All data is entered, the Item Detail screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | Returns Purchase Order is created. |  |

#### Post Goods Issue to Supplier

In this activity, you post goods issue to supplier.

|  |
| --- |
| NoteWhen you refer to the 1FM - Quality Management in Procurement to create the return purchase order, the item needs to be flagged for returns and Stock Type needs to be Blocked stock on the Delivery tab. And you should process this step to execute the post goods issue to Supplier.In the step Post Goods Issue to Supplier, please confirm there is enough quantity in the return storage location. |

##### Goods Issue with Outbound Delivery

###### Create Outbound Delivery

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
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the Shipping Specialist role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Purchase Orders, Fast Display screen is displayed. |  |
| 3 | Enter data for PO display | In the header area:Shipping Point: 331RDelivery creation dates (From): <delivery creation From date> Delete the default dateDelivery creation dates (To) <delivery creation To date> Delete the default dateCalc Rule: <calculation rule>, for example, 2.Go to the Purchase Orders tab and make the following entries then choose Run (F8):Purchasing Document: Enter a returns purchase order that you created in step: [Create Returns Purchase Order](#unique_25) [page ] 26. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. PO due for delivery is listed. |  |
| 4 | Create delivery | Select the line of Purchase order from the list. Choose Background to Create Delivery in Background. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. |  |
| 5 | Check delivery number | Choose More > Show/Hide Delivery , and note down the outbound delivery number shown in the Document field. | An outbound delivery is created. |  |

###### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity picks, packs, and ships components to the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the Shipping Specialist role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery Screen is displayed. |  |
| 3 | Enter delivery number | On the Change Outbound Delivery screen, make the following entry and choose Enter.Outbound Delivery: Enter a Outbound delivery that created in step: [Create Outbound Delivery](#unique_26) [page ] 28. | The Returns (Pur. Ord.) XXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Enter picking data | On the Returns (Pur. Ord.) XXXXXXXX Change: Overview screen, choose the Picking tab, make the following entries:Picked Qty: <picked quantity>Choose Save . | The system shows the message: Returns (Pur.Ord.) xxxxxxxx has been saved. The Change Outbound Delivery screen is displayed again. |  |
| 5 | Post goods issue | On the Change Outbound Delivery screen, choose Post Goods Issue. | Returns (Pur.Ord.) 8XXXXXXX has been saved. |  |

#### Monitor Purchase Order Items (Optional)

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
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Monitor Purchase Order Items (F2358). | The Monitor Purchase Order Items screen is displayed. |  |
| 3 | Search for Returns Purchase Orders | All basic filters are available:Display CurrencyPurchase OrderSearch for the purchase order using the appropriate filters, and then choose Go . | The search results show the details with the respective filter criteria. |  |
| 4 | Display Returns Purchase Order | Select an individual line item of the Purchase Order to display the PO details. | The Purchase Order detail information is displayed. |  |
| 5 | Verify Data | Verify data displayed on the object page. |  |  |

#### Create Credit Memo

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
| 1 | Log onto Fiori Launchpad | Log on to the Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Tile | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries:Go to the General Information area:Transaction : Credit MemoCompany Code : 3310Invoice Date: <Today>Reference: <Fill the document number> |  |  |
| 4 | Enter Returns Purchasing Document Reference | Go to the Purchasing Document References area:Reference Document Category :Purchase Order/Scheduling AgreementPurchase Order: <Returns purchase order you created>Choose Enter. |  |  |
| 5 | Check Credit Memo Items | Go to Invoice Items/Standard area, and check the Amount, Quantity and Tax Code.Tax code: <same with tax code in PO> |  |  |
| 6 | Enter Gross Invoice Amount | Go to the General information area:Gross Invoice Amount: <Total amount in PO including Tax> |  |  |
| 7 | Post Credit Memo | Choose Post.Note You can refer to the 2F9-Quality Management for Complaints Against Suppliers scope item. This scope item describes the management of complaints against suppliers, for example, after delivery of a product. | The system message is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Real-Time Reporting and Monitoring for Procurement (1JI) | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reports.The Global Filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups and more.Via contextual navigation the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or get more detailed information in the corresponding KPI Drill-Downs. |
| Accounts Payable (J60) |  |

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
- see-also :: [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-core-inventory-management]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 50,395 chars in the whole document
