---
id: 04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-by-vistex-7z8-ae-s
title: "Test Script: Enablement of SAP Excise Tax Management by Vistex (7Z8_AE), SAP S/4HANA Cloud Public Edition (7Z8_S4CLD2608_BPD_EN_AE)"
description: "SAP test script (scope item 7Z8, AE, dated 19-06-26) for SAP Excise Tax Management by Vistex: prerequisites, preliminary setup and order-to-excise-posting test steps."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/excise-tax-vistex]
aliases: [7Z8_S4CLD2608_BPD_EN_AE]
keywords: [SAP Excise Tax Management by Vistex, excise tax management, test script, preliminary steps, field values setup, tax rate document, stock ledger, excise tax posting, tax rate template, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z8_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1242
topic: 04-tax-and-statutory-reporting/excise-tax-vistex
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Enablement of SAP Excise Tax Management by Vistex (7Z8_AE), SAP S/4HANA Cloud Public Edition (7Z8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **SAP Excise Tax Management by Vistex** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Enablement of SAP Excise Tax Management by Vistex (7Z8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861303)

[2 Prerequisites 4](#_Toc232861304)

[2.1 System Access 4](#_Toc232861305)

[2.2 Roles 4](#_Toc232861306)

[2.3 Additional Manual Configuration 5](#_Toc232861307)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232861308)

[2.4.1 General Master Data and Organizational Data 5](#_Toc232861309)

[2.4.2 Master Data for Excise Tax Management 6](#_Toc232861310)

[2.5 Business Conditions 7](#_Toc232861311)

[2.6 Preliminary Steps 7](#_Toc232861312)

[2.6.1 Configure Allowed Currency and Units 7](#_Toc232861313)

[2.6.2 Create Field Values using Setup 9](#_Toc232861314)

[2.6.3 Create G/L Accounts 18](#_Toc232861315)

[2.6.4 Create Warehouse 19](#_Toc232861316)

[2.6.5 Create Accrual Customer 20](#_Toc232861317)

[2.6.6 Create Posting Area 21](#_Toc232861318)

[2.6.7 Create Warehouse Assignments 22](#_Toc232861319)

[2.6.8 Maintain Data in Cross-Reference/Assignments 23](#_Toc232861320)

[2.6.9 Upload Tax Rate Template 25](#_Toc232861321)

[2.6.10 Create Workspace Card 26](#_Toc232861322)

[2.6.11 Create a Tax Rate Document 27](#_Toc232861323)

[2.6.12 Create Initial Material Stock 29](#_Toc232861324)

[3 Overview Table 31](#_Toc232861325)

[4 Test Procedures 32](#_Toc232861326)

[4.1 Retrieve Customers 32](#_Toc232861327)

[4.2 Retrieve Products 33](#_Toc232861328)

[4.3 Create Sales Order 35](#_Toc232861329)

[4.4 Create Delivery 36](#_Toc232861330)

[4.5 Execute Picking and Post Goods Issue 37](#_Toc232861331)

[4.6 Retrieve Material Documents 38](#_Toc232861332)

[4.7 Update Stock Ledger 39](#_Toc232861333)

[4.8 Calculate Excise Tax Amounts 40](#_Toc232861334)

[4.9 Post Excise Taxes to Finance 41](#_Toc232861335)

[4.10 Verify Finance Document Posting 44](#_Toc232861336)

[5 Appendix 45](#_Toc232861337)

[5.1 Tax Rate Template 45](#_Toc232861338)

## Purpose

Overview

SAP Excise Tax Management by Vistex for Public Cloud extends SAP S/4HANA Public Cloud by providing a cloud-native framework for excise tax compliance. The solution runs on the SAP Business Technology Platform (BTP) and integrates with SAP S/4HANA Cloud for transactional, master, and financial data. Organizations can track excise-relevant goods, calculate accurate tax amounts, and generate legal reports required by authorities. The Stock Ledger Workspace allows users to validate, reprocess, and monitor excise transactions through a modern SAP Fiori user interface. For EU countries, the solution integrates with SAP GTS or third-party service providers to exchange transport information for excise-suspended goods. It also supports compliance with the Excise Movement and Control System (EMCS). The solution supports regulated industries such as alcoholic beverages, tobacco, sugar-based products, and coffee. It offers preconfigured templates to help organizations accelerate compliance readiness.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

Table 1:

|  |  |
| --- | --- |
|  | Details |
| System for SAP Excise Tax Management by Vistex | [https://consumer-vistex-gtms-pq-17.sales-solutions-by-vistex-pq.cfapps.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html#Home](https://consumer-vistex-gtms-pq-17.sales-solutions-by-vistex-pq.cfapps.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html#Home) |

### Roles

Assign the following business roles to your individual test users.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Excise Tax Management Admin | ETADMIN | Create a user with this role (instructions in the Administration Guide) to perform tests relevant for SAP Excise Tax Management by Vistex. |  |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

|  |
| --- |
| Note The following roles are provided as example roles from SAP. You can use these as templates to create your own roles |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9c2b2658f939aeefb7afb7ea74ccc3e1)

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. Master data represents materials, and customers used in the course of production and sales of excise tax-relevant products.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or use the sample data listed in the following sections as the data for the preliminary steps and the test procedures. Most of the sample data given below is available from the Enterprise Management bundle that can be activated in SAP Central Business Configuration (CBC) for SAP S/4HANA Cloud Public Edition. Any exceptions or additional actions are described in the following sections.

#### General Master Data and Organizational Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

You can substitute the master data and organizational data in this section with your own data:

Table 2:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company | 3310 |  |  |
| Plant | 3310, 33AA |  |  |
| Storage Location | 331A,331B,331C |  |  |
| Material Type | FERT |  |  |
| <operating year> | 01-Jan-2025 to 31-Dec-2025 |  | You may substitute your current calendar or fiscal year |

#### Master Data for Excise Tax Management

The master data and organizational data identified in this section is used throughout the document. If you wish to use your own data, please make consistent substitutions throughout this document.

Table 3:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Area | 3300/10/00 – you must generate this sales area in SAP S/4HANA Cloud, Public Edition; it is not the default configuration |  |  |
| Sales Order | OR |  |  |
| Delivery Type | LF |  |  |
| Material Document Type | WA |  |  |
| General Ledger Posting Account External Id(2 accounts) | 00410004000012550000 | Customer Revenue/ExpenseCustomer Clearing Account |  |
| Customer | 33105001 | Domestic CP Customer 01 | This customer should be referenced on sales orders and/or delivery documents associated with steps in this document. |
| Material | FG0506 | Single Malt Scotch 700ml | This material should be produced, moved to inventory, and sold to the above customer on documents used in scope for the tax rate document defined in the Preliminary Step 2.5.9. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

Table 4:

| Scope Item ID | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close or J59 - Accounts Receivable or J60 - Accounts Payable | These Scope Items may need to be active to provide the "journal entry" API for posting calculated amounts to SAP S/4HANA Cloud Public Edition. |

### Preliminary Steps

This section covers the prerequisite Preliminary Steps necessary for SAP Excise Tax Management by Vistex.

You must perform these steps before attempting to execute any test cases.

#### Configure Allowed Currency and Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

General configuration is needed in SAP Excise Tax Management by Vistex.

Procedure

1. Log into the Fiori link with the user Excise Tax Admin and password provided.
2. Choose the Administrative Task s tile group from the menu.
3. Choose the Admin Activities tile.
4. Choose the Expand Global Settings node.
5. Choose the Allowed Currencies .
6. Choose the Add (‘+’) button.
7. Select USD in the Currency field.
8. Choose the Create button.
9. Choose Save button after verifying the details in the document section
10. Choose the Back (‘<’) button.
11. Choose the Allowed Units under Global Settings node.
12. Choose the Add (‘+’) button.
13. Select EA in the Internal UOM field and choose Enter.
14. Choose the Create button. Repeat Steps 12 to 14 for the following additional Allowed Units:

Table 5:

| Internal Unit | Unit | Description |
| --- | --- | --- |
| EA | EA | Each |
| BOT | BT | Bottle |
| CS | CS | Case |
| PAK | PAC | Pack |
| ST | PC | Piece |
| G | G | Gram |
| KG | KG | Kilogram |
| HL | HL | Hectoliter |
| L | L | Liter |
| ML | ML | Milliliter |
| KI | CRT | Crate |
| KAR | CAR | Carton |
| LA | LA | Liters of Alcohol |
| ZHA | HLA | HL of Pure Alcohol |
| ZHP | HLP | HL/°P |
| ZHV | HLV | HL/ %ABV |

1. After verifying the details in the document section, Choose on the Save button.

You may need to define additional Unit of Measures and Allowed Units based on the units of measure used in your master data.

Result

The user selected currency is allowed. The user selected units of measure are allowed.

#### Create Field Values using Setup

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

General configuration is needed in SAP Excise Tax Management by Vistex.

Procedure

1. Log into the Fiori link with the user Excise Tax Admin and password provided.
2. Navigate to the Administrative Tasks tile group and click the Admin Activities tile.
3. Expand Field Value Node.
4. Choose the Company Code
5. Choose the Edit button and click theAdd (‘+’) button to add Company Code values.
6. Enter the below values
    - Company Code : 3310
    - Country: AE
    - Currency: AED
    - Description: AE Company Code
7. Choose Save Button.

Repeat Steps 4 to 7 to add the following additional field values for Company Code:

Table 6:

| Company Code | Country | Currency | Description |
| --- | --- | --- | --- |
| 3320 | AE | AED | Company Code 17203320 |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Expand Field Value Node.
4. Choose the Plant.
5. Choose the Edit button and click theAdd (‘+’) button to add Plant values, like Steps 4 to 6, for the following:

Table 7:

| Plant | Company Code | Country | Region | Description |
| --- | --- | --- | --- | --- |
| 3310 | US Company Code | AE | California | Plant 1 |
| 3320 | US Company Code | AE | California | Plant 2 |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Expand Field Value Node.
4. Choose the Storage Location node.
5. Choose the Edit button and click theAdd (‘+’) button to add Storage Locationvalues.

Table 8:

| Storage Locationt | Plant | Description |
| --- | --- | --- |
| 331A | Plant 1 | Plant 1/Large |
| 331B | Plant 1 | Plant 1/Medium |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Expand Field Value Node.
4. Choose the Movement Type Node.
5. Choose the Edit button and click theAdd (‘+’) button to add Movement Type Node values: If the values already exists and the Add (‘+’) button is disabled, skip this step.:

Table 9:

| Movement Type | Description |
| --- | --- |
| 101 | Goods Receipt |
| 102 | GR for PO Reversal |
| 103 | GR into Blocked State |
| 301 | Tfr Plant to Plant (One Step) |
| 302 | Tfr Plant to Plant Reversal (One-Step) |
| 311 | Transfer Posting to Storage location (One) |
| 312 | Transfer Posting to Storage location (One) |
| 551 | GI scrapping |
| 552 | RE scrapping |
| 561 | Initial stock entry |
| 601 | Issue |
| 602 | RE Goods Issue Delivery |
| 657 | GD returns blocked |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Movement Category.
4. Choose the Edit button and click theAdd (‘+’) button to add Movement Category Node values: If the values already exists and the Add (‘+’) button is disabled, skip this step.:

Table 10:

| Movement Category | Description |
| --- | --- |
| 001 | Receipt from Purchase. |
| 002 | Receipt from Own Production. |
| 101 | Issue from Sales to Customer. |
| 102 | Issue from Sales to Other Company Code. |
| 305 | Inventory loses. |
| 404 | Stock Transfer. |
| 600 | Stock Transfer GI taxed. |
| 901 | Manual Adjustment. |
| 902 | Stock in Transit. |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Ledger Group Node.
4. Choose the Edit button and click theAdd (‘+’) button to add Stock Ledger Group Node values: If the values already exists and the Add (‘+’) button is disabled, skip this step.:

Table 11:

| Stock Ledger Group | Description |
| --- | --- |
| 01080 | Own Brand Production. |
| 01090 | External Production. |
| 01360 | Domestic Purchase. |
| 01366 | Purchase from Special Partner (Untaxed). |
| 01390 | Purchase from Third Country. |
| 01540 | Issue - Stock Transfer, Taxed |
| 01550 | Issue - Stock Transfer, Tax Warehouse. |
| 01560 | Issue - Stock Transfer, EU Tax Warehouse. |
| 01561 | Issue - Stock Transfer, EU (Untaxed). |
| 01570 | Issue - Stock Transfer, Third Country |
| 02000 | Sale to Customer, EU (Taxed). |
| 02010 | Sale to Customer. |
| 02015 | Sale to Customer, Special Partner (Taxed). |
| 02016 | Sale to Customer, Special Partner (Untax). |
| 02020 | Sale to Customer, EU (Un Taxed) |
| 02030 | Sale to Customer, Third Country |
| 02040 | Sale to Customer, Tax Warehouse |
| 02060 | Sale to Customer, EU Tax Warehouse. |
| 02070 | Sale to Customer, Tax Warehouse (Internal). |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Tax Material Group Node.
4. Choose the Edit button and click theAdd (‘+’) button to add.
5. Choose the following data Field = Value data:.

Table 12:

| Material Group | Description |
| --- | --- |
| MG01 | Group 1. |
| MG02 | Group 2. |
| TB01 | Cigarettes. |
| TB02 | Cigars & Cigarillos. |
| TB04 | E-Cigarettes. |
| TB05 | Other Tobacco Products |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Permission Type.
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Permission Type values:.

Table 13:

| Permission Group | Description |
| --- | --- |
| 01 | Tax Warehouse. |
| 02 | Registered consignee/Regt. Consignor. |
| 04 | Direct Delivery. |
| 05 | Exempted organization. |
| 06 | Export. |
| 08 | Consignee. |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Exempted Organization Type.
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Organization Type values:.

Table 14:

| Exempted Organization Type | Description |
| --- | --- |
| 01 | Foreign Military Forces. |
| 02 | Staff Beverage. |
| 03 | Free Drinks. |
| 04 | Other Special Partner. |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Origin Country Type.
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Origin Country Type values:

Table 15:

| Origin Country Type | Description |
| --- | --- |
| 01 | Local. |
| 02 | Foreign. |
| 03 | Foreign (EU). |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Origin Warehouse Type.
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Origin Warehouse Type values:

Table 16:

| Origin Warehouse Type | Description |
| --- | --- |
| 01 | Tax Warehouse |
| 02 | Non-Tax Warehouse. |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Exempted Organization.
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following values:

Table 17:

| Exempted Organization | Description |
| --- | --- |
| 01 | Army |
| 02 | Free Ports. |
| 03 | Embassy |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Tax Stamp Usage.
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Tax Stamp Usage values:

Table 18:

| Tax Stamp Usage | Description |
| --- | --- |
| 01 | Damaged |
| 02 | Lost. |
| 03 | Expired |
| 04 | Finished Good |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Debit/Credit Indicator.
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Debit/Credit Indicator values:

Table 19:

| Debit/Credit Indicator | Description |
| --- | --- |
| H | Credit |
| S | Debit. |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Receiving/Issue Storage Location..
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Receiving/Issue Storage Location.values:

Table 20:

| Storage Location | Plant | Description |
| --- | --- | --- |
| Plant 1/Large | Plant 1 | Plant 1/Large |
| Plant 1/Medium | Plant 1 | Plant 1/Medium. |

1. Choose the Save button.
2. Choose the Back (‘<‘) button
3. Choose the Receiving/Issuing plant...
4. Choose the Edit button. If the Edit Button is disabled and values already exists, skip this step
5. Choose the Add (‘+’) button and enter the following Receiving/Issuing plant values:

Table 21:

| Plant | Company Code | Country | Region |
| --- | --- | --- | --- |
| Plant 1 | US Company Code | USA | California |
| Plant 2 | US Company Code | USA | California. |

1. Choose the Save button..
2. Choose the Home button.

Result

Field values are set.

#### Create G/L Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP Excise Tax Management by Vistex may generate tax amounts that are typically posted to Stock Ledger Accounts. This preliminary step links the payments to the appropriate account(s).

Procedure

1. Log into the Fiori link with the user ID and password provided for a user with the Excise Tax Admin role.
2. Choose the Postings (Tile group) and click the G/L Accounts (Tile).
3. Choose the Create button.
4. In Header Section, enter the following details
    - Posting Account External ID: 0012550000
    - Description: Excise Tax Account
    - Status: Active.
5. Choose the Check and click the Save button.
6. Repeat steps 2 to 5 for each additional Posting Account listed below.

Table 22:

| G/L Account | Description |
| --- | --- |
| 0041000000 | Expense Account |

1. Choose the Home button.

Result

G/L accounts are created.

#### Create Warehouse

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step you create the tax-relevant warehouse that will hold the finished inventory. The warehouse should be registered for the tax warehousing for Excise Tax Management.

Procedure

1. Log into the Fiori link with the user ID and password provided for a user with the Excise Tax Admin role.
2. Choose Master Data and click the Warehouses (Tile).
3. Choose the Create button.
4. Choose Header section and create the following settings:
    - Warehouse: W1001.
    - Name: Alcohol – California Warehouse.
    - Status: Tax Warehouse.
5. Choose Address section.
6. Choose Add('+') button.
7. Enter field values as indicated in the table below and choose Apply. Repeat step 6-7 for each entry.

Table 23:

| Entry No. | Field | Value |
| --- | --- | --- |
| 1 | Address Tag | AT#1 |
| Address Usage | Warehouse Location |  |
| City | Oakland |  |
| Region | California |  |
| Country | USA |  |
| 2 | Address Tag | AT#12 |
| Address Usage | Communication Address |  |
| City | Chicago |  |
| Region | Illinois |  |
| Address Tag | USA |  |

1. Choose the Tax Type Attributes section and click the Add button.
2. Enter the values in the fields as given in the table and click the Save button.

Table 24:

| Company Code | Tax Type | Warehouse License Number | Go Live Date | Warehouse Owner Number | Validity |
| --- | --- | --- | --- | --- | --- |
| US Company Code | Alcohol Tax | WHT10001 | <Today's date> | WOT10001 | < 1st day of the current month> to <Last day of the year> |

Result

A warehouse is created.

#### Create Accrual Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this Step we will create the Accrual Customer intended to purchase the taxable inventory.

Procedure

1. Choose the Master Data (tile group) and click the Accrual Customers (tile).
2. Choose the Create button.
3. Create the following settings:
    - Partner: AC001
    - Name: Accrual Partner
    - Country: US
    - Status: Taxable
4. Choose Check and then click the Save button.
5. Choose Home.

Result

Accrual Customer is created.

#### Create Posting Area

Purpose

Create the financial posting area that will receive the tax amounts. These taxes will be payable to the appropriate government tax authority.

Procedure

1. Go to the Postings tile group and choose the Posting Area tile.
2. Choose the Edit button.
3. In Excise Account tab, click the Add button.
4. Enter the values into the fields as given in the table.

Table 25:

| Company Code | Tax Type | Posting Account | Validity |
| --- | --- | --- | --- |
| US Company Code | Alcohol Tax | Excise Tax Account | <01.01.2025> to <31.12.9999> |

1. Choose the Check button.
2. Choose the Expense Account tab, click the Add button and enter the values into the fields as given in the table.

Table 26:

| Company Code | Tax Type | Posting Account | Validity |
| --- | --- | --- | --- |
| US Company Code | Alcohol Tax | Excise Tax Account | <01.01.2025> to <31.12.9999> |

1. Choose the Check button.
2. Choose the Save button.
3. Choose the Posting Area button and click the Home button.

Result

Posting Area is created.

#### Create Warehouse Assignments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Assign warehouse locations to production facilities to ensure the desired tax-exempt status of inventory until it is sold or intentionally moved to a taxable location.

Procedure

1. Choose the Master Data tile group and choose on Warehouse Assignments tile.
2. Choose the Edit button and choose (+) button to add Plant & Sloc. to Warehouse.
3. Enter the values into the fields as given in the table

Table 27:

| Plant | Storage Location | Tax Type | Tax Warehouse | Validity |
| --- | --- | --- | --- | --- |
| Plant 1 | Plant 1/Large Alcohol | Alcohol Tax | California Warehouse | <30.04.2022> to< 31.12.9999> |
| Plant 1 | Plant 1/Medium | Alcohol Tax | California Warehouse | <04.06.2022> to <31.12.9999> |

1. Choose the Check button.
2. Choose the Save button.
3. Choose the Home button.

Result

Warehouse assignments are now completed and maintained.

#### Maintain Data in Cross-Reference/Assignments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Warehouse assignments are now completed and maintained.

Procedure

1. Go to the Administrative Tasks tile group and Click on the on the Field Values & Assignment tile.
2. Choose the Tax Type Attributes.
3. Choose the Edit button and Click on (+) button to add Tax Type Attributes.
4. Enter the values into the fields as given in the table

Table 28:

| Tax Type | Quantity Decimals | Validity |
| --- | --- | --- |
| Alcohol Tax | 4 | <01.01.2025> to <31.12.9999> |

1. Choose the Check and Save button.
2. Choose the Back button.
3. Choose the Settlement Unit by Tax Type.
4. Choose the Edit button and Click on (+) button to add Settlement Unit by Tax Type..
5. Enter the values into the fields as given in the table.

Table 29:

| Tax Type | Company Code | Settlement Unit | Quantity Decimals |
| --- | --- | --- | --- |
| Alcohol Tax | US Company Code | Liters of Alcohol | 0 |
| Alcohol Tax | US Company Code | Milli litre | 0 |

1. Choose the Check and Save button.
2. Choose the Back button.
3. Choose the Movement Categories to Movement Type.
4. Choose the Edit button and Click on (+) button to add Movement Categories to Movement Type.
5. Enter the values into the fields as given in the table.

Table 30:

| Movement Type | Tax Type | Movement Category |
| --- | --- | --- |
| Transfer Plant to Plant (One Step) 301 | Alcohol Tax | Stock Transfer 404 |
| Transfer Plant to Plant Reversal (One-Step) 302 | Alcohol Tax | Stock Transfer 404 |
| Transfer Posting to Storage location (One 311) | Alcohol Tax | Stock Transfer 404 |
| Goods Issue 601 | Alcohol Tax | Issue from Sales to Customer 6101 |

1. Choose the Check and Save button.
2. Choose the Back button.
3. Choose the Stock Ledger Group Derivation.
4. Choose the Edit button and Click on (+) button to add Stock Ledger Group Derivation.
5. Enter the values into the fields as given in the table.

Table 31:

| Movement Category | Tax Type | Permission Type | Other Warehouse Type | Stock Ledger Group |
| --- | --- | --- | --- | --- |
| Issue from Sales to Customer | Alcohol Tax |  |  | Sale to Customer |
| Issue from Sales to Customer | Alcohol Tax | Exempted organization |  | Sale to Customer, Special Partner (Untax) |
| Stock Transfer | Alcohol Tax |  | Tax Warehouse | Issue - Transfer, Tax Warehouse |
| Stock Transfer | Alcohol Tax |  | Non-Tax Warehouse | Issue - Transfer, Taxed |

1. Choose the Check and Save button.
2. Click on the Back button.
3. Choose the Accrual Customer.
4. Choose the Edit button and Click on (+) button to add Accrual Customer.
5. Enter the values into the fields as given in the table.

Table 32:

| Company Code | Tax Type | Acrual Customer |
| --- | --- | --- |
| US Company Code | Alcohol Tax | Accrual Partner |

1. Choose the Check and Save button.
2. Click on the Home button.

Result

Cross reference and assignments are now completed and maintained.

#### Upload Tax Rate Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Cross reference and assignments are now completed and maintained.

Procedure

1. Choose the Tax Rate template tile group and Click on Tax Rate Document
2. Select the Tax Rate Template upload from the Upload button.

|  |
| --- |
| Note Extract all the content from Step [Tax Rate Template](#unique_20) [page ] 45, compile it into a single text file, and save the file with a Tax Rate Template.txt extension in a particular location for performing the next step |

1. Browse and select the saved Tax Rate Template.txt file to be uploaded.
2. Choose the Submit button.
3. Verify whether the Status is shown Processed and Click on Close.
4. Maintain the Agreement ID in the Template agreement field to verify the uploaded template is created.
5. Click on the Tax Rate Templates dropdown and click on the Home button.

Result

Tax Rate Template is created.

#### Create Workspace Card

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

A Workspace Card allows users to view data based on the filters configured at the card level. Additionally, users can add metrics to the card, which will be displayed based on the filtered data available within the card.

Procedure

1. Choose the Tools tile group and click on Stock Ledger tile.
2. Choose (+) button to create the new card view.
3. A popup will be shown & enter the values into the fields as given in the table

Table 33:

| View | Description | Layout ID | Sequence | Sharing |
| --- | --- | --- | --- | --- |
| ST02 | All Lines | ST07 | 1 | Public (2) |

1. Choose the Create button.
2. Choose the newly created card.
3. Choose the Go button to verify the items.
4. Choose the Home button.

Result

Workspace card assignments are now maintained.

#### Create a Tax Rate Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The tax rate document defines what products are taxable as well as how to calculate the tax amount and who should be paid the taxes.

Procedure

1. Choose the Tax Rate Document tile group and Click on Tax Rate Documents tile.
2. Choose the Create Request From Template button.
3. Enter the values into the fields as given in the table

Table 34:

| Parameter | Value |
| --- | --- |
| Description | Alcohol – United States |
| Country | USA |
| Tax Type | Alcohol Tax |
| Accrual Frequency | Monthly |
| Currency | USD |
| Validity | <01.01.2024> to <31.12.2025> |

1. Navigate to Tax Rates section and Clickon (+) button.
2. Country as USA & Tax Type as Alcohol Tax should be auto populated.
3. Select Liters of Alcohol from the Dropdown as shown.
4. Choose Scales button.
5. A popup will appear and enter the values & click the Check button.

Table 35:

| Parameter | Value |
| --- | --- |
| Scale Type | From |
| Unit Type | Alcohol Strength |
| Unit | % (Percentage) |

1. Now, Enter the values into the Scales section fields as given in the table

Table 36:

| Parameter | Value |
| --- | --- |
| Basis Unit Type | Movement Quantity |
| Basis Unit | Liters of Alcohol |

1. Choose the Add button and enter the values as given in the table

Table 37:

| Parameter | Value |
| --- | --- |
| Alcohol Strength | 1.200 |
| Rate (EUR Per 1 LA) | 13.03000 |

1. Choose Check and Apply button.
    1. Choose the Cal flow section & Select the Accrual from the Usage Dropdown
2. Choose the Check and Save button.
3. Choose the Submit button.
4. Choose the Submit button popup
5. Choose the Approve button.
6. Verify that the Status is Posted
7. Choose the Home button.

Result

A Tax Rate document is now completed. Taxes may be calculated for qualifying transactions.

#### Create Initial Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create initial stock for material FG0506 to execute this scope item

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Choose Document Type | Select Goods Receipt and Other. | The Goods Receipt Other - XXXX screen displays. |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter and SelectOn the Where tab:Movement Type: 561Plant: 3310Storage Location: 331AOn the Quantity tab:Quantity:<100 BT>On the Material tab:Material: FG0506 .Choose Next Item and select Item OK to add entries. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Retrieve Customers](#unique_25) [page ] 32 | ETA Admin | External Data (Tile group) -> Excise Tax Management (Space) ->Data Ingestion Work Managers (Tile). | Fetch master data from SAP S/4HANA Cloud, Public Edition |
| [Retrieve Products](#unique_26) [page ] 33 | ETA Admin | External Data (Tile group) -> Excise Tax Management (Space) ->Data Ingestion Work Managers (Tile). | Fetch master data from SAP S/4HANA Cloud, Public Edition |
| [Create Sales Order](#unique_27) [page ] 35 | Internal Sales Representative | Manage Sales Orders (F1873) | A sale of tax-relevant products is completed in SAP S/4HANA Cloud, Public Edition |
| [Create Delivery](#unique_28) [page ] 36 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Products are moved to a new inventory location or shipped to a customer location. The location update is made in SAP S/4HANA Cloud, Public Edition |
| [Execute Picking and Post Goods Issue](#unique_29) [page ] 37 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Quantity is picked and post goods issue is performed |
| [Retrieve Material Documents](#unique_30) [page ] 38 | ETA Admin | External Data (Tile group) ->Data Ingestion Work Managers (Tile). | Fetch transaction data from SAP S/4HANA Cloud, Public Edition |
| [Update Stock Ledger](#unique_31) [page ] 39 | ETA Admin | Tools -> Stock Ledger update | A tally of products in various locations is maintained. |
| [Calculate Excise Tax Amounts](#unique_32) [page ] 40 | ETA Admin | Tools -> Tax Amount Accrual | The tracking document contains the taxable amount for each product listed |
| [Post Excise Taxes to Finance](#unique_33) [page ] 41 | ETA Admin | Tools-> Accrual Tracking | Postings are made to the SAP S/4HANA general ledger |
| [Verify Finance Document Posting](#unique_34) [page ] 44 | General Ledger Accountant | Manage Journal Entries App | Able to preview the loading instruction. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Retrieve Customers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Customer master data from SAP S/4HANA Cloud Public Edition through the system interface. This master data will be used to create prices and/or agreements and may be referenced by transaction data (sales and/or purchase orders, claims, etc.).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Excise Tax Management by Vistex as an Excise Tax Admin. | The Fiori launchpad displays.You will execute this procedure once if you SAP Extended Price Management. Do not execute this procedure more than once to have more than one of these solutions. |  |
| 2 | Access the tile | Choose the External Data (Tile group) under Excise Tax Management (Space) and click the Data Ingestion Work Managers (Tile). |  |  |
| 3 | Schedule Customers Load | Choose the Schedule button and select 1.1 Customers Load. |  |  |
| 4 | Schedule Job | Choose the Schedule button in the popup displayed. |  |  |
| 5 | Check Completed | Choose the Refresh button (System will take few seconds to complete the job) and verify the Status is changed to Completed. | The Status is changed to Completed. |  |
| 6 | Navigate to Home | Choose the Home button. |  |  |
| 7 | Access Customer tile | Go To the Master Data tile group and choose the Customer tile. |  |  |
| 8 | Search Customer | Choose the Go button and verify the Customers. |  |  |
| 9 | Maintain Tax Attributes at Partner Level | Maintain the Partner as 33105001 and choose on the Go button. |  |  |
| 10 | Select Customer | Drill down into the Partner. |  |  |
| 11 | Tax Type parameters | Choose the Edit button & Navigate to Tax Type Attributes section. |  |  |
| 12 | Maintain Parameters | Under the Header section, maintain the status as Tax Exempted.Enter the values into the fields as given in the table.Company CodeTax TypePermission TypeExempted OrganizationUS Company CodeAlcohol TaxExempted OrganizationArmy |  |  |
| 13 | Save | Choose the Save button and click the Back < button. |  |  |

### Retrieve Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Product data from SAP S/4HANA Cloud Public Edition through the system interface. This master data will be used to create prices and may be referenced by transaction data (sales and/or purchase orders, claims, etc.).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Excise Tax Management by Vistex as an Excise Tax Admin. | The Fiori launchpad displays.You will execute this procedure once if you SAP Extended Price Management. Do not execute this procedure more than once to have more than one of these solutions. |  |
| 2 | Access the tile | Choose External Data(Tile group) under Excise Tax Management (Space) and choose Data Ingestion Work Managers. |  |  |
| 3 | Schedule Materials Load | Choose the Schedule button and select 3.1 Materials Load.. |  |  |
| 4 | Schedule Job | Choose the Schedule button in the popup displayed. |  |  |
| 5 | Check Completed | Choose the Refresh button (System will take few seconds to complete the job) and verify the status has changed to Completed. | The Status is changed to Completed. |  |
| 6 | Object Number | Choose the Object and note down the Object number. |  |  |
| 7 | Home screen | Choose the Cancel button and choose the Home button. |  |  |
| 8 | Access Material tile | Go To the Master Data tile group and choose the Materials tile.. |  |  |
| 9 | Search Materials | Choose the Go button and verify the Materials. |  |  |
| 10 | Maintain Tax Attributes at Product Level | Maintain the Product as FG0506 and choose the Go button. |  |  |
| 11 | Select Customer | Drill down into the Material. |  |  |
| 12 | Edit | Choose the Edit button. |  |  |
| 13 | Header Status | In the Header section, update the status to Excisable. |  |  |
| 14 | Tax Type parameters | Choose the Tax Type Specific Parameters section. Click on ‘+’ button.Enter the values into the fields as given in the table.Table 38:Company CodeTax TypeMaterial GroupAlcohol By VolumeValidityUS Company CodeAlcohol TaxGroup 142<01.01.2025> to < 31.12.9999> |  |  |
| 15 | Save | Choose the Save button and choose Back < button. |  |  |

### Create Sales Order

Purpose

This process step shows you how to create a sales order for the excise material and customer relevant with the conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) . | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, select Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold To party: 33105001Ship To party: 33105001Cust. Reference: <ETM Reference>Material Number: FG0506Order Quantity: 100Sales Unit : BT |  |  |
| 6 | Save Document | Choose Save. Make a note of the sales order number. | The order is saved and sales order number is displayed at the bottom of screen.System gives a message: Standard Order XXXX has been saved. |  |

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as aShipping Specialist . |  |  |
| 2. | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Planned Creation Date: <input the date range>Sales Document: Sales order number created previously |  |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5. | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries.Make a note of the delivery number. | Make a note of the delivery number. |

### Execute Picking and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to execute picking and perform Post Goods Issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as aShipping Specialist . |  |  |
| 2. | Access the App | Open Manage Outbound Deliveries (F0867A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go.Shipping point: 3310Overall Status: Ready for Picking | List of outbound deliveries displayed on the screen as per selection criteria. |  |
| 4. | Select Outbound Delivery for picking | Select the outbound delivery created in previous step and click on Pick. | Screen Pick Outbound Delivery is displayed. |  |
| 5. | Enter Picked Quantity | In the Picking tab, enter the Picked Qty as <100>. |  |  |
| 6. | Post Good Issue | Click on the Post Goods Issue. |  |  |
| 7. | Check Message Log | Click on the Message Log. | Make a note of the delivery number. |  |

### Retrieve Material Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Pull the Material Documents created from ERP system to Excise Tax Management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the GTMS system using the user ID and password provided. | The Fiori launchpad displays. |  |
| 2 | Access the tile | In the External Data Tile group, click the Data Ingestion Tile. |  |  |
| 3 | Schedule Material Documents Load | Choose the Schedule button and select the work manager 4.1 Material Documents Load. |  |  |
| 4 | Input Material Document | Enter the Material Document Number, created in the [Create Delivery](#unique_28) [page ] 36 step & choose Schedule button. |  |  |
| 5 | Check Status Completed | Choose the Refresh button until the work manager status is Completed. | The Status is changed to Completed. |  |
| 6 | Object Number | Choose the Object (1) hyperlink and note down the Object number. | Note down the Object number |  |
| 7 | Return to Home page | Choose the Cancel button and navigate to Home Page.. |  |  |

### Update Stock Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

User will be able to: Update Stock Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the GTMS system using the user ID and password provided. |  |  |
| 2 | Access Stock Ledger Update | Under Tools, choose Stock Ledger Update. |  |  |
| 3 | Schedule | Choose the Schedule button and select Select Stock Ledger Update from the dropdown menu. |  |  |
| 4 | Input Material Document Number | Enter the Material Document Number that was created in the Create Delivery and Material Document step and choose Schedule button. |  |  |
| 5 | Check Completed | Choose the Refresh button until the work manager status is Completed. | The Status is changed to Completed. |  |
| 6 | Home Page | Choose Cancel and navigate to Home Page. |  |  |
| 7 | Access Stock Ledger tile | Under the Tools tile group, choose the Stock Ledger tile. |  |  |
| 8 | All Lines card | Choose All Lines card. |  |  |
| 9 | Search Object | Search the created object using the Material Document Number that was created in the Create Delivery and Material Document step and choose Go. | The corresponding lines will be displayed.Verify that the Tax Amount (Statistical) and Tax Amount columns display the values. None of the field values should be 0.00 EUR. Verify all the data and navigation of the line item created. |  |

### Calculate Excise Tax Amounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you the Postings for the Tracking document and review the data. .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the GTMS system using the user ID and password provided. | The Fiori launchpad displays. |  |
| 2 | Access Tax Amount Accural | Under Tools , choose Tax Amount Accrual . |  |  |
| 3 | Schedule Accrual | Choose the Schedule button and then select Accrual from the dropdown. |  |  |
| 4 | Enter Tax rate document and tracking date | Enter the below details and choose the Schedule button:Tax Rate Document : Enter the Tax Rate document from step Create a Tax Rate Document (for example, 56 (Alcohol - Germany)) |  |  |
| 5 | Check Completed | Choose the Refresh button until the work manager status is Completed. | The Status is changed to Completed. |  |
| 6 | Tracking document Page | Choose the Tracking (1). | Note down the Tracking document number XXXXXXX |  |
| 7 | Access Stock Ledger tile | Under the Tools Tile group, choose the Stock Ledger Tile. |  |  |
| 8 | All Lines card | Choose All Lines card. |  |  |
| 9 | Search Object | Search the object created using the Material Document Number that was created in the Create Delivery and Material Document step and choose Go. | The corresponding lines will be displayed.Verify that the Tax Amount (Statistical) and Tax Amount columns display the values. None of the field values should be 0.00 EUR. Verify all the data and navigation of the line item created. |  |

### Post Excise Taxes to Finance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post excise taxes for the tracking document.

Procedure

|  |
| --- |
| Note The G/L Account 0041000000 needs to be tax exempted. Perform the below steps to verify if the G/L Account 0041000000is tax exempted.Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration and open Manage G/L Account Master Data (F0731A) app.Search for the G/L Account with the following filter values and choose Go,View: Chart of Accounts ViewG/L Account: 0041000000Chart of Accounts: YCOAChoose Edit and then navigate to Company Code Data tab.Choose the line corresponding to the company code 3310. This opens the Company Code Assignment page of the chosen entry.If the checkbox Post Without Tax Allowed is checked, uncheck it.In Tax Category, enter the value I0 (Tax Exempted).In Field Status Group, enter YB01.Choose OK to save the changes made. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the GTMS system using the user ID and password provided. |  |  |
| 2 | Access Accural Tracking | Under Tools, choose Accural Tracking . | The SAP Fiori launchpad displays. |  |
| 3 | Search Tracking Document | Choose the Expand Header button.Enter the Tracking document created in the previous Exercise Step in the Tracking field and choose Go. |  |  |
| 4 | Verify result | Verify the results in the worklist |  |  |
| 5 | Check Details | Choose the row and verify the details in the right-hand pane. |  |  |
| 6 | Codes tab to Post | Go to the Codes tab, select the checkbox and choose Post. |  |  |
| 7 | Save | Choose Save button. |  |  |
| 8 | Posting Status | Choose Go button and Verify the Posting Status in the row and choose the Details arrow. | Note the Posting Document Number _________ (e.g. 1905). |  |
| 9 | Verify Material Movements | Verify all the data in the Summarization and Material Movements tabs. |  |  |
| 10 | View Posting Document | Choose the Posting link in the Summarization tab to navigate to the posting document. |  |  |
| 11 | Verify data | Verify the data in the Postings tab. |  |  |
| 12 | Home page | Navigate to the Home page. |  |  |
| 13 | Access Data Extraction tile | In the External data tile group, choose Data Extraction. |  |  |
| 14 | Schedule Posting Documents Outbound | Choose the Schedule button.Select the work manager E0_Posting Documents Outbound from the drop-down menu and choose the Schedule button. |  |  |
| 15 | Check Completed data | Choose Refresh until the work manager status is completed. | After the completion of the job, the results will be displayed in the Output section. |  |
| 16 | FI Document | Choose the Success (1) link and note down the document number which is the FI document number(s). | Note the FI Document Number/ Journal Entry created: |  |
| 17 | View posting document | Choose the Cancel button and choose the Posting document Hyperlink under the Input field. |  |  |
| 18 | Check FI Document | In the popup, choose the Posting document hyperlink. | Verify if the FI Document number/Journal Entry number noted above Step is reflected in the Snapping header. |  |

### Verify Finance Document Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Verify the Tracking document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an General Ledger Accountant. |  |  |
| 2 | Access Manage Journal Entries app | In the Master Data tile group, choose on the Manage Journal Entries app. | The SAP Fiori launchpad displays. |  |
| 3 | Search FI Document | In the Journal Entry field, choose the FI Document Number noted in the previous step and choose the Go. |  |  |
| 4 | Navigate | Choose the Navigation button for the entry in the worklist. |  |  |
| 5 | FI Document Details | Choose the Full screen button. | Verify the FI Document data. |  |

## Appendix

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

This Appendix contains the contents of files that need to be uploaded are part of preliminary steps related to SAP Excise Tax Management by Vistex.

Copy the contents of each section into a text file named as the section title. It is recommended to use Notepad (default simple text editor supplied with Microsoft Windows) instead of Microsoft Excel to avoid auto-formatting issues. The contents of each section contain tab-delimited data, and the column headers (Dimension, Description, Position) should be included in the text file contents.

### Tax Rate Template

Please find the format of the Tax rate template.txt file for reference

Table 39:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Agreement External ID Status | Description | Country | Tax Type Accrual | Frequency | Valid From | Valid To | Currency | Program | Agreement Type Usage | Agreement Type |
| #HD | E0TX2 | Excise Tax - Alcohol | Germany DE | ALCT | EM | 01.01.2025 | 31.12.9999 | EUR | T | E0X0 | A |

Table 40:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Step Type | Step Number | Description | Step Contribution | Parent Step | Input | Collection |
| #A1 | E0TX | 1 | Excise Tax Lines | D |  | E0C1 |  |
| #A2 | E0PT | 2 | Final Tax D | 1 |  | E0C2 |  |

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
> Flagged while digesting this document, not verified: Internal inconsistencies in sample data: company code 3310 is described as 'AE Company Code' (country AE, AED) but plant/posting tables use 'US Company Code', USA and USD, and the tax rate rate is labelled EUR per 1 LA while the document currency is USD

> [!warning] Conflict
> Flagged while digesting this document, not verified: Calculate step cites example tax rate document '56 (Alcohol - Germany)' while the created document is 'Alcohol - United States'

## Connections
- part-of :: [[_cluster]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-4lo-1033]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 62,604 chars in the whole document
