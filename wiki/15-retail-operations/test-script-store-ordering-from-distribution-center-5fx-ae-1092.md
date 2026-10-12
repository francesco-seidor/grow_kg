---
id: 15-retail-operations/test-script-store-ordering-from-distribution-center-5fx-ae-1092
title: "Test Script: Store Ordering from Distribution Center (5FX_AE) (5FX_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5FX: stores ordering from distribution centers via stock transport orders and advanced intercompany stock transfer."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/store-ordering-from-dc]
aliases: [5FX_S4CLD2608_BPD_EN_AE]
keywords: [Store Ordering from Distribution Centers, stock transport order, stock transport requisition, automatic order conversion, intercompany stock transfer, outbound delivery, goods in transit, intercompany billing, pro forma invoice, goods issue]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FX_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1092
topic: 15-retail-operations/store-ordering-from-dc
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Store Ordering from Distribution Center (5FX_AE) (5FX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Store Ordering from Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Store Ordering from Distribution Center (5FX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856889)

[2 Prerequisites 4](#_Toc232856890)

[2.1 System Access 4](#_Toc232856891)

[2.2 Roles 4](#_Toc232856892)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856893)

[2.4 Additional Manual Configuration 7](#_Toc232856894)

[2.5 Business Conditions 7](#_Toc232856895)

[2.6 Preliminary Steps 7](#_Toc232856896)

[2.6.1 Creation of Stock Transport Requisition 7](#_Toc232856897)

[2.6.2 Create Stock in Supplying Plant 8](#_Toc232856898)

[2.6.3 Stock Availability Check using Display Advanced Stock Overview 9](#_Toc232856899)

[2.6.4 Stock Availability Check using Monitor Stock/Requirements List application [Optional] 9](#_Toc232856900)

[2.6.5 Create Condition Records 10](#_Toc232856901)

[3 Overview Table 11](#_Toc232856902)

[4 Test Procedures 13](#_Toc232856903)

[4.1 Stock Transport Order is Created with a Reference to a Stock Transport Requisition 13](#_Toc232856904)

[4.2 Stock Transport Requisitions are Automatically Converted into Stock Transport Orders 14](#_Toc232856905)

[4.3 Create Stock Transport Order 15](#_Toc232856906)

[4.4 Advanced Intercompany Stock Transfer 17](#_Toc232856907)

[4.4.1 Create Intercompany Stock Transfer Order 17](#_Toc232856908)

[4.4.2 Create Pro Forma F5 Invoice (Optional) 19](#_Toc232856909)

[4.4.3 Create Outbound Delivery for Stock Transfer Order 20](#_Toc232856910)

[4.4.4 Pick and Post Goods Issue for Outbound Delivery 21](#_Toc232856911)

[4.4.5 Confirm Internal Transfer of Control Date for Goods in Transit 22](#_Toc232856912)

[4.4.6 Create Pro Forma F8 Invoice (Optional) 24](#_Toc232856913)

[4.4.7 Confirm Quantities for Inbound Delivery 25](#_Toc232856914)

[4.4.8 Post Goods Receipt for Inbound Delivery 26](#_Toc232856915)

[4.4.9 Create Intercompany Billing Document 27](#_Toc232856916)

[4.4.10 Display Supplier Invoice 29](#_Toc232856917)

[4.4.11 Monitor Intercompany Stock Transfer Value Chain 30](#_Toc232856918)

[4.4.11.1 Display Intercompany Stock Transfer Value Chain 30](#_Toc232856919)

[4.4.11.2 Display Intercompany Sales Order 31](#_Toc232856920)

[4.4.11.3 Display Intercompany Goods in Transit Document 33](#_Toc232856921)

[4.4.11.4 Display Inbound Delivery 34](#_Toc232856922)

[4.4.11.5 Display Post Stock Transfer into Physical Stock 35](#_Toc232856923)

[5 Appendix 36](#_Toc232856924)

[5.1 Process Integration 36](#_Toc232856925)

[5.1.1 Preceding Processes 36](#_Toc232856926)

[5.1.2 Succeeding Processes 36](#_Toc232856927)

## Purpose

Overview

Stores procure their merchandise either directly from external suppliers or from distribution centers. When stores procure their merchandise from distribution centers, the procurement document is created in the form of a stock transfer order or stock transport order. The procurement process is supported in scenarios where the store and the distribution center operate in the same or a different company code (advanced intercompany process). Both process variants are supported. Typically, the demand of the store is determined automatically by the replenishment planning application, resulting in a creation of stock transfer requisitions. The conversion from a stock transfer requisition to a stock transport order can be done manually or automatically (applicable for large volumes). Alternatively, you can create transport orders manually.

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
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Purchasing | SAP_BR_PURCHASER_RFM |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In this master data sheet, we take United States as an example as the supplier for advanced intercompany stock transfer process. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1710 | Company Code 1710 |  |
| Plant | 3342 | Store 3342 AE |  |
| Plant | 1750 | DC Newtown Square |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Shipping Point | 1750 | SP DC 1750 |  |
| Purchase Group | 002 | Group 002 |  |
| Sales Organization | 1710 | Dom. Sales Org US |  |
| Distribution Channel | 50 | Distribution |  |
| Supplier | 1750 | DC Newtown Square |  |
| Material | R_3018 | Gas Grill 3-Burner Black |  |
| Supplier Invoicing Party | 17401710 | Representing Supplier in Company Code 1010 |  |
| Inter-Company Sold to Party | 3342 | Store 3342 AE |  |
| Inter-Company Bill-to Party | 33401010 |  |  |
| Supplier | 3350 | DC 3350 AE |  |
| Plant | 3340 | Store 3340 AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purch. Org | 3310 | Purch. Org. 3310 |  |
| Purch. Group | 001 | Group 001 |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Material, Single article | R_2003 | Organic Low fat milk, 1,5 % |  |
| Material, Variant Article | R_1004003 | My Best Chocolat, Christmas Flavor, Diet |  |
| Display | R_2007 | Chocolate Bar DisplayComponents:R_1003001R_1003002R_1003003R_1003004R_1003005R_1003006R_1003007R_1003008R_1003009R_1003010R_1003011R_1003012R_1003013R_1003014 |  |
| Sales Set | R_1052 | My Best Blond Shampoo & ConditionerComponents:R_1052 and R_1051 |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3f7d22ed8c8aa5ca116de0e1a0d34bcc)

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 3I7 - Replenishment Planning for Stores | Complete all relevant steps. |

### Preliminary Steps

This chapter provides an overview of detailed technical steps and other relevant prerequisites.

#### Creation of Stock Transport Requisition

In this process you can check the below scope item for automatic creation of stock transport requisition,

You can use this stock transport requisition to perform chapter [Stock Transport Order is Created with a Reference to a Stock Transport Requisition](#unique_10) [page ] 13 & [Stock Transport Requisitions are Automatically Converted into Stock Transport Orders](#unique_11) [page ] 14

| Scope Item | Description |
| --- | --- |
| 3I7 | Replenishment Planning for Stores |

#### Create Stock in Supplying Plant

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The action which was chosen last time is displayed. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | Movement type details are provided. |  |
| 4 | Enter Material | Close the header data and expand the detail data area. On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: R_2003 | Material details are provided. |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: 100Unit of Entry: <PC> | Quantity details are provided. |  |
| 6 | Enter details under Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant 3350Storage Location: 995A | Movement type, Plan and storage location details are providedSame as abovemodified. |  |
| 7 | Save Your Entries | Choose Post. | Material document posted message displays.same as aboveupdated. |  |

#### Stock Availability Check using Display Advanced Stock Overview

Purpose

In this process step you can check the stock availability in Distribution center.

This is a prerequisite for chapter [Create Stock Transport Order](#unique_14) [page ] 15.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as an Allocator (Retail) |  |  |
| 2 | Access the App | Open Display Advanced Stock Overview (RWBE) app. | The Stock Overview screen is displayed. |  |
| 3 | Enter parameters | Enter the following data:Material: R_2003Plant: 3350Choose Execute | Stock Overview:Full List screen is displayed |  |
| 4 | Verify Stock | Select the drop down for Storage Location:995A and check the quantities displayed under Unrestricted use. | Unristricted Use Stock is displayed |  |

#### Stock Availability Check using Monitor Stock/Requirements List application [Optional]

Purpose

In this process step you can check the stock availability in distribution center.

This is a prerequisite for chapter [Create Stock Transport Order](#unique_14) [page ] 15.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Replenishment Specialist - Distribution Center (Retail) |  |  |
| 2 | Access the App | Navigate to Monitor Stock / Requirements List - Old Version (MD04) app | Monitor Stock / Requirements List - Old Version (MD04) Initial screen is displayed |  |
| 3 | Enter the Parameters | On the Stock/Requirements List: Initial Screen make the following entries:Material: R_2003Plant: 3350Choose Continue | Stock/Requirements List as of XX: XX hrs is displayed |  |
| 4 | Verify Stock | Check the stock displayed under Available Qty. | Available quantity is displayed |  |

#### Create Condition Records

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps that are listed in the following table: Subsequent steps of out creation of Outbound Delivery, Pick, Pack, PGI, PGR have been covered in the another scope item which can be seen in the succeeding processes.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Stock Transport Order is Created with a Reference to a Stock Transport Requisition](#unique_10) [page ] 13 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transport order is created with reference to stock transport requisition |
| [Stock Transport Requisitions are Automatically Converted into Stock Transport Orders](#unique_11) [page ] 14 | Purchaser (Retail) | Schedule Purchasing Jobs (F1702) | Stock transport order will be generated. |
| [Create Stock Transport Order](#unique_14) [page ] 15 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | Stock transport order is created manually |

Table 3: Advance Intercompany Stock Transfer

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Intercompany Stock Transfer Order](#unique_18) [page ] 17 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | A Stock transfer Order is created |
| [Create Pro Forma F5 Invoice (Optional)](#unique_19) [page ] 19 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing Document is created |
| [Create Outbound Delivery for Stock Transfer Order](#unique_20) [page ] 20 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound Delivery is created |
| [Pick and Post Goods Issue for Outbound Delivery](#unique_21) [page ] 21 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods Issue is posted |
| [Confirm Internal Transfer of Control Date for Goods in Transit](#unique_22) [page ] 22 | Shipping Specialist | Change Outbound Delivery (VL02N) | Actual planned date is maintained |
| [Create Pro Forma F8 Invoice (Optional)](#unique_23) [page ] 24 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing Document is created |
| [Confirm Quantities for Inbound Delivery](#unique_24) [page ] 25 | Receiving Specialist | Change Inbound Delivery (VL32N) | Putaway quantity is maintained |
| [Post Goods Receipt for Inbound Delivery](#unique_25) [page ] 26 | Receiving Specialist | Change Inbound Delivery (VL32N) | Goods receipt is posted |
| [Create Intercompany Billing Document](#unique_26) [page ] 27 | Billing Clerk | Create Billing Documents (F0798) | Billing Document is created |
| [Display Supplier Invoice](#unique_27) [page ] 29 | Accounts Payable Accountant | Monitor Value Chains (F4854) | The Supplier Invoice is displayed |
| [Display Intercompany Stock Transfer Value Chain](#unique_28) [page ] 30 | Internal Sales Representative | Monitor Value Chains (F4854) | Process Flow of Advanced Intercompany Stock Transfer Process is displayed |
| [Display Intercompany Sales Order](#unique_29) [page ] 31 | Internal Sales Representative | Monitor Value Chains (F4854) | Sales Order document created as part of Advanced Intercompany Stock Transfer Process is displayed |
| [Display Intercompany Goods in Transit Document](#unique_30) [page ] 33 | Shipping Specialist | Monitor Value Chains (F4854) | Goods in Transit document created as part of Advanced Intercompany Stock Transfer Process is displayed |
| [Display Inbound Delivery](#unique_31) [page ] 34 | Purchaser (Retail) | Monitor Value Chains (F4854) | Inbound Delivery document created as part of Advanced Intercompany Stock Transfer Process is displayed |
| [Display Post Stock Transfer into Physical Stock](#unique_32) [page ] 35 | Internal Sales Representative | Monitor Value Chains (F4854) | Intercompany Purchase Order document created as part of Advanced Intercompany Stock Transfer Process is displayed |

## Test Procedures

This chapter describes procedures for each process step that belongs to this scope item.

### Stock Transport Order is Created with a Reference to a Stock Transport Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a stock transport order with reference to stock transport requisition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Switch on Document Overview | Choose Document Overview On. | A panel is displayed on the left side of page with an option to select the Variant. |  |
| 4 | Select Variant as Purchase Requisition | From the Selection Variant , Select Purchase Requisitions. | Purchase Requisitions screen is displayed. |  |
| 5 | Enter Parameters | Enter the below dataPurchase Requisition Number: <XXXXXXXX> Enter Stock Transport Requisition created using scope item Replenishment Planning for Stores (3I7) as mentioned in CHeck the Master Data SettingsChoose Execute. | Create Purchase Order screen is displayed. |  |
| 6 | Access the Stock Transport Requisition | Choose checkbox beside the Purchase Requisition Number.Choose Adopt. | Details of the stock transport requisition is displayed. |  |
| 7 | Select Order Type | Select UD - StockTranspOrderDel from Order Type dropdown list,Choose EnterNote Please don’t use Stock Transp. Order (UB) | StockTranspOrderDel is selected as order type. |  |
| 8 | Save the Stock Transport Order | Choose Save. | StockTranspOrderDel created under the number XXXXXXXXXX message is displayed.Make a note of the stock transport order. |  |

### Stock Transport Requisitions are Automatically Converted into Stock Transport Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process the stock transport requisition is automatically converted to a stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Navigate to Schedule Purchasing Jobs (F1702) app. | Application Jobs screen is displayed. |  |
| 3 | Create new job | Choose Create to create a new application job. | New Job: Automatic creation of Purchase Orders from Requisitions screen is displayed. |  |
| 4 | Enter job details | Enter the application job details in the Template Information and Scheduling Options sections (Step 1).Job Template: Automatic creation of Purchase Orders from RequisitionJob Name: Automatic creation of Purchase Orders from RequisitionChoose Step 2Flag Start ImmediatelyChoose Define Recurrence Pattern if required to change the Recurrence. | The Template Information and scheduling options are defined. |  |
| 5 | Enter the Parameters | Choose Step 3In the Parameter section,Flag Per Requisition in New Purchase Order sectionMake the following entries in Item Specific Selection section (For Testing Purpose)Purchase Requisition: <XXXXXXX> Enter Stock Transport Requisition created using scope item Replenishment Planning for Stores (3I7) as mentioned in Check the Master Data Settings. | Parameters are entered. |  |
| 6 | Check | Choose Check. | You can go ahead and schedule job message is displayed. |  |
| 7 | Schedule | Choose Schedule. | Automatic creation of Purchase Order from Requisition has been scheduled.The Application Jobs screen is displayed again, and the new job is displayed in the Jobs table. |  |
| 8 | Navigate to Results | Check the newly create job row and Choose the icon Navigate to the job Results in Results column. | Document (ID XXXXXXX) screen is displayed with purchase order number. |  |

### Create Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a stock transport order manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Select Stock Transport Order Type | Select UD - StockTranspOrderDel from Order type drop down listNote Please don’t use Stock Transp. Order (UB) | Order type is selected, |  |
| 4 | Enter the parameters | Enter the following data:Supplying Plant: 3350In the Header area, Org. Data tab:Purch. Org: 3310Purch. Group: 001Company Code: 3310In Item Overview:Material: R_2003PO Quantity: 5Delivery Date: <any date in the future>Plant: 3340Storage Location: 994A | Data entered. |  |
| 5 | Save Stock Transport Order | Choose Save | StockTranspOrderDel created under the number XXXXXXXXXX message is displayedMake a note of the stock transport order |  |

### Advanced Intercompany Stock Transfer

#### Create Intercompany Stock Transfer Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchPad displays. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | Create Purchase Order screen is dislayed. |  |
| 3 | Enter Purchase Order Document Type | Make the following data:Order Type: NBIC (IC SiT STO)Choose Enter. | All data are entered, the item detail screen opens. |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplier: for example, <1750> (U.S.)Note We are using <1750> as an example to show an international stock transfer order between your company and an American company. You may enter a different company (from another country/region)'s Supplier value to show an international intercompany stock transfer order.On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002On the Header / Partners tab:Partner Function.: PINumber: <17401710> (U.S.)Note You may refer to the note above for entering a different company (from another country/region)'s Supplier value.On the Item Overview tab:Material: R_3018Quantity: x pcPlant: 3342Storage Location: 994AOn the Item Details Invoice tab:Tax Code: <Input Tax Code>Then choose Enter.Note Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and the user needs to take a decision based on the result of the checks. | All data are entered, the item detail screen opens. |  |
| 5 | Choose Goods Receive with Inbound Delivery | Make the following data:In item Details and on Confirmations tab:Conf.Control: 0004 Inbound Delivery |  |  |
| 6 | Save Purchase Order | Choose the Save button and when the purchase order number is displayed, write it down for further use.Note If Flexible Workflow for Purchase Orders has already been activated,log on to the SAP Fiori launchpad as a Purchasing Manager role to approve your purchase orders. | A new Purchase Order is created. Purchase Order Number is displayed.Write down the Standard Purchase Order number for further usage. |  |
| 7 | Check Purchase Order Document Flow | Execute the step [Display Intercompany Stock Transfer Value Chain](#unique_28) [page ] 30 to check intercompany stock transfer document flow. | The whole Intercompany Stock Transfer documents and status are displayed. |  |
| 8 | Display the Sales Order | Execute the step [Display Intercompany Sales Order](#unique_29) [page ] 31 to check intercompany sales order automatically created by the above purchase order. | Intercompany Sales Order is automatically created.Write down the Sales Order number for further usage. |  |

#### Create Pro Forma F5 Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma F5 Invoice by referring the intercompany sales order created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Create Pro Forma Invoice | Under the Default Data tab and make the following entries:Billing Type: Pro Forma for Order(F5)Billing Date: for example, current date.Under the Docs to Be Processed Tab:Document: Enter Intercompany Sales Order number which is created in the previous step.Then choose Enter. | The Pro Forma For Order (F5) create: Overview of Billing Items screen displays. |  |
| 4 | Save | Choose Save. | The F5 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents screen, enter the Billing Number and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx (F5) Display: Overview screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Pro Forma for Order xxxxxxxx ( F5) Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display Document. | Preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

#### Create Outbound Delivery for Stock Transfer Order

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
| 1 | Log On | Log n to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Fiori App My Purchase Orders - Due for Delivery (VL10B). | The Purchase Orders, Fast Display screen appears. |  |
| 3 | Enter Data for PO Display | Make the following entries, then choose Execute:Shipping Point: for example, <1750> (U.S.)Note We are using <1750> as an example to show an international stock transfer order between your company and an American company. You may enter a different company (from another country/region)'s Shipping Point value to show an international intercompany stock transfer order.Delivery creation dates (From): <delivery creation From date> Delete the default dateDelivery creation dates (To): <delivery creation To date> Delete the default dateCalc Rule: <calculation rule> 3 |  |  |
| 4 | Execute Purchase Order | Go to tab: Purchase OrdersEnter the Purchase Order number which is created in previous Step.Choose Execute. |  |  |
| 5 | Create Delivery | Select stock transfer orders from the list. Choose Background to Create Delivery in Background. | Activities Due for Shipping “Purchase Orders, Fast Display” screen appears. |  |
| 6 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the Outbound delivery number shown in the SD Doc. field | An outbound delivery is created. |  |

#### Pick and Post Goods Issue for Outbound Delivery

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
| 1 | Log On | Log on to the SAP Fiori launch Pad as a Shipping Specialist. | The Fiori launch Pad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen appears. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Adv.CC STO XXXXXXXX: Change Overview screen displays. |  |
| 4 | Enter Picked Quantity and Save | Navigate to the Picking tab and enter quantity equal to Delivery Qty in Picked Qty field for picking related item(s) and choose Save. | The system shows the message: Replen. Adv. CC STO XXXXXXX has been saved. The screen returns to Change Outbound Delivery screen. |  |
| 5 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

Financial Posting for GIOD (Goods Issue for OD into SIT in Delivering Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Goods | 13600000 Inventory - Trading Goods | none |

#### Confirm Internal Transfer of Control Date for Goods in Transit

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The Fiori launch Pad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen appears. |  |
| 4 | Change Outbound Deliveries | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Adv.CC STO XXXXXXXX: Change Overview screen displays. |  |
| 5 | Confirm Internal Transfer of Control Dates and Times | On the top menu, choose Menu > Goto > Header > Shipment , check the field Planned Dates and Time at the screen block Internal Transfer of Control Dates, input new actual date and time in the field Actual Date andTime to reflect the actual case, for example, current System Date and Time choose Save.Note This field controls when the goods movement will be posted from Stock in Transit of the delivering company to the ordering company. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement it reaches that date and time. | Internal Transfer of Control Dates are confirmed. |  |
| 6 | Display the Goods in Transit Documents | Execute the step [Display Intercompany Goods in Transit Document](#unique_30) [page ] 33 to check Goods in Transit Documents automatically created by the above Outbound Delivery. | Goods in Transit Documents are automatically created when it reaches the actual planned date |  |
| 7 | Display the Inbound Delivery | Execute the step [Display Inbound Delivery](#unique_31) [page ] 34 to check Inbound Delivery Document automatically created by the above Outbound Delivery. | Inbound Delivery is automatically created.Write down the Inbound Delivery number for further usage. |  |

Financial Posting

Financial Posting for GIIV (Post Goods Issue from Issuing SiT in Delivering Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000 Inventory - Consumption - Trading Goods | 13600000 Inventory - Trading Goods | 51600000 Consumption - Trading Goods |

Financial Posting for GRRV (Post Goods Receipt to Receiving SiT in Receiving Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Good | 21120000 Goods Received/Invoice Received | none |

#### Create Pro Forma F8 Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Under the Default Data tab and make the following entries:Billing Type: Pro Forma Invoice for Delivery (F8)Billing Date: for example, current dateUnder the Docs to Be Processed Tab:Document: Enter outbound delivery number which is created in the previous step.Then choose Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Pro Forma Billing Number, and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx Display: Overview screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Invoice xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display Document. | Preview of document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

#### Confirm Quantities for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Conf.Control: Inbound Delivery has been chosen in a previous step Create Intercompany Stock Transfer Order.

Procedure

This activity confirms that all the materials have been put away in the correct quantities.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Receiving Specialist. | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen appears. |  |
| 3 | Enter Inbound Delivery Number | Make the following entry.Inbound Delivery: <Enter the Inbound Delivery Number Created in the Previous Step>Then choose Continue. | The Inbound Delivery XXX Change: Overview screen appears. |  |
| 4 | Confirm Quantities for Putaway without Batch Assignment | Under Item Overview tab, enter:Putaway Qty: XXXNote The put away quantity should equal to the delivery Qty.Choose Save. | Go back to the Inbound Deliveries for Putaway screen and the Inbound Delivery XXX has been saved message appears. |  |

#### Post Goods Receipt for Inbound Delivery

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
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Receiving Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the APP | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entry, then choose Continue:Inbound Delivery: < Enter the Inbound Delivery Number Created in the Previous Step>. | The Inbound Delivery XXX Change: Overview screen shows up. |  |
| 4 | Change the Inbound Delivery | Check the selected inbound deliveries and choose Post Goods Receipt.The Specify Actual Goods Receipt Date screen appears. Choose Continue. | The goods receipt is posted.A success message appears. |  |
| 5 | Display the Post Stock Transfer into Physical Stock | Execute the step Display Post Stock Transfer into Physical Stock to check Inbound Delivery Document automatically created by the above outbound delivery. | The Post Stock Transfer into Physical Stock is automatically created successfully. |  |

#### Create Intercompany Billing Document

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar and make the following settings entries:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFFChoose OK |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary, for example, the Outbound Delivery Number, press Enter. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose the button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Intercompany Invoice (IV2) and maintain billing date, for example current date, then choose button OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial Posting

In all the scenarios related to a Sales Flow, whatever Billing Document is created (Customer Invoice, Debit Note, Credit Note, Intercompany Invoice, etc.) the Journal Entry type is determined according to the following rule:

- If the Dest. Country/Region is Italy, the FI document type is W1 IT Local Cust. Sales.
- If the Dest. Country/Region is within European Union, the FI document type is W2 IT EU Cust. Sales.
- If the Dest. Country/Region is outside European Union, the FI document type is W3 IT EXEU Cust. Sales.

Financial Posting for CIIC (Intercompany Customer Invoice in Delivering Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 Receivables affiliated Companies | 41001500 Revenue Affiliate - Product | 41001500 Revenue Affiliate - Product |

#### Display Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check intercompany purchase order of the advanced intercompany sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the screen Adapt Filters pops up. In addition to the default selection, select another field Process Type, then choose OK. | Searching field Process Type is switched on. |  |
| 4 | Search value chain process | Make the following entries:Initiating Document: * + Purchase Order number which is created in previous step.Process Type: <Advanced Intercompany Stock Transfer>Then choose Go. | Business Processes match the search criteria are listed out. |  |
| 5 | Display the advanced intercompany value chain process | Click the line item from the Business Processes list. | Business Process screen displays. |  |
| 6 | Choose Supplier Invoice number | Locate the line item for the step “Supplier Invoice” from the Documents list, click the invoice number which is in the field Document ID. | Document ID screen displays. |  |
| 7 | Display Supplier Invoice | Click the invoice number. | The detail of Supplier Invoice displays. |  |

Financial Posting for SIIC (Intercompany Supplier Invoice in Receiving Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 21120000 Goods Received/Invoice Received | 21300000 Payables affiliated Companies | none |

#### Monitor Intercompany Stock Transfer Value Chain

##### Display Intercompany Stock Transfer Value Chain

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters,the screen Adapt Filters pops up. In addition to the default selection, select another field Process Type, then choose OK. | Searching field Process Type is switched on. |  |
| 4 | Search value chain process | Make the following entries:Initiating Document: * + Purchase Order number which is created in previous step.Process Type: <Advanced Intercompany Stock Transfer>Then choose Go. | Business Processes match the search criteria are listed out. |  |
| 5 | Display the advanced intercompany value chain process | Click the line item from the Business Processes list. | Business Process screen displays. |  |
| 6 | Check the Processing Stage of the advanced intercompany stock transfer value chain process | Check the value of the field Processing Stage on the screen, possible values could be from the list:Open: Value Chain is triggeredIn Process: Value Chain is in processingPending: Value Chain is pending for external processingProcessed with Errors: Error occurred on value chainReprocessing: Value Chain is under reprocessingCompleted: Value Chain is completed | The status of the intercompany sales value chain displays. |  |
| 7 | Display the Process Flow of the Advanced Intercompany Stock Transfer value chain process | Choose Process Flow tab in Business Process screen, detailed process steps of Advanced Intercompany Sales value chain are displayed in a flow chart. Each process step is displayed as a node with the following data:Step Name, for example, IC Purchase Order (POIC)Business Document Number, for example, Purchase Order 4500001234)Document Type, for example, Purchase OrderDocument ID, for example, 4500001234Document Status, for example, CompletedNote Legend of the color of process node:Green: process step is CompletedRed: process step is in an ErrorGrey: process step is OpenOrange: process step is PendingBlue: process step is Scheduled | The Process Flow of the Advanced Intercompany Stock Transfer value chain process displays. |  |

##### Display Intercompany Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check intercompany sales order of the advanced intercompany sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the screen Adapt Filters pops up. In addition to the default selection, select another field Process Type, then choose OK. | Searching field Process Type is switched on. |  |
| 4 | Search value chain process | Make the following entries:Initiating Document: * + Purchase Order number which is created in previous step.Process Type: <Advanced Intercompany Stock Transfer>Then choose Go. | Business Processes matches the search criteria are listed out. |  |
| 5 | Display the advanced intercompany value chain process | Click the line item from the Business Processes list. | Business Process screen displays. |  |
| 6 | Display Sales Order Number | Locate the line item for the step “Sales Order” from the Documents list, click Sales order number which in Field Document ID. | Document ID screen displays. |  |
| 7 | Display Sales Order | Click the Sales number. | The detail of Sales Order displays. |  |
| 8 | Note down the sales order number | Note down the Standard Sales Order number for future usage. |  |  |

##### Display Intercompany Goods in Transit Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check Intercompany Purchase Order of the Advanced Intercompany Sales Value Chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the screen Adapt Filters pops up. In addition to the default selection, select another field Process Type, then choose OK. | Searching field Process Type is switched on. |  |
| 4 | Search value chain process | Make the following entries:Initiating Document: * + Purchase Order Number which is created in the previous stepProcess Type: <Advanced Intercompany Stock Transfer >Then choose GO. | Business Processes matches the search criteria are listed out. |  |
| 5 | Display the advanced intercompany value chain process | Click the line item from the Business Processes list. | Business Process screen displays. |  |
| 6 | Display Goods in Transit Document | Locate the line item for the step “Goods Issue for OD into SIT (GIOD)” or ‘Post Goods Receipt to Receiving SIT(GRRV)’ from the Documents list, click the GIOD or GRRV number in field Document ID. | The GIOD or GRRV document detail screen displays. |  |

##### Display Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check Intercompany Purchase Order of the Advanced Intercompany Sales Value Chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the screen Adapt Filters pops up. In addition to the default selection, select another field Process Type, then choose OK. | Searching field Process Type is switched on. |  |
| 4 | Search value chain process | Make the following entries:Initiating Document: * + Purchase Order Number which is created in previous stepProcess Type: <Advanced Intercompany Stock Transfer >Then choose GO. | Business Processes matches the search criteria are listed out. |  |
| 5 | Display the advanced intercompany value chain process | Click the line item from the Business Processes list. | Business Process screen displays. |  |
| 6 | Display Inbound Delivery Number | Locate the line item for the step “Inbound Delivery” from the Documents list. | Document screen displays. |  |
| 7 | Note down the Inbound Delivery number | Note down the Inbound Delivery Number for further usage. |  |  |

##### Display Post Stock Transfer into Physical Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check Intercompany Purchase Order of the Advanced Intercompany Sales Value Chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, the screen Adapt Filters pops up. In addition to the default selection, select another field Process Type, then choose OK. | Searching field Process Type is switched on. |  |
| 4 | Search value chain process | Make the following entries:Initiating Document: * + Purchase Order Number which is created in previous stepProcess Type: <Advanced Intercompany Stock Transfer >Then choose GO. | Business Processes matches the search criteria are listed out. |  |
| 5 | Display the advanced intercompany value chain process | Click the line item from the Business Processes list. | Business Process screen displays. |  |
| 6 | Display GRID number and status | Locate the line item for the step “Post Stock Transfer into Physical Stock” from the Documents list, click the line item. | Document screen displays. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can precede this process.

| Scope Item | Business Condition |
| --- | --- |
| 3I7 - Replenishment Planning for Stores | Creation of purchase requisition through store replenishment |
| 5FL - Merchandise Allocation | Merchandise allocation |

#### Succeeding Processes

After completing the activities in this test script for procurement from distribution centers belonging to the same company code, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 5FV - Outbound Logistics for Distribution Centers | This scope item perform creation of outbound delivery, Goods Issue and goods receipt against outbound delivery. |

|  |
| --- |
| Note The above business process need not be tested for procurement from distribution centers belonging to the different company code. |

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
- related-to :: [[15-retail-operations/test-script-in-store-purchase-order-management-5fy-ae-sap-s-4hana-clou]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 60,530 chars in the whole document
