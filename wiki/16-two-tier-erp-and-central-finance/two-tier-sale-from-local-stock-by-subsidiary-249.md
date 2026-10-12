---
id: 16-two-tier-erp-and-central-finance/two-tier-sale-from-local-stock-by-subsidiary-249
title: "Two-Tier: Sale from Local Stock by Subsidiary (S4CLD2608_2T_Sale_from_Local_Stock)"
description: "SAP Cloud ERP Two-Tier customer guide: subsidiary sells from local stock with HQ visibility on quotes, orders, stock, receivables; APIs, CDS views, test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/sell-from-local-stock]
aliases: [S4CLD2608_2T_Sale_from_Local_Stock]
keywords: [Subsidiary Sales from Local Stock and Returns, two-tier erp, sale from local stock, headquarter visibility, integration apis, analytical cds views, sales order creation, outbound delivery, picking, post goods issue]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Sale_from_Local_Stock.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-249
topic: 16-two-tier-erp-and-central-finance/sell-from-local-stock
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier: Sale from Local Stock by Subsidiary (S4CLD2608_2T_Sale_from_Local_Stock)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Sale_from_Local_Stock.docx`, extracted with `mammoth`. Grouped under **Subsidiary Sales from Local Stock and Returns** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERPJune 2026English |  |
|  | Two-Tier: Sale from Local Stock by Subsidiary |
|  | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 01.09.2017 | Initial version of document |
| 1 | 20.07.2020 | Review of Document |
| 2 | 31.03.2021 | Review of Document |

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Content

[1 Purpose 7](#_Toc40968902)

[2 Value Proposition 7](#_Toc40968903)

[2.1 Business Requirements 7](#_Toc40968904)

[2.2 Two-Tier Solution 7](#_Toc40968905)

[3 Business Process Details 7](#_Toc40968906)

[3.1 Prerequisites 8](#_Toc40968907)

[3.2 Process Flow with Technical Details 8](#_Toc40968908)

[4 Technical Requirement 9](#_Toc40968909)

[4.1 Integration Requirements by using API 9](#_Toc40968910)

[4.2 Integration Requirements by using EDI/IDOC 9](#_Toc40968911)

[4.3 Reporting Requirements by using Analytical CDS Views 9](#_Toc40968912)

[4.4 Reporting Requirements by using Analytical API 9](#_Toc40968913)

[5 Test Script 9](#_Toc40968914)

[5.1 Prerequisites 9](#_Toc40968915)

[5.1.1 System Access 9](#_Toc40968916)

[5.1.2 Roles 10](#_Toc40968917)

[5.1.3 Master Data, Organizational Data, and Other Data 10](#_Toc40968918)

[5.1.4 Business Conditions 12](#_Toc40968919)

[5.1.5 Preliminary Steps 12](#_Toc40968920)

[5.2 Overview Table 16](#_Toc40968921)

[5.3 Test Procedures 17](#_Toc40968922)

[5.3.1 Basic Credit Management (BD6) – Set Credit Limit (Optional) 18](#_Toc40968923)

[5.3.2 Sales Quotation (BDG) (Optional) 18](#_Toc40968924)

[5.3.3 Quotation Visbility at Headquarter 18](#_Toc40968925)

[5.3.4 Create Sales Order 19](#_Toc40968926)

[5.3.5 Advanced Available-to-Promise Processing (1JW) (Optional) 22](#_Toc40968927)

[5.3.6 Create Attachment for Sales Order (Optional) 23](#_Toc40968928)

[5.3.7 Sales Order Visbility at Headquarter 24](#_Toc40968929)

[5.3.8 Basic Credit Management (BD6) – Review Blocked Sales Orders (Optional) 24](#_Toc40968930)

[5.3.9 Create Delivery 24](#_Toc40968931)

[5.3.10 Create Attachment for Delivery (Optional) 26](#_Toc40968932)

[5.3.11 Execute Picking 27](#_Toc40968933)

[5.3.12 Check Batches (Optional) 29](#_Toc40968934)

[5.3.13 Split Outbound Delivery (optional) 30](#_Toc40968935)

[5.3.14 Add Freight Costs (Optional) 31](#_Toc40968936)

[5.3.15 Post Goods Issue 32](#_Toc40968937)

[5.3.16 Stock Visbility at Headquarter 34](#_Toc40968938)

[5.3.17 Proof of Delivery(Optional) 34](#_Toc40968939)

[5.3.18 Create Billing Document 36](#_Toc40968940)

[5.3.19 Create Attachment for Billing (Optional) 38](#_Toc40968941)

[5.3.20 Payment Information at Headquarter 39](#_Toc40968942)

[6 Appendix 40](#_Toc40968943)

[6.1 Relevant Scope ID’s 40](#_Toc40968944)

**Two-Tier- Sale from Local Stock by Subsidiary**

## Purpose

This document will provide the detailed process on Two-Tier approach for subcontracting process where “Sale from Local Stock by Subsidiary” with process flow, technical requirements and followed with testing procedure.

## Value Proposition

### Business Requirements

Subsidiary carries out sales process independently with Headquarter requiring visibility on certain key performance indicators like Open Sales Orders, Payment Receivables and etc.

### Two-Tier Solution

With Two-Tier approach SAP Cloud ERP solution will be deployed on Subsidiary and integrates with Headquarters which runs on SAP S/4HANA On-Premise / SAP Cloud ERP Private /SAP ERP solution.

The following business benefits will be achieved in real time with Two-Tier approach.

1. Headquarter has visibility over Quotations/Leads at the Subsidiary
2. Headquarter has visibility on the Open Sales Orders at the Subsidiary
3. Headquarter has visibility on the Stock Levels at the Subsidiary
4. Headquarter has visibility on the Payment Receivables at the Subsidiary

## Business Process Details

The Two-Tier approach for Sales from Local Stock by Subsidiary with visbility to Headquarter is depicted in this document.

The process starts with the creation of a customer and standard sales order. Depending on the customer and the material, various special events take place during order entry, such as customer or material pricing.

If enough material exists in the required storage location, the process proceeds normally. If not, a stock movement takes place. Picking slips are generated to stage the product for shipment to the customer. Once picked, the physically shipped quantity must be registered in the system to ensure that there are no differences between the sales order and the delivery document.

After the completion of picking, the shipping specialist relieves the inventory. This inventory relief is the actual recording of the physical quantity that is being shipped to the customer. The cost of goods sold is recorded in financial accounting.

Once the inventory is relieved, the delivery can be invoiced. The revenue and the cost of goods sold is recorded in management accounting.

Headquarter will get information about the Quotations, Sales Orders, Stock Overview and Receivables at the Subsidiary.

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Connection/Integration between Headquarters’ On-Premise /SAP Cloud ERP Private and Subsidiary’s SAP Cloud ERP system
- Activate the Scope ID BD9, BDG and BD6 at the Subsidiary’s SAP Cloud ERP system
- Create the required Apps/Reports for extracting information at the Headquarters’ On-Premise ERP /SAP Cloud ERP Private or SAP S/4 Hana cloud for the access of Headquarters’ representative using the required APIs/CDS views

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

The following integration points are depicted in the process flow diagram:

1. Headquarters’ visibility over Quotations/Leads at the Subsidiary
2. Headquarters’ visibility on the Open Sales Orders at the Subsidiary
3. Headquarters’ visibility on the Stock Levels at the Subsidiary
4. Headquarters’ visibility on the Payment Receivables at the Subsidiary

## Technical Requirement

### Integration Requirements by using API

The following APIs are suggested for running the end-to-end process:

- API_SALES_INQUIRY_SRV –Read Sales Inquiry from SAP Cloud ERP
- API_SALES_QUOTATION_SRV- Read Sales Quotation from SAP S/4HANA Cloud
- API_SLSPRICINGCONDITIONRECORD_SRV enables to create and update Pricing Condition Records
- API_SALES_ORDER_SRV- Read Sales Order from SAP S/4HANA Cloud.
- API_OUTBOUND_DELIVERY_SRV Read Delivery from SAP S/4HANA Cloud
- READJOURNALENTRY- Read Account Receivables from SAP S/4HANA Cloud.

### Integration Requirements by using EDI/IDOC

None.

### Reporting Requirements by using Analytical CDS Views

The following CDS views can be used to extract information about Stock situation from the Subsidiary’s SAP Cloud ERP Editionto the Headquarter:

| CDS View Name | Description |
| --- | --- |
| I_MaterialStock | Material Stock calculation |
| C_MaterialStockActual | Total actual stock quantity |
| C_MaterialStockByKeyDate | Material Stock at posting date |
| I_MaterialStockTimeSeries | Material stock for periods |
| C_MaterialStockTimeSeries | Material stock for periods by type |
| I_ShpdAsPlndDelivItemsCube | Delivery Items Shipped as Planned |
| C_ShpdAsPlndDelivItemsQry) | Delivery Items Shipped as Planned |
| I_InventoryStockTypeT | Inventory Stock Type Text |
| I_InventorySpecialStockType | Inventory Special Stock Type |

### Reporting Requirements by using Analytical API

None.

## Test Script

### Prerequisites

#### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Roles

Assign the following business roles to your individual test users.

The following roles are provided as example roles from SAP. You can use these as templates for your own roles. The roels stated below are specific to the Subsidiary which runs on SAP S/4HANA Cloud. Appropriate roles required to be assigned to the users at Headquarter which runs on On-Premise / SAP Cloud ERP Private system to get the visibility of the related process.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER |  |
| Customer Master Specialist | SAP_BR_BUPA_MASTER_SPECIALIST |  |

#### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

Additional Master Data (Default Values)

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch | See sections Business Conditions and Preliminary Steps.TG11 is test for customer material record with customer 17100009. |
| Material | TG12 | Trading Good for Reg. Trading (reorder point planning)No serial number, no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Sold-to party | 17100003 17100005 17100008 17100009 | Customer domestic 03 Customer domestic 05 | You can test the scope item using another domestic customer.17100005 is for credit management.17100008 is for material listing or exclusion17100009 is for customer material record and POD (Proof-of-Delivery) |
| Ship-to party | 17100003 17100005 17100008 17100009 | Customer domestic 03 Customer domestic 05 |  |
| Payer | 17100003 17100005 17100008 17100009 | Customer domestic 03 Customer domestic 05 |  |
| Plant | 1710 |  |  |
| Storage Location | 171A |  |  |
| Shipping Point | 1710 |  |  |
| Sales organization | 1710 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following Master Data Scripts (MDS): [https://support.sap.com/content/dam/SAAP/Sol_Pack/BP_CLD_ENTPR/BP_CLD_ENTPR_S4CLD2002_19_Master_Data_EN_XX.htm](https://support.sap.com/content/dam/SAAP/Sol_Pack/BP_CLD_ENTPR/BP_CLD_ENTPR_S4CLD2002_19_Master_Data_EN_XX.htm)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |
| BND | Create Customer Master |
| BET | Create Sales Pricing Condition |

#### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials(J45) processOr create stock using FLP tile Post Goods Movement (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period | You have completed the step described in the Create New Open MM Posting Period(BNZ) master data script. Posting Period is up to date. |

#### Preliminary Steps

##### Set Initial Stock for Material

Purpose

To run through this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement | The Goods Receipt Other screen displays. | It only displays it that way if it was your last transaction. So the action for the User should be to select field Reference Document for MIGO TransactionOther |
| 3 | Input Movement Type | Make the following entry and choose EnterExecutable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Input on the Goods Receipt Other screen: Material tab | On the Goods Receipt Other screen: Material tab, make the following entry and choose Enter:Material : Material number |  |  |
| 5 | Input on the Goods Receipt Other screen: Quantity tab | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: Qty in UOMUnit of Entry: PC |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 - Receipt per initial entry of stock balances into unr.-usePlant: Plant -1710Storage Location: storage location -171A |  |  |
| 7 | Input on the Goods Receipt Other screen: Batch tab | On the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of manufacture: Enter the current date or a date in the past |  | Only relevant for material TG22. |
| 8 | Save your entries. | Click Post. |  |  |

Financial postings:

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

##### Set Relevant for Proof of Delivery in BP Master Data

Purpose

In order to run step Proof of Delivery (optional), customer master data have to maintain POD relevant indicator. From demo data, only customer 17100009 has been set, following procedure can help user to set POD relevant for other customer master data if necessary.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto the SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the Role Customer Master Specialist. |  |  |
| 2. | Access the App | Open Maintain Business Partner. |  |  |
| 3. | Enter Business Partner | On the entry screen of the Maintain Business Partner app, make the following entry and choose Enter.Business Partner: Customer ID |  |  |
| 4. | Switch to change mode | On screen Display Organization : XXXXXXXX, choose button Switch Between Display and Change. |  |  |
| 5. | Goto Sales Area – Shipping Tab | On screen Change Organization : XXXXXXXX, choose Customer (defined) in field Change in BP role. Click button Sales and Distribution in the menu, Then click tab Shipping. |  |  |
| 6. | Set POD- Relevant | Select the checkbox of POD - Relevant. |  |  |
| 7. | Save | Choose Save. |  |  |

##### Create Template Item Proposal (Optional)

Purpose

This process guides you create template item proposal if you want to use the optional step Copy item proposal to sales order later on in the process step Sales order entry

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the role Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Create Item Proposal. | The Create Item Proposal screen displays. |  |
| 3. | Enter the Item Proposal Type PV | On the Create Item Proposal Screen, make the following entries:Order Type: PVSales Organization: 1710Distribution Channel: 10Division: 00 |  |  |
| 4. | Enter Item Proposal Details | On the Create Item Proposal: Overview screen, make the following entries:Description: e.g. Item Proposal TemplateValid-From Date: e.g. current dateValid-To Date: e.g. current date + 1 yearMaterial Number: Material numberQuantity: Quantity |  |  |
| 5. | Save | Choose Save. |  |  |

### Overview Table

This scope item consists of several process steps that are listed in the following table:

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Basic Credit Management (BD6) – Set Credit Limit (Optional)](#unique_11) [page ] 18 | CREDIT_CONTROLLER | See scope item no. BD6 | Credit Limit for Customer 17100005 has been set. |
| [Sales Quotation (BDG) (Optional)](#unique_12) [page ] 18 | Internal Sales Representative | See scope item no. BDG |  |
| [Quotation](#_Quotation_Visbility_at) visbility at HQ [page] 18 | Sales Manager |  | Get information related to quotations at the subsidiary |
| [Create Sales Order](#unique_13) [page ] 19 | Internal Sales Representative | Manage Sales Orders | The Manage Sales Orders screen displays. |
| [Create Attachment for Sales Order (Optional)](#unique_14) [page ] 23 | Internal Sales Representative | Manage Sales Orders | The Display Sales Order: Initial Screen displays |
| Sales Order [visbility](#_Sales_Order_Visbility) at HQ [page] 24 | Sales Manager |  | Get information related to Sales Order at the subsidiary |
| [Basic Credit Management (BD6) – Review Blocked Sales Orders (Optional)](#unique_15) [page ] 24 | Credit Controller | See scope item no. BD6 |  |
| [Create Delivery](#unique_16) [page ] 24 | Shipping Specialist | Create Outbound Deliveries | The Create Outbound Deliveries screen displays. |
| [Create Attachment for Delivery (Optional)](#unique_17) [page ] 26 | Shipping Specialist | Display Outbound Delivery | The Display Outbound Delivery: Initial Screen displays |
| [Execute Picking](#unique_18) [page ] 27 | Shipping Specialist | My Outbound Delivery Monitor |  |
| [Check Batches (Optional)](#unique_19) [page ] 28 | Shipping Specialist | Change Outbound Delivery | Batch numbers are checked |
| [Split Outbound Delivery (optional)](#unique_20) [page ] 30 | Shipping Specialist | Split Outbound Delivery |  |
| [Add Freight Costs (Optional)](#unique_21) [page ] 31 | Shipping Specialist | Change Outbound Delivery |  |
| [Post Goods Issue](#unique_22) [page ] 32 | Shipping Specialist | My Outbound Delivery Monitor | The goods issue is posted. |
| Stock [visbility](#_Stock_Visbility_at) at HQ [page] 34 | Inventory Analyst |  | Get information of the stock at the subsidiary |
| [Proof of Delivery(Optional)](#unique_23) [page ] 34 | Shipping Specialist | Maintain Business Partner |  |
| [Create Billing Document](#unique_24) [page ] 36 | Billing Clerk | Create Billing Documents | The Create Billing Document screen displays. |
| [Create Attachment for Billing (Optional)](#unique_25) [page ] 38 | Billing Clerk | Display Billing Document | The Display Billing Document screen displays. |
| Payment [Information](#_Payment_Information_at) at HQ [page] 39 |  |  | View of the Account Receivables at the Subsidiary |

### Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, You can search for objects such as: Apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet:

1. Log onto the SAP Fiori Launchpad using the respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
3. The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, for example, Sales orders from drop-down menu in 1st field, enter sales order number in 2nd field and choose Search, The sales order is listed.
4. Choose the sales order number link: the system navigates to the factsheet screen and sales order related information is integrated and summarized in one Fiori page, You can get detailed data via choosing the corresponding links.

There are factsheets available for the following objects: (Visible depending on the assigned role)

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

#### Basic Credit Management (BD6) – Set Credit Limit (Optional)

Note Basic Credit Management (BD6)

Purpose

In this process a credit limit is set for the used customer.

Procedure

Complete all the activities described in the test script of the scope item: Basic Credit Management (BD6).

Note The credit limit currency in all company codes is set to use the group currency which is defined when the solution is activated.

#### Sales Quotation (BDG) (Optional)

Sales Quotation (BDG)

Purpose

This scope item describes the process for a standard sales quotation.

Procedure

Complete all the activities described in the Test script of the scope item: Sales Quotation (BDG).

If you want to use the optional link between scope item Sales Quotation (BDG) and Sell from Stock (BD9) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order).

#### Quotation Visbility at Headquarter

Purpose

In this activity you can view the Quotations at the Subsidiary from the Headquarter. The Headquarter can get information like Quotation Creation date, status and etc.

Procedure

Headquarter can develop their own application by using whitelisted API’s and / or available CDS views at SAP Cloud ERP which will expose the required information from Subsidiary.

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Internal Sales Representative | The SAP Fiori launchpad displays. |  |
| 2 | Access the Sales order worklist | Open Manage Sales Orders. | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, select the Create Sales Order button. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order Screen, make the following entries and choose Enter:Order Type: ORSales Organization: 1710Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | If you would like to use listing & exclusion, continue with test step Enter listed/ excluded Material Numbers.If you would like to use customer material record information, continue with test step Enter Customer Material Number.On the Create Standard Order: Overview screen, make the following entries:Sold To party: 17100003Ship To party: 17100003Customer references: <PO number>Order reason: <Order Reason>Material Number: <Material number>Quantity: <Quantity>If you would like to use item proposal, continue with test step “Copy item proposal to sales order”. |  | PO number: Enter a customer purchase order number as referenceOrder reason: for example, Excellent priceQuantity: for example, 1 PC |
| 6 | Copy item proposal to sales order | On the Create Standard Order: Overview screen, choose button Propose Items.In the pop-up window Propose Items, select item proposal created in preliminary step in Sales Document.Then choose Default with quantity. | Material and quantity recorded in item proposal is copied to sales order item. |  |
| 7 | Enter listed/excluded Material Numbers (optional) | On the Create Standard Order: Overview screen, make the following entries:Sold To party: 17100008Ship To party: 17100008PO number: PO number Enter a customer purchase order number as referenceEnter the following Material Numbers TG11, TG12 and TG20Quantity: Quantity For example 1 PC | Material TG11 is listed and can be entered without error messageMaterial TG12 is excluded; message "Material TG12 has been excluded" appearsMaterial TG20 is not listed; message Material TG20 is not listed and therefore not allowed" is processed. |  |
| 8 | Remove not listed materials (optional) | If you have selected the customer for listing/exclusion, remove Materials TG12 and TG20 if a dialog box appears. | Sales Order only can be saved if materials TG12 and TG20 have been removed. |  |
| 9 | Enter Customer Material Number (optional) | On the Create Standard Order: Overview screen, make the following entries:Sold To party: 17100009Ship To party: 17100009PO number: PO numberEnter a customer purchase order number as referenceCustomer Material Number: Description from customer material info record, such as CUS_US_TG11Quantity: QuantityFor example 1 PC | Material TG11 is automatically determined from customer material info record and copied into the sales order.You can open Manage Customer Manterial to edit or display the customer material information. |  |
| 10 | Save Document | Choose Save Make a note of the sales order number: __________.If you have installed the scope item Free Goods Processing in your system and you use material TG11 and customer 17100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter.Note If you are using TG12 in testing, the following warning may appear: Reorder point for item 000010 has been exceeded: 10 PC. To skip this warning, choose Enter. | The order is saved and the order confirmation is printed out. |  |

The system triggers an availability check. If aATP is switched on, first a PAL- Product Allocation Check can be carried out if allocations are set up (done from 1JW). In any case a PAC Product Allocation Check is carried out.

Based on the results of the checks, if requested availability cannot be fulfilled, the delivery proposal screen during sales order processing shows up and the user needs to take a decision based on the result of the checks.

Printing form– Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2. | Access the Sales order Worklist | Open Manage Sales Orders. | The Manage Sales Orders screen displays. |  |
| 3. | Search For Sales Order | Enter search term(s) in filter bar and choose GoFor example, enter sales order number in field Sales Order. | Sales order is displayed in result list. |  |
| 4. | Navigate to Sales Order Screen | Click sales order number and choose Display Sales order.Note if there is no Display Sales Order, please click Define Links, and select DIsplay Sales Order and choose OK. | The Display Sales Order xxx: Overview screen displays. |  |
| 5. | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose More > Extras > Output > Header > Edit . | The document prints. |  |
| 6. | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display PDF Document. | Choose your local destination and press Print. |  |

It can also be navigated to a fact sheet screen in app Manage Sales Orders:

1. On Manage Sales Orders screen, enter search terms in filter bar and choose Go.
2. In search result, click your sales order number and choose sales order number.

#### Advanced Available-to-Promise Processing (1JW) (Optional)

Note Advanced Available-to-Promise Processing(1JW)

Purpose

This scope item describes the optional process for Advanced Available-to-Promise Processing

.

1. From 1JW, the user can Trigger /Schedule BOP, execute a BOP Run and Monitor BOP Run.
2. From 1JW, the user can execute Release for Delivery.

Procedure

Complete all the activities described in the test script of the scope item:Advanced Available-to-Promise Processing (1JW).

#### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the role Internal sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Sales Order. | The Display Sales Document view displays. |  |
| 3 | Enter sales Order number | Enter the respective order number created in previous step and choose Enter. | The Display Standard Order XXX: Overview view displays. |  |
| 4 | Create Attachment for sales Order | Choose Services for Object on top right corner of view. Choose Create Attachment. | Import file view displays. |  |
| 5 | Import File | Click button Import from native file system.In the Open view, choose local path and file, and choose Open.Select OK.Navigate Back to Import file view, select file item, and select Choose. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of view, and choose Attachment list. | Attachment brings up in Service: Attachment list view. |  |

#### Sales Order Visbility at Headquarter

Purpose

In this activity you can view the Sales Orders at the Subsidiary from the Headquarter. The Headquarter can get information like Sales Order Creation date, Price and etc.

Procedure

Headquarter can develop their own application by using whitelisted API’s and / or available CDS views at SAP Cloud ERP which will expose the required information from Subsidiary.

#### Basic Credit Management (BD6) – Review Blocked Sales Orders (Optional)

Basic Credit Management (BD6)

Purpose

In this process you review the sales orders that might have been blocked due to the credit limit check.

Procedure

Complete all the activities described in the Test script of the scope item: Basic Credit Management (BD6).

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Shipping Specialist. |  |  |
| 2. | Access the App | Open Create Outbound Deliveries- | The Create Outbound Deliveries screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: 1710Planned Creation Date: <Delivery selection date>SD Document: Sales order number created previously |  |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5. | Check Details | Choose Display Log | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

Note Depending on the scope item-settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management.

To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.

You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).

You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.

You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation rejected with an error message.

Note With the Analyze Outbound Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document.

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery | The Change Outbound Delivery screen displays |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the Delivery number nad click Continue. From the Delivery xxxxxxxx Change: Overview screen, choose More > Extras > Delivery Output > Outbound Control | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Create Attachment for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori App | Open Display Outbound Delivery. | The Display Outbound Delivery: Initial Screen displays |  |
| 3. | Enter the outbound delivery number | On the Display Outbound Delivery screen, enter the outbound delivery number created in previous step and choose Enter. | The Display Outbound Delivery xxx: Overview screen displays. |  |
| 4. | Create Attachment for Delivery | Choose Services for Object on top right corner of screen, and then choose Create -> Create Attachment. | Import file Screen pops up. |  |
| 5. | Import File | Click button Import from native file system.In the Open screen, choose local path and file, click Open.Click OK in pop-up screen that shows import finished.Navigate Back to Import file screen, select file item, and click Choose to close window. | The attachment was successfully created, |  |
| 6. | Check Attachment | Click button Services for Object on top right corner of screen, choose Attachment list. | Attachment brings up in Service: Attachment list screen. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log onto the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad screen displays. |  |
| 2. | Access the SAP Fiori App | Open Manage Outbound Deliveries . | The Outbound Delivery Monitor screen displays. |  |
| 3. | Choose Picking | Select and Click For Picking. |  |  |
| 4. | Enter shipping point | Make the following entries and choose Execute.Shipping point: 1710Only Picking without WM: X |  |  |
| 5. | Change outbound delivery | From Day’s Workload for Picking , select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6. | Check if batch split exists | Navigate to the Picking tab, check if batch split exists in Batch Split Indicator column:Yes: go to 7.a,No: go to 7.b. |  |  |
| 7. | Enter Picked Quantity | Choose Batch Split Exists to expand sub item(s), enter quantity equal to delivery Qty in field Picked Qty for sub item.Enter quantity equal to delivery Qty in field Picked Qty for picking related item(s). |  |  |
| 8. | Choose Enter | Choose Enter. |  |  |
| 9. | Save | Choose Save. | The delivery has been picked. |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity you check the batch number assignment to the material.

Prerequisites

Use this step if batch management is used. E.g. TG21 and TG22

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log onto the SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Shipping Specialist. |  |  |
| 2. | Access the App | Open Change Outbound Delivery. |  |  |
| 3. | Enter the outbound delivery number | On the Change Outbound Delivery screen, enter the outbound delivery number and choose Enter. |  |  |
| 4. | Check the batch number assignment. | Expand Batch Spilit exists. In the Batch field, check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5. | Save Document | Choose Save. |  |  |

#### Split Outbound Delivery (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step, the user can split up single or multiple items from an existing, completely picked Outbound Delivery and move them to a new delivery document before posting Goods Issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the Role Shipping Specialist. |  |  |
| 2. | Access the App | Open Split Outbound Delivery. |  |  |
| 3. | Enter Shipping Point | On the entry screen of the Split Outbound Delivery app, make the following entry:Shipping point: 1710 |  |  |
| 4. | Enter Outbound Delivery | To speed up selection, make the following entry on the same screen:Outbound Delivery: [your Outbound Delivery Document Number] |  |  |
| 5. | Choose Split Profile | In the field Split Profile, make the following entry / select the following value from the list:Split Profile: 0003 (Delivery Split – LE Components) |  |  |
| 6. | Start Selection | Choose Execute. | A list of outbound delivery items for the selected Shipping Point and Outbound Delivery is displayed. |  |
| 7. | Select Items for Split | Select the items that should become part of a new delivery / that should be split from the current delivery. Enter the <Split Quality> and choose Save Split. | The selected items are displayed with a new delivery document number. The items not selected for the split still appear with the former document number. |  |

#### Add Freight Costs (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

You might want to add the actual freight costs to the Outbound Delivery after picking where you know the exact weights and freight charges.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Shipping Specialist. |  |  |
| 2. | Access the App | Open Change Outbound Delivery. |  |  |
| 3. | Enter the outbound delivery number | On the Change Outbound Delivery screen, enter the outbound delivery number and choose Enter. |  |  |
| 4. | Open Conditions | From the menu, choose More > Goto > Header > Conditions . |  |  |
| 5. | In the Condition Type column, enter YBHD | In the Condition Type column, enter YBHD. |  |  |
| 6. | Enter the freight costs | In the Amount column, enter the freight costs (such as 100).The system distributes the entered amount across the delivery items. The distribution is executed on the basis of the net weight of each item. |  |  |
| 7. | Save your outbound delivery | Save your outbound delivery. | Freight Costs are added to the Outbound Delivery and will be later copied to the Invoice. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log Onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Shipping Specialist. |  |  |
| 2. | Access the App | Open Manage Outbound Deliveries. | The Outbound Delivery Monitor screen displays. |  |
| 3. | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and Choose Execute.Shipping point: 1710 |  |  |
| 4. | Post good issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | The goods issue is posted. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery | The Display Outbound Delivery screen displays |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the Delivery number and click Continue. From the Delivery xxxxxxxx Display: Overview screen, choose More > Extras > Delivery Output > Output Control | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Stock Visbility at Headquarter

Purpose

In this activity you can view the Stock information at the Subsidiary from the Headquarter. The Headquarter can get information like Material, Quantity and etc.

Procedure

Headquarter can develop their own application by using whitelisted API’s and / or available CDS views at SAP Cloud ERP which will expose the required information from Subsidiary.

#### Proof of Delivery(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this test procedure, the user can record the quantities as confirmed by the respective customer after physical arrival of goods delivered and thus document the right quantities that should become subject to billing to this customer. This is only possible for Outbound Deliveries if the customer master data have been maintained in a way that this customer is "POD-relevant" (on sales area level).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the Role Shipping Specialist. |  |  |
| 2. | Access the App | Open POD - Change Outbound Delivery |  |  |
| 3. | Enter Outbound Delivery | On the entry screen of the app, make the following entry:Outbound Delivery: [your Outbound Delivery Document Number] and choose Continue. | The selected Outbound Delivery Document is displayed, tab page Overview POD is active. |  |
| 4. | Whether quantity different | If there is a quantity difference between shipping and receiving, go to step 5 & 6. |  |  |
| 5. | Enter Reason for variance in POD Delivery (optional) | In the line with the item for which a differing quantity was reported by the customer, make the following entry / select the following value from the list:Reason: ZFG2 (Underdelivery, reason unknown) |  |  |
| 6. | Enter Deviation in quantity actually delivered (optional) | In the field Quantity Difference in Sales Unit (QtyDiffinSalesUn), enter the respective quantity, which differs from the expected Delivery Quantity as per the Outbound Delivery Item and choose Enter. | The quantity displayed for the respective item in the field POD quantity has been re-calculated (Quantity Difference subtracted from Delivery Quantity), and value for the field POD Status has changed to B (Differences reported). |  |
| 7. | Confirm Proof of Delivery | Choose Confirm Proof of Delivery. | The field POD Date has been filled with the current date, and the value for the field POD Status has changed to C (Confirmed). |  |
| 8. | Save Outbound Delivery Document with Proof of Delivery | Choose Save. | The Outbound Delivery document is saved with confirmation for actually delivered quantities. These will be used for the consecutive billing step. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity you handle the billing.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents | The Create Billing Documents screen displays. |  |
| 3 | Define billing setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of sales document created previously and choose button Create. | There is one window Create Billing Documents displaying. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with ID Sxxxxxxxx will be displayed. |  |
| 7 | Save Billing Document | In the Billing Document screen, click button Save, The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.. | The system generates an invoice for billing. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 17100003Rcvbls Domestic US 3 | 41000000Rev Domestic Prod22001000Sales/Use Tax Accrue22002000Sales/Use Tax Accrue22003000Sales/Use Tax Accrue22004000Sales/Use Tax Accrue21730000(optional) Freight Clrg MM | none |

Financial Postings:

Public Customer

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Access APP | Open APP Manage Billing Documents under Sales > Billing Document | The screen Manage Billing Document will display |  |
| 2. | Search the billing document created in previous step | Input the Billing document number recorded in previous step. Choose Enter. | The billing document created in previous step will display. |  |
| 3. | Display the billing document | Select the billing document item, and choose Display. | The billing document shall be displayed. |  |
| 4. | Check Output Condition | On the Billing Document screen, choose the last assignment block – Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 5. | Display Print Preview | On the Billing Document screen choose Preview. | Preview for PDF document displays. |  |
| 6. | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel billing Docs | There is log display – Billing Document Canceled. |  |
| 7. | Update new Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8. | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by pressing the button Save in the footer bar. |  |  |

#### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Billing Document. | The Display Billing Document screen displays. |  |
| 3 | Enter the Billing number | On the Display Billing Document screen, enter the respective invoice number created in previous step and choose Enter. | The F2 Invoice xxx(F2) Display: Overview of Billing Items screen displays. |  |
| 4 | Create Attachment for Delivery | Click button Services for Object on top right corner of screen. Choose Create Attachment. | Import file Screen pops up. |  |
| 5 | Import File | Click button Import from native file system.In the Open screen, choose local path and file, and click Open.Click OK in pop up screen that shows import finished.Navigate Back to Import file screen, select file item and click Choose to close window. | The attachment was successfully created, |  |
| 6 | Check Attachment | Click button Services for Object on top right corner of screen. Choose Attachment list. | Attachment brings up in Service: Attachment list screen. |  |

#### Payment Information at Headquarter

Purpose

In this activity you can view the Stock information at the Subsidiary from the Headquarter. The Headquarter can get information like Customer Name, Payment Due, Due Date and etc.

Procedure

Headquarter can develop their own application by using whitelisted API’s and / or available CDS views at SAP Cloud ERP which will expose the required information from Subsidiary.

## Appendix

### Relevant Scope ID’s

BDG- Sales Quotation

BD9- Sell from Stock

BD6- Basic Credit Management

1JW - Advanced Available-to-Promise Processing

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Payment Information at Headquarter purpose says it views 'Stock information' though it concerns receivables (copy/paste error)

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cover says June 2026 while copyright says 2020 and last revision is 2021

> [!warning] Conflict
> Flagged while digesting this document, not verified: Intro calls the process a 'subcontracting process' though it is sale from local stock

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview table says Check Batches on page 28 while the TOC says 29

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-sell-from-local-stock-returns-customer-guide-248]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Sale_from_Local_Stock.docx` — full document · extracted with `mammoth` · 58,377 chars in the whole document
