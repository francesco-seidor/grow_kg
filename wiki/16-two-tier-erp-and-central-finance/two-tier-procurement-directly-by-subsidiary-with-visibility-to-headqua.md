---
id: 16-two-tier-erp-and-central-finance/two-tier-procurement-directly-by-subsidiary-with-visibility-to-headqua
title: Two-Tier Procurement directly by subsidiary with visibility to Headquarters (J45) (S4CLD2608_2T_Proc_J45)
description: "SAP S/4HANA Cloud 2608 customer guide and test script for scope item J45: subsidiary-run procurement and sales with HQ visibility via APIs and CDS views."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/subsidiary-procurement-with-hq-visibility]
aliases: [S4CLD2608_2T_Proc_J45]
keywords: [Subsidiary Procurement with HQ Visibility, two-tier procurement, hq visibility, purchase order approval, purchase order creation, integration requirements, analytical cds views, goods receipt, supplier invoice, gr/ir clearing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Proc_J45.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-244
topic: 16-two-tier-erp-and-central-finance/subsidiary-procurement-with-hq-visibility
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier Procurement directly by subsidiary with visibility to Headquarters (J45) (S4CLD2608_2T_Proc_J45)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Proc_J45.docx`, extracted with `mammoth`. Grouped under **Subsidiary Procurement with HQ Visibility** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| S/4HANA June 2026English |  |
|  | Two-Tier Procurement directly by subsidiary with visibility to Headquarters (J45) |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 14.09.2017 | Initial version of document |
|  |  |  |

Only add a revision when corrections are made to a published document. Do not change the original published date. Set back to revision 0 after a full upgrade of the Customer Guide.

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

[1 Purpose 6](#_Toc201244106)

[2 Value Proposition 6](#_Toc201244107)

[2.1 Solution with Two-Tier approach 7](#_Toc201244108)

[3 Business Process Details 7](#_Toc201244109)

[3.1 Prerequisites 7](#_Toc201244110)

[3.2 Process Flow with Technical Details 8](#_Toc201244111)

[4 Technical Requirement 8](#_Toc201244112)

[4.1 Integration Requirements by using API 8](#_Toc201244113)

[4.2 Integration Requirements by using EDI/IDOC 9](#_Toc201244114)

[4.3 Reporting Requirements by using Analytical CDS Views 9](#_Toc201244115)

[4.4 Reporting Requirements by using Analytical API 9](#_Toc201244116)

[5 Test Script 10](#_Toc201244117)

[5.1 Test case prerequisites 10](#_Toc201244118)

[5.1.1 System Access 11](#_Toc201244119)

[5.1.2 Roles 11](#_Toc201244120)

[5.1.3 Master Data, Organizational Data and Other Data 12](#_Toc201244121)

[5.1.4 Business Condition 13](#_Toc201244122)

[5.1.5 Preliminary Steps 13](#_Toc201244123)

[5.2 Overview Table 16](#_Toc201244124)

[5.3 Test Procedure 17](#_Toc201244125)

[5.3.1 Create Sales Order 17](#_Toc201244126)

[5.3.2 Create Purchase Order 19](#_Toc201244127)

[5.3.3 Approve Purchase Order 22](#_Toc201244128)

[5.3.4 Post Goods Receipt for Purchase Order 23](#_Toc201244129)

[5.3.5 Check Goods Receipt Details (Optional) 25](#_Toc201244130)

[5.3.6 Create delivery document 26](#_Toc201244131)

[5.3.7 Post goods issue 28](#_Toc201244132)

[5.3.8 Create Billing Document 30](#_Toc201244133)

[5.3.9 Manage Stock 32](#_Toc201244134)

[5.3.10 Creating Supplier Invoice with PO/GR relation 33](#_Toc201244135)

[5.3.11 GR / IR clearing 36](#_Toc201244136)

[5.3.12 Open Sales Order Visibility at HQ 38](#_Toc201244137)

[5.3.13 Open Purchase Order Visibility at HQ 39](#_Toc201244138)

[5.3.14 Stock Visibility at HQ 40](#_Toc201244139)

[5.3.15 Subsidiaries vendor liability visibility at HQ 41](#_Toc201244140)

[5.3.16 Account recievables at Subsidaries 42](#_Toc201244141)

[5.3.17 Financal update to HQ 43](#_Toc201244142)

[6 Appendix 45](#_Toc201244143)

[6.0 Relevant Scope ID’s / Test Scripts 45](#_Toc201244144)

**Procurement directly by Subsidiary with**

**visibility to Headquarters**

## Purpose

Scope item J45 enables independent procurement operations at subsidiary.

This is a typical scenario where a subsidiary is an independent entity with an efficient purchasing organization having strong presence in a geographical location. The subsidiary is equipped to run the procurement and manufacturing operations with ability to manage local inventory. The headquarters would prefer that the purchasing operations be independently be carried out by the subsidiary using SAP Cloud ERP for operational ease and cost effectiveness.

The process starts with customer purchase order received at Subsidiary, then system can check incoming sales orders against defined credit limits using credit management functionality before creating a sales order. Finally, Sales order is converted in to Purchase order in the system.

The purchase order is subject to approval based on a business requirements. Goods are shipped from the vendor and the goods receipt is prepared with reference to the purchase order. Order is shipped to customer after creating billing document. Invoices are entered with reference to a purchase order.

Periodic Financial update( Accounts Receivable for Billing and Accounts Payable for PO ) to the Headquarters is sent. Along with financials,sales order visibility,PO visibility and stock visibility is displayed at Headquarters.

This document provides a detailed user guide along with procedure for testing the scope item after solution deployment, reflecting the possible predefined scope of the solution. Each process step is covered in its own section, providing the system interactions (that is, test steps) in a table view.

## Value Proposition

The subsidiary is equipped to run the procurement and manufacturing operations with ability to manage local inventory. In a Two-Tier scenario supplier management and evaluation, source of supply and contract management is done locally by the subsidiary. The headquarters then has visibility into the spend, the inventory and the financial position of the subsidiary.

The following are key business requirements

- Monitoring with real time visibility of procurement activities at subsidiaries
- Headquarters can plan, guide and control procurement spend at subsidiaries
- Procurement Managers in Organizations do not clear defined responsibilities in both HQ and subsidiaries

### Solution with Two-Tier approach

With Two-Tier approach SAP Cloud ERP solution will be deployed on subsidiary and integrates with Headquarters which runs on SAP S/4HANA On-premise / ECC solutions.

The following business benefits will be achieved with Two-Tier approach.

- More autonomous procurement functions at subsidiaries.
- HQ can play more strategic role since procurement operations are managed at subsidiaries.
- Improved Process, stocks and spend visibility.
- Productivity improvement across HQ and Subsidiaries by defining clear roles & responsibilities.

## Business Process Details

This is a typical scenario where a subsidiary is an independent entity with an efficient purchasing organization having strong presence in a geographical location. The subsidiary is equipped to run the procurement and manufacturing operations with ability to manage local inventory. The headquarters would prefer that the purchasing operations be independently be carried out by the subsidiary using SAP Cloud ERP for operational ease and cost effectiveness. The supplier management and evaluation, source of supply and contract management is done locally by the subsidiary.

**Key Process Steps Covered**

**Subsidiary**

- Customer purchase order received at Subsidiary
- Credit Management
- Create Sales Order
- Create Purchase Order
- Approve PO
- Goods receipt for purchase order
- Ship Order to customer
- Create Billing
- Accounts Receivable for Billing
- Accounts Payable for PO

**Headquarters**

- Visibility of Sales Orders
- Visibility of PO Spend
- Visibility of Stock
- Visibility of Accounts Payable
- Visibility of Accounts ReceivableCreate Billing

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Connection/Integration between Headquarter and Subsidiary system
- Master data synchronization between Headquarter and Subsidiary

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

Refer technical setup guide for integration between SAP Cloud ERP and SAP S/4HANA On-premise / ECC

**Master Data Replication**

Refer the Master Data setup guide

### Integration Requirements by using API

The following API’s are required from Subsidiary (SAP Cloud ERP ) to realize the process

**Visibility scenario like Subsidiaries vendor liability, Account receivables at subsidiary and then Financial updates to HQ**

- Post Journal Entry Requests( JournalEntryCreateRequestConfirmation_In )- SOAP API

[Journal Entry - Post (Synchronous) | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b978f98fc5884ff2aeb10c8fdeb8a43b/f5c8d0579212c525e10000000a4450e5.html?version=2208.503)

### Integration Requirements by using EDI/IDOC

NA

### Reporting Requirements by using Analytical CDS Views

The following analytical CDS views are available from Subsidiary (SAP Cloud ERP ) to expose the data, so that Headquarter can create their own reports by consuming the CDS views

- I_SalesOrderItemCube for SO visibility
- C_OverduePO and C_PurchaseOrderValue for PO visibility
- I_MaterialStock for material stock display
- I_PurgCatPlanSpendAPI01 (Basic) for Purchasing Category Planned Spend

### Reporting Requirements by using Analytical API

NA

## Test Script

This section provides a detailed procedure for testing the scope item after solution deployment. Each process step is covered in its own section, providing the system interactions in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly.

### Test case prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

Note

The process to be tested in this test script is for Subsidiary side regarding a Two-Tier scenario. Hence integration between Subsidiary system (S/4HAN Cloud) and Headquarter system (SAP S/4HANA On-premise / ECC) shall be set up in advance. You will be able to process the test steps only after the corresponding buyer system has sent the required messages.

Also, customer-project-specific steps must be added.

#### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Roles

Assign the following business roles to your individual test users.

Note The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role Name | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK |  |
| Product Master Data Specialist | SAP_BR_PRODMASTER_SPECIALIST |  |
| Purchaser | SAP_BR_PURCHASER |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT |  |
| Configuration Expert (Cloud) | SAP_BR_BPC_EXPERT |  |
| HQ Analyst -Slaes | SAP_BR_INTERNAL_SALES_REP |  |
| HQ Analyst -Stocks | SAP_BR_PURCHASER |  |
| HQ Analyst -Finance | SAP_BR_AP_ACCOUNTANT |  |

#### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices for SAP CLOUD ERP , you can use the following SAP CLOUD ERP sample data.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 1010 | Plant 1 DE |  |
| Storage Location | 101A | Standard storage 1 | Shop floor w/o lean WM |
| Storage Location | 101B | Standard storage 2 | Shop floor w/o lean WM |
| Company Code | 1010 | Company Code 1010 |  |
| Purchase Organization | 1010 | Purch. Org. 1010 |  |
| Purchasing group | 001/002 | Group 001/Group 002 | depending on material |
| Vendor | 10300001 | Domestic 10 Supplier 1 |  |
| Material | TG0011 | Trading Good for Regular Procurement (PD planning) |  |
| Sold-to party | 30100001 | Domestic Customer AU 1 |  |
| Ship-to party | 30100001 | Domestic Customer AU 1 |  |
| Payer | 30100001 | Domestic Customer AU 1 |  |
| Shipping Point | 301R | Shipping Point 301R |  |
| Sales organization | 3010 | Dom. Sales Org AU |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating these master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |
| BNE | Create Supplier Master |
| BND | Create Customer Master |

#### Business Condition

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run | You have completed the steps described in the master data script. |
| BNZ - Create New Open MM Posting Period | You have completed the step described in the master data script. Posting Period is up to date. |
| 2EL – Integration of S/4HANA Sales with procurement | All relevant steps described in the Business Conditions and preliminary steps chapter are completed |

#### Preliminary Steps

##### Opening New MM Period

External Process

For this activity, run the following steps from the Create New Open MM Posting Period(BNZ) to close MM period and open new posting period.

• Closing MM Period and Opening New Posting Period

##### Assigning Release Processor for PO Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Use

In this procedure, you assign release processor for PO approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the Fiori Launch Pad as a Configuration Expert role | The SAP Fiori Launch Pad is displayed. |  |
| 2. | Open Manage Your Solution | Open Manage Your Solution. | The S/4 HANA Guided Configuration screen is displayed. |  |
| 3. | Open Configure Your Solution | In the S/4 HANA Guided Configuration screen, open Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4. | Open Purchase Order Approval Value | In the Configure Your Solution screen, search item PurchaseOrder-configureApproval , then click the Start button on the right | The Purchase Order Approval Value screen is displayed. |  |
| 5. | Configure Your Release Conditions for PO Approval | Make the following entries and choose the Save button:Purchasing Group <group>Active <X>Net Value <value>Currency <currency>Type US (User) Select one item and then choose EditAgent USER IDChoose Save. | The Purchase Order release condition is created. User ID is used for PO approval, for example, generic user PURCHASING_MANAGER, or use your own user with the related BCR role for PO approval authorization. |  |

Result

Release processor for PO approval has been assigned

### Overview Table

Process steps provided in the table below

| Process Step | HQ/Sub | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- | --- |
| Create Sales Order | Sub | Sales representative | Create Sales Order | The Create Sales Order: Initial screen displays. |
| [Create Purchase Order](#unique_12) | Sub | Purchaser | Create Purchase Order | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |
| [Approve Purchase Order](#unique_13) | Sub | Purchasing Manager | Approve Purchase Orders | A list of already created Purchase Orders is displayed. |
| [Post Goods Receipt for Purchase Order](#unique_17) | Sub | Warehouse Clerk | Post Goods Receipt for Purchase Order | The Post Goods Receipt for Purchase Order screen is displayed |
| [Check Goods Receipt Details (Optional)](#unique_19) | Sub | Warehouse Clerk | Material Documents Overview | The Material Documents Overview is displayed. |
| Create delivery | Sub | Warehouse Clerk | Create delivery Documents | The Create delivery Documents screen displays. |
| [Post Goods issue](#unique_17) | Sub | Warehouse Clerk | Post Goods issue | The Post Goods issue screen is displayed |
| Create billing document | Sub | Billing Clerk | Create Billing Documents | The Create Billing Documents screen displays. |
| [Manage Stock](#unique_23) | Sub | Inventory Manager | Manage Stock | The Manage Stock screen is displayed. |
| [Creating Supplier Invoice with PO/GR relation](#unique_24) | Sub | Accounts Payable Accountant | Create Supplier Invoice | The Create Supplier Invoice is displayed. |
| [GR / IR clearing](#unique_33) | Sub | Accounts Payable Accountant | Clear GR / IR Clearing Account | The Clear GR / IR Clearing Account screen opens |
| Open sales order report | HQ | Analyst/Business Manager | Via API | visibility from HQ |
| PO visibility | HQ | Analyst/Business Manager | Via API | visibility from HQ |
| Stock Visibility | HQ | Analyst/Business Manager | Via API | visibility from HQ |
| Subsidaries vendor liability | HQ | Analyst/Business Manager | Via API | visibility from HQ |
| Acount reciveables at subisidary | HQ | Analyst/Business Manager | Via API | visibility from HQ |
| Finacial updates to HQ | HQ | Analyst/Business Manager | Via API | visibility from HQ |

### Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

After you received cutomer purcahse order, credit check is done and then you perform this activity to create sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Internal sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage sales Orders | The Manage sales Orders screen displays. |  |
| 3 | Navigate to Create sales Order Screen | Choose Create sales Order | The Create sales Order: Initial Screen displays. |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create sales Order: Initial Screen, make the following entries:Order Type: ORSales Organization: 1710Distribution Channel: 10Division: 00Choose Enter |  |  |
| 5 | Enter Order Details | On the Create sales Order: Overview screen, make the following entries:Sold to party: example 17100001Ship-to party: example 17100001Customer Reference: PO numberOrder reason: Order ReasonMaterial Number: 2T_SG01Quantity: Quantity |  | PO number: Enter a customer purchase order number as referenceOrder reason : for example, Excellent priceQuantity: for example, 10 PC |
| 6 | Save Document | Choose Save Document. Make a note of the sales order number: __________. |  |  |

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this procedure, you create a purchase order for stock material directly. – in this case, PO is created already and hence verify all the fileds.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Purchase Order | Open Create Purchase Order. | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose the Create button. | The Create Purchase Order Screen is shown. |  |
| 4 | Enter Purchase Order data | Enter all of the necessary data.General Data:Supplier: 10300001The next data is displayed after the Supplier is enteredCompany Code: 1010Purchasing Org.:1010Purchasing Group:001Currency: EURIn Items section, choose General Data tabMaterial: TG0011Plant: 1010Quantity:xNet Price: xIn Items section, choose Delivery tabDelivery date: a date in the futureStorage Location: 101AIn Items section, choose Process Flow tabThe next data is displayed after the article is enteredGoods Receipt: xInvoice Receipt: xGR-Based IV: xIf you want your purchase order to be assigned to an approval, choose a quantity and net price higher than 500 USD (for Purchase Groups= 001 or 003 | The Create Purchase Order screen is displayed. |  |
| 5 | Add freight cost | Select General Data and choose XXX EUR under Item Value to show Pricing Elements. Choose Add Pricing elementsbutton and at the bottom of the Pricing Elelments panel, Add Price Elements section is shown. Input one of below three condition types for freight in the first empty blanket and press enterFGW1 (Freight / Gr. Weight 1), freight is calculated based on gross weight.FQU1 (Freight / Quantity 1), freight is calculated based on quantity.FVA1 (Freight / Value 1), freight is a fixed value.If you use FQU1 as an example, enter the following values:Condition type: FQU1Price Element Amount 4.00 EUR Per PCClick empty space in the Create Purchaser Order screen to go back. |  |  |
| 6 | Check Purchase Order for completeness | Choose the Simulate button and confirm Warning messages with close. | The Purchase Order is ready to be completed if no error is displayed in the dialog box. |  |
| 7 | Correct Issues (Optional) | Choose the Messages button. Check and correct the entries for errors. | You have corrected any issues. |  |
| 8 | Save Purchase Order | Choose the Submit button to save the Purchase Order. | A new Purchase Order is created. The system displays the message Purchase order xxx created. |  |

#### Approve Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this procedure, you release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country currency amount) or more require an approval (for Purchasing Group 001 and 003).

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Purchasing Manager role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Approve Purchase Order | Open Approve Purchase Orders. | A list of already created Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Enter the Purchase order number in the search area, then choose the Search button. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |
| 4. | Release Purchase Order | Select the Purchase order in left of the screen and choose Approve in bottom right. | The Submit Decision screen displays. |  |
| 4 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Order is approved. |  |
| 5 | Back to SAP Fiori Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Post Goods Receipt for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Post Goods Receipt for Purchase Order | Open Post Goods Receipt for Purchase Order. | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Search for Purchase Order | Open Purchase Order Search. | A list of Purchase Orders is displayed. |  |
| 4 | Select Purchase Order | Select your purchase order (if not in the PO, the storage location must be specified). | The system displays the data for the goods receipt on the Post Goods Receipt screen. |  |
| 5 | Enter Delivery Note | Make the following entries and Choose EnterDelivery Note: xxxControls output management after posting: Individual slip |  |  |
| 6 | Select Item | Select the items for which a goods receipt is to be posted.Select an item with a quantity of two or more pieces. | The Post button is activated. |  |
| 7 | Distribute | Choose the Distribution button.In the Stock Type field, select Blocked from the drop-down. Transfer of blocked stock will take place.Delivered: (default quantity -1) PCStock Type: Unrestricted useDelivered: 1 PCStock Type: Blocked | A. new item line is displayed. |  |
| 8 | Post | Choose the Post button. | The Post Goods Receipt screen is displayed. The system is displayed the message Material document xxx posted. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this step, the goods receipt fact sheet is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Documents Overview | Open Material Documents Overview. | The Material Documents Overview is displayed. |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose the Go button. | Plant: 1010Material Document:xxxOn the Manage Material Document screen, the relevant Material Documents / Material Document items are shown. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The list of the Material Documents is displayed.The Goods Receipts Details are shown. |  |
| 5 | Check Goods Receipts Details | Check the Status, the General Data, and the Material Document Items. | The Status of the Material Document is Not Reversed.In the General Data section, the correct Posting Date, Document Date, and the Delivery Note are shown. |  |
| 6 | Display Document Flow | Switch to the section Document Flow. | The Document Flow shows the Purchase Order and the Material Document as a flow chart. |  |
| 7 | Back to Launch Pad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Create delivery document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this step you create the return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries. | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Enter :Shipping Point: <Shipping point>, for example, 301RPlanned Creation Date: <Delivery selection date>Order: <Sales order number created previously> | The Delivery Create: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example: created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry: If delivery is created successfully, delivery number is shown on tab Deliveries, else, you can display the exact message type, text and also the related sales document on tab Messages.

#### Post goods issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you handle billing.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents under Sales > Billing Document . | The Create Billing Documents screen displays. |  |
| 3 | Define billing setting | Choose Billing Setting in bottom bar.There are four settings, we should make all of these settings to ON.Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List Item.Automatically Post Billing DocumentsDisplay Billing Document after creation. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Choose SD Document | Select the row of sales document created previously and choose button Create. | The dialog box Create Billing Documents displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo for Returns (CBRE) and maintain billing date, for example current date, then press button OK. | The draft billing document is created. |  |
| 7 | Save Billing Document | In the Billing Document screen, click button Save, The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000Rev Domestic Prod10100001 Rcvbls Domestic DE 1 |  | none |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you handle billing.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents under Sales > Billing Document . | The Create Billing Documents screen displays. |  |
| 3 | Define billing setting | Choose Billing Setting in bottom bar.There are four settings, we should make all of these settings to ON.Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List Item.Automatically Post Billing DocumentsDisplay Billing Document after creation. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Choose SD Document | Select the row of sales document created previously and choose button Create. | The dialog box Create Billing Documents displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo for Returns (CBRE) and maintain billing date, for example current date, then press button OK. | The draft billing document is created. |  |
| 7 | Save Billing Document | In the Billing Document screen, click button Save, The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial postings:

#### Manage Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

Materials must be scrapped as they are damaged and they should not appear any longer in the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Inventory Manager role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Stock | Open Manage Stock. | The Manage Stock screen is displayed. |  |
| 3 | Open Stock Overview | Enter the following data in the fields.Plant: 1010Material: TG0011 | The Manage Stock screen is displayed.The Stock Overview of the Material is shown. |  |
| 4 | Select stock | Select the icon beside the stock that you want to scrap. | A dialog box opens. The Storage Location, Stock Type, and current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Scrap Items | Enter the following data in the following data fields and choose the Post button.Stock Change:ScrappingCost Center: Such as R & DQuantity:x PC | The system displays Material document xxx created. The stock has been scrapped. |  |

#### Creating Supplier Invoice with PO/GR relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you create the supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice. | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 1010Gross Invoice Amount : XXXCurrency: EURInvoice Date: TodayPosting Date: TodayInvoice Party:10300001In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 1010Gross Invoice Amount : XXXCurrency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: TodayPosting Date: TodayReference: xxx(reference invoice number from invoicing party)Invoice Party:10300001Select See More at header area, make the following entries.Exchange Rate: XXX | The Create Supplier Invoices screen is displayed.The Exchange Rate should be changed from USD in EUR according to the customizing settings. The Exchange Rate is changeable |  |
| 4 | Enter Purchase Order References | In Purchase Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: xxx | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero | In the Tax area, you should see the same tax codes as in the items. | If there is no tax, specify the tax codeV0. |
| 8 | Change Item amount to block invoice on item level (optional) | If the item amount in supplier invoice is different from the one in PO, the item amount can be changed and the invoice will be blocked on the item level with a blocking reason.Amount: For example, change to XXX EUR (the variance exceeds the tolerance limit of price difference). Choose the arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manual Block. On the lower part of the details screen, the Blocking Reasons section shows the text Price Variance. | The item is blocked with a blocking reason.. |  |
| 9 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose the Simulate button.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area. |  | The supplier Invoice is complete to post. |
| 11 | Post Invoice | Choose the Post button. |  | The invoice is posted. The system displays the message Invoice xxx has been posted. |

#### GR / IR clearing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this step, one or more postings are cleared.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Tile Maintain GR / IR Clearing Account | Open Clear GR / IR Clearing Account. | The Clear GR / IR Clearing Account screen opens. |  |
| 3 | Search for Purchasing Documents | Make the following entries and choose the Execute (F8) button.Company Code:1010Plant: 1010Purchase Order Date to: <today> | The relevant Purchase Orders are shown. |  |
| 4 | Post Clearing | If Purchase Orders exist that need clearing, select one and choose Post Clearing (Ctrl + F12). | The clearing document is created. |  |
| 5 | Write down Clearing Document Number | The clearing document is created. Write down its number as it is needed for the next step. |  |  |
| 6 | Back to SAP Fiori Launch Pad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Open Sales Order Visibility at HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, headquarter will get the open sales orders at Subsidiary.

Prerequisites

API - Process Sales Orders implemented as per busienss requirement

Procedure

Headquarter can develop their own application by using whitelisted API’s for example Process Sales Orders. Using this, HQ should be able to display open sales order at Subsidary on SAP Cloud ERP .

#### Open Purchase Order Visibility at HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, headquarter will get the open purchaser orders at Subsidiary.

Prerequisites

API - Process Purchase Orders implemented as per busienss requirement

Procedure

Headquarter can develop their own application by using whitelisted API’s for example Process Purchase Orders. Using this, HQ should be able to display open purchase orders at Subsidary on SAP Cloud ERP .

#### Stock Visibility at HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, headquarter will get the mateiral stocks visibility at Subsidiary.

Prerequisites

API – Material stock display implemented as per busienss requirement

Procedure

Headquarter can develop their own application by using whitelisted API’s for example Material stock display Using this, HQ should be able to display material stocks at Subsidary on SAP Cloud ERP .

#### Subsidiaries vendor liability visibility at HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, headquarter will get the open payments visibility that are due for a supplier at Subsidiary.

Prerequisites

API – Post Journal entries implemented as per busienss requirement

Procedure

Headquarter can develop their own application by using whitelisted API’s for example Post Journal entries Using this, HQ should be able to display vendor liabilities at Subsidary on SAP Cloud ERP .

#### Account recievables at Subsidaries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, headquarter will get the consolidated account recievable payments visibility that are due at Subsidiary.

Prerequisites

API – Post Journal entries implemented as per busienss requirement

Procedure

Headquarter can develop their own application by using whitelisted API’s for example Post Journal entries Using this, HQ should be able to display account recievables at Subsidary on SAP Cloud ERP .

#### Financal update to HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, headquarter will get the consolidated finacial entries visibility at Subsidiary.

Prerequisites

API – Post Journal entries implemented as per busienss requirement

Procedure

Headquarter can develop their own application by using whitelisted API’s for example Post Journal entries Using this, HQ should be able get updates of financial entries Subsidary on SAP Cloud ERP .

## Appendix

### Relevant Scope ID’s / Test Scripts

The following scope ID’s are relevant for this process

-
    1. BNZ - Create New Open MM Posting Period
    2. 2EL – Integration of SAP S/4HANA Sales with procurement

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create delivery document section says 'create the return delivery' and billing uses Credit Memo for Returns (CBRE), which seems inconsistent with the outbound sales flow described in Purpose.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Test script uses sales org 1710 and customer 17100001 in the sales order step while the master data table lists sales org 3010 and customer 30100001.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-sell-from-local-stock-returns-customer-guide-248]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Proc_J45.docx` — full document · extracted with `mammoth` · 49,148 chars in the whole document
