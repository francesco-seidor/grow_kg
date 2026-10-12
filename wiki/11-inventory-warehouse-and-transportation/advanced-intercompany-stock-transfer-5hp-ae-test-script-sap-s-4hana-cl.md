---
id: 11-inventory-warehouse-and-transportation/advanced-intercompany-stock-transfer-5hp-ae-test-script-sap-s-4hana-cl
title: "Advanced Intercompany Stock Transfer (5HP_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5HP_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (5HP_AE, 2608) for advanced intercompany stock transfer: roles, master data, steps, apps and financial postings."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/advanced-intercompany-stock-transfer]
aliases: [5HP_S4CLD2608_BPD_EN_AE]
keywords: [Advanced Intercompany Stock Transfer, intercompany stock transfer, test procedures, business roles, stock transfer order, outbound delivery, goods issue, goods in transit, inbound delivery, intercompany billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HP_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1100
topic: 11-inventory-warehouse-and-transportation/advanced-intercompany-stock-transfer
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Advanced Intercompany Stock Transfer (5HP_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5HP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Advanced Intercompany Stock Transfer** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Intercompany Stock Transfer (5HP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856633)

[2 Prerequisites 4](#_Toc232856634)

[2.1 System Access 4](#_Toc232856635)

[2.2 Roles 4](#_Toc232856636)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232856637)

[2.4 Additional Manual Configuration 6](#_Toc232856638)

[2.5 Business Conditions 7](#_Toc232856639)

[2.6 Preliminary Steps 7](#_Toc232856640)

[2.6.1 Opening New MM Period 7](#_Toc232856641)

[2.6.2 Creating Stock in Supplying Plant 7](#_Toc232856642)

[2.6.3 Create Condition Records 9](#_Toc232856643)

[3 Overview Table 10](#_Toc232856644)

[4 Test Procedures 12](#_Toc232856645)

[4.1 Create Intercompany Stock Transfer Order 12](#_Toc232856646)

[4.2 Create Pro Forma F5 Invoice (Optional) 14](#_Toc232856647)

[4.3 Create Outbound Delivery for Stock Transfer Order 15](#_Toc232856648)

[4.4 Pick and Post Goods Issue for Outbound Delivery 16](#_Toc232856649)

[4.5 Check Batches (Optional) for Outbound Delivery 17](#_Toc232856650)

[4.6 Confirm Internal Transfer of Control Date for Goods in Transit 18](#_Toc232856651)

[4.7 Create Pro Forma F8 Invoice (Optional) 20](#_Toc232856652)

[4.8 Confirm Quantities for Inbound Delivery 21](#_Toc232856653)

[4.9 Post Goods Receipt for Inbound Delivery 22](#_Toc232856654)

[4.10 Create Intercompany Billing Document 23](#_Toc232856655)

[4.11 Display Supplier Invoice 24](#_Toc232856656)

[4.12 Monitor Intercompany Stock Transfer Value Chain 26](#_Toc232856657)

[4.12.1 Display Intercompany Stock Transfer Value Chain 26](#_Toc232856658)

[4.12.2 Display Intercompany Sales Order 27](#_Toc232856659)

[4.12.3 Display Intercompany Goods in Transit Document 28](#_Toc232856660)

[4.12.4 Display Inbound Delivery 29](#_Toc232856661)

[4.12.5 Display Post Stock Transfer into Physical Stock 30](#_Toc232856662)

[4.13 Schedule Resolution of Value Chain Issues (Optional) 31](#_Toc232856663)

## Purpose

Overview

The Advanced Intercompany Stock Transfer process begins with a requirement to transfer material from one company to another company. The purchaser creates purchase orders under the receiving plant.

A warehouse clerk at the issuing plant monitors the materials due to be shipped and creates deliveries as required. Once the delivery is complete, the delivery quantities are issued, appropriate documentation is generated, and the goods are shipped, ending the process for the issuing plant.

At the receiving plant, goods are received that reference the purchase documents. Inventory is received into a storage location based on fixed parameters proposed from the material master, which can be changed at the time of transactional data capture (purchase order creation or goods receipt).

Intercompany Invoicing is performed and a supplier invoice is created.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure. If you have installed SAP Best Practices Baseline Packages for Germany and US national versions, you can use the following Baseline Package scenario data:

|  |
| --- |
| Note In this master data sheet, we take United States as an example as the supplier. |

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Plant 1 AE |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase Group | 002 | Group 002 |  |
| Company Code | 1710 | Company Code 1710 |  |
| Plant | 1710 | Plant 1 US |  |
| Storage Location | 171A | Std. storage 1 |  |
| Shipping Point | 1710 | Shipping Point 1710 |  |
| Sales Organization | 1710 | Dom. Sales Org US |  |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch-controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch-controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Supplier | 17411710 | Representing the Supplying US Company/Plant (Company code 1710/ Plant 1710 )Pur.Org.1710 |  |
| Supplier Invoicing Party | 17401710 | Representing Supplier in Company Code 3310 |  |
| Inter-CompanySold to PartyInter-CompanyBill-to Party | 3341331033403310 | Customer Company code 3310 representing the Receiving Company (Company Code 3310) | Fiori App creation |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a7764e5ad6a18915c18039e1d3aea398)

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Complete all relevant steps. |

### Preliminary Steps

#### Opening New MM Period

For this activity, run the following steps from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period.

- Closing MM Period and Opening New Posting Period

#### Creating Stock in Supplying Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a real business case, the materials are usually purchased from external vendors. In that case, that process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: <Goods Receipt>Reference Document for MIGO Transaction: : <Other>Note The system saves this selection if you have selected this option before. |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: <Material Number> |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: <PC> |  |  |
| 6 | Input On the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561Note Receipt per initial entry of stock balances into unrestricted usePlant: <1710> (U.S.)Note We are using <1710> as an example to show creating initial stock between your company and an American company. You may enter a different company (from another country/region)'s Plant value.Storage Location: <171A> (U.S.)Note You may refer to the note above for entering a different company (from another country/region)'s Plant value. |  |  |
| 7 | Save your Entries. | Choose Post. |  |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory Trad-ingGd | 39912000Inv Init SF& Fin Bal | none |

#### Create Condition Records

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: International

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Intercompany Stock Transfer Order](#unique_13) [page ] 12 | Purchaser | Create Purchase Order - Advanced (ME21N) | A Stock transfer Order is created. |
| [Create Pro Forma F5 Invoice (Optional)](#unique_14) [page ] 14 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing Document is created. |
| [Create Outbound Delivery for Stock Transfer Order](#unique_15) [page ] 15 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound Delivery is created. |
| [Pick and Post Goods Issue for Outbound Delivery](#unique_16) [page ] 16 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods Issue is posted. |
| [Check Batches (Optional) for Outbound Delivery](#unique_17) [page ] 17 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Confirm Internal Transfer of Control Date for Goods in Transit](#unique_18) [page ] 18 | Shipping Specialist | Change Outbound Delivery (VL02N) | Actual planned date is maintained. |
| [Create Pro Forma F8 Invoice (Optional)](#unique_19) [page ] 20 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing Document is created. |
| [Confirm Quantities for Inbound Delivery](#unique_20) [page ] 21 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) |  |
| [Post Goods Receipt for Inbound Delivery](#unique_21) [page ] 22 | Receiving Specialist | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Create Intercompany Billing Document](#unique_22) [page ] 23 | Billing Clerk | Create Billing Documents (F0798) | Billing Document is created. |
| [Display Supplier Invoice](#unique_23) [page ] 24 | Accounts Payable Accountant | Monitor Value Chains (F4854) | The Supplier Invoice is displayed. |
| [Display Intercompany Stock Transfer Value Chain](#unique_24) [page ] 26 | Internal Sales Representative | Monitor Value Chains (F4854) |  |
| [Display Intercompany Sales Order](#unique_25) [page ] 27 | Internal Sales Representative | Monitor Value Chains (F4854) |  |
| [Display Intercompany Goods in Transit Document](#unique_26) [page ] 28 | Shipping Specialist | Monitor Value Chains (F4854) |  |
| [Display Inbound Delivery](#unique_27) [page ] 29 | Purchaser | Monitor Value Chains (F4854) |  |
| [Display Post Stock Transfer into Physical Stock](#unique_28) [page ] 30 | Internal Sales Representative | Monitor Value Chains (F4854) |  |
| [Schedule Resolution of Value Chain Issues (Optional)](#unique_29) [page ] 31 | Internal Sales Representative | Schedule Resolution of Value Chain Issues (F6868) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Intercompany Stock Transfer Order

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
| 4 | Enter Purchase Order Data | Enter the following data:Supplier: for example, <17411710> (U.S.)Note We are using <17411710> as an example to show an international stock transfer order between your company and an American company. You may enter a different company (from another country/region)'s Supplier value to show an international intercompany stock transfer order.On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002On the Header / Partners tab:Partner Function.: PINumber: <17401710> (U.S.)Note You may refer to the note above for entering a different company (from another country/region)'s Supplier value.On the Item Overview tab:Material: TG11(without batch management)； TG21/ TG22(with batch management)Quantity: x pcPlant: 3310Storage Location: 331AOn the Item Details Invoice tab:Tax Code: <Input Tax Code>Then choose Enter.Note Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and the user needs to take a decision based on the result of the checks. | All data are entered, the item detail screen opens. |  |
| 5 | Choose Goods Receive with Inbound Delivery | Make the following data:In item Details and on Confirmations tab:Conf.Control: 0004 Inbound Delivery |  |  |
| 6 | Save Purchase Order | Choose the Save button and when the purchase order number is displayed, write it down for further use.Note If Flexible Workflow for Purchase Orders has already been activated,log on to the SAP Fiori launchpad as a Purchasing Manager role to approve your purchase orders. | A new Purchase Order is created. Purchase Order Number is displayed.Write down the Standard Purchase Order number for further usage. |  |
| 7 | Check Purchase Order Document Flow | Execute the step [Display Intercompany Stock Transfer Value Chain](#unique_24) [page ] 26 to check intercompany stock transfer document flow. | The whole Intercompany Stock Transfer documents and status are displayed. |  |
| 8 | Display the Sales Order | Execute the step [Display Intercompany Sales Order](#unique_25) [page ] 27 to check intercompany sales order automatically created by the above purchase order. | Intercompany Sales Order is automatically created.Write down the Sales Order number for further usage. |  |

### Create Pro Forma F5 Invoice (Optional)

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
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx (F5) Display: Overview screen, choose Change and then choose More > Goto > Header > Output . | The Pro Forma for Order xxxxxxxx ( F5) Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display PDF Document. | Preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

### Create Outbound Delivery for Stock Transfer Order

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
| 3 | Enter Data for PO Display | Make the following entries, then choose Execute:Shipping Point: for example, <1710> (U.S.)Note We are using <1710> as an example to show an international stock transfer order between your company and an American company. You may enter a different company (from another country/region)'s Shipping Point value to show an international intercompany stock transfer order.Delivery creation dates (From): <delivery creation From date> Delete the default dateDelivery creation dates (To): <delivery creation To date> Delete the default dateCalc Rule: <calculation rule> 3 |  |  |
| 4 | Execute Purchase Order | Go to tab: Purchase OrdersEnter the Purchase Order number which is created in previous Step.Choose Execute. |  |  |
| 5 | Create Delivery | Select stock transfer orders from the list. Choose Background to Create Delivery in Background. | Activities Due for Shipping “Purchase Orders, Fast Display” screen appears. |  |
| 6 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the Outbound delivery number shown in the SD Doc. field | An outbound delivery is created. |  |

### Pick and Post Goods Issue for Outbound Delivery

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
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen appears. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Adv.CC STO XXXXXXXX: Change Overview screen displays. |  |
| 4 | Check Batch Split | Navigate to the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 5 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to ex-pand sub item(s), enter quantity equal to delivery Qty in Picked Qty field for sub item.If batch spilt doesn't exist, enter quantity equal to Delivery Qty in Picked Qty field for picking related item(s). | The system shows the message: Replen. Adv. CC STO XXXXXXX has been saved. The screen returns to Change Outbound Delivery screen. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

Financial Posting for GIOD (Goods Issue for OD into SIT in Delivering Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Goods | 13600000 Inventory - Trading Goods | none |

### Check Batches (Optional) for Outbound Delivery

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
| 1 | Open Transaction | Open the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Adv.CC STO XXXXXXXX: Change Overview screen displays. |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, select the Batch Split Indicator field, and check the batch number assignment. | Batch numbers are assigned to the materials. The batch numbers are required to be entered during the Post Goods Receipt step. |  |
| 5 | Save Document | Choose Save. |  |  |

### Confirm Internal Transfer of Control Date for Goods in Transit

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
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen appears. |  |
| 4 | Change Outbound Deliveries | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Adv.CC STO XXXXXXXX: Change Overview screen displays. |  |
| 5 | Confirm Internal Transfer of Control Dates and Times | On the top menu, choose More > Goto > Header > Shipment , check the field Planned Dates and Time at the screen block Internal Transfer of Control Dates, input new actual date and time in the field Actual Date andTime to reflect the actual case, for example, current System Date and Time.Note This field controls when the goods movement will be posted from Stock in Transit of the delivering company to the ordering company. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement it reaches that date and time. | Internal Transfer of Control Dates are confirmed. |  |
| 6 | Display the Goods in Transit Documents | Execute the step [Display Intercompany Goods in Transit Document](#unique_26) [page ] 28 to check Goods in Transit Documents automatically created by the above Outbound Delivery. | Goods in Transit Documents are automatically created when it reaches the actual planned date |  |
| 7 | Display the Inbound Delivery | Execute the step [Display Inbound Delivery](#unique_27) [page ] 29 to check Inbound Delivery Document automatically created by the above Outbound Delivery. | Inbound Delivery is automatically created.Write down the Inbound Delivery number for further usage. |  |

Financial Posting

Financial Posting for GIIV (Post Goods Issue from Issuing SiT in Delivering Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000 Inventory - Consumption - Trading Goods | 13600000 Inventory - Trading Goods | 51600000 Consumption - Trading Goods |

Financial Posting for GRRV (Post Goods Receipt to Receiving SiT in Receiving Company)

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Good | 21120000 Goods Received/Invoice Received | none |

### Create Pro Forma F8 Invoice (Optional)

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
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Pro Forma for Billing Number, and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx Display: Overview screen, choose Change and then choose More > Goto > Header > Output . | The Invoice xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display PDF Document. | Preview of PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

### Confirm Quantities for Inbound Delivery

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
| 5 | Confirm Quantities for Putaway with Batch Assignment | Under Stock Placement tab, select the Batch Split Indicator field of the item and expand the batch items of the main item. Enter:Putaway Qty: XXXThe put away quantity should be equal to the Delivery Qty of the batch item.Choose Save. | Go back to the Inbound Deliveries for Putaway screen and the Inbound Delivery XXX has been saved message appears. |  |

### Post Goods Receipt for Inbound Delivery

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

### Create Intercompany Billing Document

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
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar and make the following settings entries:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary, for example, the Delivery Number, press Enter. | Sales document(s) display in the result. |  |
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

### Display Supplier Invoice

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

### Monitor Intercompany Stock Transfer Value Chain

#### Display Intercompany Stock Transfer Value Chain

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
| 6 | Check the Status of the advanced intercompany stock transfer value chain process | Check the value of the field Status on the screen, possible values could be from the list:Open: Value Chain is triggeredIn Process: Value Chain is in processingPending: Value Chain is pending for external processingProcessed with Errors: Error occurred on value chainReprocessing: Value Chain is under reprocessingCompleted: Value Chain is completed | The status of the intercompany sales value chain displays. |  |
| 7 | Display the Process Flow of the Advanced Intercompany Stock Transfer value chain process | Choose Process Flow tab in Business Process screen, detailed process steps of Advanced Intercompany Sales value chain are displayed in a flow chart. Each process step is displayed as a node with the following data:Step Name, for example, IC Purchase Order (POIC)Business Document Number, for example, Purchase Order 4500001234)Document Type, for example, Purchase OrderDocument ID, for example, 4500001234Document Status, for example, CompletedNote Legend of the color of process node:Green: process step is CompletedRed: process step is in an ErrorGrey: process step is OpenOrange: process step is PendingBlue: process step is Scheduled | The Process Flow of the Advanced Intercompany Stock Transfer value chain process displays. |  |

#### Display Intercompany Sales Order

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

#### Display Intercompany Goods in Transit Document

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

#### Display Inbound Delivery

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

#### Display Post Stock Transfer into Physical Stock

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

### Schedule Resolution of Value Chain Issues (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job to resolve the value chain issues massively.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Resolution of Value Chain Issues (F6868). | The Application Jobs screen displays. |  |
| 3 | Create a New Application Job | Choose Create. | The New Job: Schedule Resolution of Value Chain Issues screen displays. |  |
| 4 | Select a Template | Make the following entries and choose Step 2:Job Template: Schedule Resolution of Value Chain IssuesJob Name: for example, Schedule Resolution of Value Chain Issues | The Scheduling Options screen displays. |  |
| 5 | Define One-time Scheduling Settings | Option 1:Start Immediately: SelectedOption 2:Start Immediately: UnselectedStart: Choose a date and time when this job is startedTime Zone: Choose the preferred time zone, for example, UTC+08 | One-time Scheduling Option is defined. |  |
| 6 | Define Recurrence Schedule Option | Choose Define Recurrence Pattern, make the following entries and choose OK:Job Start: A date and time when the job is started for the first timeTime Zone: for example, UTC+08Recurrence Pattern: WeeklyEvery: 1 Week(s)On: for example, FridayEnd: for example, AfterOccurrence(s): for example, 52On Non-Working Day: for example, No restrictionCalendar: Germany (Standard) | Recurrence Scheduling Option is defined. |  |
| 7 | Define Parameters | Choose Step 3, make the following entries and choose Check:Process Type: for example, IC_SALES and ICO_STOCKTRANSFERSystem runtime errors: SelectedBlocked event queues: SelectedBusiness process errors: SelectedChoose Schedule. | Resolution of Value Chain Issues job is scheduled. |  |
| 8 | Check Resolution of Value Chain Issues Job Log | Return to the Application Jobs screen.On the Application Jobs screen, after job item’s status turns to Finished, choose the status icon in the Log column.Note Choose Magnifier, and the job list is refreshed. | The Log Details list displays. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-1p9-ae-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 55,683 chars in the whole document
