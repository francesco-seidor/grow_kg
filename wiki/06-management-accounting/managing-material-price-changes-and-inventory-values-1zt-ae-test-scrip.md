---
id: 06-management-accounting/managing-material-price-changes-and-inventory-values-1zt-ae-test-scrip
title: Managing Material Price Changes and Inventory Values (1ZT_AE) - Test Script (1ZT_S4CLD2608_BPD_EN_AE)
description: "Test script for SAP S/4HANA Cloud scope item 1ZT_AE: immediate and future material price changes, stock-value adjustments, inventory value analysis."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/inventory-valuation-and-actual-costing]
aliases: [1ZT_S4CLD2608_BPD_EN_AE]
keywords: [Inventory Valuation and Actual Costing, material price changes, immediate price change, future price change, stock value adjustment, material inventory values, material valuation, test scripts, mass price upload, price monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1ZT_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-794
topic: 06-management-accounting/inventory-valuation-and-actual-costing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Managing Material Price Changes and Inventory Values (1ZT_AE) - Test Script (1ZT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1ZT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Inventory Valuation and Actual Costing** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Managing Material Price Changes and Inventory Values (1ZT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848472)

[2 Prerequisites 4](#_Toc232848473)

[2.1 System Access 4](#_Toc232848474)

[2.2 Roles 4](#_Toc232848475)

[2.3 Master Data, Organizational Data and Other Data 4](#_Toc232848476)

[2.4 Additional Manual Configuration 5](#_Toc232848477)

[3 Overview Table 6](#_Toc232848478)

[4 Test Procedures 8](#_Toc232848479)

[4.1 Immediate Price Change 8](#_Toc232848480)

[4.1.1 Monitor Material Prices 8](#_Toc232848481)

[4.1.2 Price Change for Individual Material 9](#_Toc232848482)

[4.1.3 Change Material Prices 10](#_Toc232848483)

[4.1.4 Upload Material Inventory Prices 12](#_Toc232848484)

[4.1.5 Display Material Price Change Documents 13](#_Toc232848485)

[4.2 Price Adjustment via Stock Value 14](#_Toc232848486)

[4.2.1 Price Adjustment for Individual Material via Stock Value 14](#_Toc232848487)

[4.2.2 Display Debit/Credit Material 15](#_Toc232848488)

[4.3 Future Price Change 16](#_Toc232848489)

[4.3.1 Monitor Material Prices 16](#_Toc232848490)

[4.3.2 Enter Future Prices 17](#_Toc232848491)

[4.3.3 Release Planned Price Changes 18](#_Toc232848492)

[4.3.4 Display Material Price Change Documents 20](#_Toc232848493)

[4.4 Analysis to Material Inventory Values 21](#_Toc232848494)

[4.4.1 Material Inventory Values - Balance Summary Review Booklet 21](#_Toc232848495)

[4.4.2 Material Inventory Values - Line Items 22](#_Toc232848496)

## Purpose

Overview

This scope item provides users with an example of a process description that they can use to upload material inventory prices, change material valuation prices, manage material valuations, and view and analyze material inventory values.

You can make a price change in the following ways:

- One-step procedure with immediate effect: When material costs are changed, inventory is revaluated with all price controls, including valuation with the standard price and periodic unit price.
- Debit/Credit Material-Related Account: When debiting or crediting a material, the revaluation amounts are posted as follows:
    - For standard price materials (price control S), the revaluation amount is posted to a price difference account. The standard price of the material is not changed.
    - For moving average price materials (price control V), the revaluation amount is posted to the material stock account, provided there is sufficient stock coverage. If not, only the portion for the available stock is posted to the stock account, with the remainder posted to a price difference account.
- Two-step change via Determine Future Prices and Releasing Planned Prices:
    - When future prices are entered, the new future valuation prices are updated in all currencies and valuations within the material ledger data, and in the company code currency in the material master record.
    - When planned price changes are released, the system updates the valid future prices (in various currencies and valuations) as the current standard price or valuation price. It calculates a revaluation amount for the specific inventory quantity, adjusting the inventory value by this amount. The offsetting entry occurs in the revaluation account according to account determination. If there is no material stock, only the price is updated.

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
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |

### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company is created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material Master |  | Materials used for procurement and materials that are produced. For example materials with material type FERT/HALB/ROH/VERP/HAWA | No specific materials necessary, but transaction data must be available.Note If you are using standard costing with material price control S, manual price changes via this transaction is not recommended and can lead to errors. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/2b11a669577fc09431b8b2afc9e07614)

## Overview Table

This scope item consists of several processes provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Immediate Price Change

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Monitor Material Prices](#unique_8) [page ] 8 | Cost Accountant - Inventory | Monitor Material Prices (F7245). | Helps review and compare material prices across ledgers. |
| [Price Change for Individual Material](#unique_9) [page ] 9 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | Inventory is revaluated with all price controls, including valuation with standard price and valuation with periodic unit price. |
| [Change Material Prices](#unique_10) [page ] 10 | Cost Accountant - Inventory | Change Material Prices (F6489) | Inventory prices for multiple materials are updated. |
| [Upload Material Inventory Prices](#unique_11) [page ] 12 | Cost Accountant - Inventory | Upload Material Inventory Prices (F4006) | Helps make mass changes to material inventory prices. |
| [Display Material Price Change Documents](#unique_12) [page ] 13 | Cost Accountant - Inventory | Display Material Price Change Documents (F6684) | Displays documents created by price changes. |

Table 2: Price Adjustment via Stock Value

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Price Adjustment for Individual Material via Stock Value](#unique_13) [page ] 14 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | Adjusts the inventory value and recalculates the price based on stock quantity. |
| [Display Debit/Credit Material](#unique_14) [page ] 15 | Cost Accountant - Inventory | Display Material Ledger Debit Credit Documents (F8982) | All price change documents display. |

Table 3: Future Price Change

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Monitor Material Prices](#unique_8) [page ] 8 | Cost Accountant - Inventory | Monitor Material Prices (F7245) | Helps review and compare material prices across ledgers. |
| [Enter Future Prices](#unique_15) [page ] 17 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | The new future valuation prices are updated in all currencies and valuations in the material ledger data and also in the company code currency in the material master record. |
| [Release Planned Price Changes](#unique_16) [page ] 18 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | The system does the following:Updates the valid future prices (in the various currencies and valuations) as the current standard price or valuation price.Calculates a revaluation amount for the specific inventory quantity and revaluates the inventory value by this amount.The offsetting entry takes place in the revaluation account in accordance with account determination.If no material stock exists, only the price is changed. |
| [Display Material Price Change Documents](#unique_12) [page ] 13 | Cost Accountant - Inventory | Display Material Price Change Documents (F6684) | Displays documents created by price changes. |

Table 4: Analysis to Material Inventory Values

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Material Inventory Values - Balance Summary Review Booklet](#unique_17) [page ] 21 | Cost Accountant - Inventory | Material Inventory Values - Balance Summary Review Booklet (F1422B) | This review booklet displays a data analysis page with inventory values, and a graphical display page with multiple chart options for data analysis. |
| [Material Inventory Values - Line Items](#unique_18) [page ] 22 | Cost Accountant - Inventory | Material inventory Values - Line Items (F1423B) | Insights on the values and quantities of your material inventories down to the line item level. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Immediate Price Change

#### Monitor Material Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity helps you review and compare material prices across ledgers. You can also compare inventory valuations across different ledgers and accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Monitor Material Prices (F7245). | The Monitor Material Prices screen displays. |  |
| 3 | Enter Data | Make the following entries:View Type: <Select either Compare Two Valuations OR Prices in All Valuations>Valuations to Compare: <valid for Prices in All Valuations view type; search and select all the options you want to compare, multiple selections possible>Valuation to Compare 1: <valid for Compare Two Valuations view type; search and select all the options you want to compare>Valuation to Compare 2: <valid for Compare Two Valuations view type; search and select all the options you want to compare>Material: <optional>Company Code: 3310Plant: 3310Choose Go. | All the material price lists display. |  |

#### Price Change for Individual Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity updates the material price of a single material with immediate effect.

|  |
| --- |
| Note Alternatively, you can use the app Upload Material Inventory Prices (F4006) to update the material prices of multiple materials at once. |

|  |
| --- |
| Note From 2105 release, the price must be updated for each Ledger such as 0L and 2L or 3L separately. Inventory prices can now be changed per ledger via app Manage Material Valuations (F2680).For this scope item it is assumed that the follow on standard cost estimation will update all ledgers with same standard cost (not ledger specific). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Material: TG12Plant: 3310 | The Current Material Valuation screen displays by ledger. |  |
| 4 | Enter Data | Select the first entry in the table to navigate to the details page. Choose Change Inventory Prices on the top right of the screen (if Change Inventory Prices is not visible, choose the More icon first.)Select the current date as the Posting Date.In the Company code currency row of the Reference Price area, change the value of New Price to a different numeric value, for example 10.In the Prices in other Valuations area, select the overall checkbox left of the Valuation View. Now the Convert Prices button becomes active. Choose Convert Prices.Choose Save. |  |  |

#### Change Material Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity enables the material price change for multiple materials concurrently.

|  |
| --- |
| Note You can update inventory prices via this app, but you can't update standard and future prices. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Material Prices (F6489). | The Change Material Prices (F6489) screen displays. |  |
| 3 | Enter Data | Make the following entries:Material: TG12Plant: 3310Choose the Change Prices button. | The Material Price Changes screen displays. |  |
| 4 | Enter Data | Make the following entries under the General Information section:Posting Date: <today's date>Company Code: 3310Plant: 3310Document Header Text: <enter some header text>Choose the Price Changes tab. Under Price Changes, enter material and update the price.Select the overall checkbox on the left side next to Price Category. The Convert Prices button becomes active. Choose Convert Prices.Note To add more materials, choose the Create button above the table. Enter another material and update the price as required.Choose Save. |  |  |

#### Upload Material Inventory Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to make mass changes to material inventory prices. You can download a blank spreadsheet to use as a template or you can download your existing material prices for a given company code, plants and currency type, make your changes, and then upload the new price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Upload Material Inventory Prices (F4006). | The Upload Material Inventory Prices screen displays. |  |
| 3 | Download Template | Choose the Download Templates button. In the Download Templates dialog box, in the Type dropdown, select With existing material prices. Make the following entries:Company Code: 3310Plant: 3310Currency Type/Ledger/Valuation View: <Use the dropdown to select 10/0L/Legal Valuation>Value Date: <Current Date>Material: <TG10 or any other material>Choose the Download button. Open the downloaded .csv template.Enter the field values such as inventory price (for example, 10). | Download a spreadsheet with your current prices or a blank template. |  |
| 4 | Save Template | Save the file in .csv format. |  |  |
| 5 | Enter Source File | Choose Upload > Browse.Use the .csv file that you just updated. |  |  |
| 6 | File Check | The upload performs a check to ensure that the format is correct. | Correct any error messages that appears. The list of the data uploaded appears. |  |
| 7 | Post | Choose Post. | Price change documents are posted. |  |

#### Display Material Price Change Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays documents created by price changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Material Price Change Documents (F6684). | The Display Material Price Change Documents screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Material: TG12Plant: 3310 | All price change documents display. |  |

### Price Adjustment via Stock Value

#### Price Adjustment for Individual Material via Stock Value

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity adjusts the inventory value and recalculates the price based on stock quantity. Byadjusting the stock value, the final price is calculated automatically. This functionality is best used for adjusting costs due to valuation corrections. A negative value will decrease the stock value, resulting in a lower price per unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries and choose the Go button:Company Code: 3310Material: TG11Plant: 3310 | The Current Material Valuations view displays by ledger. |  |
| 4 | Enter Data | Select the first entry in the table and choose the > icon to navigate to the Details page. Choose Debit/Credit Material on the top right of the screen (if Debit/Credit Material is not visible, choose the More icon first.)Select the current date as the Posting Date.Under Reference Debit/Credit, in the Company Code Currency row, change the value of Revaluation Amount to a different numeric value, for example 100.In the Debit/Credit in Other Valuations area, select the overall checkbox left of the Valuation View. The Convert Amounts button becomes active. Choose Convert Amounts.Choose Save.Using debit/credit adjustments, modify the material cost based on the existing stock quantity. This process alters the stock value and price. |  |  |

#### Display Debit/Credit Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays documents generated by price changes due to debit/credit adjustments and valuation corrections.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Material Ledger Debit Credit Documents (F8982). | The Display Material Debit/Credit Documents screen displays. |  |
| 3 | Enter Data | Make the following entries and choose the Go button:Company Code: 3310Plant: 3310Material: TG11 | All price change documents display. |  |

### Future Price Change

#### Monitor Material Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity helps you review and compare material prices across ledgers. You can also compare inventory valuations across different ledgers and accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Monitor Material Prices (F7245). | The Monitor Material Prices screen displays. |  |
| 3 | Enter Data | Make the following entries:View Type: <Select either Compare Two Valuations OR Prices in All Valuations>Valuations to Compare: <valid for Prices in All Valuations view type; search and select all the options you want to compare, multiple selections possible>Valuation to Compare 1: <valid for Compare Two Valuations view type; search and select all the options you want to compare>Valuation to Compare 2: <valid for Compare Two Valuations view type; search and select all the options you want to compare>Material: <optional>Company Code: 3310Plant: 3310Choose Go. | All the material price lists display. |  |

#### Enter Future Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The new future valuation prices are updated in all currencies and valuations in the material ledger data and the company code currency in the material master record.

|  |
| --- |
| Note The price must be updated for each Ledger such as 0L and 2L or 3L separately. |

For this scope item, it is assumed that the follow on standard cost estimation will update all ledgers with same standard cost (not ledger specific).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries:Material: TG12Plant: 3310Choose the Go button. |  |  |
| 4 | Enter Data | Select the box for the material with Currency Type 10 (Company code Currency) and choose Change Future Prices with Reference.Make following entries:Valid from: <Start of Next Period>Valid from Date: <keep defaulted date or enter a specific date in the future>Price Source: Standard PriceLedger to Be Translated From: 0L (Ledger 0L)Currency Type to Be Translated From: 10 (CCde Crcy)Currency Translation Date: <same data as set for Valid from Date>Exchange Rate Type: M (Standard translation at average rate)Additional Factor: Example 1,0Choose the OK button.Note Make the same entries for Crcy type/val.view 30 (Group currency) except for Currency Type/Valuation To Be Translated From should be set to Group currency. | Additional Factor: Here, you can specify a factor by which the price of the material should be multiplied.Example:If you want to increase the price of a material by 10%, enter the factor 1.1.If you want to decrease the price of a material by 10%, enter the factor 0.9. |  |
| 5 | Review Data | Select the line to navigate to the Current Material Valuation view of the material. | Here you can see the impact of price change in the future price based on additional factor that you specified.You can review the future price for company code and group. |  |

#### Release Planned Price Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The system does the following:

- Updates the valid future prices (in the various currencies and valuations) as the current standard price or valuation price.
- Calculates a revaluation amount for the specific inventory quantity and revaluates the inventory value by this amount.

The offsetting entry takes place in the revaluation account in accordance with account determination.

If no material stock exists, only the price is changed.

|  |
| --- |
| Note From 2105 release, the price must be updated for each Ledger such as 0L and 2L or 3L separately. |

Prerequisites

The planned prices must exist in the system and they must be valid (validity date). If no valid planned prices exist in the system, the materials continue to be valuated with the valuation price used up to this point.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries:Material: Example TG12Plant: 3310Choose the Go button. |  |  |
| 4 | Enter Data | Select both valuation views for the material (Company code currency and Group currency) and choose Release Planned Price Changes. |  |  |
| 5 | Enter Data | In the Release Planned Price Changes dialog box, make an entry in Document Header Text and deselect Consider Thresholds for Price Changes. Choose the Save button to execute. |  |  |
| 6 | Display Changes | Select on the entry again to navigate to the Current Material Valuation view for the material. | You can see the updated inventory price for the material in both Company code currency and Group currency. |  |

#### Display Material Price Change Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays documents created by price changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Material Price Change Documents (F6684). | The Display Material Price Change Documents screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Material: TG12Plant: 3310 | All price change documents display. |  |

### Analysis to Material Inventory Values

#### Material Inventory Values - Balance Summary Review Booklet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This review booklet displays a data analysis page with inventory values, and a graphical display page with multiple chart options for data analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2 | Access the SAP Fiori app | Open: Material Inventory Values - Balance Summary Review Booklet (F1422B). | The Material Inventory Values - Balance Summary Review Booklet screen displays. |  |
| 3 | Enter Data | Make the following entries:Ledger: <for example, 0L>Reporting Key Date: <today date>Company Code: 3310Choose Go. | This review booklet displays a data analysis page with inventory values. You can adjust the dimensions based on your requirements. It also includes a graphical display page with multiple chart options for data analysis. |  |

#### Material Inventory Values - Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can gain an understanding of the values and quantities of your material inventories down to the line item level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Inventory. |  |  |
| 2 | Access the SAP Fiori app | Open: Material inventory Values - Line Items (F1423B). | The Material Inventory Values -Line Items screen displays. |  |
| 3 | Enter Data | Make the following entries:Company Code: 3310Plant: 3310Ledger: <for example, 0L>Material: <FG126, for example>Start Date: <start of month, for example, 20240401>End Date: <current month end, for example,20240430>Choose Go. | You can analyze and display inventory value, and quantity of the journal entries that affect the value of material inventories during a particular period. |  |

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
- related-to :: [[06-management-accounting/test-script-actual-costing-33q-ae-sap-s-4hana-cloud-public-edition-903]]
- related-to :: [[06-management-accounting/test-script-inventory-valuation-for-year-end-closing-bej-ae-1260]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1ZT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 36,520 chars in the whole document
