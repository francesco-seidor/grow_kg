---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-service-order-management-in-headquarter-subsidiary-model
title: "Two-Tier ERP: Service Order Management in Headquarter-Subsidiary Model (2-Tier ERP) (S4CLD2608_2T_Service ord)"
description: "SAP customer guide for two-tier ERP where a subsidiary on Cloud ERP delivers services against a headquarter purchase order: process, EDI/IDoc/API setup, test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/subsidiary-service-delivery]
aliases: [S4CLD2608_2T_Service ord]
keywords: [Subsidiary Service Order Delivery for Headquarters, two-tier erp, service order management, headquarter-subsidiary integration, edi idoc integration, service confirmation, release for billing, billing documents, supplier invoice, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Service ord.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-250
topic: 16-two-tier-erp-and-central-finance/subsidiary-service-delivery
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP: Service Order Management in Headquarter-Subsidiary Model (2-Tier ERP) (S4CLD2608_2T_Service ord)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Service ord.docx`, extracted with `mammoth`. Grouped under **Subsidiary Service Order Delivery for Headquarters** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERPJune 2026English |  |
|  | Two-Tier ERP: Service Order Management in Headquarter-Subsidiary Model (2-Tier ERP) |
|  | Customer Guide |

Copyright

© 2021 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 31.03.2021 | Initial version of document |

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

Contents

[1 Purpose 6](#_Toc68183362)

[2 Value Proposition 6](#_Toc68183363)

[2.1 Business Requirements 6](#_Toc68183364)

[2.2 Two-Tier Solution 6](#_Toc68183365)

[3 Business Process Details 6](#_Toc68183366)

[3.1 Prerequisites 7](#_Toc68183367)

[3.2 Process Flow with Technical Details 7](#_Toc68183368)

[4 Technical Requirement 9](#_Toc68183369)

[4.1 Integration Requirements by using EDI/IDOC/API 9](#_Toc68183370)

[4.2 Technical Requirements 10](#_Toc68183371)

[5 Test Script 11](#_Toc68183372)

[5.1 Prerequisites 11](#_Toc68183373)

[5.2 Role at Subsidiary 11](#_Toc68183374)

[5.3 Role at Headquarters 12](#_Toc68183375)

[5.4 Master Data, Organizational Data, and Other Data 12](#_Toc68183376)

[5.6 Overview Table 15](#_Toc68183377)

[5.7 Test Procedures 16](#_Toc68183378)

[5.7.1 Purchase Order is created at Headquarter 16](#_Toc68183379)

[5.7.2 Send Order Confirmarion 16](#_Toc68183380)

[5.7.3 Display Service Order (Optional) 16](#_Toc68183381)

[5.7.4 Change Service Order (Optional) 16](#_Toc68183382)

[5.7.5 Release Service Order 17](#_Toc68183383)

[5.7.6 Create Confirmation 18](#_Toc68183384)

[5.7.7 Service Entry Sheet at Headquater (Optional) 19](#_Toc68183385)

[5.7.8 Release Confirmation for Billing 19](#_Toc68183386)

[5.7.9 Create Billing Document (Invoice) 20](#_Toc68183387)

[5.7.10 Send Supplier Invoice 22](#_Toc68183388)

[6 Appendix 24](#_Toc68183389)

[6.1 Relevant Scope ID’s 24](#_Toc68183390)

**Service Order Management in Headquarter-Subsidiary Model (2-Tier ERP)**

## Purpose

This document will provide the detailed process on Two-Tier ERP solution for process where “Service is delivered from Subsidiary against a Purchase order at Headquater” with process flow, technical requirements and followed with testing procedure.

## Value Proposition

### Business Requirements

The Headquarter process the customer's order and details of recipient of service are communicated as service order to subsidiary, Services are directly delivered from Subsidiary with seamless processes integration between headquarters and subsidiary.

### Two-Tier Solution

Through Two-Tier ERP solutions, seamless orchestration of process between headquarters and subsidiary along with below Integration points.

1. Purchase order at Heaquarter will be automatically transformed to service order at Subsidiary.
2. Subsidiary confirms the service order and subsequently the Purchase order at the Headquarter is updated.
3. Subsidiary creates billing documents; corresponding supplier invoice will be created at Headquarters.

## Business Process Details

The Two-Tier ERP solution where Service is delivered from Subsidiary against a Purchase order at Headquater.

The process starts where customer places order at Headquarter for services. The internal sales representative at the Headquater creates the sales order of customer, where purchase requisition is created against the sales order. The purchase requisition is converted to purchase order from the displayed list of purchase requisition. Once the purchase order is approved EDI based approach is used to automatically transfer the purchase order information, for creation of service order at Subsidiary .

Customer Service Manager will receive the automatically generated service order at subsidiary with sold-to, bill to and pay to as headquarter and ship-to as the end customer. Once the service order is confirmed, EDI based approach is used to confirm the purchase order at Headquarter

As soon as the service order is confirmed the service technician or service customer manager at subsidiary does the service and confirm the service.

One service delivery the purchaser at headquarter posts service entry sheet (this is an optional step)

Billing document is created at subsidiary and bill to headquarter, corresponding Supplier invoice will be created automatically at headquarter.

Headquarter Bills the customer

Note: For customers in S/4 Hana on premise which are using Service orders can start the process with Service order created for customer at Headquater. Since this service is to be provided by subsidiary, purchase requisition is created against the service order. The purchase requisition is converted to purchase order from the displayed list of purchase requisition. Once the purchase order is approved EDI based approach is used to automatically transfer the purchase order information, for creation of service order at Subsidiary .

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Subsidiary should be running on SAP Cloud ERP system and Headquarters should run on SAP S/4HANA On Premise/ Cloud ERP Private or ECC
- Activate the Scope ID 2EL and 3D2 at the Subsidiary’s SAP Cloud ERP system
- In case Headquarters is on:
- SAP S/4HANA On Premise / Cloud ERP Private activate the scope ID BD9
- SAP ERP follow standard sell from stock process.
- The Headquarters and Subsidiary should have business partner and product/service master data aligned for this business process to work.
- Subsidiary will be represented as a Supplier in Headquarter and Headquarter will be represented as a Customer in Subsidiary.

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

Service Order

Corporate

Tier One

Corporate

Tier Two

Service Order Confirmation

Invoice

API

API

**Tier1**

-
    - Receives customer Order for Services at Headquarter
    - Purchase requisition is created against the order
    - The purchase requisition is converted to purchase order from the displayed list of purchase requisition
    - Once the purchase order is approved EDI based approach is used to automatically transfer the purchase order information, for creation of service order at Subsidiary.

**Tier2**

-
    - Receive the automatically generated service order with sold-to as headquarter and ship-to as the end customer.
    - Once the sales order is confirmed, EDI based approach is used to confirm the purchase order at headquarter
    - Service is confirmed at the Subsidiary

**Tier1**

-
    - Service entry sheet is posted at the headquarter, this is an optional step

**Tier 2**

-
    - Billing document is created and bill to headquarter, corresponding Supplier invoice will be created automatically at headquarter.
    - Headquarter Bills the customer

The following integration points are depicted in the process flow diagram:

1. Purchase order at Headquarter will be automatically transformed to Service at Subsidiary
2. Subsidiary confirms delivery date to the Headquarter.
3. Subsidiary create billing documents correspondingly supplier invoice will be created at Headquarter.

## Technical Requirement

This section covers the process of setting up integration between the SAP Cloud ERP system and SAP S/4HANA On-Premise / Cloud ERP Private system covering the main prerequisites such as Communication arrangements, Cloud connector and API’s (Application programming interfaces) are required to enable the direct integration between the system. For detail you can refer to [Set- up instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/2EL_Set-Up_EN_XX.pdf) for SAP Best practice scope item [2EL](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2102/US/23/EN/scopeitems/2EL).

### Integration Requirements by using EDI/IDOC/API

**In SAP Cloud ERP:**

- Use Communication System SAP_COM_0424 for creating service order and sending service oder confirmarion in SAP Cloud ERP. For more details kindly refer [Service Order - Create, Change (Asynchronous)](https://api.sap.com/api/SERVICEORDERREQUEST_IN/overview)
- Use Communication System SAP_COM_0223 for Sales with Buyers Integration. For more details kindly refer [Customer Invoice - Send (B2B)](https://api.sap.com/api/CO_EDI_INVOICE_REQUEST_OUT/overview)

**In SAP S/4HANA On Premise/ Cloud ERP Private /ECC:**

Configure the Partner profiles and message control for incoming IDOCS for Sales Order creation and change and outbound IDOCS for Order Confirmation, Advance Shipping

Notification and Billing Document.

The following IDOCS are to be used:

| **Message Type** | **Direction** | **Use** |
| --- | --- | --- |
| ORDERS05 | Inbound | Sales Order Creation/Change |
| ORDRSP | Outbound | Sales Order Confirmation |
| INVOIC02 | Outbound | Billing document |

### Technical Requirements

**In SAP Cloud ERP:**

To populate purchase order in the external communication with S/4 Hana on Premise/ Cloud ERP Private /ECC, an Enhancement was done for Billing.

A new text field named Service Purcahse Order of length 10, was added via the application Custom Fields and Logic under the tab Custom Fields, for the business context Sales: Billing Document. Its usage was enabled in the SOAP API InvoiceRequest_Out.

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

A cloud BAdI implementation was created via the Application Custom Fields and logic, under the tab Custom logic, for the business context Sales: Billing document and the BAdI Modification of Custom Header Fields in Customer Invoice SOAP Message for the scenario.

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

The logic to populate the custom field should be written here.

## Test Script

### Prerequisites

The test scenario can be built in the following Two-tier system landscape:

| System | Details |
| --- | --- |
| SAP S/4HANA On-Premise system/ Cloud ERP Private /ECC - Headquarters | SAP S/4HANA On-Premise system / Cloud ERP Private /ECC |
| SAP SAP Cloud ERP system - Subsidiary | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### 5.2 Role at Subsidiary

Assign the following business roles to your individual test users at Subsidiary.

Note The following roles are provided as example roles from SAP. You can use these as templates to create your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR |  |
| Service Technician - Customer Service | SAP_BR_CUSTOMER_SRVC_TEC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT |  |

Assign the following business roles to your individual test users.

### 5.3 Role at Headquarters

The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role |
| --- |
| Internal Sales Representative |
| Purchaser |
| Purchasing Manager |
| Billing Clerk |
| Accountant |

For more information about business roles, refer to Assigning business roles to a user in the [Administration Guide for the Implementation of SAP S/4HANA](https://help.sap.com/viewer/S4HANA1709_AdminGuide).

### 5.4 Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, Services, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values and enables you to go through the process steps of this scope item.

Note Additional Master Data (Default Values)

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Note Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data.

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure. Below is the Master data maintained at SAP Cloud ERP.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Service | SRV_01 | Services |  |
| Sold-to party | 10100050 | Ausländischer Kunde | This Sold to party represensts Headquater |
| Ship-to party/ServiceRecipient | 17100012 | Domestic Customer Invoice List | Customer to which services are to be shipped |
| Payer | 10100050 | Ausländischer Kunde | Payer represents Headquater |
| Sales organization | 1010 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Company Code | 1010 | Company Code 1010 |  |
| Condition Master |  |  | Condition master can be managed centrally at Headquarters with the buying price for the headquater and selling price for subsidiary being same by using release accelerators on ‘Centralised Pricing’. In parallel you can also use whitelisted API’s in API Hub. |

Master Data maintained in Headquarters on Premise System

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Service | SRV_01 |  |  |
| Vendor | XXXXXXX | Customer no. subsidiary | Subsidiary to be maintained as a supplier in Headquarter. Mapping for Customer number at subsidiary is also must be done. |
| Condition Master |  |  | Condition master can be managed centrally at Headquarters with the buying price for the headquater and selling price for subsidiary being same by using release accelerators on ‘Centralised Pricing’. In parallel you can also use whitelisted API’s in API Hub. |

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 2EL | For more details on master data, converting External to internal Partner Number, Assign Customer or Supplier to Sales Organization Data and set up please check 2EL |

## 5.6 Overview Table

| Test Step # | Test Step Name | Business Role | Expected Result |
| --- | --- | --- | --- |
| 1 | Create Purchase order in headquarter |  | Service order is created automatically in subsidiary based on the PO received from the Headquarter. |
| 2 | Order Confirmation updated in the Purchase order confirmation at headquater |  | Order confirmation is created automatically based on the service order. |
| 3 | Display Service Order (Optional) at subsidiary | Customer Service Manager | PO is transferred to Subsidiary as service order |
| 4 | Change Service Order (optional) | Customer Service Manager | Service order changed |
| 5 | Release Service Order | Customer Service Manager | The service order has been released |
| 6 | Create Confirmation | Customer Service Manager | A follow-up service confirmation has been creat-ed |
| 7 | Service Entry sheet created at Headquarter (optional) |  |  |
| 8 | Release Confirmation for Billing | Customer Service Manager | The confirmation has been released for billing |
| 9 | Create Billing Document (Invoice) | Billing Clerk | Aninvoice (billing document) is created. |
| 10 | Supplier Invoice is automatically sent to the Headquarter system |  | Supplier Invoice is automatically sent to the Headquarter system. |

### 5.7 Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### 5.7.1 Purchase Order is created at Headquarter

Sales order is created at Headquater, where purchase requisition is created against the sales order. The purchase requisition is converted to purchase order from the displayed list of purchase requisition. Once the purchase order is approved EDI based approach is used to automatically transfer the purchase order information, for creation of service order at Subsidiary .

### 5.7.2 Send Order Confirmarion

An Order Confirmation is automatically sent to the Headquarter System

### 5.7.3 Display Service Order (Optional)

In this activity, you see newly created service order in SAP S/4HANA subsidiary system.

### 5.7.4 Change Service Order (Optional)

This step describes how you can change an existing service order.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR). | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 2 | Open Manage Service Order application | Choose the Manage Service Orders application tile. | The list report page is displayed. |  |
| 3 | Find Service Order | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 4 | Open Service Order in the Edit mode | Choose Edit for your Service Order in the list. | The edit view of the Service Order will be opened. |  |
| 5 | Change Service team and employee responsible | Add employee responsible and the Service team | Service Order saved |  |

### 5.7.5 Release Service Order

This step describes how you can release an service order.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR). | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 2 | Open Manage Service Order application | Choose the Manage Service Orders application tile. | The list report page is displayed. |  |
| 3 | Find Service Order | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 4 | Open Service Order in the Edit mode | Choose Edit for your Service Order in the list | The edit view of the Service Order will be opened. |  |
| 5 | Release Service Order | Change the Life Cycle Status to ReleasedChoose Save. | Your service order has been released.You can create follow-up confirmations for all items of this service order. |  |

### 5.7.6 Create Confirmation

In this step a follow-up service confirmation will be created. It includes setting the confirmation to completed as well as the final confirmation (final flag).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR) or Service Technician - Customer Service (SAP_BR_CUSTOMER_SRVC_TEC). | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 2 | Open Manage Service Order application | Choose the Manage Service Orders or for the Technician Process Service Orders application tile. | The list report page is displayed. |  |
| 3 | Find Service Order | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 4 | Display Service Order Details | Choose your Service Order ID from the Service Order result list. | You should be navigated to the object page for the corresponding Service Order. |  |
| 5 | Open Create Service Confirmation window | Choose Create Service Confirmation on the top. | A simple Create Service Confirmation window will be displayed. |  |
| 6 | Maintain Service Confirmation data | Enter the following data to create a service confirmation:Final Confirmation: YesExec. Service Employee: for example, 9980000xxx (CONSULTANT1_US)Maintain all quantities of all items of the service order in the confirmation:Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new confirmation has been created.The edit view of the Service Confirmation will be opened. |  |
| 7 | Open the details view of the Service Item | Choose Items tab or scroll down to the items area.Choose Edit for the line item which contains the service item <SRV_01>. | The details view of the service item is displayed. |  |
| 9 | Complete the Service Confirmation | Change the Life Cycle Status to Completed.Check the field Final Confirmation and flag the checkbox if not yet done.Then, choose Save. | With the status being completed, this confirmation cannot be changed anymore, but only cancelled.Further since the final confirmation has been set, the Life Cycle status of the related service order will be automatically set to completed. This is the prerequisite for the items to be released for billing. |  |
| 10 | Check Life Cycle Status of Service Order | Check the Life Cycle Status of the Service Order. | The life Cycle Status should be ‘Completed’. |  |

### 5.7.7 Service Entry Sheet at Headquater (Optional)

Service Entry sheet is to be created at Headquarter (optional)

### 5.7.8 Release Confirmation for Billing

The Service manager releases the items of the confirmation for Billing.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager (SAP_BR_CUSTOMER_SRVC_MGR). | The Fiori Launchpad with access to the Release for Billing application is displayed. |  |
| 2 | Open Release for Billing application | Choose the Release for Billing application tile. | The list report page is displayed. |  |
| 3 | Find your items to be Released for Billing | In the search area on the top,Enter the ID of your service confirmation in the Search field.Choose Go. | All items of the respective confirmation which have been confirmed and completed in the service order, are displayed in the list. |  |
| 4 | Release a confirmation item | Select an item and choose the action ‘Release for Billing’. | The selected transactions and items should be Released for billing on Success.If any error occurs, you should see a popup with a list of Errors returned from this action. |  |

### 5.7.9 Create Billing Document (Invoice)

In this activity the billing clerk creates an invoice for the service confirmation items that was released for billing in the previous step. The invoice or billing document is created by the billing clerk.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Billing Clerk ( SAP_BR_BILLING_CLERK). | The Home screen appears. |  |
| 2 | Access Billing Due List Items | Open Create Billing Documents (Billing Due List Items). | The Create Billing Documents view with the Billing Due List Items list is displayed. |  |
| 3 | Define Billing Settings | In the Create Billing Documents view, choose Billing Settings in the bottom bar (next to the Create button).On the Billing Settings dialog window, maintain the following settings:Set billing date and type before billing: ON.Create separate billing document for each item of billing due list: OFF.Automatically post billing documents: ON.Display billing documents after creation: ONChoose OK. | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Select Item(s) for Billing | Maintain the following search criteria:SD Document Category: <Billing Document Request>In order to better find your items to be billed, choose the icon Settings.In View Settings select to display the field BDR Source Document.Choose OK and find your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select the row(s) of billing document requests created for your service confirmation items. Then choose Create.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | A Create Billing Documents dialog window is displayed. |  |
| 5 | Select Billing Type and Billing Date | On the Create Billing Documents dialog window, choose the following values:Billing Type: F2 Invoice (F2)Billing Date: <today’s date>Then choose OK. | The F2 Invoice screen is displayed. |  |
| 6 | Save Billing Document | In the F2 Invoice screen, choose Save.The billing document with ID xxxxxxxx is created. Make a note of the billing document number for further reference. | The system has generated an invoice for billing. |  |

### 5.7.10 Send Supplier Invoice

This step is automatically generated. Invoice is sent to the Headquarter system.

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

### 6 Appendix

### 6.1 Relevant Scope ID’s

The SAP Cloud ERP API’s are relevant for the following scope item ID’s in [Service Order Management and Monitoring (‏3D2‏)](https://rapid.sap.com/bp/#/browse/scopeitems/3D2) and [Integration of Sales with External Buyers (2EL)‎](https://rapid.sap.com/bp/#/browse/scopeitems/2EL)

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Integration point 2 is described as 'Subsidiary confirms delivery date' in one list and as 'confirms the service order, PO updated' in another

## Connections
- part-of :: [[_cluster]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-scenario-managing-intercompany-professional-services-projects]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_Service ord.docx` — full document · extracted with `mammoth` · 29,783 chars in the whole document
