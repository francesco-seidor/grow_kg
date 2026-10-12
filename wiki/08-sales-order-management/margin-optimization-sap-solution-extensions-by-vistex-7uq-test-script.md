---
id: 08-sales-order-management/margin-optimization-sap-solution-extensions-by-vistex-7uq-test-script
title: Margin Optimization – SAP Solution Extensions by Vistex (7UQ) – Test Script (7UQ_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 7UQ: integrating SAP margin optimization solutions by Vistex with S/4HANA Cloud Public Edition; prerequisites, preliminary steps, 11 test procedures."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/condition-contract-settlement]
aliases: [7UQ_S4CLD2608_BPD_EN_XX]
keywords: ["Rebates, Commissions and Royalties Settlement", margin optimization, vistex integration, channel programs, vendor programs, rights and royalties, sales rebates, purchasing rebates, price management, master data retrieval]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7UQ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1230
topic: 08-sales-order-management/condition-contract-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Margin Optimization – SAP Solution Extensions by Vistex (7UQ) – Test Script (7UQ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7UQ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Rebates, Commissions and Royalties Settlement** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Margin Optimization – SAP Solution Extensions by Vistex (7UQ)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Margin Optimization – SAP Solution Extensions by Vistex (7UQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232842674)

[2 Prerequisites 4](#_Toc232842675)

[2.1 System Access 4](#_Toc232842676)

[2.2 Roles 4](#_Toc232842677)

[2.3 Additional Manual Configuration 5](#_Toc232842678)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232842679)

[2.4.1 General Master Data and Organizational Data 5](#_Toc232842680)

[2.4.2 Master Data for Pricing 6](#_Toc232842681)

[2.4.3 Master Data for Channel Programs 6](#_Toc232842682)

[2.4.4 Master Data for Vendor Programs 7](#_Toc232842683)

[2.4.5 Master Data for Rights & Royalties 8](#_Toc232842684)

[2.5 Business Conditions 8](#_Toc232842685)

[2.6 General Preliminary Steps 9](#_Toc232842686)

[2.6.1 Configure Allowed Currency and Units 9](#_Toc232842687)

[2.6.2 Create Field Values 10](#_Toc232842688)

[2.7 Preliminary Steps for Channel Programs 13](#_Toc232842689)

[2.7.1 Create G/L Accounts 13](#_Toc232842690)

[2.7.2 Assign Customer Posting Accounts 14](#_Toc232842691)

[2.7.3 Create Sales Agreement 18](#_Toc232842692)

[2.7.4 Create Sales Order 20](#_Toc232842693)

[2.8 Preliminary Steps for Vendor Programs 20](#_Toc232842694)

[2.8.1 Create G/L Accounts 20](#_Toc232842695)

[2.8.2 Assign Vendor Posting Accounts 21](#_Toc232842696)

[2.8.3 Create Purchasing Agreement 25](#_Toc232842697)

[2.8.4 Create Purchase Order 27](#_Toc232842698)

[2.9 Preliminary Steps for Rights & Royalties 28](#_Toc232842699)

[2.9.1 Create Cross References 28](#_Toc232842700)

[2.9.2 Create Dimensions 29](#_Toc232842701)

[2.9.3 Create G/L Accounts 30](#_Toc232842702)

[2.9.4 Assign Royalty Posting Accounts 31](#_Toc232842703)

[2.9.5 Create Media Rights Out Program 33](#_Toc232842704)

[2.9.6 Create Royalty Agreement 36](#_Toc232842705)

[3 Overview Table 38](#_Toc232842706)

[4 Test Procedures 40](#_Toc232842707)

[4.1 Retrieve Customers 40](#_Toc232842708)

[4.2 Retrieve Vendors 41](#_Toc232842709)

[4.3 Retrieve Products 42](#_Toc232842710)

[4.4 Retrieve Prices 43](#_Toc232842711)

[4.5 Maintain Prices 46](#_Toc232842712)

[4.6 Retrieve Sales Invoices 50](#_Toc232842713)

[4.7 Determine Sales Rebate 51](#_Toc232842714)

[4.8 Retrieve Purchase Orders 56](#_Toc232842715)

[4.9 Determine Purchasing Rebate 58](#_Toc232842716)

[4.10 Retrieve R&R Master Data 64](#_Toc232842717)

[4.11 Determine Royalty 66](#_Toc232842718)

[5 Appendix 70](#_Toc232842719)

[5.1 Language.txt 70](#_Toc232842720)

[5.2 Right Type.txt 73](#_Toc232842721)

[5.3 Territory.txt 78](#_Toc232842722)

## Purpose

Overview

This scope item covers the integration of SAP margin optimization solutions by Vistex to SAP S/4HANA Cloud Public Edition.

The SAP margin optimization solutions by Vistex include:

- SAP Extended Price Management by Vistex
- SAP Price Staging Hub by Vistex
- SAP Channel Program Management by Vistex
- SAP Vendor Program Management by Vistex
- SAP Rights & Royalty Management by Vistex, cloud edition

Each of these solutions addresses a critical business process in the buying or selling of goods or services: setting pricing and discounting strategies, negotiating incentive or promotional programs, tracking applicable benefits, and managing the lagged payment cashflow. When combined, these solutions offer deep insight into the true gross-to-net margins and profitability of complex and overlapping incentives and ensure full utilization and compliance of program terms and conditions.

SAP margin optimization solutions by Vistex can be integrated into SAP S/4HANA Cloud Public Edition using the available APIs published by SAP. The full functional capabilities of the suite of margin optimization solutions are not represented in this document, but the full scope of integration between the SAP margin optimization solutions suite and SAP S/4HANA Cloud Public Edition is represented and tested by the scenarios in this document.

There are several margin optimization solutions available. This document covers the integration test cases for all SAP margin optimization solutions by Vistex, but only some preliminary steps and test procedures are applicable to each margin optimization solution. The relevance of each preliminary step (or portion thereof) and test procedure is noted; if no specific mention is given, the preliminary step or test procedure is relevant to any or all margin optimization solutions.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System for SAP Vendor Program Management by Vistex or SAP Extended Price Management by Vistex or SAP Price Staging Hub by Vistex | [https://8e2a9e40-0594-1ede-8e86-c4173e2da333.abap-web.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html](https://8e2a9e40-0594-1ede-8e86-c4173e2da333.abap-web.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html) |
| System for SAP Channel Program Management by Vistex | [https://56e312d4-3cdd-1eee-8e86-1cbb1a3401a0.abap-web.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html](https://56e312d4-3cdd-1eee-8e86-1cbb1a3401a0.abap-web.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html) |
| System for SAP Rights & Royalty Management by Vistex | [https://0e991bcf-02b0-1edd-bab6-429fa33e313b.abap-web.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html](https://0e991bcf-02b0-1edd-bab6-429fa33e313b.abap-web.eu10.hana.ondemand.com/sap/bc/ui5_ui5/vui/bnlnpd/index.html) |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Log On |
| --- | --- | --- |
| Channel Program Admin | MXTPAD | Create a user with this role (instructions in the [Administration Guide](https://help.sap.com/docs/SALES_SOLUTIONS_BY_VISTEX_CLOUD)) to perform tests relevant for SAP Channel Program Management by Vistex (sell-side activities). |
| Vendor Program Admin | WXPQ_UIP15 | Create a user with this role (instructions in the [Administration Guide](https://help.sap.com/docs/SALES_SOLUTIONS_BY_VISTEX_CLOUD)) to perform tests relevant for SAP Vendor Program Management by Vistex (buy-side activities).This role is also able to perform tests relevant for SAP Extended Price Management by Vistex (price setting and changes) and SAP Price Staging Hub by Vistex (price determination and publishing). |
| Rights & Royalty Admin | RRADMIN | Create a user with this role (instructions in the [Administration Guide](https://help.sap.com/docs/SALES_SOLUTIONS_BY_VISTEX_CLOUD)) to perform tests relevant for SAP Rights & Royalty Management by Vistex (rights & royalties activities). |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f87a66ed934fe4909e69fbf6ac458f34)

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or use the sample data listed in the following sections as the data for the preliminary steps and the test procedures. Most of the sample data given below is available for SAP S/4HANA Cloud Public Edition when you select the Enterprise Management bundle in SAP Central Business Configuration. Any exceptions or additional actions are described in the following sections.

#### General Master Data and Organizational Data

The master data and organizational data in this section should be used—or substituted with your own data—regardless of which SAP margin optimization solutions by Vistex you have subscribed.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company | 1710 |  | Relevant for all activities (any SAP margin optimization solutions by Vistex) |
| Plant | 1710 |  | Relevant for all activities (any SAP margin optimization solutions by Vistex) |
| Storage Location | 171A |  | Relevant for all activities (any SAP margin optimization solutions by Vistex) |
| Material Type(3 types) | FERTHAWAMAT |  | Relevant for all activities (any SAP margin optimization solutions by Vistex) |
| <operating year> | 01-Jan-2024 to 31-Dec-2024 |  | You may substitute your current calendar or fiscal year |

#### Master Data for Pricing

The master data and organizational data in this section should be used—or substituted with your own data—if you have subscribed to SAP Extended Price Management by Vistex or SAP Price Staging Hub by Vistex.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11_PH_CO21 | Combination wrench 21mm | Relevant for pricing activities (SAP Extended Price Management by Vistex or SAP Price Staging Hub by Vistex) |

#### Master Data for Channel Programs

The master data and organizational data in this section should be used—or substituted with your own data—if you have subscribed to SAP Channel Program Management by Vistex.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Area | 17AA/10/00 – you must generate this sales area in SAP S/4HANA Cloud Public Edition; it is not default config |  | Relevant for sell-side activities (SAP Channel Program Management by Vistex) |
| Sales Order | OR |  | Relevant for sell-side activities (SAP Channel Program Management by Vistex) |
| Delivery Type | LF |  | Relevant for sell-side activities (SAP Channel Program Management by Vistex) |
| Invoice | F2 (with copy controls enabled for Reference Field value from Sales Order to Invoice) |  | Relevant for sell-side activities (SAP Channel Program Management by Vistex) |
| General Ledger Posting Account External Id (3 accounts) | 004100040000125500000021720200 | Customer Revenue/ExpenseCustomer Clearing AccountWrite off Supplier | Relevant for sell-side activities (SAP Channel Program Management by Vistex) |
| Reconciliation Posting Account External ID | 0012100000 | Customer Recon. Account | Relevant for sell-side activities (SAP Channel Program Management by Vistex) |
| Customer | 17100001 – you must extend this customer to the new 17AA/10/00 sales area | Domestic US Customer 1 | Relevant for sell-side activities (SAP Channel Program Management by Vistex)This customer should be referenced on sales orders intended to be in scope for the sales agreement to be defined in the Preliminary Step 2.7.3. |
| Material | FG011 – you must extend this material to the new 17AA/10/00 sales area | Electric Fan | Relevant for sell-side activities (SAP Channel Program Management by Vistex)This material should be sold to the above customer on sales orders intended to be in scope for the sales agreement to be defined in the Preliminary Step 2.7.3. |

#### Master Data for Vendor Programs

The master data and organizational data in this section should be used—or substituted with your own data—if you have subscribed to SAP Vendor Program Management by Vistex.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Area | 1710/10/00 |  | Relevant for buy-side activities (SAP Vendor Program Management by Vistex) |
| Purchase Organization | 1710/001 |  | Relevant for buy-side activities (SAP Vendor Program Management by Vistex) |
| Purchase Order | NB |  | Relevant for buy-side activities (SAP Vendor Program Management by Vistex) |
| General Ledger Posting Account External Id (3 accounts) | 004100000000125010000021540000 | Supplier RevenueSupplier Clearing AccountWrite off Supplier | Relevant for buy-side activities (SAP Vendor Program Management by Vistex) |
| Reconciliation Posting Account External ID | 0021100000 | Supplier Recon. Account | Relevant for buy-side activities (SAP Vendor Program Management by Vistex) |
| Vendor | 17305001 | Domestic US Supplier CP001 | Relevant for buy-side activities (SAP Vendor Program Management by Vistex)This vendor should be referenced on purchase orders intended to be in scope for the purchasing agreement to be defined in the Preliminary Step 2.8.3. |
| Material | TG0501 | Thermo Coffee Cup 0,4l | Relevant for buy-side activities (SAP Vendor Program Management by Vistex)This material should be purchased from the above vendor on purchase orders intended to be in scope for the purchasing agreement to be defined in the Preliminary Step 2.8.3. |

#### Master Data for Rights & Royalties

The master data and organizational data in this section should be used—or substituted with your own data—if you have subscribed to SAP Rights and Royalty Management by Vistex, cloud edition.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Partner | 17100088 | Domestic US Supplier 88 | Relevant for royalty activities (SAP Rights & Royalty Management by Vistex) |
| Material | FG126 | FIN126, MTS-DI, PD, SERIALNO | Relevant for royalty activities (SAP Rights & Royalty Management by Vistex) |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Required to be selected to provide the journal entry API for posting calculated amounts to SAP S/4HANA Cloud Public Edition. This is only relevant for SAP Channel Program Management by Vistex, SAP Vendor Program Management by Vistex, and/or SAP Rights and Royalty Management by Vistex, cloud edition. |
| J59 - Accounts Receivable | Required to be selected to provide the journal entry API for posting calculated amounts to SAP S/4HANA Cloud Public Edition. This is only relevant for SAP Channel Program Management by Vistex, SAP Vendor Program Management by Vistex, and/or SAP Rights and Royalty Management by Vistex, cloud edition. |
| J60 - Accounts Payable | Required to be selected to provide the journal entry API for posting calculated amounts to SAP S/4HANA Cloud Public Edition. This is only relevant for SAP Channel Program Management by Vistex, SAP Vendor Program Management by Vistex, and/or SAP Rights and Royalty Management by Vistex, cloud edition. |

### General Preliminary Steps

This section covers the prerequisite Preliminary Steps necessary for any SAP margin optimization solution by Vistex.

You must perform these steps for any solution(s) to which you have subscribed.

#### Configure Allowed Currency and Units

Use

General configuration is needed in SAP margin optimization solutions by Vistex. This step is required regardless of the SAP margin optimization solutions by Vistex licensed.

Procedure

1. Log into the Fiori link with the user ID and password provided.
2. Click on the Administrative Tasks tile group from the menu.
3. Click on the Admin Activities tile.
4. Click on the Currencies and Units node.
5. Click on the Allowed Currencies.
6. Click on the Add (‘+’) button.
7. Select <USD> in the Currency field.
8. Click on the Create button.
9. Click Save button after verifying the details in the document section.
10. Click on the Back (‘<’) button.
11. Click on the Allowed Units under Currencies and Units node.
12. Click on the Add (‘+’) button.
13. Click on the selection symbol in the Internal UOM field.
14. Select ST in the Internal UOM field or enter <PC> in the field and press Enter.
15. Click on the Create button.
16. After verifying the details in the document section, click on the Save button.
17. Again click on the Add ('+') button.
18. Select EA in the Internal UOM field or enter <PC> in the field and press Enter.
19. Click on the Create button.
20. After verifying the details in the document section, click on the Save button.
21. Repeat Steps 17 to 20 for the following additional Allowed Units:
    - M3 (Cubic meter)
    - G (Gram)
    - KG (Kilogram)
    - LB (Pound)

You may need to define additional Allowed Units based on the units of measure used in your master data.

Result

The user-selected currency is allowed. The user-selected units of measure are allowed.

#### Create Field Values

Use

General configuration is needed in SAP margin optimization solutions by Vistex. This step is required regardless of the SAP margin optimization solutions by Vistex licensed.

Procedure

1. Navigate to the Administrative Tasks tile group and click on the Admin Activities tile.
2. Expand Field Values Node.
3. Click on the Product Group 1.
4. Click on the Edit button and click on the Add (‘+’) button to add Product Group 1 values.
5. Enter Product Group 1 value as PRM and Description as Premium.
6. Click on the Apply button.
7. Repeat Steps 4 to 6 to add the following additional field values for Product Group 1:
    - STD (Standard)
    - VAL (Value)
    - L001 (Trading Materials)
    - L002 (Finished Goods)
8. Click on the Save button.
9. Click on the Back (‘<‘) button.
10. Expand Field Values node.
11. Click on the Product Group 2.
12. Click on the Edit button and click on the Add (‘+’) button to add Product Group 2 values, similar to Steps 4 to 6, for the following:
    - ARTL (Air Tools)
    - BOLT (Bolts)
    - DHW (Door Hardware)
    - ENG (Engines & Generators)
    - HNTL (Hand Tools)
13. Click on the Save button.
14. Click on the Back (‘<‘) button.
15. Expand Field Values node.
16. Click on the Customer Classification.
17. Click on the Edit button and click on the Add (‘+’) button to add Customer Classification values.
    - CO (Corporate)
    - DI (Distributor)
    - DR (Direct)
    - ID (Indirect)
    - RS (Reseller)
    - SR (Store/Retail)
18. Click on the Save button.
19. Click on the Back (‘<‘) button.
20. Expand Field Values node.
21. Click on the Customer Group 1.
22. Click on the Edit button and click on the Add (‘+’) button to add Customer Group 1 values:
    - AU (Auto Dealers)
    - HD (Hardware Stores)
    - IN (Industrial Supply)
    - RE (Other Retail)
23. Click on the Save button.
24. Click on the Back (‘<‘) button.
25. Click on the Customer Group 2.
26. Click on the Edit button and click on the Add (‘+’) button to add Customer Group 2 values:
    - LRG (Large)
    - MED (Medium)
    - SML (Small)
27. Click on the Save button.
28. Click on the Back (‘<‘) button.
29. Click on the Vendor Classification.
30. Click on the Edit button. Click on the Add (‘+’) button to add Vendor Classification values:
    - DO (Domestic)
    - IN (International)
    - ON (One Time)
31. Click on the Save button.
32. Click on the Back (‘<‘) button.
33. Click on the Company.
34. Click on the Edit button and click on the Add (‘+’) button.

Enter the following Field = Value data:

-
    - Company = 1710
    - Currency = USD
    - FI Posting Period Profile = Monthly
    - Description = Vanguard Tool

1. Click on the Save button.
2. Click on the Back (‘<‘) button.
3. Click on the Business Unit.
4. Click on the Edit button.
5. If you have licensed SAP Channel Program Management by Vistex…

Click on the Add (‘+’) button and enter the following Business Unit Value:

-
    - Business Unit = NA02
    - Company = Vanguard Tool
    - Description = US Manufacturing

1. If you have licensed SAP Vendor Program Management by Vistex…

Click on the Add (‘+’) button and enter the following Business Unit Value:

-
    - Business Unit = NA01
    - Company = Vanguard Tool
    - Description = US Distribution

1. If you have licensed SAP Rights & Royalty Management by Vistex…

Navigate to the General Configuration tile group and click on the Admin Activities tile.

Expand Field Values Node.

Click on the Business Unit and click on the Edit button.

Click on the Add (‘+’) button and enter the following Business Unit Value:

-
    - Business Unit = NA3
    - Description = US Rights and Royalty
    - Group Currency = USD

1. Click on the Save button.
2. Click on the Back (‘<‘) button twice.
3. Navigate to the General Configuration tile group and click on the Admin Activities tile.
4. Expand Field Values Node.
5. Click on the IP Type.
6. Click on the Edit button and click on the Add (‘+’) button.
7. Enter IP Type as RBRA and Description as Brand.
8. Click on the Save button.
9. Click on the Home button.

Result

Field values are set.

### Preliminary Steps for Channel Programs

This section covers the prerequisite Preliminary Steps for SAP Channel Program Management by Vistex.

You do not need to perform these steps if you have not subscribed to this solution.

#### Create G/L Accounts

Use

Channel Programs may generate rebate or reimbursement payments that are typically posted to Accounts Payable for payment or Accounts Receivable as a credit against other amounts owed by the customer. This preliminary step links the payments to the appropriate account(s).

Procedure

1. Navigate to the Master Data tile group and click on the G/L Accounts tile.
2. Click on the Create button.
3. Enter one Posting Account using a single line from the list of accounts below:
    - Posting Account External Id as 0041000400, Description as Customer Revenue/Expense, and status as Active
    - Posting Account External Id as 0012550000, Description as Customer Clearing Account, and status as Active
    - Posting Account External Id as 0021720200, Description as Write off Supplier, and status as Active
4. Click on the Check button and then click on the Save button.
5. Repeat Steps 2 to 4 above for each additional Posting Account listed above.
6. Click on the Home button.
7. Navigate to the Master Data tile group and click on the Reconciliation Account tile.
8. Click on the Create button.
9. Enter Posting Account External Id as 0012100000, Description as Customer Recon. Account, and status as Active.
10. Click on the Check button and then click on the Save button.
11. Click on the Home button.

Result

G/L accounts are created.

#### Assign Customer Posting Accounts

Use

Link customer-specific accounts in SAP S/4HANA Cloud Public Edition to the customer-specific subledgers in SAP Channel Program Management by Vistex.

Procedure

1. Log into the Fiori link with the user ID and password provided for a user with the Channel Program Admin role.
2. Navigate to the Master Data tile group and click on the Posting Area tile.
3. Click on the Edit button.
4. In the B/S Account tab, click on the Add (‘+’) button.
5. Enter field values as indicated in the table below.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| Entry No. | Field | Value |
| --- | --- | --- |
| 1 | Posting Application | BB Accrual |
|  | Business Unit | US Manufacturing |
|  | Posting Group | Liability Account |
|  | Posting Account | 0012550000 (Customer Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |
| 2 | Posting Application | BB Settlement |
|  | Business Unit | US Manufacturing |
|  | Posting Group | Liability Account |
|  | Posting Account | 0012550000 (Customer Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |
| 3 | Posting Application | CR Accrual |
|  | Business Unit | US Manufacturing |
|  | Posting Group | Liability Account |
|  | Posting Account | 0012550000 (Customer Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |
| 4 | Posting Application | CR Settlement |
|  | Business Unit | US Manufacturing |
|  | Posting Group | Liability Account |
|  | Posting Account | 0012550000 (Customer Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |

1. Click on the P/L Account tab.
2. Click on the Add (‘+’) button.
3. Enter the field values as indicated in the table below.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| Entry No. | Field | Value |
| --- | --- | --- |
| 1 | Posting Application | BB Accrual |
|  | Business Unit | US Manufacturing |
|  | Posting Group | P&L Account |
|  | Posting Account | 0041000400 (Customer Revenue/Expense) |
|  | validity | <operating year> |
|  | Status | Active |
| 2 | Posting Application | CR Accrual |
|  | Business Unit | US Manufacturing |
|  | Posting Group | P&L Account |
|  | Posting Account | 0041000400 (Customer Revenue/Expense) |
|  | validity | <operating year> |
|  | Status | Active |
| 3 | Posting Application | CR Settlement |
|  | Business Unit | US Manufacturing |
|  | Posting Group | P&L Account |
|  | Posting Account | 0041000400 (Customer Revenue/Expense) |
|  | validity | <operating year> |
|  | Status | Active |

1. Click on the Write Off Account tab. Click on the Add button.
2. Enter the field values as indicated in the table below.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| Entry No. | Field | Value |
| --- | --- | --- |
| 1 | Posting Application | BB Settlement |
|  | Business Unit | US Manufacturing |
|  | Posting Group | Billback Adjustment Account |
|  | Posting Account | 0021720200 (Write off Customer) |
|  | validity | <operating year> |
|  | Status | Active |
| 2 | Posting Application | CR Settlement |
|  | Business Unit | US Manufacturing |
|  | Posting Group | Write Off |
|  | Posting Account | 0021720200 (Write off Customer) |
|  | validity | <operating year> |
|  | Status | Active |

1. Click on the Save button.
2. Click on the Home button.

Result

Customer Posting Accounts are assigned.

#### Create Sales Agreement

Use

This scenario illustrates the Customer rebate pay out based on sales volume. The Tracking document captures the sales invoices data and calculates rebate payout according to the conditions maintained in the agreement. The Agreement document holds the eligible Accrual and Settlement amounts which will be posted.

Procedure

Complete the following tasks in this document before attempting this Preliminary Step:

- General Preliminary Steps 2.6.1 and 2.6.2
- Preliminary Steps 2.7.1 and 2.7.2
- Test Procedure 4.1 Retrieve Customers
- Test Procedure 4.3 Retrieve Products

1. Log into the Fiori System using a user ID and password having Channel Program Admin role.
2. Navigate to the Rebates tile group and click on the Master Agreements tile.
3. Click on the Create button.
4. In the General Data tab, the default Status will display.
5. Maintain values in fields as mentioned below:
    - Master Agreement Description: User Defined
    - Master Agreement: User Defined (must be unique every time)
    - Master Request Description: User Defined
    - Business Unit: US Manufacturing
    - Company: Vanguard Tool
    - Currency: USD
    - Master Agreement Program: Rebates
    - Legal Validity: <operating year>
    - Validity: <operating year>
6. Master Agreement Category data will auto-populate and click on the Check button.
7. Click on the Eligibility Customer tab.
8. Click on the Add (‘+’) button in the Eligible Customer section.
9. Click on the drop-down in Applies To and select the Customer.
10. In the Customer field, enter 17100001 and click on the Check button.
11. Click on the Sub-Agreement tab and click on the Create button.
12. Enter Sub-Agreement ID and Description (Both are user-defined and must be unique values).
13. Maintain values in fields as mentioned below:
    - Sub Agreement Program: Volume Rebate-$/unit (Qty Scale) (MX_TP_VOL01)
    - Legal Validity: <operating year>
    - Processing Sequence: 1
    - Period Profile: Monthly
    - Accrual Frequency: Monthly
    - Settlement Frequency: Monthly
14. Drill-Down to the Sub-Agreement by clicking on the Details (‘>‘) icon at the end of the Sub-Agreement row.
15. Click on the Eligibility tab and click on the Add (‘+’) button in the Sources tab.
16. Click on the Source drop-down, select DirectSales, click on the F4 button, and select SalesInvoice.
17. Scroll down to Eligible Product Groupings and click on the Add (‘+’) button.
18. Enter the Group name as User Defined, Group type as Payout, Source as Direct Sales, and click on the Create Flexible Group Icon.
19. Enter Description as User Defined, click on the drop-down menu of the Find Icon and select Product.
20. In the Product field enter FG011(Electric Fan) and click on the OK button.
21. Click on the Apply button.
22. Click on the Benefits tab and click on the Add button.
23. Click on the Product Group F4 button, select product group, Rate type as Rate per Unit, and enter Rate as 7, Per as 1, and On as Sales Quantity (Q)
24. Click on the Define Scale button.
25. Click on the Add button three times and enter data for three scales as described below:
    - Sales Quantity (Q) = 50, 200, 500
    - Rate = 7, 10, 15
26. Click on the Check button.
27. Click on the Apply button.
28. Click on the Estimated Accrual Rate tab and click on the Add button.
29. Click on the Appliesto drop–down select Payout group.
30. Click on the F4 button and select Payout Group (e.g. Material), Rate Type as Rate Per Unit, and enter Rate as 20, Per as 1, and On field as Sales Quantity (Q).
31. Click on the Apply button and click on the Save button.
32. Click on the Submit button and click on the Submit in the pop-up, note the Master request ID number (e.g. 643).
33. Click on the Approve button and click on the Approve in the pop-up.
34. Note the Master Agreement (e.g. Sales RebateMA03).
35. Click on the Home button.

Result

Sales Agreement is created.

#### Create Sales Order

Use

This scenario illustrates the Customer rebate pay out based on sales volume. A sales order records the customer’s purchase and might qualify for a rebate payment.

Procedure

Complete the following tasks in this document before attempting this Preliminary Step:

- General Preliminary Steps 2.6.1 and 2.6.2
- Preliminary Steps 2.7.1 and 2.7.2
- Test Procedure 4.1 Retrieve Customers
- Test Procedure 4.3 Retrieve Products

1. Log into the SAP S/4HANA Cloud Public Edition system.
2. Create a sales order of type OR, with customer 17100001 and material FG011, on a date with the <operating year>, a reasonable quantity, and any remaining required fields can be <user defined>.
3. Click on the Home button.

Result

Sales order is created.

### Preliminary Steps for Vendor Programs

This section covers the prerequisite Preliminary Steps for SAP Vendor Program Management by Vistex.

You do not need to perform these steps if you have not subscribed to this solution.

#### Create G/L Accounts

Use

Vendor Programs may generate rebate or reimbursement amounts expected to be received from the vendor that are typically posted to Accounts Receivable for deposits or Accounts Payable as a credit against amounts owed to the vendor for purchases. This preliminary step links the expected receipts to the appropriate account(s).

Procedure

1. Navigate to the Master Data tile group and click on the G/L Accounts tile.
2. Click on the Create button.
3. Enter one Posting Account using a single line from the list of accounts below:
    - Posting Account External Id as 0041000000, Description as Supplier Revenue, and status as Active
    - Posting Account External Id as 0012501000, Description as Supplier Clearing Account, and status as Active
    - Posting Account External Id as 0021540000, Description as Write off Supplier, and status as Active
4. Click on the Check button and then click on the Save button.
5. Repeat Steps 2 to 4 above for each additional Posting Account listed above.
6. Click on the Home button.
7. Navigate to the Master Data tile group and click on the Reconciliation Account tile.
8. Click on the Create button.
9. Enter Posting Account External ID as 0021100000, Description as Supplier Recon. Account, and status as Active.
10. Click on the Check button and then click on the Save button.
11. Click on the Home button.

Result

G/L accounts are created.

#### Assign Vendor Posting Accounts

Use

Link customer-specific accounts in SAP S/4HANA Cloud Public Edition to the customer-specific subledgers in SAP Vendor Program Management by Vistex.

Procedure

1. Log into the Fiori link with the user ID and password provided for a user with the Vendor Program Admin role.
2. Navigate to the Master Data tile group and click on the Postings Area tile.
3. Click on the Edit button.
4. Click on the P/L Account tab.
5. Click on the Add (‘+’) button.
6. Enter field values as indicated in the table below.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| Entry No. | Field | Value |
| --- | --- | --- |
| 1 | Posting Application | VR Accrual |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Revenue |
|  | Posting Account | 0041000000 (Supplier Revenue) |
|  | validity | <operating year> |
|  | Status | Active |
| 2 | Posting Application | VR Settlement |
|  | Business Unit | US Distribution |
|  | Posting Group | Income P&L |
|  | Posting Account | 0041000000 (Supplier Revenue) |
|  | validity | <operating year> |
|  | Status | Active |
| 3 | Posting Application | CB Accrual |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Chargeback Revenue |
|  | Posting Account | 0041000000 (Supplier Revenue) |
|  | validity | <operating year> |
|  | Status | Active |
| 4 | Posting Application | CB Settlement |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Chargeback Revenue |
|  | Posting Account | 0041000000 (Supplier Revenue) |
|  | validity | <operating year> |
|  | Status | Active |

1. Click on the Write Off Account tab.
2. Click on the Add (‘+’) button.
3. Enter field values as indicated in the table below.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| Entry No. | Field | Value |
| --- | --- | --- |
| 1 | Posting Application | VR Settlement |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Write Off |
|  | Posting Account | 0021540000 (Write off Supplier) |
|  | validity | <operating year> |
|  | Status | Active |
| 2 | Posting Application | CB Settlement |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Write Off |
|  | Posting Account | 0021540000 (Write off Supplier) |
|  | validity | <operating year> |
|  | Status | Active |

1. Click on the Clearing Account tab.
2. Click on the Add (‘+’) button.
3. Enter field values as indicated in the table below.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| Entry No. | Field | Value |
| --- | --- | --- |
| 1 | Posting Application | VR Accrual |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Clearing |
|  | Posting Account | 0012501000 (Supplier Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |
| 2 | Posting Application | VR Settlement |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Clearing |
|  | Posting Account | 0012501000 (Supplier Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |
| 3 | Posting Application | CB Accrual |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Clearing |
|  | Posting Account | 0012501000 (Supplier Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |
| 4 | Posting Application | CB Settlement |
|  | Business Unit | US Distribution |
|  | Posting Group | Vendor Clearing |
|  | Posting Account | 0012501000 (Supplier Clearing Account) |
|  | validity | <operating year> |
|  | Status | Active |

1. Click on the Save button.
2. Click on the Home button.

Result

Vendor Posting Accounts are assigned.

#### Create Purchasing Agreement

Use

Execute this Preliminary Step if you have subscribed to SAP Vendor Program Management by Vistex. This Preliminary Step is not relevant for other SAP margin optimization solutions by Vistex.

This Scenario illustrates the Rebate process between a Distributor and the Manufacturer (Vendor) based on the Purchasing amount made by the Distributor. Both parties enter an Agreement based on the purchased amount by the distributor. The Tracking Document captures the purchase invoice data and calculates Rebate Payout according to the conditions maintained in the program. The Agreement document holds the eligible Accrual and Settlement amounts for posting.

Procedure

Complete the following tasks in this document before attempting this Preliminary Step:

- General Preliminary Steps 2.6.1 and 2.6.2
- Preliminary Steps 2.8.1 and 2.8.2
- Test Procedure 4.2 Retrieve Vendors
- Test Procedure 4.3 Retrieve Products

1. Log into the Fiori System using a user ID and password having Vendor Program Admin role.
2. Navigate to the Vendor Rebates tile group and click on the Master Agreements tile.
3. Click on the Create button.
4. Enter the Description as mentioned below:
    1. Enter the Master Request, Master Agreement, and Master Agreement Description field values – <User Defined>.

|  |
| --- |
| Note Master Agreement value must be unique. |

-
    1. Enter the Business Unit – US Distribution.
    2. Enter the Company – Vanguard Tool.
    3. Enter the Currency – USD.
    4. Enter the Master Agreement Program as – Vendor Rebate Master Program.
    5. Enter the Eligible Vendor – 17305001.
    6. Enter the Legal Validity To and From as <operating year>

1. Click on the Sub Agreements tab and click on the Create button.
2. Enter the below description as mentioned below.
    1. Enter the Sub Agreement ID and Description field values – <User Defined>.

|  |
| --- |
| Note Sub Agreement ID must be unique. |

-
    1. Enter the Sub Agreement Program as - Volume Rebate-% Based (WX_VP_VOL02).
    2. Enter the Legal Validity as <operating year>.
    3. Enter the Period Profile as Quarterly, Accrual Frequency as Monthly, and Settlement Frequency as Quarterly, and maintain the status as Active.

1. Drill down into the Sub Agreement by clicking on the Details (‘>‘) icon at the end of the row.
2. Click on the Eligibility tab and click on the Add (‘+’) button.
3. Click on the Source drop-down menu and select Purchases. Click on the F4 in the Purchase Group field and select Purchase Transactions.
4. Click on the Add (‘+’) button for Base Units.
5. Select Net Purchases from the drop-down menu.
6. Drill down into Base Units entry by clicking the Details (‘>‘) icon at the end.
7. Click on the Add (‘+’) button in the Eligible Base Values pop-up.
8. Maintain Source as Purchases, Source Field as Net value, Contribution as Add, and Eligible Percentage as 100%.
9. Click on the Apply button.
10. In Eligible Product Groupings, click on the Add (‘+’) button.
11. Enter the Group Name as <User Defined> (e.g. PR03), Group Type as Payout, Source as Purchases, and then click on the Create Flexible Group icon.
12. Enter the Description: User defined (e.g. Products) and click on the Find button.
13. In the Product field, enter TG0501 (Thermo Coffee Cup 0,4l).
14. Click on the OK button and then click on the Apply button.
15. Click on the Benefits tab and click on the Add (‘+’) button.
16. Click on the F4 in the Payout Group field and select the Payout Group entered in Step 17 above. Enter Rate as 0.50 and click on the Scales icon.
17. Enter Net Purchases and Rate information in the scales as given below (click on the Add button for each new row):
    - Net Purchases (Amount) = 40000, 100000, 300000
    - Rate (% on Net Basis Amount) = 0.50, 1.00, 2.00
18. After entering scale information above, click on the Check button and then click Apply button.
19. Click on the Estimated Accrual Rate tab and then click on the Add (‘+’) button.
20. Select the Payout Group in the Applies To field. Click on the F4 for the Payout Group field and select the group maintained in Step 17.
21. Maintain Source as Purchases, Rate Type as Percentage (%) and Rate as 3%.
22. Click on the Check button and then click Apply button.
23. Click on the Save button.
24. Click on the Submit button and then click on the Submit button in the pop-up.
25. Click on the Approve and then click on the Approve button in the pop-up. Verify status of Agreement is Active after approval process completes.
26. Click on the Home button.

Result

Purchasing Agreement is created.

#### Create Purchase Order

Use

This scenario illustrates the Customer rebate pay out based on sales volume. A sales order records the customer’s purchase and might qualify for a rebate payment.

Procedure

Complete the following tasks in this document before attempting this Preliminary Step:

- General Preliminary Steps 2.6.1 and 2.6.2
- Preliminary Steps 2.8.1 and 2.8.2
- Test Procedure 4.2 Retrieve Vendors
- Test Procedure 4.3 Retrieve Products

1. Log into the SAP S/4HANA Cloud Public Edition system.
2. Create a purchase order of type NB, with vendor 17305001 and material TG0501, on a date with the <operating year>, a reasonable quantity, and any remaining required fields can be <user defined>.
3. Click on the Home button.

Result

Purchase order is created.

### Preliminary Steps for Rights & Royalties

This section covers the prerequisite Preliminary Steps for SAP Rights & Royalty Management by Vistex, cloud edition.

You do not need to perform these steps if you have not subscribed to this solution.

#### Create Cross References

Use

This Preliminary Step links the intellectual properties to the SAP materials.

Procedure

1. Navigate to the MasterData Sync tile group and click on the Product Types tile.
2. Click on the Go button to view existing entries.
3. Click on the Edit button.
4. Click on the Add button.
5. Enter the following…
    - Document Type = MAT, Material Type = Hierarchy Group
    - Document Type = FERT, Material Type = Film
    - Document Type = HAWA, Material Type = Licensing Product
6. Click on the Save button.
7. Click on the Home button.

Result

Three Cross References are created.

#### Create Dimensions

Use

The Dimensions used in the Rights & Royalty test case can be uploaded from text files. Refer to the Appendix in this document for the text file contents to be uploaded.

Procedure

1. Navigate to the Master Data tile group and click on the Dimensions tile.
2. Click on the Language from the Dimensions menu.
3. Click on the Edit button.
4. Click on the Upload drop-down button and select Language from the drop-down menu.
5. Click on the Upload button in the upper part of the pop-up window.
6. Navigate to the upload file and select the file named Language.txt.
7. Click on the Upload button in the lower part of the pop-up window (next to the Cancel button).
8. Click on the Save button.
9. Click on the Back (‘<‘) button.
10. Click on the Right Type from the Dimensions menu.
11. Click on the Edit button.
12. Click on the Upload drop-down button and select Right Type from the drop-down menu.
13. Click on the Upload button in the upper part of the pop-up window.
14. Navigate to the upload file and select the file named Right Type.txt.
15. Click on the Upload button in the lower part of the pop-up window (next to the Cancel button).
16. Click on the Save button.
17. Click on the Back (‘<‘) button.
18. Click on the Territory from the Dimensions menu.
19. Click on the Edit button.
20. Click on the Upload drop-down button and select Territory from the drop-down menu.
21. Click on the Upload button in the upper part of the pop-up window.
22. Navigate to the upload file and select the file named Territory.txt.
23. Click on the Upload button in the lower part of the pop-up window (next to the Cancel button).
24. Click on the Save button.
25. Click on the Back (‘<‘) button.

Result

Dimension of each type is created.

#### Create G/L Accounts

Use

Royalty amounts expected to be received or due to be paid need to be linked to the revenue or expense accounts in the general ledger.

Procedure

1. Navigate to the Maintenance tile group and click on the G/L Posting Accounts tile.
2. Click on the Create button.
3. Enter one Posting Account using a single line from the list of accounts below:
    - Posting Account External Id as 0041000000, Description as Revenue Account, and status as Active
    - Posting Account External Id as 0041000400, Description as Expense Account, and status as Active
    - Posting Account External Id as 0012550000, Description as Deferred Revenue, and status as Active
    - Posting Account External Id as 0021540000, Description as Deferred Expense, and status as Active
    - Posting Account External Id as 0012501000, Description as Non-Recoupable Royalty, and status as Active
4. Click on the Check button and then click on the Save button.
5. Repeat Steps 2 to 4 above for each additional Posting Account listed above.
6. Click on the Home button.
7. Navigate to the Maintenance tile group and click on the Reconciliation Posting Accounts tile.
8. Click on the Create button.
9. Enter Posting Account External ID as 0021100000, Description as Recon. Account, and status as Active.
10. Click on the Check button and then click on the Save button.
11. Click on the Home button.

Result

G/L accounts are created.

#### Assign Royalty Posting Accounts

Use

Link partner-specific accounts in SAP S/4HANA Cloud Public Edition to the partner-specific subledgers in SAP Rights & Royalty Management by Vistex, cloud edition.

Procedure

1. Log into the Fiori link with the user ID and password provided for a user with the Rights & Royalty Admin role.
2. Navigate to the Maintenance tile group and click on the Posting Area tile.
3. Click on the Edit button.
4. Click on the Add (‘+’) button in the Derive Revenue Account tab.
5. Fill the data into fields of Derive Revenue Account as given in the below table.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| FIELD | VALUE | DESCRIPTION |
| --- | --- | --- |
| Business Unit | NA3 | US Rights and Royalties |
| Posting Account | 0041000000 | Revenue Account |
| Valid From | 01.01.2024 |  |
| Valid To | 31.12.9999 |  |

1. Click on the Derive Expense Account tab and click on the Add (‘+’) button.
2. Fill the data into fields of Derive Expense Account as given in the below table.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| FIELD | VALUE | DESCRIPTION |
| --- | --- | --- |
| Business Unit | NA3 | US Rights and Royalties |
| Posting Account | 0041000400 | Expense Account |
| Valid From | 01.01.2024 |  |
| Valid To | 31.12.9999 |  |

1. Click on the Derive Def Revenue tab and click on the Add (‘+’) button.
2. Fill the data into fields of Derive Def Revenue as given in the below table.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| FIELD | VALUE | DESCRIPTION |
| --- | --- | --- |
| Business Unit | NA3 | US Rights and Royalties |
| Posting Account | 0012550000 | Deferred Revenue |
| Valid From | 01.01.2024 |  |
| Valid To | 31.12.9999 |  |

1. Click on the Derive Def Expense tab and click on the Add (‘+’) button.
2. Fill the data into fields of Derive Def Expense as given in the below table.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| FIELD | VALUE | DESCRIPTION |
| --- | --- | --- |
| Business Unit | NA3 | US Rights and Royalties |
| Posting Account | 0021540000 | Deferred Expense |
| Valid From | 01.01.2024 |  |
| Valid To | 31.12.9999 |  |

1. Click on the Determine Non-Recoupable Royalties tab and click on the Add (‘+’) button.
2. Fill the data into fields of Determine Non-Recoupable Royalties as given in the below table.

|  |
| --- |
| Tip Fill the values of Posting Account manually and click on the Check button. |

| FIELD | VALUE | DESCRIPTION |
| --- | --- | --- |
| Business Unit | NA3 | US Rights and Royalties |
| Posting Account | 0012501000 | Non-Recoupable Royalty |
| Valid From | 01.01.2024 |  |
| Valid To | 31.12.9999 |  |

1. Click on the Save button.
2. Click on the Home button.

Result

Royalty Posting Accounts are assigned.

#### Create Media Rights Out Program

Use

Execute this Preliminary Step if you have subscribed to SAP Rights & Royalty Management by Vistex. This Preliminary Step is not relevant for other SAP margin optimization solutions by Vistex.

The purpose of the scenario is to create a template for R&R agreements.

Procedure

1. Log into the Fiori System using a user ID and password having Rights & Royalty Admin role.
2. Navigate to the Media Division Contracts tile group and click on the Media Programs tile.
3. Click on the Create Program button from the worklist and select Media Rights Out agreement type from the list.
4. Enter the following information in the General tab:
    - Contract ID = MRO1
    - Description = 1 Media Rights Out
    - Currency = USD
    - Business Unit = US Rights and Royalty
    - Start Date = 01.01.2024
    - End Date = 31.12.9999
5. Click on the Check button.
6. Click on the Calcflow tab.
7. Select Royalties from the Usage drop-down menu.
8. Click on the Add Group button.
9. On the Add Group pop-up screen, select Step Type (Description) as Licensed Sales.
10. Click on the Continue button.
11. Again, click on the Add Group button.
12. On the Add Group pop-up screen, select Step Type (Description) as Calculate Royalties.
13. Click on the Continue button.
14. Enter 1 in the Parameters field for the Calculate Royalties step.
15. Click on the Check button.
16. Again, click on the Add Group button.
17. On the Add Group pop-up screen, select Step Type (Description) as Net Royalties.
18. Click on the Continue button.
19. Click on the icon under Formula for the Net Royalties step.
20. Click on the Add (‘+’) button on the Subtotal of pop-up.
21. Select Add under the Step Contribution heading and select Calculate Royalties under the Step heading.
22. Click on the Apply button.
23. Again, click on the Add Group button.
24. On the Add Group pop-up screen, select Step Type (Description) as Overages.
25. Click on the Continue button.
26. Mark the checkbox for the Overages Step and click on the Add Step button in the tab header.
27. On the Add Step pop-up screen, select Step Type (Description) as Royalties by Schedule.
28. Click on the Continue button.
29. Expand the Overages Step by clicking on the ‘v’ symbol at the beginning of the row to show the newly added Royalties by Schedule step.
30. Enter 3 in the Parameters field for the Royalties by Schedule step.
31. Click on the Check button.
32. Again, mark the checkbox for the Overages Step and click on the Add Step button in the tab header.
33. On the Add Step pop-up screen, select Step Type (Description) as Recouped Royalties.
34. Click on the Continue button.
35. Enter 4.1 in the Parameters field for the Recouped Royalties step.
36. Click on the Check button.
37. Again, click on the Add Group button.
38. On the Add Group pop-up screen, select Step Type (Description) as Total Due.
39. Click on the Continue button.
40. Click on the icon under Formula for the Total Due step.
41. Click on the Add (‘+’) button on the Subtotal of pop-up.
42. Select Add under the Step Contribution heading and select Overages under the Step heading.
43. Click on the Apply button.
44. Again, click on the Add Group button.
45. On the Add Group pop-up screen, select Step Type (Description) as Due from Partner.
46. Click on the Continue button.
47. Enter 5 in the Parameters field for the Due from Partner step.
48. Click on the Check button.
49. Select Fee Installment from the Usage drop-down menu near the top of the Calcflow tab.
50. Click on the Add Group button.
51. On the Add Group pop-up screen, select Step Type (Description) as Schedule Totals.
52. Click on the Continue button.
53. Mark the checkbox for the Schedule Totals Step and click on the Add Step button in the tab header.
54. On the Add Step pop-up screen, select Step Type (Description) as Non-Recoupable Schedule Total.
55. Click on the Continue button.
56. Expand the Schedule Totals Step by clicking on the ‘v’ symbol at the beginning of the row to show the newly added Non-Recoupable Schedule Total step.
57. Again, mark the checkbox for the Schedule Totals Step and click on the Add Step button in the tab header.
58. On the Add Step pop-up screen, select Step Type (Description) as Recoupable Schedule Total.
59. Click on the Continue button.
60. Click on the Add Group button.
61. On the Add Group pop-up screen, select Step Type (Description) as Due from Partner.
62. Click on the Continue button.
63. Enter 1 in the Parameters field for the Due from Partner step.
64. Click on the Check button.
65. Click on the Save button.
66. Note the above created Program Number and Description ______________ (e.g. Contract No:MRO1 and Description:1 Media Rights Out)
67. Click on the Back (‘<‘) button twice.

Result

Media Rights Program is created.

#### Create Royalty Agreement

Use

Execute this Preliminary Step if you have subscribed to SAP Rights & Royalty Management by Vistex. This Preliminary Step is not relevant for other SAP margin optimization solutions by Vistex.

The purpose of the scenario is to provide insight into a typical Rights Out Process. The Rights Out Process is initiated with an agreement when a Licensee acquires Rights from the Licensor. The agreement is a collection of rules that help determine the Rights acquired and Royalty rates that are maintained based on categories like Geography, Right Type defined as a Set. Advance amounts are maintained at the title and set level which are then recouped from the royalty calculated as per the settlement’s period profile. This scenario highlights the various stages of the Rights Out process from maintenance of Master data, Rights-Out agreement to execution of Calculations using Calcflow Tracking.

Procedure

Complete the following tasks in this document before attempting this Preliminary Step:

- General Preliminary Steps 2.6.1 and 2.6.2
- Preliminary Steps 2.9.1 through 2.9.5
- Test Procedure 4.10 Retrieve R&R Master Data

1. Log into the Fiori link with the user ID (Rights & Royalty Admin) and password provided.
2. Navigate to the Media Division Contracts tile group and click on the Media Rights Out tile.
3. Click on the Create button.
4. Enter data provided in the table below and click on the Check button.
    - Description = <user defined>
    - Licensee = 17100088
    - Currency = USD
    - Program = Refer to Prerequisites (e.g. 1 Media Rights Out)
    - Business Unit = US Rights and Royalty
    - Legal Valid From / To = <operating year>
    - Processing Start / End Date = <operating year>
5. Click on the Rights Granted tab and click on the Create button.
6. Under the Exclusivity field heading, choose Exclusive from drop-down menu.
7. Click on the Check button.
8. Under the Title field heading, choose FIN126,MTS-DI,PD,SERIALNO (FG126) value.
9. Click on the New button under the Set field heading.
10. By default, all dimensions will be selected in the Create Media Rights window.
11. Click on the Search bar next to Include drop-down menu and enter Premium Subscription Television and select the Premium Subscription Television – Television<All value.
12. In the same Search bar, enter North America and select the North America – American Continent<America<All value.
13. Click on the Add (‘+’) button.
14. Click Apply button on the pop-up screen.
15. Click on the Check button.
16. Click on the Fees tab. In Recoupable Fees section, click on the Create button.
17. Under the Title field heading, enter FIN126,MTS-DI,PD,SERIALNO (FG126).
18. Click on the New button under Set field heading.
19. Repeat Step 9 to Step 15 above for creation of Set.
20. Click Create button under Schedule field heading.
21. Enter a Description, such as <Minimum Guarantee> and a Total Amount, such as <10,000>.
22. Click on the Create button.
23. Enter a Description, such as <Minimum Guarantee> and an Amount, such as <10,000>, and Due Date<start of operating year>.
24. Click on the Apply button.
25. Enter Rate as <100>% and click on the Check button.
26. Click on the Royalty Rate tab. In Royalty Rate section, click on the Create button.
27. Enter Title field value as FIN126,MTS-DI,PD,SERIALNO (FG126).
28. Click on the New button under Set field heading.
29. Repeat Step 9 to Step 15 above for creation of Set.
30. Enter Rate as <25>% and click on the Check button.
31. Click on the Save button.
32. Click on the Submit button.
33. On the Submit pop-up, enter a <comment> in the text box and click on the Submit button.
34. Click on the Approve button.
35. On the Approve pop-up, enter a <comment> in the text box and click on the Approve button.
36. Agreement Request will be auto posted, and Agreement will be created.
37. Note the Contract ID number in the header ________ (e.g. 723). This is also a hyperlink to the Agreement.

Result

Royalty Agreement is created.

## Overview Table

This scope item consists of several process steps provided in the table below.

| Test Procedure | Prerequisite Steps | Test Purpose | Expected Results |
| --- | --- | --- | --- |
| 4.1 [Retrieve Customers](#unique_34) [page ] 40 | 2.6.2 [Create Field Values](#unique_15) [page ] 10 | Customers are sold various materials at specific prices. Customers may also be eligible to receive rebates based on their purchases.Fetch the customer master data from SAP S/4HANA Cloud Public Edition to…Assign customer-specific pricing in SAP Extended Price Management by Vistex.Calculate customer-specific pricing with SAP Price Staging Hub by Vistex.Define customer eligibility for a rebate in an agreement using SAP Channel Program Management by Vistex. | Fetch master data from SAP S/4HANA Cloud Public Edition |
| 4.2 [Retrieve Vendors](#unique_35) [page ] 41 | 2.6.2 [Create Field Values](#unique_15) [page ] 10 | Purchasing select materials may be incentivized with rebate offers from a vendor.Fetch the vendor master data from SAP S/4HANA Cloud Public Edition to define material eligibility for a rebate in an agreement using SAP Vendor Program Management by Vistex. | Fetch master data from SAP S/4HANA Cloud Public Edition |
| 4.3 [Retrieve Products](#unique_36) [page ] 42 | 2.6.1 [Configure Allowed Currency and Units](#unique_14) [page ] 92.6.2 [Create Field Values](#unique_15) [page ] 10 | Materials can be finished goods purchased from vendors for reselling (distribution) or as finished components or raw goods for manufacturing value-added materials.Fetch material master data from SAP S/4HANA Cloud Public Edition to…Assign list or customer-specific pricing in SAP Extended Price Management by Vistex.Calculate customer-specific pricing with SAP Price Staging Hub by Vistex.Define material eligibility for a rebate in an agreement using SAP Channel Program Management by Vistex (for sales) or SAP Channel Program Management by Vistex (for purchases). | Fetch master data from SAP S/4HANA Cloud Public Edition |
| 4.4 [Retrieve Prices](#unique_37) [page ] 43 | 4.3 [Retrieve Products](#unique_36) [page ] 42 | Prices defined in SAP S/4HANA Cloud Public Edition can be used as a basis for defining more specific pricing (e.g. a list price discounted for sales, or a unit price used to determine a larger package price).Fetch prices already defined in SAP S/4HANA Cloud Public Edition to use in SAP Extended Price Management by Vistex or SAP Price Staging Hub by Vistex. | Fetch condition records from SAP S/4HANA Cloud Public Edition |
| 4.5 [Maintain Prices](#unique_38) [page ] 46 | 4.4 [Retrieve Prices](#unique_37) [page ] 43 | Prices can be set or changed using SAP Extended Price Management by Vistex. | Create/change prices and post to SAP S/4HANA Cloud Public Edition Condition Records |
| 4.6 [Retrieve Sales Invoices](#unique_39) [page ] 50 | 4.1 [Retrieve Customers](#unique_34) [page ] 404.3 [Retrieve Products](#unique_36) [page ] 422.7.4 [Create Sales Order](#unique_20) [page ] 20 | Invoices from sales orders in SAP S/4HANA Cloud Public Edition can be evaluated to determine if any sales transaction qualifies for a rebate based on agreements defined in SAP Channel Program Management by Vistex. | Fetch transaction data from SAP S/4HANA Cloud Public Edition |
| 4.7 [Determine Sales Rebate](#unique_40) [page ] 51 | 2.7 [Preliminary Steps for Channel Programs](#unique_16) [page ] 134.6 [Retrieve Sales Invoices](#unique_39) [page ] 50 | The rebate agreement defined with SAP Channel Program Management by Vistex has eligibility rules for customers and materials and defines the formula and rates for rebate amount calculations. | Calculate amounts and post to SAP S/4HANA Cloud Public Edition Journal Entry |
| 4.8 [Retrieve Purchase Orders](#unique_41) [page ] 56 | 4.2 [Retrieve Vendors](#unique_35) [page ] 414.3 [Retrieve Products](#unique_36) [page ] 422.8.4 [Create Purchase Order](#unique_25) [page ] 27 | Purchase orders in SAP S/4HANA Cloud Public Edition can be evaluated to determine if any purchase transaction qualifies for a rebate based on agreements defined in SAP Vendor Program Management by Vistex. | Fetch transaction data from SAP S/4HANA Cloud Public Edition |
| 4.9 [Determine Purchasing Rebate](#unique_42) [page ] 58 | 2.8 [Preliminary Steps for Vendor Programs](#unique_21) [page ] 204.8 [Retrieve Purchase Orders](#unique_41) [page ] 56 | The rebate agreement defined with SAP Vendor Program Management by Vistex has eligibility rules for vendors and materials and defines the formula and rates for rebate amount calculations. | Calculate amounts and post to SAP S/4HANA Cloud Public Edition Journal Entry |
| 4.10 [Retrieve R&R Master Data](#unique_43) [page ] 64 | 2.6 [General Preliminary Steps](#unique_13) [page ] 92.9.1 [Create Cross References](#unique_27) [page ] 282.9.2 [Create Dimensions](#unique_28) [page ] 292.9.3 [Create G/L Accounts](#unique_29) [page ] 302.9.4 [Assign Royalty Posting Accounts](#unique_30) [page ] 31 | Sales of products that contain intellectual property can produce a liability for the licensee and an income for the licensor.Fetch the business partners and materials from SAP S/4HANA Cloud Public Edition to define the intellectual properties, the rights for its use, and the agreement for royalty payments using SAP Rights & Royalty Management by Vistex. | Fetch master data from SAP S/4HANA Cloud Public Edition |
| 4.11 [Determine Royalty](#unique_44) [page ] 66 | 2.9 [Preliminary Steps for Rights & Royalties](#unique_26) [page ] 284.10 [Retrieve R&R Master Data](#unique_43) [page ] 64 | The royalty agreement defined with SAP Rights & Royalty Management by Vistex has eligibility rules for materials containing intellectual properties and defines the formula and rates for royalty amount calculations. | Calculate amounts and post to SAP S/4HANA Cloud Public Edition Journal Entry |

## Test Procedures

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
| 1 | Log On | Log on to the system for SAP Vendor Program Management as a Vendor Program Admin or the system for SAP Extended Price Management (same for SAP Price Staging Hub by Vistex) as a Vendor Program Admin.Repeat this entire procedure for SAP Channel Program Management as a Channel Program Admin, if also relevant. | The Fiori launchpad displays.You will execute this procedure once if you have either SAP Vendor Program Management or SAP Extended Price Management or SAP Price Staging Hub by Vistex. Do not execute this procedure more than once for having more than one of these solutions.You will execute this procedure (possibly for the second time) if you have SAP Channel Program Management. |  |
| 2 |  | For Vendor Program Management, Extended Price Management, or SAP Price Staging Hub by Vistex: Navigate to Master Data tile group and click on the Data Ingestion tile.For Channel Program Management: Navigate to Master Data tile group and click on the Work Manager tile. |  |  |
| 3 |  | For Vendor Program Management, Extended Price Management, or SAP Price Staging Hub by Vistex: Click on the Schedule drop-down and select Customer Data Full Load from S/4 PC.For Channel Program Management: Click on the Schedule drop-down and select Business Partner Full Load from S/4 PC. |  |  |
| 4 |  | Click on the Schedule button in the pop-up window. |  |  |
| 5 |  | Click on the Refresh button (System will take few seconds to complete the job) and verify the Status is changed to Completed. |  |  |
| 6 |  | Click on the Home button. |  |  |
| 7 |  | Click on the Customers tile in Master Data tile group. |  |  |
| 8 |  | Click on the Go button to view the list of customers. |  |  |
| 9 |  | Click on the Home button. |  |  |

### Retrieve Vendors

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Vendor master data from SAP S/4HANA Cloud Public Edition through the system interface. This master data will be used to create prices and/or agreements and may be referenced by transaction data (sales and/or purchase orders, claims, etc.).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Vendor Program Management as a Vendor Program Admin. | The Fiori launchpad displays. |  |
| 2 |  | Navigate to Master Data tile group and click on the Data Ingestion tile. |  |  |
| 3 |  | Click on the Schedule drop-down and select Supplier Data Full Load from S/4 PC. |  |  |
| 4 |  | Click on the Schedule button in the pop-up window. |  |  |
| 5 |  | Click on the Refresh button (System will take few seconds to complete the job) and verify the Status is changed to Completed. |  |  |
| 6 |  | Click on the Home button. |  |  |
| 7 |  | Click on the Vendors tile in Master Data tile group. |  |  |
| 8 |  | Click on the Go button to view the list of vendors. |  |  |
| 9 |  | Click on the Home button. |  |  |

### Retrieve Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Material master data from SAP S/4HANA Cloud Public Edition through the system interface. This master data will be used to create prices and/or agreements and may be referenced by transaction data (sales and/or purchase orders, claims, etc.).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Vendor Program Management as a Vendor Program Admin or the system for SAP Extended Price Management (same for SAP Price Staging Hub by Vistex) as a Vendor Program Admin.Repeat this entire procedure for SAP Channel Program Management as a Channel Program Admin, if also relevant. | The Fiori launchpad displays.You will execute this procedure once if you have either SAP Vendor Program Management or SAP Extended Price Management or SAP Price Staging Hub by Vistex. Do not execute this procedure more than once for having more than one of these solutions.You will execute this procedure (possibly for the second time) if you have SAP Channel Program Management. |  |
| 2 |  | For Vendor Program Management, Extended Price Management, or SAP Price Staging Hub by Vistex: Navigate to Master Data tile group and click on the Data Ingestion tile.For Channel Program Management: Navigate to Master Data tile group and click on the Work Manager tile. |  |  |
| 3 |  | Click on the Schedule drop-down and select Products Master Full Load from S/4 PC. |  |  |
| 4 |  | Click on the Schedule button in the pop-up window. |  |  |
| 5 |  | Click on the Refresh button (System will take few seconds to complete the job) and verify the Status is changed to Completed. |  |  |
| 6 |  | Click on the Home button. |  |  |
| 7 |  | Navigate to the Master Data tile group and click on the Products tile. |  |  |
| 8 |  | Click on the Go button to view the list of products. |  |  |
| 9 |  | Click on the Home button. |  |  |

### Retrieve Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Condition Records from SAP S/4HANA Cloud Public Edition through the system interface.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Extended Price Management (same for SAP Price Staging Hub by Vistex) as a Vendor Program Admin. | The Fiori launchpad displays. |  |
| 2 | Load Purchase Condition Records | Navigate to My Home tile group and click on the Replicate by Replication Model tile. |  |  |
| 3 |  | Select Replication Model from the dropdown menu (e.g. “WB – Condition Record for Pricing in Purchasing”). |  |  |
| 4 |  | Select the given Target system (e.g. “VIQWB”) and select Initialization in the replication mode section. Select the Purchasing Condition Record in the Business object to be replicated section. |  |  |
| 5 |  | Click on the Replicate button. |  |  |
| 6 |  | Click on the Home button. |  |  |
| 7 |  | Click on the Monitor Replication tile in Data Replication tile group. |  |  |
| 8 |  | Select Replication Model from the dropdown menu (e.g. WB – Condition record for pricing in purchasing). |  |  |
| 9 |  | Select the Purchasing condition record checkbox in the Business Object section. Click on the Continue button. |  |  |
| 10 |  | Verify the messages in replication log by selecting 2nd entry in Propagated type/ Date/ Time/User section. |  |  |
| 11 |  | Click on the Home button. |  |  |
| 12 |  | In another session, log on to Fiori Launchpad with the user ID and password provided. |  |  |
| 13 |  | Click on the Pricing Records (Buy Side) tile in Pricing tile group. |  |  |
| 14 |  | Click on the Go button. |  |  |
| 15 |  | Verify the data in Acquisition Cost / Purchase Cost sheet. |  |  |
| 16 | Load Sales Condition Records | Navigate to My Home tile group and click on the Replicate by Replication Model tile. |  |  |
| 17 |  | Select Replication model from the dropdown menu (e.g. “WB – Condition Record for Pricing in Sales”). |  |  |
| 18 |  | Select the given Target system (e.g. “VIQWB”) and select Initialization in the replication mode section. Select the Sales Condition Record in the Business object to be replicated section. |  |  |
| 19 |  | Click on the Replicate button. |  |  |
| 20 |  | Click on the Home button. |  |  |
| 21 |  | Click on the Monitor Replication tile in Data Replication tile group. |  |  |
| 22 |  | Select Replication model from the dropdown menu (e.g. WB – Condition record for pricing in Sales). |  |  |
| 23 |  | Select the Sales condition record checkbox in the Business Object section. |  |  |
| 24 |  | Click on the Continue button. |  |  |
| 25 |  | Verify the messages in replication log by selecting 2nd entry in Propagated type/ Date/ Time/User section. |  |  |
| 26 |  | Click on the Home button. |  |  |
| 27 |  | In another session, log on to Fiori Launchpad with the user ID and password provided. |  |  |
| 28 |  | Click on the Pricing Records (Sell Side) tile in Pricing tile group. |  |  |
| 29 |  | Click on the Go button. |  |  |
| 30 |  | Verify the data in the List Price and Customer Specific List Price sheets. |  |  |
| 31 |  | Click on the Home button. | Note: Price Records which are relevant to Distribution and Manufacturing can be seen under Calculation Area tile group > Price Setting tile. |  |

### Maintain Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Execute this test case if you have subscribed to SAP Extended Price Management by Vistex. This test case is not relevant for other SAP margin optimization solutions by Vistex.

SAP Condition Records (prices) can be created, changed and displayed. The Price Review provides users a means to review changes prior to being posted (changes committed).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Vendor Program Admin. | The Fiori launchpad displays. |  |
| 2 |  | Click on the Price Review tile in the Pricing tile group. |  |  |
| 3 |  | Click on the Create button. |  |  |
| 4 |  | Enter Description as <User Defined> and select Status as Released in the Header Data tab. |  |  |
| 5 |  | Click on the Selections tab, enter Business unit as US Distribution and enter Product as TG11_PH_CO21 (Combination wrench 21mm). | The records with the above selections have been maintained in the List Price and Customer Specific List Price sheets in the Pricing Records (Sell Side) Calculation area. Users can navigate to the existing calculation records in a new browser session and verify the records:Pricing tile group -> Pricing Records (Sell Side) tile -> List Price (#) tabPricing tile group -> Pricing Records (Sell Side) tile -> Customer Specific List Price (#) tab |  |
| 6 |  | Click on the Price Review Document section Steps tab. Click on the Add (‘+’) button. |  |  |
| 7 |  | Under Definitions tab, select <New Step> from the Step Group drop-down menu. |  |  |
| 8 |  | Select Maintain Material List Price from the Step Type drop-down menu. |  |  |
| 9 |  | Select the Material list price from the filter drop-down menu. |  |  |
| 10 |  | Enter Description as <Step Description> and click on the Check button. | Inclusions and Actions sections will be displayed. |  |
| 11 |  | Select Business Unit as US Distribution and select Product as TG11_PH_CO21. |  |  |
| 12 |  | In the Actions section, select Valid from (VLDFR) from the Field drop-down and select Current Date from Basis Date drop-down menu.Select Valid to (VLDTO) field from Field drop-down and select Source Valid to from Basis Date drop-down menu.Select Rate (CLRAT) from Field drop-down, select Increase by % from Field Options drop-down and enter 10 in Value field. |  |  |
| 13 |  | Click on the Check button and then click on the Apply button. | Step <Step Description > will be displayed. |  |
| 14 |  | Click on the Save button. |  |  |
| 15 |  | Click on the Generate button. | Price Review Generation Status will change from Not Yet Generated to Generated. |  |
| 16 |  | Click on the List Price tab to verify the data. | Source Process is maintained as ‘End Date Records’, Valid from as ‘Current date’, valid to as ‘Source valid to’. The records have been split as Source Record has been ended one day before the Current Date as Valid From is maintained as Current date for the new record.For Material Price tab, the record is displayed with increase of 10% in calculation rate and changed validity dates. |  |
| 17 |  | Click on the Post button. | Confirmation messages will be displayed.After Posting, the status changes from Released to Posted. |  |
| 18 |  | Click on the Sheets tab and note the Request _________ (e.g. 5) that was created. |  |  |
| 19 |  | Click on the Home button. |  |  |
| 20 |  | Click on the Pricing tile group and click on the Price Request (Sell Side) tile. |  |  |
| 21 |  | Enter request number (e.g. 5, noted in Step 18) in request search field and click on the Go button. |  |  |
| 22 |  | Drill down into details by clicking the Details (‘>‘) icon at the end of the record. | Verify the data in the List Price (#) tab. |  |
| 23 |  | Click on the Edit button. |  |  |
| 24 |  | Click on the Post button. | Verify the communication messages. |  |
| 25 |  | Click on the Home button. |  |  |
| 26 |  | Navigate to the Pricing Records Sell Side tile, enter the current date in Valid on field and search for the newly created records (refer to Step 5). |  |  |
| 27 |  | Click on the Details (‘>‘) icon to see the details of the records. | Verify the validity dates. |  |
| 28 |  | Change the Valid on date to one day before the current date. |  |  |
| 29 |  | Search for the changed records. These are the two changed records in List Price tab. |  |  |
| 30 |  | Click on the Details (‘>‘) icon to see the details of the records. | Verify the validity dates. |  |
| 31 | Schedule a Job for Posting | Navigate to the Pricing tile group and click on the Work Manager tile. |  |  |
| 32 |  | In the Overview tab, from the Schedule drop-down menu, select Push Condition Records to S4 PC. |  |  |
| 33 |  | Click on the Refresh button to see results of the executed steps. After clicking on the Schedule button, system requires some time to start executing work manager. | Step Messages should display as Success. |  |
| 34 | Verify Condition Records Posting in SAP S/4HANA Cloud Public Edition | Log into the SAP S/4HANA Cloud Public Edition system. |  |  |
| 35 |  | Navigate to the My Home tile group and click on the Set Material Prices tile. |  |  |
| 36 |  | Enter Condition Type PPR0 and click on Key Combination. In the Key Combination pop-up, select the radio button for Material with release status. |  |  |
| 37 |  | Click on the Choose button. |  |  |
| 38 |  | Search for the posted Condition Record.Select the sales organization (e.g. 1710), distribution channel (e.g. 10), material (e.g. TG11_PH_CO21). Select the valid on date (e.g. <operating date>). |  |  |
| 39 |  | Click on the Execute button. | Verify condition record updated price and validities. |  |
| 40 |  | Return (log in) to the SAP margin optimization solutions by Vistex in SAP BTP before continuing to any other Test Procedure in this document. |  |  |

### Retrieve Sales Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Sales Invoices from SAP S/4HANA Cloud Public Edition through the system interface. These transactions are evaluated to determine if a rebate should be paid to a customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Channel Program Admin. | The Fiori launchpad displays. |  |
| 2 |  | In the Transactions tile group, click on the Work Manager tile in Admin Activities section. |  |  |
| 3 |  | Click on the Schedule button and select Billing Documents Full Load from S/4 PC. |  |  |
| 4 |  | Click on the Schedule button in the pop-up. |  |  |
| 5 |  | Click on the Refresh button to see the results of the Work Manager. |  |  |
| 6 |  | Verify the status changed to Completed. |  |  |
| 7 |  | Click on the Home button. |  |  |
| 8 |  | Click on the Sales Data tile in the Transactions tile group. |  |  |
| 9 |  | Search for the Data Object Number noted in Step 6 and click on the Go button. |  |  |
| 10 |  | Click on the Details (‘>‘) icon at the right to show the details. |  |  |
| 11 |  | Verify the items containing total number of items fetched along with document numbers. |  |  |
| 12 |  | Verify the External ID data of sales invoices in the document which are moved from SAP S/4HANA Cloud Public Edition system. |  |  |

### Determine Sales Rebate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Execute this test case if you have subscribed to SAP Channel Program Management by Vistex. This test case is not relevant for other SAP margin optimization solutions by Vistex.

In this step, User will schedule a Work Manager to create Tracking and Posting Document(s). The Tracking Document holds the calculation results for any eligible sales rebate arising from the applicable sales order transactions. Sales rebate amounts accrue until the end of the accounting period, at which point the rebate totals are paid.

Prerequisite

Create Sales Agreement

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Channel Program Admin. | The Fiori launchpad displays. |  |
| 2 | Calculate Rebate Accrual | Navigate to the Rebates tile group and click on the Other Work Manager tile in the Admin Activities section. |  |  |
| 3 |  | Click on the Schedule button and select G- Customer Rebate Tracking from the drop-down menu. |  |  |
| 4 |  | In the New Job for G- Customer Rebate Tracking pop-up window, select or enter the following information:Job Name = <User Defined>Tracking Type as Customer Rebate – Accrual Tracking from the drop-downMaster Agreement as noted in Preliminary Step 2.7.3. Create Sales AgreementTracking Date as 31.01.<operating year>Post = Yes |  |  |
| 5 |  | Click on the Schedule button. |  |  |
| 6 |  | Click on the Refresh button to see step results. (It takes few seconds to complete the Work Manager execution) | After the completion of the job, the results will be displayed in the Documents section. |  |
| 7 |  | Click on the Tracking hyperlink. | Note the Tracking and Posting Documents number displayed _____ (e.g. 656 and 287) |  |
| 8 |  | Click on the Home button. |  |  |
| 9 |  | Click on the Rebates tile group from the menu. Click on the Accrual Tracking tile. |  |  |
| 10 |  | Search for Tracking document as noted in Step 7 (e.g. 656). |  |  |
| 11 |  | Click on the Go button. |  |  |
| 12 |  | Click on the Details ‘>’ icon at the end of the Tracking record to drill-down into details. | Click on each tab (listed below) and view the data.AllocationBR & CR Accruals (Source Lines)SummaryEligible RevenueAccrual RevenueAccrual Amount |  |
| 13 |  | Click on the Home button. |  |  |
| 14 | Post Rebate Accrual to SAP S/4HANA Cloud Public Edition | Navigate to the Rebates tile group and click on the Posting Accrual tile. |  |  |
| 15 |  | Enter the Postings document number (noted in Step 7) in the Posting Document field. Click on the Go button and open the document. | Verify the Net value, Credit and Debit amounts.At this point, note that the Document No. field in the header is blank. This refers to the corresponding accounting document posted in SAP S/4HANA Cloud Public Edition. The next steps will run the interface to push the posting document in SAP margin optimization solutions by Vistex into SAP S/4HANA Cloud Public Edition. |  |
| 16 |  | Click on the Home button. |  |  |
| 17 |  | Navigate to the Rebates tile group and click on the Other Work Manager tile in the Admin Activities section. |  |  |
| 18 |  | Click on the Schedule button and select the Customer Postings Accrual to S/4 PC Full. |  |  |
| 19 |  | Click on the Schedule button. |  |  |
| 20 |  | Click on the Refresh button to see the step results. | After the completion of the job, the results will be displayed in the Output section. |  |
| 21 |  | Click on the Posting Document hyperlink under Output label. |  |  |
| 22 |  | Navigate to the same Posting document that was created in Step 7 and used in Step 15. | Note the Document No. shown in the header (e.g. 100000431). |  |
| 23 |  | Click on the Home button. |  |  |
| 24 | Verify Rebate Accrual in SAP S/4HANA Cloud Public Edition | Log into the SAP S/4HANA Cloud Public Edition system. |  |  |
| 25 |  | Navigate to the My Home tile group and click on the Manage Journal Entries (Old Version) tile. |  |  |
| 26 |  | Enter the document number (noted in Step 22) in the Journal Entry field and click on the Go button. |  |  |
| 27 |  | Drill down to the details of the document by clicking the Details (‘>‘) icon at the end of the document record. | Verify the accounts and amounts match the accruals in the SAP margin optimization solutions by Vistex. |  |
| 28 |  | Return (log in) to the SAP margin optimization solutions by Vistex in SAP BTP before continuing to any other Test Procedure in this document. |  |  |
| 29 | Calculate Rebate Settlement | Navigate to the Rebates tile group and click on the Work Manager tile in the Admin Activities section. |  |  |
| 30 |  | Click on the Schedule button and select G- Customer Rebate Tracking. |  |  |
| 31 |  | In the New Job for G- Customer Rebate Tracking pop-up window, select or enter the following information:Job Name = <User Defined>Tracking Type as Customer Rebate – Settlement Tracking from the drop-downMaster Agreement as noted in Preliminary Step 2.7.3. Create Sales AgreementTracking Date as 31.01.<operating year> |  |  |
| 32 |  | Click on the Schedule. |  |  |
| 33 |  | Click on the Refresh button to see step results. (There may be a waiting period after the previous step.) | After completion of the job, view the results displayed in the Documents section.Note the Tracking and Posting document numbers on the Output: Tracking: _____ (e.g. 657 & 288). |  |
| 34 |  | Click on the Home button. |  |  |
| 35 |  | Click on the Rebates tile group from the menu. Click on the Settlement Tracking tile. |  |  |
| 36 |  | Search for Tracking as noted in above Step 33. (e.g. 657) |  |  |
| 37 |  | Click on the Go button. |  |  |
| 38 |  | Click on the Details (‘>‘) icon at the end of the Tracking record to drill-down into details. | Click on each tab (listed below) and view the data.AllocationCR Settlements (Source Lines)SummaryCP Eligible RevenueCP Eligible Payout RevenueCP Calculated RebateCP Final Rebate |  |
| 39 |  | Click on the Home button. |  |  |
| 40 | Post Rebate Settlement to SAP S/4HANA Cloud Public Edition | Navigate to the Rebates tile group and click on the Settlement Postings tile. |  |  |
| 41 |  | Enter the Posting document number as noted in Step 34 (e.g. 288) in the Posting Document field. |  |  |
| 42 |  | Click on the Go button and open the document by clicking the Details (‘>‘) icon to the right. | Verify the Net value, Debit and Credit.At this point, note that the Document No. field in the header is blank. This refers to the corresponding accounting document posted in SAP S/4HANA Cloud Public Edition. The next steps will run the interface to push the posting document in SAP margin optimization solutions by Vistex into SAP S/4HANA Cloud Public Edition. |  |
| 43 |  | Click on the Home button. |  |  |
| 44 |  | Navigate to the Rebates tile group and click on the Work Manager tile in the Admin Activities section. |  |  |
| 45 |  | Click on the Schedule button and select the Customer Postings Settlement to S/4 PC Full. |  |  |
| 46 |  | Click on the Schedule button. |  |  |
| 47 |  | Click on the Refresh button to see the step results. | After the completion of the job, the results will be displayed in the Output section. |  |
| 48 |  | Click on the Posting Document hyperlink under Output label. |  |  |
| 49 |  | Navigate to the same Posting document that was created in Step 7 and used in Step 15. | Note the Document No. shown in the header (e.g. 100000431). |  |
| 50 |  | Click on the Home button. |  |  |
| 51 | Verify Rebate Settlement in SAP S/4HANA Cloud Public Edition | Log into the SAP S/4HANA Cloud Public Edition system. |  |  |
| 52 |  | Navigate to the My Home tile group and click on the Manage Journal Entries (Old Version) tile. |  |  |
| 53 |  | Enter the document number (noted in Step 50) in the Journal Entry field and click on the Go button. |  |  |
| 54 |  | Drill down to the details of the document by clicking the Details (‘>‘) icon at the end of the document record. | Verify the accounts and amounts match the accruals in the SAP margin optimization solutions by Vistex. |  |
| 55 |  | Return (log in) to the SAP margin optimization solutions by Vistex in SAP BTP before continuing to any other Test Procedure in this document. |  |  |

### Retrieve Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Purchase Orders from SAP S/4HANA Cloud Public Edition through the system interface. These transactions are evaluated to determine if a rebate has been earned and should be expected to be received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a Vendor Program Admin. | The Fiori launchpad displays. |  |
| 2 |  | In the Transactions tile group, click on the Work Manager tile in Admin Activities section. |  |  |
| 3 |  | Click on the Schedule button and select Purchase Order Full Load from S/4 PC. |  |  |
| 4 |  | Click on the Schedule button. |  |  |
| 5 |  | Click on the Refresh button to see the results of the Work Manager. | The execution may take some time to complete. Click on the Refresh button and verify that the status has changed to Completed. |  |
| 6 |  | Click on the last (bottom) Object listed under Documents and note the Object number____________. |  |  |
| 7 |  | Click on the Home button. |  |  |
| 8 |  | Click on the Purchase Data tile in the Transactions tile group. |  |  |
| 9 |  | Search for the Data Object Number noted in Step 6 and click on the Go button. |  |  |
| 10 |  | Click on the Details (‘>‘) icon at the right to show the details. |  |  |
| 11 |  | Verify the items containing total number of items fetched along with document numbers. |  |  |
| 12 |  | Verify the External ID data of purchase orders in the document which are moved from SAP S/4HANA Cloud Public Edition system. |  |  |

### Determine Purchasing Rebate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Execute this test case if you have subscribed to SAP Vendor Program Management by Vistex. This test case is not relevant for other SAP margin optimization solutions by Vistex.

In this step, User will schedule a Work Manager to create Tracking and Posting Document(s). The Tracking Document holds the calculation results for any eligible purchasing rebate arising from the applicable purchase order transactions. Purchasing rebate amounts accrue until the end of the accounting period, at which point the rebate totals are expected to be received.

Prerequisite

Create Purchasing Agreement

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Vendor Program Management as a Vendor Program Admin. | The Fiori launchpad displays. |  |
| 2 | Create Rebate Accrual for First Period (January) | Navigate to the Vendor Rebates tile group and click on the Work Manager tile in the Admin Activities section. |  |  |
| 3 |  | Click on the Schedule button and select Vendor Rebate Tracking. |  |  |
| 4 |  | Select the tracking type Vendor Rebate – Accrual from the drop-down menu. |  |  |
| 5 |  | In the Master Agreement field, enter the Master Agreement as noted in Preliminary Step 2.8.3. Create Purchasing Agreement. |  |  |
| 6 |  | Enter the tracking date as 31.01.<operating year> and select Yes from the Post drop-down menu. |  |  |
| 7 |  | Click on the Schedule button. |  |  |
| 8 |  | Click on the Refresh button to see step results. The execution of the Work Manager may take a few seconds to complete. | After the job is completed, the results will be displayed in the Documents section. |  |
| 9 |  | Click on the Tracking hyperlink. | Note the Tracking & Posting Document number displayed on the Output: Tracking screen. Tracking: _______ (e.g. 2105), Posting Document: _______ (e.g. 634) |  |
| 10 |  | Click on the Home button. |  |  |
| 11 |  | Navigate to the Vendor Rebates tile group and click on the Accrual Tracking tile. |  |  |
| 12 |  | Enter the tracking number in the Tracking field (e.g. 2105, which was noted in Step 9) and click on the Go button. |  |  |
| 13 |  | Drill down to the document by clicking the Details (‘>‘) icon at the end. | Verify the posting status, Total amount, and Cumulative Total amount.Verify the values in each tab:AllocationSource LinesSummaryEligible PurchasesEligible Accrual BasisEligible Accrual Amount |  |
| 14 |  | Click on the Home button. |  |  |
| 15 |  | Navigate to the Vendor Rebates tile group and click on the Postings Accrual tile. |  |  |
| 16 |  | Enter the Posting document number in the Posting Document field (e.g. 634, which was noted in Step 9) and click on the Go button. |  |  |
| 17 |  | Drilldown to the document by clicking on the Details (‘>‘) icon at the end. | Verify the Net Value. |  |
| 18 |  | Click on the Home button. |  |  |
| 19 | Create Rebate Accrual for Second Period (February) | Repeat Steps 2 to 18 above with the following changes:In Step 6, enter the tracking date as 29.02.<operating year>In Step 9, note the Tracking & Posting Document number displayed on the Output: Tracking screen Tracking: _____ (e.g. 2106), Posting Document: _____ (e.g. 635).In Step 12, enter the Tracking number in the Tracking field (e.g. 2106) noted above.In Step 16, enter the Posting document number (e.g. 635) noted above in the Posting Document field. |  |  |
| 20 | Create Rebate Accrual for Third Period (March) | Repeat Steps 2 to 18 above with the following changes:In Step 6, enter the tracking date as 31.03.<operating year>In Step 9, note the Tracking & Posting Document number displayed on the Output: Tracking screen Tracking: _____ (e.g. 2107), Posting Document: _____ (e.g. 636).In Step 12, enter the Tracking number in the Tracking field (e.g. 2107) noted above.In Step 16, enter the Posting document number (e.g. 636) noted above in the Posting Document field. | The next steps will run the interface to push the posting documents in SAP margin optimization solutions by Vistex into SAP S/4HANA Cloud Public Edition. |  |
| 21 | Post Rebate Accrual to SAP S/4HANA Cloud Public Edition | Go to the Vendor Rebates tile group and click on the Work Manager tile in the Admin Activities section. |  |  |
| 22 |  | Click on the Schedule button and select the Vendor Postings Accrual to S/4 PC Full. |  |  |
| 23 |  | Click on the Schedule button. |  |  |
| 24 |  | Click on the Refresh button to see the step results. | After the completion of the job, the results will be displayed in the Output section. |  |
| 25 |  | Click on the Posting Document hyperlink under Output label. |  |  |
| 26 |  | Navigate to the same Posting document that was created in Step 9 and used in Step 16.Click the Back button and repeat for the other two posting documents (from Step 19 and Step 20). | Note the Document No. shown in the header (e.g. 100000431). |  |
| 27 |  | Click on the Home button. |  |  |
| 28 | Verify Rebate Accrual in SAP S/4HANA Cloud Public Edition | Log into the SAP S/4HANA Cloud Public Edition system. |  |  |
| 29 |  | Go to the My Home tile group and click on the Manage Journal Entries tile. |  |  |
| 30 |  | Enter the one of the document numbers noted in Step 26 in the Journal Entry field and click on the Go button. |  |  |
| 31 |  | Drill down to the details of the document by clicking the Details (‘>‘) icon at the end of the document record. | Verify the accounts and amounts match the accruals in the SAP margin optimization solutions by Vistex. |  |
| 32 |  | Repeat Steps 30 and 31 for the other two documents from Step 26. |  |  |
| 33 |  | Return (log in) to the SAP margin optimization solutions by Vistex in SAP BTP before continuing to any other Test Procedure in this document. |  |  |
| 34 | Create Rebate Settlement for Quarterly Period (January - March) | Navigate to the Admin Activities section in the Vendor Rebates tile group and click on the Work Manager tile. |  |  |
| 35 |  | Click on the Schedule button and select Vendor Rebate Tracking. |  |  |
| 36 |  | Select the tracking type Vendor Rebate – Settlement from the drop-down menu. |  |  |
| 37 |  | In the Master Agreement field, enter the Master Agreement as noted in Preliminary Step 2.8.3. Create Purchasing Agreement. |  |  |
| 38 |  | Enter the tracking date as 31.03.<operating year> and select Yes from the Post drop-down menu. |  |  |
| 39 |  | Click on the Schedule button. |  |  |
| 40 |  | Click on the Refresh button to see step results. The execution of the Work Manager may take a few seconds to complete. |  |  |
| 41 |  | After the job is completed, the results will be displayed in the Documents section. Click on the Tracking hyperlink. | Note the Tracking & Posting Document number displayed on the Output: Tracking screen. Tracking: _______ (e.g. 2108), Posting Document: _______ (e.g. 637) |  |
| 42 |  | Click on the Home button. |  |  |
| 43 | Verify Rebate Settlement for Quarterly Period | Navigate to the Vendor Rebates tile group and click on the Settlement Tracking tile. |  |  |
| 44 |  | Enter the tracking number in the Tracking field (e.g. 2108, which was noted in Step 41) and click on the Go button. |  |  |
| 45 |  | Drill down to the document by clicking the Details (‘>‘) icon at the end. | Verify the posting status, Total amount, and Cumulative Total amount.Verify the values in each tab. |  |
| 46 |  | Click on the Home button. |  |  |
| 47 | Post Rebate Settlement to SAP S/4HANA Cloud Public Edition | Navigate to the Vendor Rebates tile group and click on the Postings Settlement tile. |  |  |
| 48 |  | Enter the Posting document number in the Posting Document field (e.g. 637, which was noted in Step 41) and click on the Go button. |  |  |
| 49 |  | Drilldown to the document by clicking on the Details (‘>‘) icon at the end. | Verify the Net Value, Debit & Credit.At this point, note that the Document No. field in the header is blank. This refers to the corresponding accounting document posted in SAP S/4HANA Cloud Public Edition. The next steps will run the interface to push the posting document in SAP margin optimization solutions by Vistex into SAP S/4HANA Cloud Public Edition. |  |
| 50 |  | Click on the Home button. |  |  |
| 51 |  | Navigate to the Vendor Rebates tile group and click on the Work Manager tile in the Admin Activities section.Click on the Schedule button and select the Vendor Postings Settlement to S/4 PC Full. |  |  |
| 52 |  | Click on the Schedule button. |  |  |
| 53 |  | Click on the Refresh button to see the step results. | After the completion of the job, the results will be displayed in the Output section. Click on the Posting Document hyperlink under the Output label. |  |
| 54 |  | Navigate to the same Posting document that was created in Step 41 and used in Step 48. | Note the Document No. shown in the header (e.g. 100000431). |  |
| 55 |  | Click on the Home button. |  |  |
| 56 | Verify Rebate Settlement in SAP S/4HANA Cloud Public Edition | Log into the SAP S/4HANA Cloud Public Edition system. |  |  |
| 57 |  | Navigate to the My Home tile group and click on the Manage Journal Entries tile. |  |  |
| 58 |  | Enter the document number (noted in Step 54) in the Journal Entry field and click on the Go button. |  |  |
| 59 |  | Drill down to the details of the document by clicking the Details (‘>‘) icon at the end of the document record. | Verify the accounts and amounts match the accruals in the SAP margin optimization solutions by Vistex. |  |
| 60 |  | Return (log in) to the SAP margin optimization solutions by Vistex in SAP BTP before continuing to any other Test Procedure in this document. |  |  |

### Retrieve R&R Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Retrieve Licensors/Licensees and Products master data from SAP S/4HANA Cloud Public Edition through the system interface. This master data will be used to in royalty agreements and may be referenced by royalty transaction data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Rights & Royalty Management as a Rights & Royalty Admin. | The Fiori launchpad displays. |  |
| 2 | Retrieve Business Partners | Navigate to the Master Data Sync tile group and click on the Monitor Data Sync tile. |  |  |
| 3 |  | Click Schedule drop-down and select the Load R&R – Business Partner Work Manager. |  |  |
| 4 |  | Select S4 HANA Public Cloud as the Logical System value. |  |  |
| 5 |  | Click on the Schedule button in the pop-up. |  |  |
| 6 |  | Click Refresh button to see results of executed steps (system will take few seconds to complete the job). |  |  |
| 7 |  | Click on the created Object for Load Business Partners. | The pop-up displaying the document number appears.Note the Document Number(s) ______________ (e.g. 4653). |  |
| 8 |  | Click on the Cancel button in the pop-up. |  |  |
| 9 |  | Click on the Home button. |  |  |
| 10 |  | Navigate to the Data Sync tile group and click on the Partners tile. |  |  |
| 11 |  | Enter the Document Number from Step 7 (e.g. 4653) into the Object field in the header and click on the Go button. | The Document Object record is displayed. |  |
| 12 |  | Drill down to the details of the Object by clicking on the Details (‘>‘) icon at the end of the Object record. | Verify the header data containing total number of documents (Licensees & Licensors) fetched along with document numbers.Verify the Posting Status is Posted. |  |
| 13 |  | Click on the Postings tab. |  |  |
| 14 |  | Click on the Details (‘>‘) icon at the start of the Posting record to expand the Partners node. |  |  |
| 15 |  | Navigate to the most-recently created document using the Document Number hyperlink. | Verify the document data. |  |
| 16 |  | Click on the Back (‘<’) button. |  |  |
| 17 |  | Click on the Home button. |  |  |
| 18 | Retrieve R&R Products | Navigate to the Master Data Sync tile group and click on the Monitor Data Sync tile. |  |  |
| 19 |  | Click Schedule drop-down and select the Load R&R –Products Work Manager. |  |  |
| 20 |  | Select S4 HANA Public Cloud as the Logical System value. |  |  |
| 21 |  | Click on the Schedule button in the pop-up. |  |  |
| 22 |  | Click Refresh button to see results of executed steps (system will take few seconds to complete the job). |  |  |
| 23 |  | Click on the created Object for Load Products. | The pop-up displaying the document number appears.Note the Document Number(s) ______________ (e.g. 4564). |  |
| 24 |  | Click on the Cancel button in the pop-up. |  |  |
| 25 |  | Click on the Home button. |  |  |
| 26 |  | Navigate to the Data Sync tile group and click on the Products tile. |  |  |
| 27 |  | Enter the Document Number from Step 23 (e.g. 4564) into the Object field in the header and click on the Go button. | The Document Object record is displayed. |  |
| 28 |  | Drill down to the details of the Object by clicking on the Details (‘>‘) icon at the end of the Object record. | Verify the header data containing total number of documents (Titles & Products) fetched along with document numbers.Verify the Posting Status is Posted. |  |
| 29 |  | Click on the Postings tab. |  |  |
| 30 |  | Click on the Details (‘>‘) icon at the start of the Posting record to expand the Titles node and the Products node. |  |  |
| 31 |  | Navigate to the most-recently created document in both the Titles and Products nodes using the Document Number hyperlink for each. | Verify the document data for both Titles and Products. |  |
| 32 |  | Click on the Back (‘<’) button. |  |  |
| 33 |  | Click on the Home button. |  |  |

### Determine Royalty

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Execute this test case if you have subscribed to SAP Rights & Royalty Management by Vistex. This test case is not relevant for other SAP margin optimization solutions by Vistex.

In this step, User will schedule a Work Manager to create Tracking and Posting Document(s).

Prerequisite

Create Royalty Agreement

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system for SAP Rights & Royalty Management as a Rights & Royalty Admin . | The Fiori launchpad displays. |  |
| 2 | Create Advance Billing Due Invoice | Navigate to the Calculations tile group and click on the Installments Due tile. |  |  |
| 3 |  | In the search fields, enter the following search parameters:Contract ID (noted at the end of Preliminary Step 2.9.6 (Create Royalty Agreement), e.g. 723)Agreement Type = Media Rights OutSchedule Type = Recoupable Fee by PeriodDue Date = <start date of operating year> |  |  |
| 4 |  | Click on the Go button. |  |  |
| 5 |  | Select the check box for the row. |  |  |
| 6 |  | Click on the Task Scheduler drop-down menu and select Generate Invoice Rights Out option. |  |  |
| 7 |  | On the New Job for Generate Invoice pop-up screen, click on the Schedule button. | If the Status shows as In Process, click on the Refresh button after few seconds. Repeat until Status shows as Completed. |  |
| 8 |  | Click on the Tracking hyperlink to view the created tracking document. | Note the Tracking Document Number _________ (e.g. 1905). |  |
| 9 |  | Click on the Back (‘<‘) button twice to go to the Home screen. |  |  |
| 10 |  | Navigate to Media Division Contracts tile group and click on the Media Rights Out tile. |  |  |
| 11 |  | Search for the Contract for which Tracking is created in Step 3 (e.g. 723) and click on the Go button. |  |  |
| 12 |  | Click on the Details (‘>‘) icon at the end of the row to view the details of the agreement. |  |  |
| 13 |  | Click on the Document Flow tab. | The tracking document created in Step 8 should be displayed. |  |
| 14 |  | Click on the document number hyperlink under the Tracking heading to view the data. | Click on each tab and view the data.DetailsSummarySchedule TotalsDue from PartnerMedia RO Fee Installment |  |
| 16 |  | Click on the Home button. |  |  |
| 17 | Post Advance Billing Due List | Navigate to Calculations tile group and click on the Unposted Fee Installments tile. |  |  |
| 18 |  | Search for the Tracking document noted in Step 8. |  |  |
| 19 |  | Click on the Go button. |  |  |
| 20 |  | Click on the Details (‘>‘) icon at the end of record to view details of the Tracking document. |  |  |
| 21 |  | Click on the Edit button. |  |  |
| 22 |  | Click on the Post button. |  |  |
| 23 |  | Click on the Media RO Fee Installment tab. | Note the Posting Document number ______ (e.g. 939) |  |
| 24 |  | Click on the Posting Document number hyperlink. | Click on each tab and view the data.PostingsItems |  |
| 26 |  | Click on the Home button. |  |  |
| 27 | Schedule a Job for Posting | Navigate to the Master Data Sync tile group and click on the Monitor Data Sync tile. |  |  |
| 28 |  | In the Overview tab, from the Schedule drop-down menu, select Push RR – Posting Documents. |  |  |
| 29 |  | In the Parameters tab, enter a Job Name and click on the Schedule button. |  |  |
| 30 |  | Click on the Refresh button to see results of the executed steps. After clicking on the Schedule button, system requires some time to start executing work manager. | Step results will be displayed in Documents section after completion of the job. |  |
| 31 |  | Click on the Posting Document hyperlink and click on the Posting Document number noted in Step 23 above (e.g. 939). | Note the FI document (posting document) number in the Posting Document header ________________ (e.g. 100000014). |  |
| 32 | Verify Advance Billing Due Posting in SAP S/4HANA Cloud Public Edition | Log into the SAP S/4HANA Cloud Public Edition system. |  |  |
| 33 |  | Navigate to the My Home tile group and click on the Display Journal Entries tile. |  |  |
| 34 |  | Search for the posted Accrual Posting Document (noted in Step 31, e.g. 100000014) in the Journal Entry field.Select the company code (e.g. 1710) in the Company Code drop-down menu.Select the fiscal year (e.g. <operating year>) in the Fiscal Year drop-down menu. |  |  |
| 35 |  | Click on the Continue button. | Verify document and amounts. |  |
| 36 |  | Return (log in) to the SAP margin optimization solutions by Vistex in SAP BTP before continuing to any other Test Procedure in this document. |  |  |

## Appendix

This Appendix contains the contents of files that need to be uploaded are part of preliminary steps related to SAP Rights & Royalty Management by Vistex, cloud edition.

Copy the contents of each section into a text file named as the section title. It is recommended to use Notepad (default simple text editor supplied with Microsoft Windows) instead of Microsoft Excel to avoid auto-formatting issues. The contents of each section contain tab-delimited data, and the column headers (Dimension, Description, Position) should be included in the text file contents.

### Language.txt

| Dimension | Description | Position |
| --- | --- | --- |
| RRNBL | Ndebele (Southern) | 1 |
| RRNSO | Sotho (Northern) | 2 |
| RRPAN | Punjabi | 3 |
| RRPER | Persian / Farsi | 4 |
| RRPOL | Polish | 5 |
| RRPOR | Portuguese | 6 |
| RRRON | Romanian | 7 |
| RRRUS | Russian | 8 |
| RRSLO | Slovak | 9 |
| RRSLV | Slovenian | 10 |
| RRSPA | Spanish | 11 |
| RRSRP | Serbian | 12 |
| RRSSW | Swati | 13 |
| RRSWA | Swahili | 14 |
| RRTAM | Tamil | 15 |
| RRTEL | Telugu | 16 |
| RRTGK | Tajik | 17 |
| RRTSN | Tswana | 18 |
| RRTSO | Tsonga | 19 |
| RRTUK | Turkmen | 20 |
| RRTUR | Turkish | 21 |
| RRUKR | Ukrainian | 22 |
| RRUZB | Uzbek | 23 |
| RRVEN | Venda | 24 |
| RRVIE | Vietnamese | 25 |
| RRWUU | Wu Chinese | 26 |
| RRXHO | Xhosa | 27 |
| RRYUE | Yue Chinese (includes Cantonese) | 28 |
| RRZUL | Zulu | 29 |
| RRMAC | Macedonian | 30 |
| RRAFR | Afrikaans | 31 |
| RRALB | Albanian | 32 |
| RRARA | Arabic | 33 |
| RRARM | Armenian | 34 |
| RRAZE | Azerbaijani | 35 |
| RRBEL | Belarusian | 36 |
| RRBEN | Bengali | 37 |
| RRBOS | Bosnian | 38 |
| RRBUL | Bulgarian | 39 |
| RRCHI | Chinese | 40 |
| RRCMN | Mandarin Chinese | 41 |
| RRCZE | Czech | 42 |
| RRENG | English | 43 |
| RREST | Estonian | 44 |
| RRFRE | French | 45 |
| RRGEO | Georgian | 46 |
| RRGER | German | 47 |
| RRGRE | Greek | 48 |
| RRHAU | Hausa | 49 |
| RRHEB | Hebrew | 50 |
| RRHIN | Hindi | 51 |
| RRHRV | Croatian | 52 |
| RRHUN | Hungarian | 53 |
| RRITA | Italian | 54 |
| RRJAV | Javanese | 55 |
| RRJPN | Japanese | 56 |
| RRKAZ | Kazakh | 57 |
| RRKIR | KRRgyz | 58 |
| RRKOR | Korean | 59 |
| RRLAV | Latvian | 60 |
| RRLIT | Lithuanian | 61 |
| YRFLE | Flemish | 62 |
| RRFLE | Flemish | 63 |

### Right Type.txt

| Dimension | Dimension | Description | Position |
| --- | --- | --- | --- |
| RR000900 |  | Television | 9 |
| RR001000 | RR000900 | Free Television | 10 |
| RR001100 | RR001000 | Free TV Terrestrial | 11 |
| RR001110 | RR001100 | Free TV Terrestrial Network | 12 |
| RR001120 | RR001100 | Free TV Terrestrial Syndication | 13 |
| RR001200 | RR001000 | Free TV Satellite | 14 |
| RR001300 | RR001000 | Free TV Cable/Wired | 15 |
| RR001400 | RR001000 | Free TV IPTV | 16 |
| RR001500 | RR001000 | Free TV World Wide Web | 17 |
| RR001600 | RR001000 | Free TV Wireless | 18 |
| RR001700 | RR000900 | Basic Subscription Television | 19 |
| RR001800 | RR001700 | Basic Subscription TV Terrestrial | 20 |
| RR001900 | RR001700 | Basic Subscription TV Satellite | 21 |
| RR002000 | RR001700 | Basic Subscription TV Cable/Wired | 22 |
| RR002100 | RR001700 | Basic Subscription TV IPTV | 23 |
| RR002200 | RR001700 | Basic Subscription TV World Wide Web | 24 |
| RR002300 | RR001700 | Basic Subscription TV Wireless | 25 |
| RR002400 | RR000900 | Premium Subscription Television | 26 |
| RR002500 | RR002400 | Premium Subscription TV Terrestrial | 27 |
| RR002600 | RR002400 | Premium Subscription TV Satellite | 28 |
| RR002700 | RR002400 | Premium Subscription TV Cable/Wired | 29 |
| RR002800 | RR002400 | Premium Subscription TV IPTV | 30 |
| RR002900 | RR002400 | Premium Subscription TV World Wide Web | 31 |
| RR003000 | RR002400 | Premium Subscription TV Wireless | 32 |
| RR003100 | RR000900 | Pay per View | 33 |
| RR003200 | RR003100 | PPV Terrestrial | 34 |
| RR003300 | RR003100 | PPV Satellite | 35 |
| RR003400 | RR003100 | PPV Cable/Wired | 36 |
| RR003500 | RR003100 | PPV IPTV | 37 |
| RR003600 | RR003100 | PPV World Wide Web | 38 |
| RR003700 | RR003100 | PPV Wireless | 39 |
| RR003800 |  | On Demand (OD) | 40 |
| RR003900 | RR003800 | Subscription VOD (SVOD) | 41 |
| RR004000 | RR003800 | Transaction VOD (TVOD) | 42 |
| RR004100 | RR003800 | Ad-Supported VOD (AVOD) | 43 |
| RR004200 | RR003800 | Catchup OD | 44 |
| RR004300 | RR004200 | On Demand Catchup Terrestrial | 45 |
| RR004400 | RR004200 | On Demand Catchup Satellite | 46 |
| RR004500 | RR004200 | On Demand Catchup Cable/Wired | 47 |
| RR004600 | RR004200 | On Demand Catchup IPTV | 48 |
| RR004700 | RR004200 | On Demand Catchup World Wide Web | 49 |
| RR004800 | RR004200 | On Demand Catchup Wireless | 50 |
| RR004900 |  | Home Video | 51 |
| RR005000 | RR004900 | Home Video Rental | 52 |
| RR005100 | RR005000 | Videogram Rental | 53 |
| RR005200 | RR005000 | Download to Rent (DTR) | 54 |
| RR005300 | RR004900 | Home Video Sell-Through | 55 |
| RR005400 | RR005300 | Videogram Sell-Through | 56 |
| RR005500 | RR005300 | Electronic Sell-Through (EST) | 57 |
| RR005600 |  | Derivative Rights | 58 |
| RR005700 | RR005600 | Feature | 59 |
| RR005800 | RR005600 | Live Performance/Stage Play | 60 |
| RR005900 | RR005600 | Live TV | 61 |
| RR006000 | RR005600 | New Derivative Type | 62 |
| RR006100 | RR005600 | Radio | 63 |
| RR006200 | RR005600 | Remake/Sequel | 64 |
| RR006300 | RR005600 | TV Series | 65 |
| RR006400 |  | Merchandising | 66 |
| RR006500 |  | Closed Network | 67 |
| RR006600 | RR006500 | ClosedNet Downloading | 68 |
| RR006700 | RR006500 | ClosedNet Streaming | 69 |
| RR006800 | RR006500 | ClosedNet Streaming/Downloading | 70 |
| RR006900 |  | Clip | 71 |
| RR007000 | RR006900 | Clips for Promotion | 72 |
| RR007100 | RR006900 | Clips for Reuse | 73 |
| RR007200 |  | Publishing | 74 |
| RR007300 | RR007200 | Trade Publishing | 75 |
| RR007400 | RR007200 | Professional Publishing | 76 |
| RR007500 | RR007200 | Mass Market Paperback | 77 |
| RR007600 | RR007200 | Educational Publishing | 78 |
| RR007900 | RR007200 | Subrights | 81 |
| RR008000 | RR007900 | Electronic Database | 82 |
| RR008100 | RR007900 | Book Club | 83 |
| RR008300 | RR007900 | First Serial | 85 |
| RR008800 | RR007900 | Second Serial | 90 |
| RR008900 | RR007900 | Anthology/Permission | 91 |
| RR007230 | RR007200 | Academic Journals | 83 |
| RR009100 |  | Interactive Entertainment | 93 |
| RR009200 | RR009100 | Console | 94 |
| RR009300 | RR009100 | Mobile | 95 |
| RR009400 | RR009100 | PC | 96 |
| RR009500 |  | Ancillary | 97 |
| RR009600 | RR009500 | Commercial Tie In | 98 |
| RR009700 | RR009500 | Covermount Rights | 99 |
| RR009800 | RR009500 | Film Clips | 100 |
| RR009900 | RR009500 | Music Publishing | 101 |
| RR010000 | RR009500 | New Ancillary Type | 102 |
| RR010100 | RR009500 | Product Placement | 103 |
| RR010200 | RR009500 | Records/Soundtracks | 104 |
| RR010300 | RR009500 | Theme Parks | 105 |
| RR000100 |  | Cinematic | 98 |
| RR000800 | RR000100 | Public Video | 8 |
| RR000300 | RR000100 | Non-Theatrical | 9 |
| RR000600 | RR000300 | Ships | 1 |
| RR000400 | RR000300 | Airlines | 2 |
| RR000500 | RR000300 | Hotels | 3 |
| RR000700 | RR000300 | Military Bases | 4 |
| RR000200 | RR000100 | Theatrical | 10 |
| RR001001 |  | Images | 99 |
| RR001020 | RR001001 | Advertising | 1 |
| RR001010 | RR001001 | Internal | 2 |
| RR001030 | RR001001 | Edit | 3 |

### Territory.txt

| Dimension | Dimension | Description | Position |
| --- | --- | --- | --- |
| RR1000 |  | Africa | 1 |
| RR1100 | RR1000 | Eastern Africa | 2 |
| X00027 | RR1100 | Burundi | 3 |
| X00040 | RR1100 | Comoros | 4 |
| X00056 | RR1100 | Ethiopia | 5 |
| X00058 | RR1100 | Eritrea | 6 |
| X00064 | RR1100 | Djibouti | 7 |
| X00096 | RR1100 | Kenya | 8 |
| X00111 | RR1100 | Madagascar | 9 |
| X00112 | RR1100 | Malawi | 10 |
| X00118 | RR1100 | Mauritius | 11 |
| X00125 | RR1100 | Mozambique | 12 |
| X00155 | RR1100 | Rwanda | 13 |
| X00164 | RR1100 | Seychelles | 14 |
| X00170 | RR1100 | Somalia | 15 |
| X00172 | RR1100 | Zimbabwe | 16 |
| X00175 | RR1100 | South Sudan | 17 |
| X00194 | RR1100 | Uganda | 18 |
| X00200 | RR1100 | Tanzania, United Republic Of Tanzania | 19 |
| X00211 | RR1100 | Zambia | 20 |
| RR1200 | RR1000 | Middle Africa | 21 |
| X00005 | RR1200 | Angola | 22 |
| X00030 | RR1200 | Cameroon | 23 |
| X00033 | RR1200 | Central African Republic | 24 |
| X00035 | RR1200 | Chad | 25 |
| X00042 | RR1200 | Congo, The Democratic Republic Of The | 26 |
| X00055 | RR1200 | Equatorial Guinea | 27 |
| X00065 | RR1200 | Gabon | 28 |
| X00160 | RR1200 | Sao Tome And Principe | 29 |
| RR1300 | RR1000 | Northern Africa | 30 |
| X00003 | RR1300 | Algeria | 31 |
| X00106 | RR1300 | Libya | 32 |
| X00124 | RR1300 | Morocco | 33 |
| X00176 | RR1300 | Sudan | 34 |
| X00177 | RR1300 | Western Sahara | 35 |
| X00190 | RR1300 | Tunisia | 36 |
| X00198 | RR1300 | Egypt | 37 |
| RR1400 | RR1000 | Southern Africa | 38 |
| X00020 | RR1400 | Botswana | 39 |
| X00103 | RR1400 | Lesotho | 40 |
| X00127 | RR1400 | Namibia | 41 |
| X00171 | RR1400 | South Africa | 42 |
| X00180 | RR1400 | Swaziland | 43 |
| RR1500 | RR1000 | Western Africa | 44 |
| X00032 | RR1500 | Cape Verde | 45 |
| X00049 | RR1500 | Benin | 46 |
| X00067 | RR1500 | Gambia | 47 |
| X00071 | RR1500 | Ghana | 48 |
| X00076 | RR1500 | Guinea | 49 |
| X00091 | RR1500 | Cote D'ivoire | 50 |
| X00105 | RR1500 | Liberia | 51 |
| X00115 | RR1500 | Mali | 52 |
| X00117 | RR1500 | Mauritania | 53 |
| X00135 | RR1500 | Niger | 54 |
| X00136 | RR1500 | Nigeria | 55 |
| X00162 | RR1500 | Senegal | 56 |
| X00165 | RR1500 | Sierra Leone | 57 |
| X00186 | RR1500 | Togo | 58 |
| X00202 | RR1500 | Burkina Faso | 59 |
| RR2000 |  | North America | 60 |
| X00006 | RR2000 | Antigua And Barbuda | 61 |
| X00011 | RR2000 | Bahamas | 62 |
| X00015 | RR2000 | Barbados | 63 |
| X00022 | RR2000 | Belize | 64 |
| X00031 | RR2000 | Canada | 65 |
| X00043 | RR2000 | Costa Rica | 66 |
| X00045 | RR2000 | Cuba | 67 |
| X00051 | RR2000 | Dominica | 68 |
| X00052 | RR2000 | Dominican Republic | 69 |
| X00054 | RR2000 | El Salvador | 70 |
| X00074 | RR2000 | Grenada | 71 |
| X00075 | RR2000 | Guatemala | 72 |
| X00078 | RR2000 | Haiti | 73 |
| X00080 | RR2000 | Honduras | 74 |
| X00092 | RR2000 | Jamaica | 75 |
| X00119 | RR2000 | Mexico | 76 |
| X00134 | RR2000 | Nicaragua | 77 |
| X00142 | RR2000 | Panama | 78 |
| X00151 | RR2000 | Puerto Rico | 79 |
| X00156 | RR2000 | Saint Kitts And Nevis | 80 |
| X00157 | RR2000 | Saint Lucia | 81 |
| X00158 | RR2000 | Saint Vincent And The Grenadines | 82 |
| X00188 | RR2000 | Trinidad And Tobago | 83 |
| X00201 | RR2000 | United States | 84 |
| RR3000 |  | South America | 85 |
| X00008 | RR3000 | Argentina | 86 |
| X00018 | RR3000 | Bolivia | 87 |
| X00021 | RR3000 | Brazil | 88 |
| X00036 | RR3000 | Chile | 89 |
| X00039 | RR3000 | Colombia | 90 |
| X00053 | RR3000 | Ecuador | 91 |
| X00077 | RR3000 | Guyana | 92 |
| X00144 | RR3000 | Paraguay | 93 |
| X00145 | RR3000 | Peru | 94 |
| X00179 | RR3000 | Suriname | 95 |
| X00203 | RR3000 | Uruguay | 96 |
| X00205 | RR3000 | Venezuela | 97 |
| RR4000 |  | Asia | 98 |
| RR4100 | RR4000 | Central Asia | 99 |
| X00094 | RR4100 | Kazakhstan | 100 |
| X00100 | RR4100 | Kyrgyzstan | 101 |
| X00184 | RR4100 | Tajikistan | 102 |
| X00192 | RR4100 | Turkmenistan | 103 |
| X00204 | RR4100 | Uzbekistan | 104 |
| RR4200 | RR4000 | Eastern Asia | 105 |
| X00037 | RR4200 | China | 106 |
| X00038 | RR4200 | Taiwan, Province Of China | 107 |
| X00081 | RR4200 | Hong Kong | 108 |
| X00093 | RR4200 | Japan | 109 |
| X00097 | RR4200 | Korea, Democratic People's Republic Of | 110 |
| X00098 | RR4200 | Korea, Republic Of | 111 |
| X00110 | RR4200 | Macao | 112 |
| X00121 | RR4200 | Mongolia | 113 |
| RR4300 | RR4000 | Middle East | 114 |
| X00012 | RR4300 | Bahrain | 115 |
| X00087 | RR4300 | Iraq | 116 |
| X00089 | RR4300 | Israel | 117 |
| X00095 | RR4300 | Jordan | 118 |
| X00099 | RR4300 | Kuwait | 119 |
| X00102 | RR4300 | Lebanon | 120 |
| X00126 | RR4300 | Oman | 121 |
| X00152 | RR4300 | Qatar | 122 |
| X00161 | RR4300 | Saudi Arabia | 123 |
| X00183 | RR4300 | Syrian Arab Republic | 125 |
| X00189 | RR4300 | United Arab Emirates | 126 |
| X00208 | RR4300 | Yemen | 128 |
| RR4400 | RR4000 | Southern Asia | 129 |
| X00001 | RR4400 | Afghanistan | 130 |
| X00013 | RR4400 | Bangladesh | 131 |
| X00017 | RR4400 | Bhutan | 132 |
| X00034 | RR4400 | Sri Lanka | 133 |
| X00084 | RR4400 | India | 134 |
| X00086 | RR4400 | Iran, Islamic Republic Of | 135 |
| X00114 | RR4400 | Maldives | 136 |
| X00129 | RR4400 | Nepal | 137 |
| X00141 | RR4400 | Pakistan | 138 |
| RR4500 | RR4000 | South Eastern Asia | 139 |
| X00024 | RR4500 | Brunei Darussalam | 140 |
| X00026 | RR4500 | Myanmar | 141 |
| X00029 | RR4500 | Cambodia | 142 |
| X00085 | RR4500 | Indonesia | 143 |
| X00101 | RR4500 | Lao People's Democratic Republic | 144 |
| X00113 | RR4500 | Malaysia | 145 |
| X00146 | RR4500 | Philippines | 146 |
| X00150 | RR4500 | Timor-Leste | 147 |
| X00166 | RR4500 | Singapore | 148 |
| X00168 | RR4500 | Vietnam | 149 |
| X00185 | RR4500 | Thailand | 150 |
| RR4600 | RR4000 | Western Asia | 151 |
| X00007 | RR4600 | Azerbaijan | 152 |
| X00014 | RR4600 | Armenia | 153 |
| X00066 | RR4600 | Georgia | 154 |
| RR5000 |  | Europe | 155 |
| RR5100 | RR5000 | Eastern Europe | 156 |
| X00025 | RR5100 | Bulgaria | 157 |
| X00028 | RR5100 | Belarus | 158 |
| X00048 | RR5100 | Czech Republic | 159 |
| X00082 | RR5100 | Hungary | 160 |
| X00147 | RR5100 | Poland | 161 |
| X00153 | RR5100 | Romania | 162 |
| X00154 | RR5100 | Russian Federation | 163 |
| X00167 | RR5100 | Slovakia | 164 |
| X00195 | RR5100 | Ukraine | 165 |
| RR5200 | RR5000 | Northern Europe | 166 |
| X00050 | RR5200 | Denmark | 167 |
| X00059 | RR5200 | Estonia | 168 |
| X00061 | RR5200 | Finland | 169 |
| X00083 | RR5200 | Iceland | 170 |
| X00088 | RR5200 | Ireland | 171 |
| X00104 | RR5200 | Latvia | 172 |
| X00108 | RR5200 | Lithuania | 173 |
| X00137 | RR5200 | Norway | 174 |
| X00181 | RR5200 | Sweden | 175 |
| X00199 | RR5200 | United Kingdom | 176 |
| RR5300 | RR5000 | Southern Europe | 177 |
| X00002 | RR5300 | Albania | 178 |
| X00004 | RR5300 | Andorra | 179 |
| X00019 | RR5300 | Bosnia And Herzegovina | 180 |
| X00044 | RR5300 | Croatia | 181 |
| X00046 | RR5300 | Cyprus | 182 |
| X00073 | RR5300 | Greece | 183 |
| X00079 | RR5300 | Holy See (Vatican City State) | 184 |
| X00090 | RR5300 | Italy | 185 |
| X00116 | RR5300 | Malta | 186 |
| X00123 | RR5300 | Montenegro | 187 |
| X00148 | RR5300 | Portugal | 188 |
| X00159 | RR5300 | San Marino | 189 |
| X00163 | RR5300 | Serbia | 190 |
| X00169 | RR5300 | Slovenia | 191 |
| X00174 | RR5300 | Spain | 192 |
| X00191 | RR5300 | Turkey | 193 |
| X00196 | RR5300 | Macedonia, The Former Yugoslav Republic | 194 |
| RR5400 | RR5000 | Western Europe | 195 |
| X00010 | RR5400 | Austria | 196 |
| X00016 | RR5400 | Belgium | 197 |
| X00062 | RR5400 | France | 198 |
| X00068 | RR5400 | Germany | 199 |
| X00107 | RR5400 | Liechtenstein | 200 |
| X00109 | RR5400 | Luxembourg | 201 |
| X00120 | RR5400 | Monaco | 202 |
| X00130 | RR5400 | Netherlands | 203 |
| X00149 | RR5400 | Guinea-Bissau | 204 |
| X00182 | RR5400 | Switzerland | 205 |
| RR6000 |  | Oceania | 206 |
| RR6100 | RR6000 | Ashmore and Cartier Islands | 207 |
| RR6200 | RR6000 | Antarctica | 208 |
| X00009 | RR6000 | Australia | 209 |
| X00023 | RR6000 | Solomon Islands | 210 |
| X00060 | RR6000 | Fiji | 211 |
| X00063 | RR6000 | French Polynesia | 212 |
| X00072 | RR6000 | Kiribati | 213 |
| X00128 | RR6000 | Nauru | 214 |
| X00131 | RR6000 | New Caledonia | 215 |
| X00132 | RR6000 | Vanuatu | 216 |
| X00133 | RR6000 | New Zealand | 217 |
| X00138 | RR6000 | Micronesia, Federated States Of | 218 |
| X00140 | RR6000 | Palau | 219 |
| X00143 | RR6000 | Papua New Guinea | 220 |
| X00187 | RR6000 | Tonga | 221 |
| X00193 | RR6000 | Tuvalu | 222 |
| X00206 | RR6000 | Samoa | 223 |

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
- related-to :: [[08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[08-sales-order-management/sales-rebate-processing-1b6-ae-test-script-sap-s-4hana-cloud-public-ed]]
- related-to :: [[08-sales-order-management/test-script-condition-contract-with-customer-hierarchy-consumer-produc]]
- related-to :: [[08-sales-order-management/test-script-sales-commissions-external-sales-representative-2tt-ae-863]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7UQ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 130,830 chars in the whole document
