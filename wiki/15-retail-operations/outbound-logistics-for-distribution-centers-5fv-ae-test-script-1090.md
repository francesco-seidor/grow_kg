---
id: 15-retail-operations/outbound-logistics-for-distribution-centers-5fv-ae-test-script-1090
title: Outbound Logistics for Distribution Centers (5FV_AE) - Test Script (5FV_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script (19-06-26) for scope item 5FV_AE: stock transfer order, outbound delivery, pick/pack, goods issue and store goods receipt."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/dc-outbound-logistics]
aliases: [5FV_S4CLD2608_BPD_EN_AE]
keywords: [Outbound Logistics for Distribution Centers, outbound logistics, stock transfer order, outbound delivery, pick pack goods issue, goods receipt, delivery note printing, output parameter determination, initial stock, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FV_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1090
topic: 15-retail-operations/dc-outbound-logistics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Outbound Logistics for Distribution Centers (5FV_AE) - Test Script (5FV_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FV_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Outbound Logistics for Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Outbound Logistics for Distribution Centers (5FV_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Outbound Logistics for Distribution Centers (5FV_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856917)

[2 Prerequisites 4](#_Toc232856918)

[2.1 System Access 4](#_Toc232856919)

[2.2 Roles 4](#_Toc232856920)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856921)

[2.4 Business Conditions 5](#_Toc232856922)

[2.5 Preliminary Steps 6](#_Toc232856923)

[2.5.1 Create Initial Stock in the Distribution Center 6](#_Toc232856924)

[3 Overview Table 8](#_Toc232856925)

[4 Test Procedures 9](#_Toc232856926)

[4.1 Create Stock Transfer Order 9](#_Toc232856927)

[4.2 Create Replenishment Delivery for Stock Transfer Order 10](#_Toc232856928)

[4.3 Print Outbound Delivery (Optional) 11](#_Toc232856929)

[4.4 Pick, Pack, and Post Goods Issue for Delivery 12](#_Toc232856930)

[4.5 Post Goods Receipt for Outbound Delivery 13](#_Toc232856931)

[5 Appendix 15](#_Toc232856932)

[5.1 Process Integration 15](#_Toc232856933)

[5.1.1 Preceding Processes 15](#_Toc232856934)

[5.1.2 Succeeding Processes 15](#_Toc232856935)

[5.1.3 Configuration (Optional) 15](#_Toc232856936)

[5.1.3.1 Output Parameter Determination 16](#_Toc232856937)

## Purpose

Overview

The stock transfer order is the basis for procurement of merchandise for the store from the distribution center. The stock transfer order is a variation of the purchase order for internal procurement. A worklist item is created based on the articles, dates, and logistical parameters. An automatic process analyzes the delivery-due list and creates the relevant outbound deliveries for processing. These outbound deliveries form the basis for the logistical processes, such as picking and optional packing. On completion, the goods issue is posted with reference to the outbound delivery. Inventory is adjusted and the financial accounts are posted. A delivery note can be printed before or after posting the goods issue. For legal requirements, you may need to attach shipping documents for goods identification for physical transport.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This chapter summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing |  |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Outbound Delivery Processing | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Materials Management - Warehouse Execution |  |  |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Retail Store Operations |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Single Article | R_1006 | My Best Frozen Strawberries |  |
| Generic Article | R_1003 | Chocolate |  |
| Sales set Article | R_1052 | My Best Blond Shampoo & Conditioner |  |
| Display Article | R_2007 | Chocolate Bar Display |  |
| Packaging Article (Material or Product) | R_CARTON | Carton |  |
| Packaging Article (Material or Product) | R_PALLET | Pallet |  |
| Packaging Article (Material or Product) | R_WIRE_BASKET | Wire Basket |  |
| Supplier (Supplying Plant) | 3350 | DC 3350 AE |  |
| Plant (Site or Location) | 3340 | Store 3340 AE |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Shipping Point | 3350 | SP DC 3350 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Company Code | 3310 | Company Code 3310 |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 5FX - Store Ordering from Distribution Center | To run through this scope item, stock transfer order must be created manually, corresponding to which replenishment delivery is created in the distribution center. |

### Preliminary Steps

#### Create Initial Stock in the Distribution Center

Use

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app.It only displays if it was your last transaction. So, the action for the user is to select Reference Document for MIGO Transaction > Other. | The Goods Receipt Other screen is displayed. |  |
| 3 | Input Movement Type | Make the following entry and select Enter :Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and select Enter:Material: R_1006 |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and select Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: <CAR> |  |  |
| 6 | Enter Information in Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and select Enter:Movement Type: 561Receipt per initial entry of stock balances into unrestricted use:Plant: 3350Storage Location: 995ANote If generic article is entered as the material then you should enter quantity in the variant matrix grid which appears on expanding the tree display for the material.Else, enter the variant article as the material for which stock needs to be created as generic articles are logical entities which are not entitled for physical stocks creation. |  |  |
| 7 | Save Your Entries | Select Post. | Material document <document number> posted success message is displayed. |  |

Result

You have created stock for the materials

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| ID (Role Template) | Name (Role Template) | App | Expected Results |
| --- | --- | --- | --- |
| [Create Stock Transfer Order](#unique_9) [page ] 9 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transfer order (STO) is created. |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_10) [page ] 10 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery document with reference to STO, is created |
| [Print Outbound Delivery (Optional)](#unique_11) [page ] 11 | Shipping Specialist | Change Outbound Delivery (VL02N) | Delivery note is manually printed out. |
| [Pick, Pack, and Post Goods Issue for Delivery](#unique_12) [page ] 12 | Shipping Specialist | Change Outbound Delivery (VL02N) | Material is picked then packed. Handling units are generated. Goods issue is posted for the Outbound Delivery. |
| [Post Goods Receipt for Outbound Delivery](#unique_13) [page ] 13 | Retail Store Associate | Receive Products (F1248) | Goods receipt is posted against the outbound delivery document. |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Create Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a stock transfer order (STO) manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | Create Purchase Order - Advanced (ME21N) app screen is displayed. |  |
| 3 | Enter Order Document Type and Other Data | Enter the following data, then select Enter:Order Type: StockTranspOrderDel or UD StockTranspOrderDelSupplying Plant: 3350On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 001In Item Overview section:Material: R_1006Plant: 3340Storage Location: 994APO Quantity: x | Data is entered. The item detail screen is displayed. |  |
| 6 | Save Stock Transfer Order | Select Save and when the stock transfer order number is displayed, note it down for further use. | A new stock transfer order is created. order number is displayed. |  |

### Create Replenishment Delivery for Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you manually create replenishment or outbound delivery with reference to stock transfer order (STO).

|  |
| --- |
| Note You can create outbound deliveries by scheduling background job which is in close alignment with the DC and their work shifts there. However, to test this scope outbound deliveries are created manually. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Orders, Fast Display screen is displayed. |  |
| 3 | Start Selection for Outbound Delivery Creation | On the entry screen of the Purchase Orders, Fast Display app, make the following entries and Select Execute:Remove Deliv. Creation Date (both from and to dates)Shipping point: 3350Go to Purchase Orders tab view, enter Purchasing Document:STO Document Number created in [Create Stock Transfer Order](#unique_9) [page ] 9. | A list of purchasing documents for the selected shipping point is displayed. |  |
| 4 | Select Purchasing Document for Outbound Delivery Creation | Mark your purchasing documents and select Background. | Outbound delivery document is created. |  |
| 5 | View the Created Outbound Delivery Document Number | Select Log for delivery creation, then select Documents on the right top of the Delivery Creation Log screen. | Outbound delivery document number is displayed. |  |

### Print Outbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to manually trigger print out of delivery note for an outbound delivery.

|  |
| --- |
| Note Delivery notes (shipping documents) can be printed for an outbound delivery before goods issue. A delivery note normally contains the delivery note number, the delivery date, the ship-to party and the individual delivery items. The creation of this document is set up automatically in background, but it is also possible to trigger the delivery note printing manually. You must execute this process step if Output Type is set-up. For more information, see [Output Parameter Determination](#unique_15) [page ] 16 chapter of this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. |  |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter <your Delivery Number> and select Continue.On the Replenishment Dlv. XXXXXXXX Change: Overview screen, select Menu > Extras > Delivery Output > Output Control. | The Replenishment Dlv.: Outputscreen is displayed. |  |
| 4 | Print Preview | On the Replenishment Dlv.: Output screen, select the line with the DELIVERY_NOTE output type and select Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | Select Print from preview of the document. | The delivery note is printed. |  |

### Pick, Pack, and Post Goods Issue for Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you pick and pack materials to create handling units and post the goods to remove them from the distribution center's inventory management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N) app. |  |  |
| 3 | Open Outbound Delivery Document | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and select Continue. |  |  |
| 4 | Specify Picked Quantity | Go to Picking tab and specify: Picked Qty : <Enter quantity equal to delivery quantity> | Picked quantity is updated. |  |
| 5 | Save the Outbound Delivery Document | Select Save. | Outbound delivery document is saved. |  |
| 6 | Open Outbound Delivery Document Again | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and select Pack. |  |  |
| 7 | Enter Packaging Material | On the Processing of Handling Units for Outbound Delivery <Outbound Delivery Number> screen, under the Pack Material tab and under All Existing HUs (Available for Packing ), enter <Your packaging Material> in the Packaging Materials column. | Handling units are generated. |  |
| 8 | Pack Material with Packaging Material | Mark the material and handling unit line items under Materials to Be Packed and All Existing HUs (Available for Packing) sections, respectively. Select Pack. | The message for material is packed is displayed. |  |
| 9 | Save the Outbound Delivery Document | Select Save. | Outbound delivery document is saved. |  |
| 10 | Post Goods Issue | On the Change Outbound Delivery (VL02N) app screen, enter <your outbound delivery document number> and select Post Goods Issue. | Goods issue is successful. Inventory stock is reduced from the supplying plant. |  |

### Post Goods Receipt for Outbound Delivery

|  |
| --- |
| Note This process step of posting goods receipt in store is optional here as this is also part of the scope of 5FY - In-Store Purchase Order Management. So, you can do posting of goods receipt in store while going through the scope of 5FY - In-Store Purchase Order Management. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you match the receipt of goods in the store to the outbound delivery you created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Retail Store Associate. |  |  |
| 2 | Access the Application | Open Receive Products (F1248) app.Note In case user does not have store assignment, you get pop up to navigate to assign store app. Make sure that store 3340 is assigned to store associate user in My Store Assignment (F4334) app. | The Post Goods Receipt app screen is displayed. |  |
| 3 | Enter Outbound Delivery Number | Select Enter ID.In the Find a Document pop-up <Enter Outbound Delivery Number Created earlier>Select OK. | The selected outbound delivery details are displayed. |  |
| 4 | Check and Post the Goods Receipt for Outbound Delivery | In the Product section, toggle Checked on the bottom right of the screen. Select Post. | Document item was posted successfully message is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 5FX - Store Ordering from Distribution Center | To run through this scope item, stock transfer order must be created manually, corresponding to which replenishment delivery is created in the DC. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Not Applicable |  |

#### Configuration (Optional)

Prerequisite

To carry out the following activity, a business user with a business role must exist. The business role must contain the business catalog SAP_CA_BC_OC_PC (Output Management - Output Control), for example, the business role SAP_BR_CONF_EXPERT_BUS_NET_INT (Configuration Expert - Business Process Configuration).

##### Output Parameter Determination

Use

This document describes additional configuration step that must be carried out from the Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app, by customers to add and activate the output type required to trigger printing of delivery note from the Change Outbound Delivery (VL02N) app, as described in Chapter [Print Outbound Delivery (Optional)](#unique_11) [page ] 11 of this document.

Procedure

1. Log on to the SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system.
2. Navigate to Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app.
3. In the Select Business Rules section, enter Show rules for: Outbound Delivery and Determination Step: Output Type.
4. In the Maintain Business Rules section, select Edit then select +.
5. Enter Delivery Type: <Blank or your Outbound Delivery Type> by selecting Direct Value Input from the Delivery Type column dropdown list then enter the relevant value and select OK .
6. Enter Document Cat.: J(Delivery)by selecting Direct Value Input from the Document Cat. column in dropdown list then enter the value and select OK.
7. Scroll right to find the Output Type column, enter Output Type : DELIVERY_NOTE by selecting Direct Value Input from the Output Type column in dropdown list then enter the value and select OK.
8. Enter Dispatch Time: 1 (Immediately) by selecting Direct Value Input from the Dispatch Time column in dropdown list then then enter the value and select OK.
9. Select the row and select Activate.
10. Select Yes on the Confirm Activation pop-up to confirm the activation of the entry.

Result

You have activated the output type for your outbound delivery document type.

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
> Flagged while digesting this document, not verified: Initial stock is posted to storage location 995A while the sample data and the STO use storage location 994A for the supplying side, which may be an internal inconsistency.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[15-retail-operations/test-script-store-ordering-from-distribution-center-5fx-ae-1092]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FV_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 25,456 chars in the whole document
