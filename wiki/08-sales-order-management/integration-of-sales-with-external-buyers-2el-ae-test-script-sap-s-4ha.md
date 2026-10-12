---
id: 08-sales-order-management/integration-of-sales-with-external-buyers-2el-ae-test-script-sap-s-4ha
title: "Integration of Sales with External Buyers (2EL_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2EL_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP scope item 2EL_AE: automated sales order, delivery, billing and returns exchange with external buyers via SOAP APIs."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/b2b-sales-integration]
aliases: [2EL_S4CLD2608_BPD_EN_AE]
keywords: [B2B Sales Integration with Buyers and SAP Business Network, sales order integration, b2b integration, sales order creation, customer expected price, order confirmation, outbound delivery, picking, post goods issue, advance shipping notice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EL_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-815
topic: 08-sales-order-management/b2b-sales-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Integration of Sales with External Buyers (2EL_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2EL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **B2B Sales Integration with Buyers and SAP Business Network** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Integration of Sales with External Buyers (2EL_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Integration of Sales with External Buyers (2EL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849287)

[2 Prerequisites 4](#_Toc232849288)

[2.1 Additional Manual Configuration 4](#_Toc232849289)

[2.2 System Access 4](#_Toc232849290)

[2.3 Roles 4](#_Toc232849291)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232849292)

[2.5 Business Conditions 6](#_Toc232849293)

[2.6 Preliminary Steps 6](#_Toc232849294)

[2.6.1 Set Initial Stock for Material 6](#_Toc232849295)

[3 Overview Table 8](#_Toc232849296)

[4 Test Procedures 10](#_Toc232849297)

[4.1 Create/Update/Cancel Sales Order from PO 10](#_Toc232849298)

[4.2 Send Order Confirmation 10](#_Toc232849299)

[4.3 Display Sales Orders (Optional) 11](#_Toc232849300)

[4.4 Manage Sales Documents with Customer Expected Price 12](#_Toc232849301)

[4.5 Send Order Confirmation Change 13](#_Toc232849302)

[4.6 Create Delivery 13](#_Toc232849303)

[4.7 Executive Picking 14](#_Toc232849304)

[4.8 Post Goods Issue 15](#_Toc232849305)

[4.9 Send Advance Shipping Notice 16](#_Toc232849306)

[4.10 Create Billing Document 17](#_Toc232849307)

[4.11 Send Invoice 18](#_Toc232849308)

[4.12 Display and Release Return Order (Optional) 18](#_Toc232849309)

[4.13 Send Return Order Confirmation (Optional) 19](#_Toc232849310)

[4.14 Create Refund Credit Request (Optional) 20](#_Toc232849311)

[4.15 Create Billing Document (Optional) 20](#_Toc232849312)

[4.16 Send Credit Memo (Optional) 21](#_Toc232849313)

[5 Appendix 22](#_Toc232849314)

[5.1 Process Integration 22](#_Toc232849315)

[5.1.1 Preceding Processes 22](#_Toc232849316)

[5.1.2 Succeeding Processes 22](#_Toc232849317)

## Purpose

Overview

For sales organizations whose buyers use traditional data exchange protocols such as electronic data interchange (EDI), or in Two-Tier scenarios, where subsidiaries are on SAP S/4HANA Cloud Public Edition, this scope item provides a set of robust application programming interfaces (APIs) to simplify and automate exchanging sales documents and their follow-on messages.

The following documents and functions are supported:

Sales Process:

- Create, change, or cancel sales order (inbound message)
- Send purchase order confirmation (outbound message)
- Send Advance Shipping Notification (ASN, outbound delivery message)
- Send supplier invoice (outbound message)

Return Process:

- Create return order (inbound message)
- Return order confirmation (outbound message)
- Send Credit Memo (outbound message)

The Simple Object Access Protocol (SOAP) messaging protocol is supported.

You can enable B2B integration with the corresponding Integration of Procurement with External Suppliers (2EJ) scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/8f987751339a4e08bb7f957011478eee)

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on the new global template will be used once they're available. In the table you still see the master data used for the current baseline.

Essential master data and organizational data were created in your S/4HANA system in the implementation phase. This includes data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, suppliers, and customers.

This master data usually consists of standardized SAP Best Practices default values and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values, which have the same characteristics.Check your SAP system to find out which other material master data is already available. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch | See the chapters [Business Conditions](#unique_7) [page ] 6 and [Preliminary Steps](#unique_8) [page ] 6. |
| Sold-to party | 33100080 | Customer domestic 80 | You can test the scope item using 33100080. |
| Ship-to party | 33100080 | Customer domestic 80 |  |
| Payer | 33100080 | Customer domestic 80 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You must have completed the step described in the test script for BNZ, Create New Open MM Posting Period. Additionally, ensure that the posting period is up-to-date. |
| 2EJ - Integration of Procurement with External Suppliers | You need a Buyer system to fetch the POs for sales order creation. You also need to check whether the whole process flow is working. |

### Preliminary Steps

#### Set Initial Stock for Material

To run through this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Warehouse Clerk role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access app | Open the Post Goods Movement app. | The Goods Receipt Other screen is displayed. | It will be displayed this way only if it was your last transaction. So the action for the user should be to select the Reference Document for MIGO TransactionOther field. |
| 3 | Enter the Movement Type | Select the following options and then choose Enter.Goods Receipt - Executable Action in Transaction MIGOOther - Reference Document for MIGO Transaction |  |  |
| 4 | Make entry in the Goods Receipt Other screen: Material tab | In the Goods Receipt Other screen: Material tab, make the following entry and choose Enter.Material : Material number |  |  |
| 5 | Make entry in the Goods Receipt Other screen: Quantity tab | In the Goods Receipt Other screen: Quantity tab, make the following entries and choose Enter.Qty in Unit of Entry: Quantity in UOMUnit of Entry: PC |  |  |
| 6 | Make entry in the Goods Receipt Other screen: Where tab | In the Goods Receipt Other screen: Where tab, make the following entries and choose Enter.Movement Type: 561- Receipt per initial entry of stock balances into unr.-usePlant: PlantStorage Location: Storage Location |  |  |
| 7 | Make entry in the Goods Receipt Other screen: Batch tab | In the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of manufacture: <Current date or a past date> |  | Only relevant for batch-relevant materials |
| 8 | Save your entries | Choose Post. |  |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report, or Item | App/Transaction | Business Role | Expected Results |
| --- | --- | --- | --- |
| [Create/Update/Cancel Sales Order from PO](#unique_11) [page ] 10 |  |  | Sales order is created automatically based on the PO received from the Buyer system. |
| [Send Order Confirmation](#unique_12) [page ] 10 |  |  | Order confirmation is created automatically based on the sales order. |
| [Display Sales Orders (Optional)](#unique_13) [page ] 11 | Display Sales Orders - VA03 (VA03) | Internal Sales Representative | PO is transferred to SAP S/4HANA system (supplier side) as sales order. |
| [Manage Sales Documents with Customer Expected Price](#unique_14) [page ] 12 | Manage Sales Orders (F1873) | Internal Sales Representative | Incomplete Sales Order due to customer expected price mismatch can be released manually by accepting, changing, or rejecting the sales order. |
| [Send Order Confirmation Change](#unique_15) [page ] 13 |  |  | An automatic confirmation is sent to the Buyer system. |
| [Create Delivery](#unique_16) [page ] 13 | Create Outbound Delivery - With Order Reference (VL01N) | Shipping Specialist | Outbound delivery is created. |
| [Executive Picking](#unique_17) [page ] 14 | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Shipping Specialist | The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. |
| [Post Goods Issue](#unique_18) [page ] 15 | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Shipping Specialist | An advanced shipping notification is sent to the Buyer system. |
| [Send Advance Shipping Notice](#unique_19) [page ] 16 |  |  | ASN is automatically sent to the Buyer system. |
| [Create Billing Document](#unique_20) [page ] 17 | Create Billing Documents (F0798) | Billing Clerk | Invoice is created and sent from the SAP S/4HANA system (supplier side) to the Buyer system. |
| [Send Invoice](#unique_21) [page ] 18 |  |  | Supplier Invoice is automatically sent to the Buyer system. |
| [Display and Release Return Order (Optional)](#unique_22) [page ] 18 | Display Sales Orders - VA03 (VA03) | Internal Sales Representative | Return Order is released. |
| [Send Return Order Confirmation (Optional)](#unique_23) [page ] 19 |  |  | Confirmation automatically sent to the Buyer system. |
| [Create Refund Credit Request (Optional)](#unique_24) [page ] 20 | Manage Customer Returns (F1708) | Returns and Refund Clerk | Credit Memo Request is created. |
| [Create Billing Document (Optional)](#unique_25) [page ] 20 | Create Billing Documents (F0798) | Billing Clerk | Credit Memo is created. |
| [Send Credit Memo (Optional)](#unique_26) [page ] 21 |  |  | Credit Memo is automatically sent to the Buyer system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create/Update/Cancel Sales Order from PO

Purpose

A Sales Order is automatically created from PO.

Prerequisites

PO must have been created and automatically sent to the SAP S/4HANA system (supplier side). For details, refer to the scope item 2EJ.

Procedure

This step is automatically generated.

### Send Order Confirmation

Purpose

An Order Confirmation is automatically sent to the Buyer system.

Prerequisites

Sales Order must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

### Display Sales Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you see newly created sales order in SAP S/4HANA supplier system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. |  |  |
| 2 | Open Display Sales Orders | Open the Display Sales Orders - VA03 (VA03) tile. |  |  |
| 3 | Enter search criteria | Enter PO number from the previous step in the Purchase Order No. field and choose Search. Then double-click the entry with purchase order number in the popup window. |  |  |
| 4 | Display sales order | Sales order should be displayed with correct data. Make a note of the sales order ID. | You can see all the sales order details. |  |
| 5 | Status Overview | On the Sales Order: Status Overview screen, choose Status Overview. In the Status Overview tree structure in the last line, check if the status is Complete Item Data. | Skip the test procedure [Manage Sales Documents with Customer Expected Price](#unique_14) [page ] 12. |  |
| 6 | Status Overview | In the Status Overview tree structure in the last line, check if the status is Incomplete Item Data. | Proceed with the test procedure [Manage Sales Documents with Customer Expected Price](#unique_14) [page ] 12. |  |

### Manage Sales Documents with Customer Expected Price

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the incomplete sales order in SAP S/4HANA Supplier system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access App | Open the Manage Sales Docs with Customer-Expected Price (F2713) app. |  |  |
| 3 | Enter Search Criteria | To search for the sales order that you've created, enter the following search criteria:ExampleSales Organization: 3310Sold-to-Party: 33100080Choose Go. Select the entry with the previously created sales order number. | List of Standard Order Order number appears. |  |
| 4 | Define Action | To change the price in the sales order, proceed with test steps 5 to 7.To discard the customer price, proceed with test step 8.To reject the item, proceed with test step 9. |  |  |
| 5 | Change Price in Sales Order | Make a note of the customer expected price. Then choose the arrow on the right side. |  |  |
| 6 | Change Sales Order | Choose Change. In the Sales tab, go to All Items and change the amount to customer expected price that you had noted down in the previous step. |  |  |
| 7 | Save Sales Order | Choose Save. The order confirmation change is sent. Proceed with [Create Delivery](#unique_16) [page ] 13. | Standard Order Sales Order number is saved. |  |
| 8 | Discard Customer Price | Select the sales order and choose Discard Customer Price. Proceed with [Create Delivery](#unique_16) [page ] 13.Note If the price difference exceeds the price tolerance limit, the purchase order confirmation will not be processed. | You get the messageItem Successfully Discarded. |  |
| 9 | Reject Item | Select the sales order and choose Reject Item. In the Reject Item dialog box that appears, select the reason for rejection from the dropdown list. Choose OK. Since the sales order is rejected, the process testing ends here. | You get the messageData has been saved. |  |

### Send Order Confirmation Change

Purpose

An Order Confirmation Change is automatically sent to the Buyer system.

Prerequisites

Sales Order must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The supplier logs on to the SAP S/4HANA system to create an outbound delivery for the previously received sales order (purchase order).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Shipping Specialist. |  |  |
| 2 | Access App | Open Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery - From Sales Orders screen is displayed. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Selection Date: < Sales order creation date + 2 months>Order: < Sales order number created previously>Choose Continue. |  |  |
| 4 | Create Delivery | Choose Save. | Creation of a delivery is triggered. |  |

### Executive Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area, where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Shipping Specialist. |  |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose For Picking | Choose the For Picking button. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute.Shipping point: 3310Select the Only Picking without WM option.Picking Date : <Current Date + 1>Choose Execute. |  |  |
| 5 | Change Outbound Delivery | From Day’s Workload for Picking, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Check Whether Batch Split Exists | Go to the Picking tab and check if batch split exists in the Batch Split Indicator column:If it is Yes, proceed with the first option in the test step 7.If it is No, proceed with the second option in the test step 7. |  |  |
| 7 | Enter Picked Quantity | Choose Batch Split Exists to expand sub items and enter a quantity equal to the delivery quantity in the Picked Qty field for subitem.Enter a quantity equal to the delivery quantity in the Picked Qty field for picking related items. |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery is picked now. |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt in the SAP S/4HANA Buyer system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Shipping Specialist. |  |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and then choose Execute:Shipping point: 3310 |  |  |
| 4 | Post Goods Issue | Mark the relevant delivery and choose Post Goods Issue. Select the current date from the dialog box. | The goods issue is posted. |  |

### Send Advance Shipping Notice

Purpose

ASN is automatically sent to the Buyer system.

Prerequisites

Goods issued must have been posted in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a supplier creates an invoice in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). |  |  |
| 3 | Define Billing Setting | Choose Billing Settings on the bottom right of the screen.There are four settings, and you must switch all of them to ON.Set billing date and type before billingCreate separate billing date for each item of billing due listAutomatically post Billing DocumentsDisplay billing documents after creation. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if required. | Sales documents are displayed in the results. |  |
| 5 | Choose Individual Billing Document | Select a row of sales document created previously and choose Create. | The Create Billing Documents screen is displayed. |  |
| 6 | Maintain Billing Date | Choose the billing type F2 Invoice (F2) and maintain billing date, for example, the current date. Choose OK and then Save. | New billing document is created. |  |
| 7 | Display Billing Document After Creation | The billing document appears automatically. | The system generates an invoice for billing. |  |

### Send Invoice

Purpose

Invoice is sent to the Buyer system.

Prerequisites

The Billing Document must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

### Display and Release Return Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you see the return order in SAP S/4HANA supplier system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. |  |  |
| 2 | Open Display Sales Order | Open the Display Sales Orders - VA03 (VA03) tile. | The Display Sales Document screen is displayed. |  |
| 3 | Enter Search Criteria | Enter Return PO number in the Purchase Order No. field and choose Search. Then double-click the entry with return PO number in the dialog box. |  |  |
| 4 | Display Accelerated Return Order | Accelerated Return Order should be displayed with correct data. Make a note of the Accelerated Return ID. | You can see all the return order details. |  |
| 5 | Change Mode | Switch to Change Mode. |  |  |
| 6 | Release the Return Order | Choose the Returns tab. Change the Approval status from Item to Be Revised to Blank and save the document. | The confirmation message is sent to the buyer system.The advanced returns delivery is also automatically created in the background. |  |

### Send Return Order Confirmation (Optional)

Purpose

An Order Confirmation is automatically sent to the Buyer system.

Prerequisites

Return Order must have been released in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

### Create Refund Credit Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the refund request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Returns and Refund Clerk. |  |  |
| 2 | Access Manage Customer Returns | Open Manage Customer Returns (F1708) and on the next screen choose Go. | A list of all the returns documents is displayed. |  |
| 3 | Determine Refund | Select the correct Accelerated Return from the list and choose the Determine Refund button. |  |  |
| 4 | Release | Select the item by marking the checkbox and choose the Release Selected Items. | A message is displayed indicating that refund request has been created. |  |
| 5 | Log Out | Log out once and then log in as Internal Sales Representative. |  |  |
| 6 | Display Document Flow | In Display Sales Order, enter the return sales document ID and choose Continue. On the next screen, choose Display Document Flow, and note the credit memo request ID. |  |  |

### Create Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the billing document based on the credit memo request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. |  |  |
| 2 | Access Create Billing Document (VF01) | Open Create Billing Documents (F0798). |  |  |
| 3 | Create Credit Memo | Enter the Credit Memo Request ID from the previous step in Document to Be Processed and choose Enter.Choose Save. | The Credit Memo saved is displayed. |  |

### Send Credit Memo (Optional)

Purpose

Credit Memo is sent to the Buyer system.

Prerequisites

Billing Document must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You must have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| ScopeItem_Name (2EJ) | ScopeItem_BusinessCondition |
| ScopeItem_Name (ScopeItem_Id) | ScopeItem_BusinessCondition |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| ScopeItem_Name (J59) | ScopeItem_BusinessCondition |
| ScopeItem_Name (ScopeItem_Id) | ScopeItem_BusinessCondition |

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
> Flagged while digesting this document, not verified: The Overview Table names the app for Manage Sales Documents with Customer Expected Price as 'Manage Sales Orders (F1873)', while the test procedure opens 'Manage Sales Docs with Customer-Expected Price (F2713)'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Post Goods Issue purpose says 'post the goods receipt in the SAP S/4HANA Buyer system', but the steps are performed by the Shipping Specialist in VL06O_CLOUD on the supplier side and post a goods issue.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 33,645 chars in the whole document
