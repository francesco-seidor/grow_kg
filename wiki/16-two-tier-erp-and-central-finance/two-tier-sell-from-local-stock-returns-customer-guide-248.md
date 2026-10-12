---
id: 16-two-tier-erp-and-central-finance/two-tier-sell-from-local-stock-returns-customer-guide-248
title: "Two Tier – Sell from Local Stock: Returns (Customer Guide) (S4CLD2608_2T_Local_Stock_Returns)"
description: SAP Cloud ERP two-tier customer guide and test script for customer returns at a subsidiary (return order to credit memo) with HQ visibility via API/CDS views.
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/sell-from-local-stock]
aliases: [S4CLD2608_2T_Local_Stock_Returns]
keywords: [Subsidiary Sales from Local Stock and Returns, two-tier returns, return order creation, return delivery, goods receipt posting, credit memo billing, hq visibility, api integration, test script, billing block removal]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Local_Stock_Returns.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-248
topic: 16-two-tier-erp-and-central-finance/sell-from-local-stock
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two Tier – Sell from Local Stock: Returns (Customer Guide) (S4CLD2608_2T_Local_Stock_Returns)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Local_Stock_Returns.docx`, extracted with `mammoth`. Grouped under **Subsidiary Sales from Local Stock and Returns** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERPJune 2026English |  |
|  | Two Tier – Sell from Local Stock: Returns |
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
| 0 | 13.09.2017 | Initial version of document |
| 1 | 27.05.2020 | Document Revision |
| 2 | 31.03.2021 | Review of Document |

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

[1 Purpose 6](#_Toc41558148)

[2 Value Proposition 6](#_Toc41558149)

[2.1 Business Requirements 6](#_Toc41558150)

[2.2 Two-Tier Solution 6](#_Toc41558151)

[3 Business Process Details 7](#_Toc41558152)

[3.1 Prerequisites 7](#_Toc41558153)

[3.2 Process Flow with Technical Details 8](#_Toc41558154)

[4 Technical Requirement 8](#_Toc41558155)

[4.1 Integration Requirements by using API 8](#_Toc41558156)

[4.2 Integration Requirements by using EDI/IDOC 8](#_Toc41558157)

[4.3 Reporting Requirements by using Analytical CDS Views 9](#_Toc41558158)

[4.4 Reporting Requirements by using Analytical API 9](#_Toc41558159)

[5 Test Script 10](#_Toc41558160)

[5.1 Purpose 10](#_Toc41558161)

[5.2 Prerequisites 10](#_Toc41558162)

[5.2.1 System Access 11](#_Toc41558163)

[5.2.2 Roles 11](#_Toc41558164)

[5.2.3 Master Data, Organizational Data and Other Data 12](#_Toc41558165)

[5.2.4 Business Condition 14](#_Toc41558166)

[5.3 Overview Table 14](#_Toc41558167)

[5.4 Test Procedure 14](#_Toc41558168)

[5.4.1 Create Return Order 15](#_Toc41558169)

[5.4.2 Create Attachment for Sales Order (Optional) 17](#_Toc41558170)

[5.4.3 Return Sales Order Visibility at HQ 19](#_Toc41558171)

[5.4.4 Create Return Delivery 20](#_Toc41558172)

[5.4.5 Create Attachment for Delivery (Optional) 22](#_Toc41558173)

[5.4.6 Post Goods Receipt 23](#_Toc41558174)

[5.4.7 Stock Visibility at HQ 26](#_Toc41558175)

[5.4.8 Remove Billing Block 27](#_Toc41558176)

[5.4.9 Create Billing Document 28](#_Toc41558177)

[5.4.10 Create Attachment for Billing (Optional) 31](#_Toc41558178)

[5.4.11 Information Update on Account Receivable at HQ 32](#_Toc41558179)

[5.4.12 Succeeding Processes 33](#_Toc41558180)

[5.4.13 Scheduling Job (alternative) 34](#_Toc41558181)

[6 Appendix 42](#_Toc41558182)

[6.1 Relevant Scope ID’s / Test Scripts 42](#_Toc41558183)

**Subsidiary as Production Unit and Internal Supplier to Head Quarter**

## Purpose

This document will provide the detailed process on Two Tier approach on Sell from Local Stock – Returns scenario with process flow chart with the test script which required for execution of the process from business user.

## Value Proposition

In this Two-Tier approach, business can have seamless information flow between Subsidiary and HQ with HQ having visibility of the process at Subsidiary. HQ can also control or provide inputs for doing the sales from local sales office.

### Business Requirements

There are many challenges faced by the business during integration of their HQ and Subsidiary with different systems landscape.

- Visibility of the Data at HQ – This will restrict HQ for making decision, as HQ will not be getting the live information
- Information flow between Subsidiary and HQ – Because of limitation of visibility of the data at HQ, information needs to be passed through manually like phone calls, mails and etc., which will affect the productivity of the business

### Two-Tier Solution

With Two-Tier Approach SAP Cloud ERP solution will be deployed on subsidiary and integrates with Headquarters which runs on S/4HANA OP / ECC solutions.

The following business benefits will be achieved:

- Better information flow – By integrating HQ and Subsidiary, information flow would be automatic and through live data HQ can take better decisions
- Reduction in manual information flow – Because of automated information flow, manual activity is reduced, thereby increasing the productivity

## Business Process Details

This scenario describes the entire process sequence for a return sales process from local sales office with a customer. The business process encompasses all steps from creating a return order to payment to the customer through credit memo creation.

Following is the process which is expected to be followed between Subsidiary and the:

- Customer rejects material and sends back to the Sales Office directly
- Refund clerk creates return order for the quantity of the returned product with the necessary information during the order creation with billing block status
- Information on Return Order will be sent to HQ through API integration
- Shipping specialist will create the return delivery and subsequently do the Goods Receipt against the return delivery
- Return stock information is sent to HQ
- Decision needs to be taken once Goods Receipt is done on whether the stock needs to be scrapped, to be returned to the supplier or need to be send to manufacturing for re-work, accordingly, process to be followed as per defined scope ID’s
- Billing block in the Return Sales Order is removed by Refund Clerk
- Billing Clerk will create the credit memo by referencing to the Return Delivery
- Account Payable clerk will perform the payment activities to the customer
- Financial update is sent to HQ through API integration

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Connection/Integration between Headquarter and Subsidiary system
- Master data – Business Partner and Material Master synchronization between Headquarter and Subsidiary

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

Refer technical setup guide for integration between SAP Cloud ERP and S/4HANA OP / ECC

**Master Data Replication**

Refer the Master Data setup guide

### Integration Requirements by using API

The following API’s are required from Subsidiary (SAP Cloud ERP) to realize the process

**Visibility of the Return Order**

- API_CUSTOMER_RETURN_SRV – ODATA API to read the return sales order

[Communication Scenario: Sales Order Integration (SAP_COM_0157)]

**Financial Update of Account Receivable:**

- Read API (oDATA) for Financial Document as Journal Entry (SAP_COM_0303)

### Integration Requirements by using EDI/IDOC

N/A

### Reporting Requirements by using Analytical CDS Views

The following analytical CDS views are available from Subsidiary (SAP Cloud ERP) to expose the data, so that Headquarter can get their own reports by consuming the CDS views

| CDS View Name | Description |
| --- | --- |
| I_MaterialStock | Material Stock calculation |
| C_MaterialStockActual | Total actual stock quantity |
| C_MaterialStockByKeyDate | Material Stock at posting date |
| I_MaterialStockTimeSeries | Material stock for periods |
| C_MaterialStockTimeSeries | Material stock for periods by type |

### Reporting Requirements by using Analytical API

NA

## Test Script

### Purpose

This scope item describes in Two-Tier approach, handling of sales order returns processing at local stock and subsequent visibility of the process to the Headquarter.

The process starts with a customer request for authorization to return materials to the plant for credit, referred to as a Return Material Authorization (RMA). The request is approved, and a return sales order is created with reference to the original invoice for the goods. An RMA document is printed and forwarded to the customer to be attached to the incoming goods. The goods are shipped back, a return delivery is created with reference to the RMA, and the material is received into return stock.

The return stock location is set to be non-MRP relevant. The goods are inspected, resulting in a disposition to either return them to stock, or scrap. A credit memo is created from the billing run and posted to the customer's account.

Headquarter will get the needed information like Return Sales Order, Stock returned at Subsidiary and Payment data from Customer for visibility of the process at Subsidiary.

This document provides a detailed procedure for testing the scope item after solution deployment, reflecting the predefined scope of the solution. Each process step is covered in its own section, providing the system interactions (that is, test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly (see the Test Step column). Customer-project-specific steps must be added.

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

Note:

The process to be tested in this test script is for Subsidiary side regarding a Two-Tier scenario. Hence integration between Subsidiary system (S/4HAN Cloud) and Headquarter system (S/4HANA OP / ECC) shall be set up in advance. You will be able to process the test steps only after the corresponding buyer system has sent the required messages.

#### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Roles

Assign the following business roles to your individual test users.

The following roles are provided as example roles from SAP. You can use these as templates to create your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK |  |

Appropriate roles required to be assigned to the users at Headquarter which may run on SAP ECC or S4H OP or Any Non-SAP system to get the visibility of the related process.

#### Master Data, Organizational Data and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

Additional Master Data (Default Values)

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trading Good for Reg. Trading (reorder point planning)no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH) (BLJ)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH) (BLJ)(BLP).See sections Business Conditions and Preliminary Steps. |
| Sold-to party | 30100001 | Domestic Customer AU 1 |  |
| Ship-to party | 30100001 | Domestic Customer AU 1 |  |
| Payer | 30100001 | Domestic Customer AU 1 |  |
| Plant | 3010 | Plant 1 AU |  |
| Storage Location | 301R | Storage Location Returns |  |
| Shipping Point | 301R | Shipping Point 301R |  |
| Sales organization | 3010 | Dom. Sales Org AU |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |
| BND | Create Customer Master |

#### Business Condition

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | To run through this scope item, you must already have sold some goods. |

### Overview Table

The scope item Customer Returns consists of several process steps, reports, items provided in the table below.

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Return Order](#unique_8) [page ] 15 | Internal Sales Representative | Create Sales Order | The Create Sales Order: Initial screen displays. |
| Get Return Order Visibility at HQ [page] 19 | Sales Manager |  | Get the information related to Return Sales Order |
| [Create Return Delivery](#unique_9) [page ] 20 | Shipping Specialist | Create Outbound Deliveries | The Create Outbound Deliveries screen displays. |
| [Post Goods Receipt](#unique_10) [page ] 23 | Shipping Specialist | Manage Outbound Deliveries | The Manage Outbound Deliveries screen displays. |
| Stock Visiblity at HQ [page] 26 | Inventory Analyst |  | Get the Stock of Returned Inventory |
| [Remove Billing Block](#unique_11) [page ] 27 | Internal Sales Representative | Change Sales Order | The Change Sales Document screen displays. |
| [Create Billing Document](#unique_12) [page ] 28 | Billing Clerk | Create Billing Documents | The Create Billing Documents screen displays. |
| Payment Information at HQ [page] 32 | Accountant Receivable |  | Payment Information to Customer |

### Test Procedure

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

#### Create Return Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you create the return order.

Prerequisites

You must have a reference invoice number and a billing document according to Sell from Stock (BD9).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Order | The Create Sales Order: Initial screen displays. |  |
| 3 | Enter Sales Document Type | Make the following entries and choose Enter:Sales Document Type: <sales order type> , for example, CBRESales Organization: <sales organization>Distribution channel: <distribution channel>Division: <division> | The Create with Reference dialog box displays. |  |
| 4 | Enter reference billing document | Make the following entries and choose Item selection:Billing Document: <Billing document> Enter the billing document number to be referenced. | The Create with Reference screen displays. |  |
| 5 | Copy | Select the items to be referenced in which open quantity is not equal to ‘0’ and choose Copy: | The Create Customer Return: Overview screen displays. |  |
| 6 | Enter Order Details | Make the following entries:Order reason: <Order Reason> For example, Poor quality. |  |  |
| 7 | Enter storage location | Select the item, choose Display item Detail. Navigate to Shipping tab and enter 301Rin Stor. Location field to ensure that it is the correct storage for return goods. |  |  |
| 8 | Maintain batch number | Only relevant for material TG21 and TG22:Double click the item and maintain the batch number on the Sales A tab. |  |  |
| 9 | Save | Choose Save.Note Please ignore any pop-up windows. | The return order has been created. |  |

Note If you have installed the scope item Rebate Processing: Free Goods in your system and you use material TG11 and customer 30100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter.

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

#### Return Sales Order Visibility at HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you run an app to check the return sales order visibility like material, quantity, expected date of return, return value and so on.

Prerequisites

You must have created Return Sales Order at Subsidiary.

Procedure

Headquarter can develop their own application by using whitelisted API’s and / or available CDS views at S4H Cloud which will expose the required information from Subsidiary.

#### Create Return Delivery

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
| 2 | Access the App | Open Create Outbound Deliveries – From Sales Orders | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Enter :Shipping Point: <Shipping point>, for example, 301RPlanned Creation Date: <Delivery selection date>Sales Document : <Sales order number created previously> | The Delivery Create: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example: created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry: If delivery is created successfully, delivery number is shown on tab Deliveries, else, you can display the exact message type, text and also the related sales document on tab Messages.

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery | The Change Outbound Delivery screen displays |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the Delivery number and click Continue. From the Delivery xxxxxxxx Change: Overview screen, choose More > Extras > Delivery Output > Output Control | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display PDF Document. | A preview of the print document is displayed. |  |
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

#### Post Goods Receipt

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
| 2. | Access the App | Open Manage Outbound Deliveries. | The Manage Outbound Deliveries screen displays. |  |
| 3. | Open Manage Outbound Deliveries | Shipping point: 301RChoose Overall Status Ready to Post GI. Make the following entries and Choose Execute. |  |  |
| 4. | Post good issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | The goods issue is posted. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 51600000Consptn Trde Gds | none |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery | The Display Outbound Delivery screen displays |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the Delivery number and click Continue. From the Delivery xxxxxxxx Display: Overview screen, choose More > Extras > Delivery Output > Output Control | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Stock Visibility at HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, headquarter will get the stock information for the returned goods at Subsidiary.

Prerequisites

You must have done the Goods Receipt against the return delivery before executing this app.

Procedure

Headquarter can develop their own application by using whitelisted API’s and / or available CDS views for Stock related information like the quantity of the stock returned against the return delivery and return sales order which will expose the required information from S4H Cloud.

#### Remove Billing Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, billing block is removed from sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Sales Order. | The Change Sales Document screen displays. |  |
| 3 | Enter return order number | Enter return order number in the field Order and choose Enter. | The Change Customer Return 6XXXXXXX: Overview screen displays. |  |
| 4 | Enter reference billing document | On Sales tab, remove Check Credit Memo in the field Billing Block, then choose Save. | Billing block is removed from return order. |  |

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

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000Rev Domestic Prod10100001 Rcvbls Domestic DE 1 |  | none |

Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Access APP | Open APP Manage Billing Documents under Sales > Billing Document | The screen Manage Billing Document displays. |  |
| 2. | Search the billing document | Enter the billing document number recorded previously in field Billing Document and choose Enter. | The billing document which create in previous step displays. |  |
| 3. | Display the billing document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4. | Check Output Condition | On the Billing Document screen, go to the last assignment block – Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 5. | Display Print Preview | On the Billing Document screen choose Preview. | Preview for PDF document displays. |  |
| 6. | Cancel Billing Document (Optional) | On the Billing Document screen, select certain Billing document and choose Cancel billing Document | There is log display – Billing Document Canceled. |  |
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

#### Information Update on Account Receivable at HQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Prerequisites

You must have created the credit memo for the goods return and subsequent payment done to the customer.

Procedure

Headquarter can develop their own application by using whitelisted API’s and / or available CDS views which will expose the required information from S4H Cloud.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Post the incoming payment.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable(J59) (Section Post Incoming Payments) |
| Return to Supplier (BMK) (optional) | Dispose of the inventory by returning to the vendor. Do not process any other activities in this document after running the external process.Using the master data from this document, complete the following activities described in the test script:Return to Supplier (BMK) |
| Core Inventory Management (BMC) (Optional) | Returned material can be blocked or scrapped.Using the master data from this document, complete the following activities described in the test script:Core Inventory Management (BMC) |
| Rework Processing - Stock-Manufactured Material (BJN) (optional) | Rework activities and material postings after production execution for the original material (including goods receipt of the product) with an additional rework production order.Using the master data from this document, complete the following activities described in the test script:Rework Processing - Stock-Manufactured Material (BJN) |
| Sales Order Fulfillment Monitoring (BKK) (optional) | Collection of periodic activities such as day ending activities.Using the master data from this document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring (BKK) (Sections on Review Sales Documents blocked for billing, Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents) |

#### Scheduling Job (alternative)

##### Job Scheduling for Delivery Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step, you can schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Logon | Logon to the SAP Fiori Launchpad using Role Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Schedule Delivery Creation. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3. | Create Delivery Creation Schedule | Choose New to define a new job. | The New Job screen is displayed. Job Template should default as Schedule Delivery Creation. |  |
| 4. | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5. | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Delivery Creation Job Log | In screen Application Jobs, after job item’s status turned to Finish, choose Status symbol in column Log.Note Click the Magnifier, the job list will refresh. | Screen goes to job log details. |  |

##### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step, you can schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Logon | Log on to the SAP Fiori Launchpad using Role Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open the Schedule Goods Issue For Deliveries. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3. | Create Goods Issue Deliveries Schedule | Choose the New to define a new job. | The New Job screen is displayed. Job Template should default as Schedule goods issue for Deliveries. |  |
| 4. | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5. | Schedule | Choose the Schedule. | A schedule goods issue for deliveries job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Goods Issue Deliveries Job Log | In screen Application Jobs, after job item’s status turned to Finish, choose Status symbol in the column Log.Note Choose the Magnifier, the job list will refresh. | The job log details displays. |  |

##### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step, you can schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Logon | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open the Schedule Billing Creation. | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3. | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job screen is displayed. Job Template should default as Schedule Billing Creation. |  |
| 4. | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5. | Schedule | Choose the Schedule. | A billing creation job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Billing Creation Job Log | In screen Application Jobs, after job item’s status turned to Finish, choose Job Log.Note Select the Magnifier, and the job list will refresh. | The log details displays. |  |

##### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step, you can schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open the Schedule Billing Release. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3. | Create Billing Release Schedule | Choose New to define a new job for billing creation.. | The New Job screen is displayed. Job Template defaultly should be Schedule Billing Release. |  |
| 4. | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5. | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6. | Check Billing Release Job Log | In screen Application Jobs, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, the job list will refresh. | The log details displays. |  |

##### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step, you can schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open the Schedule Billing Output. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3. | Create Billing Output Schedule | Choose the New to define a new job for billing creation. | The New Job screen is displayed. Job Template should default as Schedule Billing Output. |  |
| 4. | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose the Check. | The system displays the message Go ahead and schedule the job. |  |
| 5. | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6. | Check Billing Output Job Log | In screen Application Jobs, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, the job list will refresh. | The log details displays. |  |

## Appendix

### Relevant Scope ID’s / Test Scripts

The following scope ID’s are relevant for this process

-
    1. BD9 – Sell from Stock
    2. BDD – Customer Returns
    3. J59 – Account Receivable
    4. BMK – Return to Vendor
    5. BJN – Rework Processing – Stock manufactured Material
    6. BMC – Stock Usage Blocking and Usage
    7. BKK – Sales Order Fulfilment Monitoring

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-sale-from-local-stock-by-subsidiary-249]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Local_Stock_Returns.docx` — full document · extracted with `mammoth` · 49,502 chars in the whole document
