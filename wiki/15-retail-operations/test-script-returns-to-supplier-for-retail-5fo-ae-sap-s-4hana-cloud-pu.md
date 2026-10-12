---
id: 15-retail-operations/test-script-returns-to-supplier-for-retail-5fo-ae-sap-s-4hana-cloud-pu
title: "Test Script: Returns to Supplier for Retail (5FO_AE) - SAP S/4HANA Cloud Public Edition (5FO_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 5FO_AE: retail returns to supplier, from returns PO to delivery, goods issue, then credit memo or replacement."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-procurement-and-invoice-verification]
aliases: [5FO_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Procurement, Invoice Verification and Supplier…", returns to supplier, returns purchase order, outbound delivery, goods issue, credit memo, replacement material, goods receipt, invoice verification, return reasons]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1084
topic: 15-retail-operations/retail-procurement-and-invoice-verification
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Returns to Supplier for Retail (5FO_AE) - SAP S/4HANA Cloud Public Edition (5FO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Procurement, Invoice Verification and Supplier Returns** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Returns to Supplier for Retail (5FO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856711)

[2 Prerequisites 4](#_Toc232856712)

[2.1 System Access 4](#_Toc232856713)

[2.2 Roles 4](#_Toc232856714)

[2.3 Master Data, Organizational Data and Other Data 5](#_Toc232856715)

[2.4 Business Conditions 5](#_Toc232856716)

[2.5 Preliminary Steps 6](#_Toc232856717)

[2.5.1 Return Reason “Wrong Product Delivered” 6](#_Toc232856718)

[2.5.2 Return Reason “Too much Delivered” 6](#_Toc232856719)

[2.5.3 Return Reason “Product Damaged” 6](#_Toc232856720)

[2.5.4 Return Reason “Product Defective” 6](#_Toc232856721)

[2.5.5 Stock Overview Analysis (Optional) 7](#_Toc232856722)

[2.5.6 Set Stock for Material (Optional) 7](#_Toc232856723)

[2.5.7 Stock Transfer (Optional) 8](#_Toc232856724)

[2.5.8 Analyse Stock Overview (Optional) 9](#_Toc232856725)

[2.5.9 Determine Output Parameter 10](#_Toc232856726)

[3 Overview Table 12](#_Toc232856727)

[4 Test Procedures 13](#_Toc232856728)

[4.1 Create Returns Purchase Order 13](#_Toc232856729)

[4.2 Monitor Returns Purchase Order 14](#_Toc232856730)

[4.3 Create Outbound Delivery 15](#_Toc232856731)

[4.4 Pick and Post Goods Issue 16](#_Toc232856732)

[4.5 Create Credit Memo (Option 1) 17](#_Toc232856733)

[4.6 Receive Replacement Material (Option 2) 19](#_Toc232856734)

[4.6.1 Post Goods Receipt 20](#_Toc232856735)

[4.6.2 Follow-Up Activities for Replacement Material 21](#_Toc232856736)

[4.6.3 Check Invoice Document 22](#_Toc232856737)

[5 Appendix 24](#_Toc232856738)

[5.1 Process Integration 24](#_Toc232856739)

[5.1.1 Preceding Processes 24](#_Toc232856740)

## Purpose

Overview

Returning merchandise to external suppliers is a regular process for a retailer. It’s important that the process can be executed as automatically and flexibly as possible to meet the requirements of each supplier. Returns can be initiated by different business situations, such as an agreement that the unsold quantities can be returned at the end of season, or the need to return spoiled, broken, or poor quality articles.

The return process begins with the creation of a return purchase order and is followed by the generation of an outbound delivery. The items are then picked and shipped to the supplier. The process is finalized with the creation of a credit memo, which transfers the liability to the corresponding supplier.

Returns management provides end-to-end support for both simple and complex returns scenarios by integrating all the necessary steps.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Operational Purchasing | SAP_BR_PURCHASER_RFM |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM | Retail Inventory Management | SAP_BR_INVENTORY_MGR_RFM |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK_RFM |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Article | R_2005 | Showergel with caffeine, 200 ml |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Plant | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Storage Location | 995R | St.Loc.Return |  |
| Sales Set | R_1052 | My Best Blond Shampoo & ConditionerComponents:R_1051 and R_1050 |  |

### Business Conditions

Not applicable while using the sample data provided in chapter [Master Data, Organizational Data and Other Data](#unique_5) [page ] 5

| Scope Item | Business Condition |
| --- | --- |
| 5FU - Inbound Logistics for Distribution Centers | To run through the scope of Returns to Supplier, the material must be available in stock. If you use trading goods (HAWA) you can either:Run through the Inbound Logistics for Distribution Centers (5FU) test script process.OrCreate stock using Post Goods Movement (MIGO) app (for details see chapters Preliminary Steps)Transfer the stock to return storage location using Transfer Stock - In-Plant (F1061) app (for details see chapters Preliminary Steps) |

### Preliminary Steps

#### Return Reason “Wrong Product Delivered”

During the goods receipt process the warehouse clerk detects that wrong material was delivered. Therefore the material was posted into the blocked stock and moved into the restricted – use stock

This situation can be the result of chapter Post Goods Receipt for Inbound Delivery in scope item 5FU.

#### Return Reason “Too much Delivered”

During the goods receipt process the warehouse clerk detects that too many materials were delivered. Therefore the additional material was posted into the blocked stock and moved into the storage location for returns

This situation can be the result of chapter Post Goods Receipt for Inbound Delivery in scope item 5FU.

#### Return Reason “Product Damaged”

During the goods receipt process the warehouse clerk detects that the product was damaged during the transit. Therefore the material was posted into the blocked stock and moved into the storage location for returns.

This situation can be the result of chapter Post Goods Receipt for Inbound Delivery in scope item 5FU.

#### Return Reason “Product Defective”

During the goods receipt process, the warehouse clerk detects that defective product was supplied and hence the quality inspection failed. Therefore, the material was posted into return stock with status blocked.

This situation can be the result of chapter Post Goods Receipt for Inbound Delivery in scope item 5FU.

#### Stock Overview Analysis (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check stock of the material at storage location and stock type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori Launchpad as Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Stock - Single Material (F1076) app. | The Stock - Single Material (F1076) screen is displayed. |  |
| 3 | Enter material | Make the following entries:Material: R_2005Choose Enter | Reviewing stock requirements helps to analyse and determine if stock for particular material sufficient or perform addition of stock through chapter [Set Stock for Material (Optional)](#unique_12) [page ] 7. |  |

#### Set Stock for Material (Optional)

Purpose

In this activity, you can add sufficient stock to the material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The action which was chosen last time is displayed. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | Goods Receipt Other-<UserName> screen is displayed |  |
| 4 | Enter Material | Close the header data and expand the detail data area. On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: R_2005 | Material details are provided. |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: 100Unit of Entry: <PC> | Quantity details are provided. |  |
| 6 | Enter details under Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant : 3350Storage Location: 995A | Movement type, plan and storage location details are provided. |  |
| 7 | Save Your Entries | Choose Post. | Material document posted message is displayed |  |

#### Stock Transfer (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to be used if business requirements exist to move inventory (physically and in the system) from a standard storage location to the return storage location of distribution center.

Please use option “Add Storage Location” to add Storage Location 995R if the storage location is not visible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk (Retail) |  |  |
| 2 | Access the SAP Fiori App | Open Transfer Stock - In-Plant (F1061) app. | The Transfer Stock - In-Plant (F1061) screen is displayed. |  |
| 3 | Input material | Make the following entries.Plant: 3350Material: R_2005Press Enter | Material details are provided. |  |
| 4 | Choose the source stock | In the line of Std. storage 1 (995A) , choose the icon beside the quantity of Unrestricted-Use Stock. | The icon is highlight.For performing this you should use buttons with arrows near the unrestricted-use stock figures. |  |
| 5 | Choose the destination stock | In the line of Returns (995R), choose the icon beside the quantity of Unrestricted-Use Stock. | Transfer Stock screen is displayed. |  |
| 6 | Input the quantity for material | Input value in the dialog box:Quantity: XX |  |  |
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

You can use this step to see stock for material in the storage locations of a plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Stock - Single Material (F1076) app. | The Stock - Single Material (F1076) screen is displayed. |  |
| 3 | Enter material | Make the following entry:Material: R_2005Choose Enter. | The system is displayed stock for the material in plant 3350 on the different storage locations. |  |

#### Determine Output Parameter

Before you can test this scope item, you must complete the following additional configuration. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you.

Below mentioned configurations needs to be maintained in Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app for electronic data interchange (EDI) message Output.

Procedure:

1. Log on to the SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system.
2. Navigate to App Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN).
3. Enter Show rules for: Purchase Order and Determination Step: Channel.
4. Go to section “Maintain Business Roles”, choose “Edit”
5. Go to section “Table Contents”, choose “+” (Insert New Row)
6. Go to column “Output Type”, choose “Direct Value Input”
7. Enter “is equal to”, “PURCHASE_ORDER”, choose “OK”
8. Go to column “Role”, choose “Direct Value Input”
9. Enter “is equal to”, “LF”, choose “OK”
10. Go to column “Channel”, choose “Direct Value Input”
11. Enter “is equal to”, “EDI”, choose “OK”
12. Go to section “Maintain Business Roles”, choose “Activate”

For each supplier to whom you would like to send purchase orders via EDI, create an entry such as the one below:

| Output Type | Role | Recipient | Channel |
| --- | --- | --- | --- |
| PURCHASE_ORDER | LF |  | EDI (EDI) |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Purchase Order](#unique_17) [page ] 13 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Return purchase order is created. |
| [Monitor Returns Purchase Order](#unique_18) [page ] 14 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Processing status of return purchase order turns green. |
| [Create Outbound Delivery](#unique_19) [page ] 15 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery created. |
| [Pick and Post Goods Issue](#unique_20) [page ] 16 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post goods issue posted. |
| [Create Credit Memo (Option 1)](#unique_21) [page ] 17 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Credit memo is posted. |
| [Receive Replacement Material (Option 2)](#unique_22) [page ] 19 | Receiving Specialist | Receive Replacement Materials - From Vendor (MSR_VRM_GR) | The replacement purchase order is created. |
| [Post Goods Receipt](#unique_23) [page ] 20 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt for inbound delivery is posted. |
| [Follow-Up Activities for Replacement Material](#unique_24) [page ] 21 | Receiving Specialist | My Follow-Up Activities - For Replacement Materials (MSR_VRM_LFU) | The follow up activity for replacement material is initiated. |
| [Check Invoice Document](#unique_25) [page ] 22 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | The invoice document number is displayed. |

## Test Procedures

This chapter describes procedures for each process step that belongs to this scope item.

### Create Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process returns purchase order to supplier is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app | Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Enter Parameters | Select Order type: Enh.Ret.to Supplier from dropdown listEnter the following details:Supplier: 33213001Doc.Date: <Current Date>Select Org.Data tab and enter below details:Purch. Org: 3310Purch. Group: 001Company Code: 3310 |  |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_2005PO Quantity: 2Deliv. Date: <Provide any future date>Plant: 3350 |  |  |
| 5 | Enter Parameters | Select Returns tab in the Header sectionFrom the Return Reason drop down list, select Product damagedFrom the Follow-Up-Activity drop down list, select Ship to SupplierChoose Copy to Items. | Item level the Returns Item flag is set. |  |
| 6 | Save Returns Purchase Order | Choose Save. | Return Purchase order is created.Make a note of return purchase order. |  |

### Monitor Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process returns purchase order is monitored.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. | Display Purchase Order - Advanced (ME23N) screen is displayed. |  |
| 3 | Access Return Purchase Order | Choose Document Overview OnFrom the Selection Variants dropdown list, select Purchase Orders | Purchasing Document screen is displayed |  |
| 4 | Access Returns Purchase Order | In the Program Selections section, enter below details:Purchasing Document : <Returns Purchase Order>Choose Execute. | Purchase order is displayed in the Document overview section. |  |
| 5 | Select Return Purchase Order | Select Return Purchase orderChoose Adopt. | Return purchase order is displayed. |  |
| 6 | Check Returns Overview | Choose Returns Tab,Choose Returns Overview. | Returns Overview for Returns Purchase Order xxxxxxxxxx screen is displayed. |  |
| 7 | Check Processing Status | Check Processing Status. | Processing Status is displayed as Process Incomplete. |  |
| 8 | Check Return Steps | In the Detail Tree sectionCheck Return Purchase Order status in Return Steps Column. | Processing status is green. |  |

### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process outbound delivery for the returns purchase order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Order s, Fast Display screen is displayed. |  |
| 3 | Enter Parameters | Enter below detail,CalcRuleDefltDlvCrDt: <blank>Choose Purchase Orders and enter below detail,Purchasing Document: <Returns Purchase Order>Choose Execute. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. |  |
| 4 | Create Outbound Delivery | Select Return Purchase OrderChoose Background. | See Log for information about creating deliveries message is displayed. |  |
| 5 | Check the Outbound Delivery Number | Choose the newly created line item with the same Return Purchase Order entryFrom the <!-- image omitted: unnamed -->(More) icon drop down list, select Show/Hide Delivery. | Outbound Delivery number xxxxxxxx is displayed in the Document coloumn.Make a note of outbound delivery number. |  |

### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process post goods issue for the returns purchase order is initiated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery : <Outbound Delivery number>Choose Continue. | RTS Outbound Dlv. XXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Enter the Picked Quantity | Choose PickingIn the All Items section,Enter the below field as value in Deliv.Qty ,Picked Qty : <Deliv.Qty>Press Enter. | OvrllPickStatus is displayed as C (Fully Picked). |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | RTS Outbound Dlv. XXXXXXXX saved, material document XXXXXXXXXX created message is displayed. |  |

### Create Credit Memo (Option 1)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process invoice to the returns purchase order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO) app | Enter Company Code pop up is displayed. |  |
| 3 | Enter Company Code | Enter below detail,Company Code :3310Choose Continue. | Enter Incoming Invoice : Company Code 3310 screen is displayed. |  |
| 4 | Select Credit Memo | From the Transaction drop down list, select Credit Memo | Credit Memo is selected |  |
| 5 | Enter Reference Purchase Order | In the Basic Data section, enter the below detailsReference: <Return Purchase Order Number>Document date: <Current Date>Under the Details tab, select the corresponding document type in the Doc. Types field.In the PO Reference section,Select Purchase Order/Scheduling Agreement from the drop down listEnter below detail:Purchasing Document: <Return Purchase Order Number>Press Enter | Details of the reference purchase order is displayedAmount auto populate in Balance. |  |
| 6 | Enter Amount | In the Basic Data sectionEnter the amount in the below field to maintain the balance amount as 0.00,Note Calculate and enter the amount to make the balance zero.Amount: XXXXSelect V0 from the dropdown list.Flag Calculate TaxPress Enter | Balance amount display as 0.00 |  |
| 7 | Save the Document | Choose Post. | Document.no: XXXXXXXXXX created message is displayed |  |
| 8 | Monitor Returns Purchase Order | See chapter [Monitor Returns Purchase Order](#unique_18) [page ] 14. | Supplier invoice is displayed in Detail tree section.Processing Status in Header section is displayed as Completed. |  |

### Receive Replacement Material (Option 2)

If the credit memo is created, and supplier will not deliver the replacement material, then please skip the steps under Receive Replacement Material (Option 2). The receive replacement material related steps are only optional and not the standard case.

Repeat steps described under 4.1. – 4.4 and in [Create Returns Purchase Order](#unique_17) [page ] 13 chapter check Flag Replacement Material Requested in Return tab on creating return purchase order.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you receive the replacement materials from supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist |  |  |
| 2 | Access the App | Open Receive Replacement Materials - From Vendor (MSR_VRM_GR) app. | Supplier Replacement Material-Document Selection dialog box is displayed. |  |
| 3 | Enter Parameters | Enter the following entries:Returns Purchase Order Type: <NB2>Returns Purchase Order: <Returns Purchase Order>Choose Execute | Receive Replacement Materials - From Vendor (MSR_VRM_GR) screen is displayed. |  |
| 4 | Choose Return Purchase Order | Expand Supplier /Purchase Order/Item on the left screen,double click the Item Number . | Return purchase order details displayed. |  |
| 5 | Enter Parameters | In the Replacement section,enter following details:Replacement Quantity: <PO Quantity in Return Purchase Order>Replacement Quantity must be the same with Quantity for Returns Purchase Order. | The replacement quantityhas been entered |  |
| 6 | Go to Goods Movement | In the Goods Movement section, enter following details:Receiving Stor.Loc : 995RChoose Stock Type as S (Block stock) . | The Receiving Storage Location and Stock Type have been entered. |  |
| 7 | Save | Choose Save. | Replacement purchase order xxxxxxxxxx created.Make note of replacement purchase order. |  |
| 8 | Check the Inbound Delivery of Replacement Material Number | Choose Menu > Goto > Post Goods Receipt . | The inbound delivery xxxxxxxx of replacement material is automatically created.Make a note of inbound delivery. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you specify put away quantity and post goods receipt for inbound delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N) app | Change Inbound Delivery (VL32N) screen is displayed. |  |
| 3 | Enter inbound delivery number | Enter the following detail:Inbound Delivery : <Inbound Delivery Number> | Change Inbound Delivery XXXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Qty | In the Item overview sectionEnter the following detail:Putaway Qty: <Delivery Qty> | The Putaway Qty has been entered. |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt | Goods Receipt for inbound delivery posted message is displayed. |  |

#### Follow-Up Activities for Replacement Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you set follow-up activity for the replacement material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open My Follow-Up Activities - For Replacement Materials (MSR_VRM_LFU) app. | Document Selection of Inbound Deliveries screen is displayed. |  |
| 3 | Maintain Selection Criteria | Enter the following details:Deliveries without confirmed logistical follow-up activity: SelectedShow all items of selected deliveries: SelectedDelivery: <Inbound Delivery number>Choose Execute | The inbound delivery is selected |  |
| 4 | Enter Follow-Up Activity | In the Logistical Follow-Up section, enter following detail:From the Follow-Up Activity drop down list,select 0011 Transfer to Free Available Stock | Follow-up activity details are provided. |  |
| 5 | Save | Choose Save and Confirm within the header menu.Choose Continue to confirm the Information screen. | Logistical follow-up activity has been saved message is displayed. |  |

#### Check Invoice Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you check the document in Invoice Verification that the system has created automatically after the goods receipt for the replacement purchase order has been posted. This document represents a credit memo of value 0 for the returns purchase order and an invoice of value 0 for the replacement purchase order. The document is required to balance the GR/IR clearing account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). |  |  |
| 2 | Access App | Open Display Purchase Order - Advanced (ME23N) app. | Display Purchase Order - Advanced (ME23N) screen is displayed. |  |
| 3 | Access Returns Purchase Order | Choose Document Overview OnFrom the Selection Variants dropdown list, select Purchase Orders | Purchasing Document screen is displayed |  |
| 4 | Access Return Purchase Order | In the Program Selections section, enter below details:Purchasing Document : <Returns Purchase Order>Choose Execute. | Purchase order is displayed in the Document overview section. |  |
| 5 | Select Return Purchase Order | Select Return Purchase orderChoose Adopt. | Return purchase order is displayed. |  |
| 6 | Check Returns Overview | Choose Returns Tab,Choose Returns Overview | Returns Overview of Return Purchase Order xxxxxxxxxx screen is displayed. |  |
| 7 | Check Invoice | In the Detail Tree sectionIn Document Number column, Check the Invoice number against Invoice Verification. | The system automatically creates a document in Invoice Verification that serves both as a credit memo and an invoice with value 0. |  |
| 8 | Check Processing status | Check Processing Status | Processing Status is displayed as Complete. |  |
| 9 | Check Return Steps | In the Detail Tree sectionCheck statusof documents in Return Steps Column | Processing Status of all documents is green. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can precede this process.

| Scope Item | Business Condition |
| --- | --- |
| 5FM - Procurement for Retail | This scope item Purchase Requisition generated for external supplier is converted into a purchase order |
| 5FU - Inbound Logistics for Distribution Centers | This scope item perform creation of inbound delivery and goods receipt at distribution center |

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
- related-to :: [[15-retail-operations/invoice-verification-for-retail-5fn-ae-test-script-sap-s-4hana-cloud-p]]
- related-to :: [[15-retail-operations/test-script-procurement-for-retail-5fm-ae-sap-s-4hana-cloud-public-edi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 37,415 chars in the whole document
