---
id: 11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-1p9-ae-sap-s-4hana-cloud-publi
title: "Test Script: Intercompany Stock Transfer (1P9_AE) - SAP S/4HANA Cloud Public Edition (1P9_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 1P9: domestic and international intercompany stock transfer, from STO to billing and supplier invoice."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/advanced-intercompany-stock-transfer]
aliases: [1P9_S4CLD2608_BPD_EN_AE]
keywords: [Advanced Intercompany Stock Transfer, intercompany stock transfer, stock transport order, replenishment delivery, goods issue, goods receipt, inbound delivery, intercompany billing, supplier invoice, pro forma invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1P9_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-753
topic: 11-inventory-warehouse-and-transportation/advanced-intercompany-stock-transfer
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Stock Transfer (1P9_AE) - SAP S/4HANA Cloud Public Edition (1P9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1P9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Advanced Intercompany Stock Transfer** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Stock Transfer (1P9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847468)

[2 Prerequisites 4](#_Toc232847469)

[2.1 System Access 4](#_Toc232847470)

[2.2 Roles 4](#_Toc232847471)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847472)

[2.4 Additional Manual Configuration 8](#_Toc232847473)

[2.5 Business Conditions 8](#_Toc232847474)

[2.6 Preliminary Steps 9](#_Toc232847475)

[2.6.1 Opening New MM Period 9](#_Toc232847476)

[2.6.2 Creating Stock in Supplying Plant 9](#_Toc232847477)

[2.6.2.1 Create Initial Stock in the Domestic Shipping Plant 9](#_Toc232847478)

[2.6.2.2 Create Initial Stock in the International Shipping Plant 11](#_Toc232847479)

[2.6.3 Create Condition Records (Optional) 12](#_Toc232847480)

[2.6.3.1 Check Flexible Workflow for Purchase Order Approval 12](#_Toc232847481)

[2.6.3.2 Configure Flexible Workflow for Purchase Order 14](#_Toc232847482)

[3 Overview Table 16](#_Toc232847483)

[4 Test Procedures 18](#_Toc232847484)

[4.1 Domestic 18](#_Toc232847485)

[4.1.1 Create Intercompany Stock Transfer Order 18](#_Toc232847486)

[4.1.2 Create Replenishment Delivery for Stock Transfer Order 20](#_Toc232847487)

[4.1.3 Pick and Post Goods Issue for Stock Transfer Order 21](#_Toc232847488)

[4.1.4 Check Batches (Optional) 22](#_Toc232847489)

[4.1.5 Check Status of Stock Transfer 22](#_Toc232847490)

[4.1.6 Post Goods Receipt for Stock Transfer Order 23](#_Toc232847491)

[4.1.7 Inbound Delivery Processing (optional) 25](#_Toc232847492)

[4.1.7.1 Confirm Quantities for Putaway 25](#_Toc232847493)

[4.1.7.2 Post Goods Receipt for Inbound Delivery 26](#_Toc232847494)

[4.1.8 Check Status of Stock Transfer 27](#_Toc232847495)

[4.1.9 Create Intercompany Billing Document 28](#_Toc232847496)

[4.1.10 Create Supplier Invoice 29](#_Toc232847497)

[4.2 International 31](#_Toc232847498)

[4.2.1 Create Intercompany Stock Transfer Order 31](#_Toc232847499)

[4.2.2 Create Replenishment Delivery for Stock Transfer Order 33](#_Toc232847500)

[4.2.3 Create Pro Forma Invoice (Optional) 34](#_Toc232847501)

[4.2.4 Pick and Post Goods Issue for Stock Transfer Order 35](#_Toc232847502)

[4.2.5 Check Batches (Optional) 36](#_Toc232847503)

[4.2.6 Check Status of Stock Transfer 37](#_Toc232847504)

[4.2.7 Post Goods Receipt for Stock Transfer Order 38](#_Toc232847505)

[4.2.8 Inbound Delivery Processing (optional) 39](#_Toc232847506)

[4.2.8.1 Confirm Quantities for Putaway 39](#_Toc232847507)

[4.2.8.2 Post Goods Receipt for Inbound Delivery 41](#_Toc232847508)

[4.2.9 Check Status of Stock Transfer 41](#_Toc232847509)

[4.2.10 Create Intercompany Billing Document 42](#_Toc232847510)

[4.2.11 Create Supplier Invoice 43](#_Toc232847511)

[5 Appendix 46](#_Toc232847512)

[5.1 Scheduling Job (Alternative) 46](#_Toc232847513)

[5.1.1 Job Scheduling for Delivery Creation (Alternative) 46](#_Toc232847514)

## Purpose

Overview

The stock transfer process begins with a requirement to transfer material from one company or plant to another company or plant within the same country. The Purchaser creates purchase orders under the receiving plant.

A warehouse clerk at the issuing plant monitors the materials due to be shipped and creates deliveries as required. For international processes, a proforma invoice is generated. Once the delivery is complete, the delivery quantities are issued, appropriate documentation is generated, and the goods are shipped, ending the process for the issuing plant.

Goods are received at the receiving plant referencing the purchase documents. Inventory is received into a storage location based on fixed parameters proposed from the material master, which can be changed at the time of transactional data capture (purchase order creation or goods receipt).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

|  |
| --- |
| Caution In order to have the Intercompany Stock Transfer working properly for Brazil, the pricing type (V_TVCPFLP-KNPRS) used when creating the CBST billing document (from a NLCC delivery type) must be adjusted to “C” (Copy manual price elements and redetermine the others).You may change your system's configuration (in this case, bear in mind that this will affect all countries) or implement the Cloud BAdI SD_BIL_DATA_TRANSFER with more specific conditions to overwrite the pricing type configured in the copying control rules. |

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

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
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure. If you have installed SAP Best Practices Baseline Packages for Germany and US national versions, you can use the following Baseline Package scenario data:

Domestic

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Plant 1 AE |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase Group | 002 | Group 002 |  |
| Company Code | 3320 | Company Code 3320 | Flex.Org App or Set Up Organizational (CBC) extension |
| Plant | 3330 | Plant 3 AE | Flex.Org App or Set Up Organizational (CBC) extension |
| Storage Location | 333A | Std. storage 1 | Flex.Org App extension in Plant 2 AE or Set Up Organizational (CBC) extensionShop floor w/o lean WM |
| Shipping Point | 3330 | Shipping Point 3330 | Flex.Org App or Set Up Organizational (CBC) extension |
| Sales Organization | 3330 | Sales Organization in Company 3320 | Flex.Org App or Set Up Organizational (CBC) extension |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch-controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch-controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Supplier | 33413330 | Representing the Supplying Company/Plant (Company Code 3320/ Plant 3330) | Fiori App creation |
| SupplierInvoicing Party | 33403320 | Representing Supplier in Company Code 3310 AE | Fiori App creation |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

International

|  |
| --- |
| Note In this master data sheet, we take United-States as an example as the supplier. |

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
| SupplierInvoicing Party | 1741171017401710 | Supplier in Company Code 3310 AE representing the Supplying US Company/Plant (Company code 1710/ Plant 1010 )Pur.Org.1710 |  |
| Inter-CompanySold to PartyInter-CompanyShip-to Party |  | Customer Company code 1710 USrepresenting the Receiving Company (Receiving Plant 1710) |  |
| Inter-CompanySold to PartyInter-CompanyShip-to Party | 1740171017401710 | Customer Company code 1710 USrepresenting the Receiving Company (Company Code 1710) | Fiori App creation |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/fc524d7e1008638a710f526f4fbba7fd)

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Complete all relevant steps. |

### Preliminary Steps

#### Opening New MM Period

Purpose

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

##### Create Initial Stock in the Domestic Shipping Plant

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: <Goods Receipt>Reference Document for MIGO Transaction: <Other>Note (The system saves this selection if you have selected this option before.) |  |  |
| 4 | Enter Material | On the Goods Receipt Other screen: Material tab, make the following entry and choose Enter:Material: <Material Number> |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: <PC> |  |  |
| 6 | Input on the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561Note (Receipt per initial entry of stock balances into unrestricted use)Plant: 3330Storage Location: 333A |  |  |
| 7 | Input On the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of manufacture: <Enter the Current Date or a Date in the Past>Note Only relevant for batch relevant materials. |  |  |
| 8 | Save your Entries. | Choose Post. |  |  |

##### Create Initial Stock in the International Shipping Plant

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: <Goods Receipt>Reference Document for MIGO Transaction: : <Other>Note The system saves this selection if you have selected this option before. |  |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: <Material Number> |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: <PC> |  |  |
| 6 | Input On the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561Note Receipt per initial entry of stock balances into unrestricted usePlant: <1710> (U.S.)Note We are using <1710> as an example to show creating initial stock between your company and an American company. You may enter a different company (from another country/region)'s Plant value.Storage Location: <171A>(U.S.)Note You may refer to the note above for entering a different company (from another country/region)'s Plant value. |  |  |
| 7 | Input On the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of manufacture: <Enter the Current Date or a Date in the Past>Note Only relevant for batch relevant materials. |  |  |
| 8 | Save your Entries. | Choose Post. |  |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory Trad-ingGd | 39912000Inv Init SF& Fin Bal | none |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

##### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure flexible workflow for purchase order with NB document is activated, and flexible workflow for purchase order approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow:<Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen is displayed. |  |
| 3 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow:<Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

##### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure release conditions for purchase order approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872) . | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Add, and make the following entries:Name: <Test Workflow for Purchase Order>Select Preconditions, and in the Preconditions area, make the following entries:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Add another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the STEP SEQUENCE area, choose Add and make the following entries:Type: Release of Purchase OrderIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Add.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Domestic

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Intercompany Stock Transfer Order](#unique_17) [page ] 18 | Purchaser | Create Purchase Order - Advanced (ME21N) | A Stock transfer Order is created. |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_18) [page ] 20 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound Delivery is created. |
| [Pick and Post Goods Issue for Stock Transfer Order](#unique_19) [page ] 21 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods Issue is posted. |
| [Check Status of Stock Transfer](#unique_20) [page ] 22 | Warehouse Clerk | Stock - Single Material (F1076) | Display Stock in Transit. |
| [Check Batches (Optional)](#unique_21) [page ] 22 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Post Goods Receipt for Stock Transfer Order](#unique_22) [page ] 23 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Confirm Quantities for Putaway](#unique_23) [page ] 25 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) |  |
| [Post Goods Receipt for Inbound Delivery](#unique_24) [page ] 26 | Receiving Specialist | Inbound Deliveries for Goods Receipt (VL06IG) | Goods receipt is posted. |
| [Check Status of Stock Transfer](#unique_25) [page ] 27 | Warehouse Clerk | Stock - Single Material (F1076) | Display Stock in Transit. |
| [Create Intercompany Billing Document](#unique_26) [page ] 28 | Billing Clerk | Create Billing Documents - VF04 (VF04) | Billing Document is created. |
| [Create Supplier Invoice](#unique_27) [page ] 29 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | The Create Supplier Invoice is displayed. |

Table 4: International

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Intercompany Stock Transfer Order](#unique_28) [page ] 31 | Purchaser | Create Purchase Order - Advanced (ME21N) | A Stock transfer Order is created. |
| [Create Replenishment Delivery for Stock Transfer Order](#unique_29) [page ] 33 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound Delivery is created. |
| [Create Pro Forma Invoice (Optional)](#unique_30) [page ] 34 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing Document is created. |
| [Pick and Post Goods Issue for Stock Transfer Order](#unique_31) [page ] 35 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods Issue is posted. |
| [Check Status of Stock Transfer](#unique_32) [page ] 37 | Warehouse Clerk | Stock - Single Material (F1076) | Display Stock in Transit. |
| [Check Batches (Optional)](#unique_33) [page ] 36 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Post Goods Receipt for Stock Transfer Order](#unique_34) [page ] 38 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Confirm Quantities for Putaway](#unique_35) [page ] 39 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) |  |
| [Post Goods Receipt for Inbound Delivery](#unique_36) [page ] 41 | Receiving Specialist | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| [Check Status of Stock Transfer](#unique_37) [page ] 41 | Warehouse Clerk | Stock - Single Material (F1076) | Display Stock in Transit. |
| [Create Intercompany Billing Document](#unique_26) [page ] 28 | Billing Clerk | Create Billing Documents - VF04 (VF04) | Billing Document is created. |
| [Create Supplier Invoice](#unique_38) [page ] 43 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | The Create Supplier Invoice is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Domestic

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Enter Purchase Order Document Type | Make the following data:Order Type: NB (Standard PO)Choose Enter. | All data are entered, the item detail screen opens. |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplier: 33413330 (for domestic)On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002On the Header / Partners tab:Partner Function: PINumber: 33403320On the Item Overview tab:Material: TG11(without batch management)； TG21/ TG22(with batch management)Quantity: x pcDelivery Date: <any date in the future>Plant: 3310Storage Location: 331AOn the Item Details Invoice tab:Tax Code: <Input Tax Code>Then choose Enter.Note Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and you needs to take a decision based on the result of the checks. | All data are entered, the item detail screen opens. |  |
| 5 | Choose Goods Receive with Inbound Delivery (optional) | Make the following data:In Item Details section on Confirmations tab:Conf.Control: Inbound Delivery |  |  |
| 6 | Save Purchase Order | Choose the Save button and when the purchase order number is displayed, write it down for further use.Note If Flexible Workflow for Purchase Orders has already been activated,log on to the SAP Fiori launchpad as a Purchasing Manager role to approve your purchase orders. | A new Purchase Order is created. Purchase Order Number is displayed.Write down the Standard Purchase Order number for further usage. |  |

#### Create Replenishment Delivery for Stock Transfer Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Fiori App My Purchase Orders - Due for Delivery (VL10B). | The Purchase Order, Fast Display screen appears. |  |
| 3 | Enter Data for PO Display | Click the Purchase Orders tab and make the following entries, then click Execute:Shipping Point: 3330Delivery creation dates (From): <delivery creation From date> Delete the default dateDelivery creation dates (To): <delivery creation To date> Delete the default dateCalc Rule: <calculation rule> 3 |  |  |
| 4 |  | Go to tab: Purchase OrdersEnter PO number which is created in previous Step.Choose Run. |  |  |
| 5 | Create Delivery | Select stock transfer orders from the list. Choose Background to Create Delivery in Background. | The Activities Due for Shipping “Purchase Orders, Fast Display” screen appears. |  |
| 6 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the Outbound delivery number shown in the SD Doc. field. | An outbound delivery is created. |  |

#### Pick and Post Goods Issue for Stock Transfer Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen appears. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | Replen.Cross-Company XXXXXXXX: Overview screen displays. |  |
| 4 | Check Batch Split | Navigate to the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 5 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to ex-pand sub item(s), enter quantity equal to delivery Qty in Picked Qty field for sub item.If batch spilt doesn't exist, enter quantity equal to delivery Qty in Picked Qty field for picking related item(s). | The system shows the message: Replen.Cross-Company xxxxxxxx has been saved. The Change Outbound Delivery screen displays. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

#### Check Batches (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Cross-Company XXXXXXXX: Overview screen displays. |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, select the Batch Split Indicator field, and check the batch number assignment. | Batch numbers are assigned to the materials. The batch numbers are required to be entered during the Post Goods Receipt step. |  |
| 5 | Save Document | Choose Save. |  |  |

#### Check Status of Stock Transfer

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Stock in Transit (MB5T). | The Display Stock in Transit screen displays. |  |
| 3 | Enter Transfer Order Data | Make the following entries:Material Number: TG11Receiving Plant: 3310Then choose Execute. | You receive an overview of the stock transfer orders that are currently in transit. This concerns all materials that have left the supplying plant and have not yet reached the receiving plant. |  |

#### Post Goods Receipt for Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Open Post Goods Receipt for Purchase Order | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search for Purchasing Document | Open Purchasing Document Search . | A list of purchasing documents displays. |  |
| 4 | Select the Stock Transfer Order | Select your purchase order. | The system displays the data for the goods receipt on the Post Goods Receipt screen. |  |
| 5 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: xxxPrinting (Controls output management after posting): Individual slip |  |  |
| 6 | Enter Batch Numbers | Enter Batch numbers with which has been assigned to the Outbound Delivery on the item.Note The batch number assignment is requied when the material master data is batch management relevant. | The batch number has been assigned to the item. |  |
| 7 | Select Item and Post Goods Receipt | Select the items for which a goods receipt is to be posted (the storage location must be specified, if not in the PO).Enter the following data:Storage Location: for example, 331AChoose Post. | The Post is activated.The Success screen displays. The system displays the messagedocument(s) created: Material Document XXX. |  |

Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchPad as a Warehouse Clerk. | The Fiori launchpad is displayed. |  |
| 2 | Open Overdue Materials Stock in Transit | Open Overdue Materials - Stock in Transit (F2139). | The Overdue Materials - SiT screen displays. |  |
| 3 | Select Criteria | Enter the following data:Material: TG11Choose Go. |  |  |
| 4 | Check the Stock transfer Order | Check the quantity under the Goods issue Quantity for your stock transfer order. | You will see Goods issue Quantity. |  |
| 5 | Post Goods Receipt for Purchasing Documents | Select the purchasing documents, choose Post Goods Receipt for Purchase order. | Goods Receipt screen displays. |  |
| 6 | Post | Choose Select item, enter storage location and choose Post. | A system message material document xxxxxxxxx posted is displayed. |  |

#### Inbound Delivery Processing (optional)

##### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Conf.Control: Inbound Delivery has been chosen in the previous step Create Intercompany Stock Transfer Order.

Procedure

This process step shows you how to confirm that all the materials have been put away in the correct quantities.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP). | The Inbound Deliveries for Putaway screen appears. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Purchasing document: <Enter the Stock Transfer Number created in the previous step>.Delivery Date: <Delete the default date>. | The selected Inbound Delivery appears. |  |
| 4 | Change the Inbound Delivery | Check the selected Inbound deliveries and choose Change Inbound Deliveries. | The Inbound Delivery XXX Change: Overview screen appears. |  |
| 5 | Confirm Quantities for Putaway without Batch Assignment | Under Item Overview tab, enter:Putaway Qty: XXXNote The put away quantity should equal to the delivery Qty.Choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message appears. |  |
| 6 | Confirm Quantities for Putaway with Batch Assignment | Under Stock Placement tab, select the Batch Split Indicator field of the item and expand the batch items of the main item, input:Putaway Qty: XXXThen put away quantity should equal to the Delivery Qty of the batch item.Choose Save. | Back to the Inbound Deliveries for Putaway screen andInbound Delivery XXX has been savedmessage appears. |  |

##### Post Goods Receipt for Inbound Delivery

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
| 1 | Log On | Log on the SAP Fiori launchpad as a Receiving Specialist role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the APP | Open Inbound Deliveries for Goods Receipt (VL06IG). | The Goods Receipt screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Purchasing Document: <Enter Stock Transfer Order number created in the previous step>.Delivery Date: <Delete the default date>. | The Goods Receipt for Inbound Deliveries to be Posted screen shows up.The selected Inbound Deliveries shows. |  |
| 4 | Change the Inbound Delivery | Check the selected Inbound deliveries and choose Post Goods Receipt.The Specify Actual Goods Receipt Date screen appears and choose Continue. | Goods Receipt posted.A success message appears. |  |

#### Check Status of Stock Transfer

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Stock in Transit (MB5T). | The Display Stock in Transit screen displays. |  |
| 3 | Enter Transfer Order Data | Make the following entries:Material Number: TG11Receiving Plant: 3310Then choose Execute. | The stock transfer orders will not be displayed in this report if all materials have reached to receiving plant. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF04 (VF04). | The Maintain Billing Due List screen displays. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as sold-to party. In the Documents to Be Selected filter, choose Delivery-Related Intercompany Billing.Choose Display Billing List. | A list of delivery-related billing due list items displays. |  |
| 4 | Select Billing Due List Item | Select a row and set a check mark next to the billing due list item that you want to create a billing document for. | The appropriate billing due list item is selected. |  |
| 5 | Create and Display Invoice | Choose Individual Billing Document at the bottom of the screen.Choose Save. | The system generates a billing document. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries:Transaction: <Invoice>Company Code: 3310Gross Invoice Amount: <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(enter 00 + invoice number from invoicing party)Invoice Party:33403320In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <XXX>Currency: <XXX>(change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(enter 00 + invoice number from invoicing party)Invoice Party :33403320Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Create Supplier Invoices screen is displayed.The Exchange Rate should be changed from USD to EUR according to the customizing settings. The Exchange Rate is changeable. |  |
| 4 | Enter Purchase Order References | In Purchase Order References, make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxxxxxxx> | The Purchase Order References screen is displayed. |  |
| 5 | Check the Purchase Order Items Data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order.). | The Purchase Order Item's table is displayed. |  |
| 6 | Check Tax Code | In the section Tax, check if there is tax code information and enter the tax amount when the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items. | If there is no tax, specify the tax code <Input Tax Code> . |
| 7 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate button.If there are no differences (or if the value is within the defined tolerance), a new screen Simulation Results appears. You can check the simulation results in Overview and Details area. | The supplier invoice is complete to post. |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message Invoice xxx has been posted. |  |

### International

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
| 3 | Enter Purchase Order Document Type | Make the following data:Order Type: NB (Standard PO)Choose Enter. | All data are entered, the item detail screen opens. |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplier: for example, <17411710> (U.S.)Note We are using <17411710> as an example to show an international stock transfer order between your company and an American company. You may enter a different company (from another country/region)'s Supplier value to show an international intercompany stock transfer order.On the Header / Org. Data tab:Company Code: 3310Purchasing Org.: 3310Purchasing Group: 002On the Header / Partners tab:Partner Function.: PINumber: <17401710> (U.S.)Note You may refer to the note above for entering a different company (from another country/region)'s Supplier value.On the Item Overview tab:Material: TG11(without batch management)； TG21/ TG22(with batch management)Quantity: x pcDelivery Date: <any date in the future>Plant: 3310Storage Location: 331AOn the Item Details Invoice tab:Tax Code: <Input Tax Code>Then choose Enter.Note Currently the system triggers an availability check. Based on the results of the checks, if requested availability cannot be fulfilled, the Confirmation Proposal screen shows up and the user needs to take a decision based on the result of the checks. | All data are entered, the item detail screen opens. |  |
| 5 | Choose Goods Receive with Inbound Delivery | Make the following data:In item Details and on Confirmations tab:Conf.Control: section Inbound Delivery |  |  |
| 6 | Save Purchase Order | Choose the Save button and when the purchase order number is displayed, write it down for further use.Note If Flexible Workflow for Purchase Orders has already been activated,log on to the SAP Fiori launchpad as a Purchasing Manager role to approve your purchase orders. | A new Purchase Order is created. Purchase Order Number is displayed.Write down the Standard Purchase Order number for further usage. |  |

#### Create Replenishment Delivery for Stock Transfer Order

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
| 4 |  | Go to tab: Purchase OrdersEnter PO number which is created in previous Step.Choose Run. |  |  |
| 5 | Create Delivery | Select stock transfer orders from the list. Choose Background to Create Delivery in Background. | Activities Due for Shipping “Purchase Orders, Fast Display” screen appears. |  |
| 6 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the Outbound delivery number shown in the SD Doc. field | An outbound delivery is created. |  |

#### Create Pro Forma Invoice (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Create Intercompany Billing Document | Choose billing type Pro Forma Invoice for Delivery (F8) and maintain billing date, for example, current date. Enter delivery number, then press Enter. |  |  |
| 4 | Save | Choose Save. | F8 billing document is created. |  |

#### Pick and Post Goods Issue for Stock Transfer Order

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
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Cross-Company XXXXXXXX: Overview screen displays. |  |
| 4 | Check Batch Split | Navigate to the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 5 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to ex-pand sub item(s), enter quantity equal to delivery Qty in Picked Qty field for sub item.If batch spilt doesn't exist, enter quantity equal to Delivery Qty in Picked Qty field for picking related item(s). | The system shows the message: Replen.Cross-Company xxxxxxxx has been saved. The screen returns to Change Outbound Delivery screen. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

#### Check Batches (Optional)

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
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Cross-Company XXXXXXXX: Overview screen displays. |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, select the Batch Split Indicator field, and check the batch number assignment. | Batch numbers are assigned to the materials. The batch numbers are required to be entered during the Post Goods Receipt step. |  |
| 5 | Save Document | Choose Save. |  |  |

#### Check Status of Stock Transfer

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
| 1 | Log On | Log on to the SAP Fiori launch Pad as a Warehouse Clerk. | The Fiori launch Pad displays. |  |
| 2 | Access the App | Open Display Stock in Transit (MB5T). | The Display Stock in Transit screen displays. |  |
| 3 | Enter Transfer Order Data | Make the following entries:Material Number: TG11Receiving Plant: 3310Then choose Execute. | You receive an overview of the stock transfer orders that are currently in transit. This concerns all materials that have left the supplying plant and have not yet reached the receiving plant. |  |

#### Post Goods Receipt for Stock Transfer Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Acess the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Search for Purchasing Document | Open Purchasing Document Search . | A list of purchasing documents displays. |  |
| 4 | Select the Stock Transfer Order | Select your purchase order. | The system displays the data for the goods receipt on the Post Goods Receipt screen. |  |
| 5 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: xxxPrinting (Controls output management after posting): Individual slip |  |  |
| 6 | Enter Batch Numbers | Enter Batch numbers with which has been as-signed to the Outbound Delivery on the item.Note The batch number assignment is requied when the material master data is batch management relevant. | The batch number has been assigned to the item. |  |
| 7 | Select Item and Post Goods Receipt | Select the items for which a goods receipt is to be posted (the storage location must be specified, if not in the PO).Enter the following data:Storage Location: for example, 331AChoose Post. | The Post is activated.The Success screen displays. The system displays the message document(s) created: Material Document XXX. |  |

Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Acess the App | Open Overdue Materials - Stock in Transit (F2139). | The Overdue Materials - SiT screen displays. |  |
| 3 | Select Criteria | Enter the following data:Material: TG11choose Go. |  |  |
| 4 | Check the Stock Transfer Order | Check the quantity under the Goods issue Quantity for your stock transfer order. | You will see Goods issue Quantity. |  |
| 5 | Post Goods Receipt for Purchasing Documents | Select the purchasing documents, choose Post Goods Receipt for Purchase order. | Goods Receipt screen displays. |  |
| 6 | Post | Choose Select item, enter storage location and choose Post. | A system message material document xxxxxxxxx posted is displayed. |  |

#### Inbound Delivery Processing (optional)

##### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The Conf.Control: Inbound Delivery has been chosen in the previous step Create Intercompany Stock Transfer Order.

Procedure

This activity confirms that all the materials have been put away in the correct quantities.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launch Pad as a Receiving Specialist. | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP). | The Inbound Deliveries for Putaway screen appears. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then click Execute:Purchasing document: Enter the Stock Transfer Number Created in the Previous Step.Delivery Date: <Delete the Default Date>. | The selected Inbound Delivery appears. |  |
| 4 | Change the Inbound Delivery | Check the selected Inbound deliveries and choose Change Inbound Deliveries. | The Inbound Delivery XXX Change: Overview screen appears. |  |
| 5 | Confirm Quantities for Putaway without Batch Assignment | Under Item Overview tab, enter:Putaway Qty: XXXNote The put away quantity should equal to the delivery Qty.Choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message appears. |  |
| 6 | Confirm Quantities for Putaway with Batch Assign-ment | Under Stock Placement tab, select the Batch Split Indicator field of the item and expand the batch items of the main item, enter:Putaway Qty: XXXThen put away quantity should equal to the Delivery Qty of the batch item.Choose Save. | Back to the Inbound Deliveries for Putaway screen andInbound Delivery XXX has been savedmessage appears. |  |

##### Post Goods Receipt for Inbound Delivery

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
| 2 | Access the APP | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Purchasing document: <Enter Stock Transfer Order Number Created in the Previous Step>.Delivery Date: <Delete the Default Date>. | The Goods Receipt for Inbound Deliveries to be Posted screen shows up.The selected Inbound Deliveries is shown. |  |
| 4 | Change the Inbound Delivery | Check the selected Inbound deliveries and click Post Goods Receipt.The Specify Actual Goods Receipt Date screen appears and choose Continue. | Goods Receipt posted.A success message appears. |  |

#### Check Status of Stock Transfer

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
| 1 | Log On | Log on to the SAP Fiori launch Pad as a Warehouse Clerk. | The SAP Fiori launch Pad dispalys. |  |
| 2 | Access the App | Open Display Stock in Transit (MB5T) | The Display Stock in Transit screen dispalys. |  |
| 3 | Enter Transfer Order Data | Make the following entries:Material Number: TG11Receiving Plant: 3310Then choose Execute. | The stock transfer orders will not be displayed in this report if all materials have reached to receiving plant. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF04 (VF04). | The Maintain Billing Due List screen displays. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as sold-to party. In the Documents to Be Selected filter, choose Delivery-Related Intercompany Billing.Choose Display Billing List. | A list of delivery-related billing due list items displays. |  |
| 4 | Select Billing Due List Item | Select a row and set a check mark next to the billing due list item that you want to create a billing document for. | The appropriate billing due list item is selected. |  |
| 5 | Create and Display Invoice | Choose Individual Billing Document at the bottom of the screen.Choose Save. | The system generates a billing document. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

This process step shows you how to create supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Acess the App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries:Transaction: <Invoice>Company Code: 3310Gross Invoice Amount: <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(enter 00 + invoice number from invoicing party)Invoice Party, for example, 17401710In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <XXX>Currency: <XXX>(change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(enter 00 + invoice number from invoicing party)Invoice Party:for example, 17401710Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Create Supplier Invoices screen displays.The Exchange Rate should be changed from USD to EUR according to the customizing settings. The Exchange Rate is changeable. |  |
| 4 | Enter Purchase Order References | In Purchase Order References field, make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxxxxxxx> | The Purchase Order References screen displays. |  |
| 5 | Check the Purchase Order Items Data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 6 | Check Tax Code | In the section Tax, check if there is tax code information and enter the tax amount when the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items. | If there is no tax, specify the tax code <Input Tax Code>. |
| 7 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), a new screen Simulation Results appears. You can check the simulation results in Overview and Details area. | The supplier invoice is complete to post. |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message Invoice xxx has been posted. |  |

## Appendix

### Scheduling Job (Alternative)

#### Job Scheduling for Delivery Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays.The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new Job. | The New Job screen displays. The Job Template should be displayed as Schedule Delivery Creation for Purchase Orders by default. |  |
| 4 | Scheduling Options | Choose Step 2 to define scheduling for the batch job if necessary. | Depending on the scheduling options, the delivery creation is started immediately or at a specific time. |  |
| 5 | Job Parameters | Choose Step 3 to define Parameters, and make at least the following entries:Shipping Point: 3320Purchasing Document: Stock Transport Order # created aboveThen choose Check. | The system displays the message You can go ahead and schedule the job. |  |
| 6 | Schedule | Choose Schedule. | A delivery creation job is scheduled.Screen goes back to Application Jobs. |  |
| 7 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finished, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list is refreshed. | The Job Details screen displays. |  |

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
> Flagged while digesting this document, not verified: Appendix scheduled delivery job uses Shipping Point 3320, while the master data and the manual delivery creation (VL10B) for the domestic supplying side use Shipping Point 3330 (3320 is listed only as a company code).

> [!warning] Conflict
> Flagged while digesting this document, not verified: The International 'Post Goods Receipt for Inbound Delivery' step uses app F0843 in the test steps and overview table, while the same step in the Domestic flow uses VL06IG.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/advanced-intercompany-stock-transfer-5hp-ae-test-script-sap-s-4hana-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1P9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 73,913 chars in the whole document
