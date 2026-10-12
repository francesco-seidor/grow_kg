---
id: 15-retail-operations/test-script-merchandise-allocation-5fl-ae-sap-s-4hana-cloud-public-edi
title: "Test Script: Merchandise Allocation (5FL_AE) - SAP S/4HANA Cloud Public Edition (5FL_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition retail test script, scope item 5FL: create, change, follow on and delete allocation tables to push merchandise to stores."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/merchandise-distribution-and-allocation]
aliases: [5FL_S4CLD2608_BPD_EN_AE]
keywords: [Merchandise Distribution and Allocation, allocation tables, merchandise distribution, recall allocation, follow-on documents, allocation table deletion, returns purchase orders, scope item testing, purchase orders, job scheduling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FL_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1081
topic: 15-retail-operations/merchandise-distribution-and-allocation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Merchandise Allocation (5FL_AE) - SAP S/4HANA Cloud Public Edition (5FL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Merchandise Distribution and Allocation** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Merchandise Allocation (5FL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856613)

[2 Prerequisites 4](#_Toc232856614)

[2.1 System Access 4](#_Toc232856615)

[2.2 Roles 4](#_Toc232856616)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856617)

[2.4 Business Conditions 5](#_Toc232856618)

[2.5 Preliminary Steps 6](#_Toc232856619)

[2.5.1 Create Purchase Order 6](#_Toc232856620)

[2.5.2 Create Stock in Store 7](#_Toc232856621)

[2.5.3 Stock Overview – Single Material 8](#_Toc232856622)

[3 Overview Table 10](#_Toc232856623)

[4 Test Procedures 11](#_Toc232856624)

[4.1 Create Allocation Table 11](#_Toc232856625)

[4.1.1 Create Allocation Table with Reference to the Purchase Order 11](#_Toc232856626)

[4.1.2 Create Allocation Table Manually 13](#_Toc232856627)

[4.1.3 Create Recall Allocation Table (Optional) 14](#_Toc232856628)

[4.2 Change Allocation Table 16](#_Toc232856629)

[4.3 Display Allocation Table (Optional) 17](#_Toc232856630)

[4.4 Generate Follow-On Document 18](#_Toc232856631)

[4.4.1 Create Follow-On Document (WA08) 18](#_Toc232856632)

[4.4.2 Schedule Jobs for Follow-On Documents 19](#_Toc232856633)

[4.5 Allocation Table Factsheet (Optional) 21](#_Toc232856634)

[4.6 Change Returns Purchase Order 21](#_Toc232856635)

[4.7 Display Purchase Order (Optional) 22](#_Toc232856636)

[4.8 Delete Allocation Tables (Optional) 23](#_Toc232856637)

[4.9 Delete Allocation Tables in Emergency (Optional) 24](#_Toc232856638)

[5 Appendix 26](#_Toc232856639)

[5.1 Process Integration 26](#_Toc232856640)

[5.1.1 Preceding Processes 26](#_Toc232856641)

[5.1.2 Succeeding Processes 26](#_Toc232856642)

## Purpose

Overview

Most retailers must push merchandise to stores to support certain scenarios. This is for various reasons, such as one-off articles, stock reduction in distribution centers, special offer from supplier, end-of-season clearance, and so on.

The push scenario complements the pull scenario realized via consumption-based replenishment. For more information, see the Replenishment Planning for Stores (3I7) scope item . The planning tool for the push scenario is the so-called allocation table. First, the user enters relevant articles, the quantities to be distributed, store groups, and various dates (order date, receiving dates for stores and distributions centers, and optionally, delivery phases). One of several available types of merchandise distribution is then selected, including:

- Distributions centers procure from an external supplier and distribute merchandise to stores
- Available stock of distribution centers is distributed to stores
- Direct store delivery from external suppliers

The quantities for each receiving store are calculated based on different available options (such as ratios or strategies). Once the planning is finalized, the respective orders can be created automatically; the orders are handed over to operational procurement for execution.

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

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL | Allocation and Merchandise Distribution | SAP_BR_ALLOCATOR_RETAIL |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing / Retail Sourcing and Contracting | SAP_RFM_SPT_PURCHASING_PC / SAP_RFM_SPT_SOURCING_PC |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In the following table, sample values for master data are provided for the country/region US. You can either use the country-dependent sample master data or create and use your own master data while executing the test procedure. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Article | R_1006 | My Best Frozen Strawberries | Single article |
| Merchandise category | R1193001 | Frozen Fruit |  |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| Store (Site) | 3340 | Store 3340 AE |  |
| Store (Site) | 3341 | Store 3341 AE |  |
| Storage locations store | 994A | St.Loc.Neg.Stock |  |
| Storage location distribution center | 995A | Storage Loc. DC |  |
| Storage location distribution center | 995R | St.Loc.Return |  |
| Purchasing organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 | Group 001 |  |
| Site group | R_SITEGROUP_AE_01 | R_SITEGROUP_AE_01 |  |
| Company Code | 3310 | Company Code 3310 |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, the following business conditions must be met before you can test this scope item,

| Scope Item ID | Business Condition |
| --- | --- |
| 3I1 - Products for Retail | Must be run before this test script. |
| 3I3 - Sites for Retail | Must be run before this test script. |
| 5FJ - Product Taxonomies for Retail | Must be run before this test script. |

### Preliminary Steps

#### Create Purchase Order

Use

This process step shows you how to create allocation table using a purchase order in a process variant. The prerequisite is to create a manual purchase order. Each purchase order items must have the value, in the field Distribution Relevant, equal to 1 under “Retail” tab, so that the allocation can be created for each purchase order line item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser (Retail) |  |  |
| 2 | Access the app | Open Create Purchase Order - Advanced (ME21N) app. |  |  |
| 3 | Basic settings | Within the Create Purchase Order AppSelect the menu as follows:Menu > Settings > Interaction Design > VisualizationEnable the following Settings:Show drop-down list with keys and Sort drop-down list by their keysSelect Save | Key values of drop-down list are displayed. |  |
| 4 | Make entries for header level | Enter the following data:Type: NB Standard PO andSupplier: for example 33213002Press ENTERPrompts to fill the below fields in the header section:Purch.Org: for example 3310Purch. Group : 001Company Code: for example 3310Choose ENTER. | The values entered on the respective value fields are accepted based on the validation. |  |
| 5 | Make entries for item level | Enter the following data on Item Overview:Material: R_1006PO Quantity: 1000Plant ( Plnt): for example 3350Storage Location: 995ANote Maintain price in field Net Price, if not auto populated. | The values at the item level are accepted based on the validation. |  |
| 6 | Trigger enter | Choose ENTER | Depending on data entered, warning messages are displayed. |  |
| 7 | Fill the fields | Select on the article line-item tab RetailSelect 1 Distribution-Relevant: Putaway from the drop-down listNote This step is necessary to create allocation table with reference to the purchase order. |  |  |
| 8 | Save the purchase order | Select SavePlease take a note of PO number. | Standard PO created with the number XXXXX. |  |

Result

The purchase order is created which would be used to create the allocation table.

#### Create Stock in Store

Use

To execute this scope item, the materials must be available in stock. This step is only needed for the recall scenario (see [Create Recall Allocation Table (Optional)](#unique_9) [page ] 14), where a recall allocation table will be created to allocate a specific quantity of merchandise among the stores to be returned to distribution center and then returned from distribution center to the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk |  |  |
| 2 | Access the app | Open Post Goods Movement (MIGO) app. |  |  |
| 3 | Input movement type | Make the following entry and select Enter :Init . entry of Stbal:561Executable Action in Transaction MIGO: A01 Goods ReceiptReference Document for MIGO Transaction: R10 Other | Entry is accepted. |  |
| 4 | Enter material | Close the header data and expand the detail data area. On the Goods Receipt Other Screen: Material tab, make the following entry and select Enter:Material: R_1006 | Entry is accepted. |  |
| 5 | Enter quantity data | On the Goods Receipt Other screen: Quantity tab, make the following entry and select Enter:Qty in Unit of Entry: 10Unit of Entry: <PC>Ext. Amount LC: 20 | Entry is accepted. |  |
| 6 | Input on the goods receipt other screen: where tab | On the Goods Receipt Other screen: Where tab, make the following entries and select Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant for example 3340Storage Location: for example 994A | Entry is accepted. |  |
| 7 | Save your entries | select Post. | A message is displayed as Material document 490000XXX posted. |  |

Result

The stock of 10 PC is available in the store 3340.

#### Stock Overview – Single Material

Use

This process step shows you how to display material stock in the storage locations of a plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk |  |  |
| 2 | Access the app | Open Stock - Single Material (F1076) app. |  |  |
| 3 | Enter material | Make the following entries:Material: R_1006Select Enter. | The stock of material R_1006 in all the sites and storage locations are displayed in the Stock - Single Material (F1076) screen. |  |

Result

The stock is available in the store 3340 for article R_1006.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Allocation Table |  |  |  |
| [Create Allocation Table with Reference to the Purchase Order](#unique_12) [page ] 11 | Allocator (Retail) | Create Allocation Table (WA01) | Allocation Table is created with reference to Purchase Order. |
| [Create Allocation Table Manually](#unique_13) [page ] 13 | Allocator (Retail) | Create Allocation Table (WA01) | Allocation Table is created manually. |
| [Create Recall Allocation Table (Optional)](#unique_9) [page ] 14 | Allocator (Retail) | Create Allocation Table (WA01) | Recall allocation table is created. |
| [Change Allocation Table](#unique_14) [page ] 16 | Allocator (Retail) | Maintain Allocation Table (WA02) | Allocation table is changed. |
| [Display Allocation Table (Optional)](#unique_15) [page ] 17 | Allocator (Retail) | Display Allocation Table (WA03) | Allocation table is displayed. |
| [Generate Follow-On Document](#unique_16) [page ] 18 |  |  |  |
| [Create Follow-On Document (WA08)](#unique_17) [page ] 18 | Allocator (Retail) | Generate Follow-On Documents - Allocation Table (WA08) | Follow-on documents are generated. |
| [Schedule Jobs for Follow-On Documents](#unique_18) [page ] 19 | Allocator (Retail) | Schedule Follow-on Document Generation - Allocation Table (F5327) | Job is scheduled for follow-on documents. |
| [Change Returns Purchase Order](#unique_19) [page ] 21 | Purchaser (Retail) | Change Purchase Order - Advanced (ME22N) | Returns Purchase order is changed. |
| [Display Purchase Order (Optional)](#unique_20) [page ] 22 | Purchaser (Retail) | Manage Purchase Orders (Version 2) (F0842A) | Purchase Order is displayed. |
| [Delete Allocation Tables (Optional)](#unique_21) [page ] 23 | Allocator (Retail) | Delete Allocation Table (WA09) | Allocation table is deleted. |
| [Delete Allocation Tables in Emergency (Optional)](#unique_22) [page ] 24 | Allocator (Retail) | Force Delete Allocation Table (WA09H) | Allocation table is deleted. |

## Test Procedures

This chapter describes test procedures for each process step that belongs to this scope item.

### Create Allocation Table

#### Create Allocation Table with Reference to the Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an allocation table in SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business to allocate a specific quantity of merchandise among the stores. The allocation table contains all the important information on how the merchandise is to be distributed, such as the articles to be allocated, the source of supply, the recipients, the quantity each recipient is to receive, and the delivery dates. The allocation table creation is driven by an existing purchase order where the DC can plan to distribute items to the stores based on the purchase order quantity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Create Allocation Table (WA01) app |  |  |
| 3 | Make entries | On the Create allocation table screen, make the following entries:Allocation Table Type : 0002(1- step alloc int)Note follow-on documents will create only store order with 1 step allocation.1 Step Allocation is used to allocate the goods among the stores from distribution centerPurchasing Organization: for example 3310Purchasing Group: 001 | Field values are accepted. |  |
| 4 | Fill required fields | On the top corner in the screen, select on >Menu select Allocation table > select Create with ref > select To Purchase orderOn Create allocation table : Purchase order Reference popup screen, under selection based on header data,Enter Purchase Order: PO Number Created in preliminary step [Create Purchase Order](#unique_7) [page ] 6Select Execute. | A popup message is displayed. |  |
| 5 | Select all entries | Select Select All in MoreSelect Adopt in alloc tbl | Purchase order data is adopted in allocation table. |  |
| 6 | Fill the fields | On the Create allocation table screen, make the following entries:Allocation Table Description: <Description>Plant Delivery Date: today’s date + 4 (Days)DC Delivery Date: today’s date + 3 (Days)Enter dates in future and DC delivery date one day less than plant delivery dateSelect ENTER. | Entry is accepted. |  |
| 7 | Site group assignment | Navigate as follows:Select the line item.Select Item button, under Menu.On the Create allocation table: Fast Change Item Data (For Selected Items) screen, make the following entries:Plant group: for example R_SITEGROUP_AE_01Select ENTERSelect Check then select ExecuteIf a message ‘…Change item nonetheless?’ is displayed, select ContinueThe message “Fast entry results: ... item(s) selected; ... item(s) changed; errors: 0” is displayed, select ContinueNote Item category: F Proposed | An allocation table is created. |  |
| 8 | Save | Select Save to save your entries.Make a note of the Allocation Table.Note Refer step – [Change Allocation Table](#unique_14) [page ] 16 to change the allocation table and step – [Display Allocation Table (Optional)](#unique_15) [page ] 17 to display the allocation table. | An allocation table is created. |  |

#### Create Allocation Table Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an allocation table in SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business to allocate a specific quantity of merchandise among the stores. The allocation table contains all the important information on how the merchandise is to be distributed, such as the articles to be allocated, the source of supply, the recipients, the quantity each recipient is to receive, and the delivery dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Create Allocation Table (WA01) app |  |  |
| 3 | Make entries | On the Create allocation table screen, make the following entries:Allocation Table Type : 0002(1-step Alloc int)Purchasing Organization : for example 3310Purchasing Group : 001Select Continue | Values entered in the initial screen of allocation is accepted. |  |
| 4 | Fill the fields | On the Create allocation table screen, make the following entries:Allocation Table Description : <Description>Plant Delivery Date : today’s date + 4 (Days)DC Delivery Date : today’s date + 3 (Days)Enter dates in future and DC delivery date one day less than plant delivery date.Material: for example R_1006Plan Quantity: 10Select ENTERNote All the dates must be working days in future. | Field values are accepted. |  |
| 5 | Site group assignment | Select the line item and select Item button, on the Create allocation table: Fast Change Item Data (For Selected Items) screen, make the following entries:Plant group: for example R_SITEGROUP_AE_01Select ENTERSelect Check then select ExecuteIf a message ‘…Change item nonetheless?’ is displayed, select ContinueThe message “Fast entry results: ... item(s) selected; ... item(s) changed; errors: 0” is displayed, select ContinueNote Item category: F Proposed |  |  |
| 6 | Save | Select Save to save your entriesMake a note of the Allocation Table number. | An allocation table is created. |  |

#### Create Recall Allocation Table (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a recall allocation table to allocate a specific quantity of merchandise among the stores to be returned to DC and then returned from DC to the Supplier.

|  |
| --- |
| Note There can be situations where at the end of promotional period, DC recalls all the remaining promotional articles from the store. There can also be a situation where the defective articles sent to the stores must be returned to the vendor via the DC. We will cover the second use case in the following test procedure using Advanced Returns Management. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Create Allocation Table (WA01) app |  |  |
| 3 | Make entries | On the Create allocation table screen, make the following entries:Allocation Table Type : 0004(2 step return alloc)Note The follow-on document in the following steps would be created for return purchase order and return stock transfer order.Purchasing Organization : for example 3310Purchasing Group : 001Select Continue | Values entered in the initial screen of allocation is accepted. |  |
| 4 | Fill the fields | On the Create allocation table screen, make the following entries:Allocation Table Description: <Description>Plant Delivery Date : today’s date + 3 (Days)DC Delivery Date : today’s date + 4 (Days)Material: R_1006Plan Quantity: 10ENTERNote All the dates must be working days in future | Field values are accepted. |  |
| 5 | Enter plant | Select the line item and select Plants, make the following entries:Plant: for example 3341Planned Quantity: 10Choose Back |  |  |
| 6 | Supplier | Select the line item and then select Distribution Centre s and make the following EntrySupplier: 33213002Note Select Sources of Supply to get a list of supplier | Distribution centre maintained for XX-line item is displayed. |  |
| 7 | Save | Select Save to save your entries.Make a note of the Allocation Table number. | An allocation table is created. |  |

### Change Allocation Table

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check recipient matrix and possible to look of all variants of the generic article with the quantities for all stores. Furthermore, the recipient matrix can be used for all other articles (single articles, prepack, set).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Maintain Allocation Table (WA02) app. |  |  |
| 3 | Fill the input | Enter the Allocation Table (created in previous steps) and select Continue | Entry is accepted. |  |
| 4 | Adopt changes | Select the line itemChoose Recipient MatrixChange the article quantities for one or two recipients (remember your changes!) and select Adjust Quantities > Quantities changed message is displayedSelect Back to go back to the allocation tableMark all items of the allocation table by using More > Select All (Shift +F8) and check the completeness of the allocation table by using incompleteness logMessage “ No exceptions occurred during Incompleteness check” is displayed when there is no error occurred and Select ContinueShow the log and if there are some errors, go back to the recipient matrix to change the quantities again (analogue see above) till the ordered quantities are equal the distributed quantities | Article quantities are changed. |  |
| 5 | Save | If there are no errors, go back and save the changes by selecting Save | Changes to alloc. tbl XXX posted. |  |

### Display Allocation Table (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the allocation table which has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Display Allocation Table (WA03) app. |  |  |
| 3 | Fill the inputs | Enter the Allocation table (created in previous steps)And select ENTER | Details of allocation table are displayed. |  |

### Generate Follow-On Document

There are two options to generate the follow-on documents, as described below,

#### Create Follow-On Document (WA08)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate follow-on documents for allocation table.

|  |
| --- |
| Note The check box supplier purchase order not to be selected if the allocation table is created with reference to a purchase order (step [Create Allocation Table with Reference to the Purchase Order](#unique_12) [page ] 11). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Generate Follow-On Documents - Allocation Table (WA08) app. |  |  |
| 3 | Provide input values | On the initial screen, make the following entry in selection criteria.Select parameters forUnder Doc Cats select the following entries:Purchase Orders : ‘ X’ ” (only applicable for Recall allocation table)Stock Transport Orders : ‘X’Under General Criteria select the following entries:Allocation Table:(Enter the Allocation table created manually in Step [Create Allocation Table Manually](#unique_13) [page ] 13 and Step [Create Recall Allocation Table (Optional)](#unique_9) [page ] 14 )Latest Generation Date: today’s date to : today’s date + 10 daysSelect Execute | A Worklist is created with the list of allocation table items displaying supplier/ DC information and the relevant document type for the PO/STO generation. |  |
| 4 | Generate documents | All the documents will be auto selectedSelect Generate DocumentsMake a note of all the POs, return POs, STOs and Return STOs created. | Follow- on documents (PO and STOs) generated.Status becomes green, if generated. Select Generation log. It shows PO and STO document number. |  |

#### Schedule Jobs for Follow-On Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create follow-on document via Job scheduling.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Schedule Follow-on Document Generation - Allocation Table (F5327) app. |  |  |
| 3 | Provide input values | On the initial screen, select Create make the following entry in selection criteria.Select Job Template: Schedule Follow-on Document Generation - Allocation TableJob Name: Schedule Follow-on Document Generation - Allocation TableSelect Step-2check Start Immediately: ‘X’Select Step-3 and make the following entry in selection criteriaSelect parameters forUnder Document Category section, select the following entry:Stock Transport Order : ‘X’Under General Criteria section, select the following entries:Allocation Table: Enter the allocation table created in Step [Create Allocation Table with Reference to the Purchase Order](#unique_12) [page ] 11Select on F4 help in latest generation date:From : today’s dateto: today’s date + 10Select OkUnder section Stock Transport Order : ensure following entries are selectedStandard Items: ‘X’Return Items : ‘X’ | Entry is accepted. |  |
| 4 | Check | Select Check for validating. | A popup message is displayed. |  |
| 5 | Schedule | Select Schedule , following message appears Job Schedule Follow - on Document Generation - Allocation has been scheduled. | The job is done, and follow-on document generated. |  |
| 6 | Check result output | Refresh once if result not generated. Select the Result and validate the follow-on document generated. Make a note of the stock transfer order generated. | Follow-on document is generated. |  |

### Allocation Table Factsheet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to access the allocation table factsheet to display the allocation table status and other details i.e. General Information, Receiving Stores, Purchase Orders etc.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Allocation Table (F0333A) app. |  |  |
| 3 | Fill the inputs | Enter the Allocation table(Created in Step [Create Allocation Table with Reference to the Purchase Order](#unique_12) [page ] 11) and select GO | The allocation table, status, and creation log are displayed in the Allocation table overview screen. |  |
| 4 | Display details | Select the right-hand side arrow to display the details of allocation table. | The details of the allocation table, that is, general information, item details, receiving stores, purchase orders etc. are displayed in the Allocation table details screen. |  |

### Change Returns Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change the storage location in the Returns PO from the default value proposed by the article master to returns storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser (Retail) |  |  |
| 2 | Access the app | Open Change Purchase Order - Advanced (ME22N) app. |  |  |
| 3 | Open return PO details | Select Other Purchase OrderEnter the following and select Other DocumentPur. Order: XXXXXX(Enter the Return PO created in Step [Create Follow-On Document (WA08)](#unique_17) [page ] 18) | The values entered on the respective value fields are accepted on validation. |  |
| 4 | Change item entry | Select Display/ChangeChange the following data on item level:Stor. Location: for example 995ASelect ENTER |  |  |
| 5 | Save your entries | Select SaveNote the return PO number below | Enh. Rets. To Supplier XXXXXXXXXX changed message is displayed. |  |

### Display Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the Purchase order which has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser (Retail) |  |  |
| 2 | Access the app | Open Manage Purchase Orders (F0842A) app. |  |  |
| 3 | Fill the inputs | Enter the Purchase order number (from step [Allocation Table Factsheet (Optional)](#unique_24) [page ] 21), and select 'GO ’ | Purchase Order overview is displayed. |  |
| 4 | Display purchase order | Select the Radio and select arrow on right corner | The purchase order is displayed.Under item tab Retail: Allocation table number and allocation table relevant field is displayed. |  |

### Delete Allocation Tables (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to delete the allocation table with activity status “1 - Not Active” or “4 - Done”.

|  |
| --- |
| Note You need to have Follow-On Documents - Purchase Orders/Stock Transfer Orders to be created completely for having Allocation Table in "4-Done" Status.Kindly note for Allocation Table with status as "4-Done" if ILM Object is Active then Allocation Table cannot be deleted using this App. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad asAllocator (Retail) |  |  |
| 2 | Access the app | Open Delete Allocation Table (WA09) app. |  |  |
| 3 | Give the inputs | Make the following entries:In Deletion for section:Alloc tab: 'x' selected by defaultIn organizat. data section:Purchasing organization: for example 3310Purchasing Group : 001In General Data section:Allocation table: Enter a new allocation table without a follow-on document (Create a new table manually through the Step Create Allocation Table Manually)In processing status section:Done: X selected by defaultSelect Execute | An allocation table that needs to be deleted is displayed. |  |
| 4 | Execute | Select the respective allocation table you want to delete. | The allocation table is accepted, and a popup message is displayed. |  |
| 5 | Delete | Select Delete Allocation Table. Pop up will display for confirmation “Do you want to delete the selected allocation table”Select YsXXX Allocation table with a total of XXX items deleted. | An allocation table is deleted. |  |

### Delete Allocation Tables in Emergency (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to delete the allocation table with activity status “2 – Partially active” or “3 - Active”.

|  |
| --- |
| Note In order to have allocation table status as “2 – Partially active” or “3 - Active” , the follow-on document generation in previous step should be done partially for few of the line items. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Allocator (Retail) |  |  |
| 2 | Access the app | Open Force Delete Allocation Table (WA09H) app. |  |  |
| 3 | Give the inputs | Make the following entries:Allocation table: XXX (Enter the allocation table with “3-Active” status).Select Execute | The allocation table is accepted, and a popup message is displayed. |  |
| 4 | Delete | Select YESAllocation table deleted | An Allocation table is deleted. |  |

## Appendix

### Process Integration

We can create Supplier order (Purchase Order), Return PO, Stock Transfer Rrder (STO), and Return STO for distribution center through allocation.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| Not applicable | Not applicable |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

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
> Flagged while digesting this document, not verified: Change Returns Purchase Order: purpose says to change the PO item storage location to the returns storage location, but the step enters 995A (listed in sample data as 'Storage Loc. DC'); 995R is the listed 'St.Loc.Return'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/merchandise-distribution-and-collective-purchase-order-71o-ae-test-scr]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,740 chars in the whole document
