---
id: 15-retail-operations/returns-from-store-5fr-ae-1086
title: Returns from Store (5FR_AE) (5FR_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5FR_AE: returning merchandise from a store to a distribution center via returns stock transport order."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/store-returns]
aliases: [5FR_S4CLD2608_BPD_EN_AE]
keywords: [Returns from Store, store returns, test script, returns stock transport order, outbound delivery, inbound delivery, material inspection, goods issue, goods receipt, stock status]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FR_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1086
topic: 15-retail-operations/store-returns
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Returns from Store (5FR_AE) (5FR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Returns from Store** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Returns from Store (5FR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856765)

[2 Prerequisites 4](#_Toc232856766)

[2.1 System Access 4](#_Toc232856767)

[2.2 Roles 4](#_Toc232856768)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856769)

[2.4 Preliminary Steps 5](#_Toc232856770)

[2.4.1 Return Reason “Wrong Product Delivered” 5](#_Toc232856771)

[2.4.2 Return Reason “Too much Delivered” 6](#_Toc232856772)

[2.4.3 Return Reason “Product Damaged” 6](#_Toc232856773)

[2.4.4 Return Reason “Product Defective” 6](#_Toc232856774)

[2.4.5 Create Stock in Store 6](#_Toc232856775)

[2.4.6 Check Stock Availability 7](#_Toc232856776)

[3 Overview Table 9](#_Toc232856777)

[4 Test Procedures 10](#_Toc232856778)

[4.1 Create Returns Stock Transport Order 10](#_Toc232856779)

[4.2 Create Outbound Delivery 11](#_Toc232856780)

[4.3 Perform Picking and Post Goods Issue for Outbound Delivery 12](#_Toc232856781)

[4.4 Check Stock Status 13](#_Toc232856782)

[4.5 Check Inbound Delivery 14](#_Toc232856783)

[4.6 Perform Post Goods Receipt 15](#_Toc232856784)

[4.7 Perform Material Inspection 16](#_Toc232856785)

[4.8 Check Stock Status 17](#_Toc232856786)

[5 Appendix 19](#_Toc232856787)

[5.1 Process Integration 19](#_Toc232856788)

[5.1.1 Preceding Processes 19](#_Toc232856789)

[5.1.2 Succeeding Processes 19](#_Toc232856790)

## Purpose

Overview

A store may need to return merchandise to a distribution center for various reasons, such as quality recalls, end-of-season returns, or returns to balance stock shortages in other stores.

A store associate creates the stock transfer return order document. A store employee monitors the products due to be shipped and creates outbound deliveries as required. Once a return delivery is created, a picking list is generated for the products.

A store associate gathers the products and confirms the picked quantities. The goods issue is posted when the return delivery is complete. As a result, an inbound delivery is automatically created for the receiving distribution center as a follow-on document.

At the distribution center, a receiving specialist inspects the goods and confirms the put-away, referencing the inbound delivery.

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

The test should be conducted with the following system:

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
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK_RFM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Single Article | R_1006 | My Best Frozen Strawberries |  |
| Distribution Center | 3350 | DC 3350 AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Plant | 3340 | Store 3340 AE |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |
| Variant Article | R_1004003 | My Best Chocolat, Christmas Flavor, Diet |  |
| Display | R_2007 | Chocolate Bar DisplayComponents:R_1003001 - R_1003014 |  |
| Sales Set | R_1052 | My Best Blond Shampoo & ConditionerComponents:R_1051 and R_1052 |  |

### Preliminary Steps

#### Return Reason “Wrong Product Delivered”

During the goods receipt process the warehouse clerk detects that wrong material was delivered. Therefore the material was posted into the blocked stock and moved into the storage location for returns

This issue may have arisen as a result of the 3HQ test script (In-Store Merchandise Management)

#### Return Reason “Too much Delivered”

During the goods receipt process the warehouse clerk detects that too much material was delivered. Therefore the additional material was posted into the blocked stock and moved into the storage location for returns

This situation can be the result of the testscript 3HQ (Ordering, Receiving and Customer Inquiry in Store)

#### Return Reason “Product Damaged”

During the goods receipt process the warehouse clerk detects that the product was damaged during the transit. Therefore the material was posted into the blocked stock and moved into the storage location for returns.

This situation can be the result of the testscript 3HQ (Ordering, Receiving and Customer Inquiry in Store)

#### Return Reason “Product Defective”

During the goods receipt process, the warehouse clerk detects that defective product was supplied and hence the quality inspection failed. Therefore, the material was posted into return stock with status blocked.

This situation can be the result of the testscript 3HQ (Ordering, Receiving and Customer Inquiry in Store)

#### Create Stock in Store

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The action which was chosen last time is displayed. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | Movement type details are provided |  |
| 4 | Enter Material | Close the header data and expand the detail data area. On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: R_1006 |  |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: 100Unit of Entry: <PC> |  |  |
| 6 | Enter details under where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant 3340Storage Location: 994A |  |  |
| 7 | Save Your Entries | Choose Post. | . |  |

#### Check Stock Availability

Purpose

In this process step you can check the stock availability in Store.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the App | Open Display Advanced Stock Overview (RWBE) app. | Stock Overview screen is displayed. |  |
| 3 | Enter parameters | Enter the following data:Material: R_1006Plant: 3340Choose Execute. | Stock Overview: Full List screen is displayed. |  |
| 4 | Verify Stock | Check the availability of the mentioned material. | Unrestricted Use Stock is available for the material. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Stock Transport Order](#unique_13) [page ] 10 | Purchaser (Retail) | Create Purchase Order - Advanced (ME21N) | STO del return stock transport order is created. |
| [Create Outbound Delivery](#unique_14) [page ] 11 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound delivery for returns stock transport order is created. |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_15) [page ] 12 | Shipping Specialist | Change Outbound Delivery (VL02N) | Post Goods Issue is posted. |
| [Check Stock Status](#unique_16) [page ] 13 | Warehouse Clerk (Retail) | Stock - Single Material (F1076)Display Stock in Transit (MB5T) | Stock analysed. |
| [Check Inbound Delivery](#unique_17) [page ] 14 | Purchaser (Retail) | Display Purchase Order - Advanced (ME23N) | Auto created inbound delivery is noted. |
| [Perform Post Goods Receipt](#unique_18) [page ] 15 | Receiving Specialist | Change Inbound Delivery (VL32N) | Post Goods Receipt is performed for inbound delivery. |
| [Perform Material Inspection](#unique_19) [page ] 16 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Check Stock Status](#unique_20) [page ] 17 | Warehouse Clerk (Retail) | Stock - Single Material (F1076) | Stock analysed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Returns Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Enter Parameters | Select UD2 STO Del Return from dropdown listEnter the following details:Supplying Plant: 3350Doc.Date: <Current Date>Select Org.Data tab and enter below details:Purch. Org: 3310Purch. Group: 001Company Code: 3310 | Required parameters are defined. |  |
| 4 | Enter Parameters | Expand Item Overview sectionEnter below details:Material: R_1006PO Quantity: 2Deliv. Date: <Provide any future date>Plant: 3340 |  |  |
| 5 | Parameters that Gets Determined Automatically | In Item Overview sectionStorage Location: 994AIn Confirmatons tab in Item Details sectionConf. Control : 0004-Inbound Delivery | Parameters determined automatically. |  |
| 6 | Enter Parameters | Select Returns tab in the Header section.From the Return Reason drop down list, select 003-Product damagedFrom the Follow-Up-Activity drop down list, select 0004-Ship to Other PlantChoose Copy to Items. | Parameters are provided. |  |
| 7 | Save Return Stock Transport Order | Choose Save. | Returns Stock Transport Order xxxxxxxxxxx created.Make a note of return stock transport order number. |  |

### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the outbound delivery for the returns stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B) app. | Purchase Orders, Fast Display screen is displayed. |  |
| 3 | Enter Parameters | Enter below detail,CalcRuleDefltDlvCrDt: <blank>Choose Purchase Orders and enter the below detail:Purchasing Document: <Return Stock Transport Order>Choose Execute. | Activities Due for Shipping "Purchase Orders, Fast Display" screen is displayed. |  |
| 4 | Create Outbound Delivery | Select the Return Stock Transport Order entryChoose Background. | See Log for information about creating deliveries message is displayed. |  |
| 5 | Check the Outbound Delivery Number | Choose the newly created line item with the same Return Stock Order entryFrom the <!-- image omitted: unnamed -->(More) icon drop down list, select Show/Hide Delivery. | Outbound Delivery number xxxxxxxxx is displayed in the Document coloumn.Make a note of outbound delivery number. |  |

### Perform Picking and Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick and post goods issue for outbound delivery created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | Change Outbound Delivery (VL02N) screen is displayed. |  |
| 3 | Enter Parameters | Enter the Outbound Delivery :<Provide Outbound Delivery number>Choose Continue. | RST Outbound Dlv. xxxxxx Change: Overview screen is displayed. |  |
| 4 | Enter the Picked Quantity | Choose Picking.In the All Items section,Enter the below field as value in Deliv.Qty ,Picked Qty: <Deliv.Qty>Choose Enter. | OvrllPickStatus is displayed as C (Fully Picked). |  |
| 5 | Post Goods Issue | Choose Post Goods Issue. | Post goods issue initiated. |  |

### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check stock status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Option 1: Open Stock - Single Material (F1076) app. | The Stock - Single Material (F1076) screen is displayed. |  |
| 3 | Enter Material Data | Option 1:Enter the following details:Material : R_1006Choose Enter. | You receive an overview of the materials and of the returns stock transport orders that are currently in transit. It concerns all materials that have left the store and have not yet reached the Distribution Center. |  |

### Check Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you can check the inbound delivery for the return stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser (Retail). |  |  |
| 2 | Access the App | Open Display Purchase Order - Advanced (ME23N) app. | Display Purchase Order - Advanced (ME23N) screen is displayed. |  |
| 3 | Access Return Purchase Order | Choose Document Overview OnFrom the Selection Variants, select Purchase Orders. | Purchasing Document screen is displayed. |  |
| 4 | Access Returns Purchase Order | In the Program Selections section, enter below details:Purchasing Document : <Returns Purchase Order>Choose Execute. | Purchase Order is displayed in the Document overview section. |  |
| 5 | Select Return Purchase Order | Double click on the Return Purchase order. | Return purchase order is displayed. |  |
| 6 | Check Returns Overview | Choose Returns Tab,Choose Returns Overview. | Returns Overview for Returns Purchase Order xxxxxxxxxx screen is displayed. |  |
| 7 | Check Inbound Delivery | Check Inbound Delivery number in Document Number Column. | Inbound delivery number xxxxxxxx displayed.Make a note of inbound delivery number. |  |

### Perform Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you perform post goods receipt for inbound delivery.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Receiving Specialist. |  |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N) app. | Change Inbound Delivery (VL32N) screen is displayed. |  |
| 3 | Enter Inbound Delivery Number | Enter the following detail:Inbound Delivery : <Inbound Delivery Number>Choose Continue. | Change Inbound Delivery XXXXXXXXX Change: Overview screen is displayed. |  |
| 4 | Parameter that Get Determined Automatically | In Item Overview section, enter the following detail:Putaway Qty: 2 | Parameters entered. |  |
| 5 | Change Storage Location | Storage location: 995A | Storage location is changed |  |
| 6 | Post Goods Receipt | Choose Post Goods Receipt. | Goods Receipt for inbound delivery XXXXXXXX posted (Material Document xxxxxxxxxx) message is displayed. |  |

### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after you have posted the goods receipt in the receiving plant. The further logistical handling of the returned materials is decided. This process step shows you how to perform material inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist |  |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH) app. | The Worklist Selection of Deliveries screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Delivery items waiting for inspection: <select>Delivery: <Inbound delivery number> | The Change: Material Inspection in Warehouse for Delivery screen is displayed. |  |
| 4 | Choose Item Tab | Choose Item. |  |  |
| 5 | Enter Inspection Result | In the Inspection Result subarea, enter the following data and choose Enter:Inspection Code: <inspection code>Inspected quantity: <inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Enter Follow-Up Activity | In Logistical Follow-Up subarea, enter the following data and choose Enter:Follow-Up Activity: <Follow-up activity>Choose appropriate logistical follow-up activity according to inspection code. For example, choose follow-up activity 0011--Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | Under the Header tab, in Basic Data subarea, Inspection status shows Inspected, which means all received material is inspected completely. | All received material is inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm. | Inspection result is recorded, logistical follow-up document is posted accordingly. |  |

### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check stock status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Stock - Single Material (F1076) app. | Stock - Single Material (F1076) screen is displayed. |  |
| 3 | Enter Parameters | Enter the following details:Material : R_1006Choose Enter | You receive an overview of the materials. This concerns all materials that have left the supplying plant and have already reached the receiving plant.Unrestricted use stock is increased after confirming the follow-up activity 0011--Transfer to Free Available Stock. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can precede this process.

| Process | Business Condition |
| --- | --- |
| 3HQ | In-Store Merchandise Management |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 5FU | Inbound Logistics for Distribution Centers |

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
> Flagged while digesting this document, not verified: Preliminary steps name 3HQ both as 'In-Store Merchandise Management' and 'Ordering, Receiving and Customer Inquiry in Store'

## Connections
- part-of :: [[_cluster]]
- see-also :: [[15-retail-operations/test-script-inbound-logistics-for-distribution-centers-5fu-ae-1089]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,649 chars in the whole document
