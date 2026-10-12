---
id: 10-procurement/test-script-guided-buying-for-central-procurement-with-sap-ariba-buyin
title: "Test Script: Guided Buying for Central Procurement with SAP Ariba Buying (3EN) (3EN_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3EN: Guided Buying with SAP Ariba Buying and Central Procurement, from shopping cart to supplier invoice."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-guided-buying]
aliases: [3EN_S4CLD2608_BPD_EN_XX]
keywords: [Guided Buying with SAP Ariba Buying, guided buying, central procurement, shopping cart, shopping cart approval, inventory reservation, purchase order creation, goods receipt, supplier invoice, service entry sheet]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3EN_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-930
topic: 10-procurement/ariba-guided-buying
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Guided Buying for Central Procurement with SAP Ariba Buying (3EN) (3EN_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3EN_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Guided Buying with SAP Ariba Buying** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Guided Buying for Central Procurement with SAP Ariba Buying (3EN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232835867)

[2 Prerequisites 4](#_Toc232835868)

[2.1 Additional Manual Configuration 4](#_Toc232835869)

[2.2 System Access 4](#_Toc232835870)

[2.3 Roles 4](#_Toc232835871)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232835872)

[2.5 Business Conditions 5](#_Toc232835873)

[2.6 Preliminary Steps 6](#_Toc232835874)

[2.6.1 Configure Automatic Creation of Reservation for Inventory Items (Optional) 6](#_Toc232835875)

[2.6.2 Create Catalogs for Inventory Items (Optional) 8](#_Toc232835876)

[2.6.3 Set Up Pro-Rata VAT New Tax Codes 9](#_Toc232835877)

[3 Overview Table 10](#_Toc232835878)

[4 Test Procedures 12](#_Toc232835879)

[4.1 Open Guided Buying App 12](#_Toc232835880)

[4.2 Create Shopping Cart 13](#_Toc232835881)

[4.3 Approve Shopping Cart 16](#_Toc232835882)

[4.4 Create Reservation (Automated) 17](#_Toc232835883)

[4.5 Display Shopping Cart (Resesrvation) 18](#_Toc232835884)

[4.6 Post Goods Movement (Reservation) 18](#_Toc232835885)

[4.7 Display Shopping Cart (Purchase Requisition) 20](#_Toc232835886)

[4.8 Create Purchase Order (Automated) 21](#_Toc232835887)

[4.8.1 Create Purchase Order (Manually, Optional) 21](#_Toc232835888)

[4.9 Display Shopping Cart (Purchase Order) 23](#_Toc232835889)

[4.10 Create Service Entry Sheet (Optional) 24](#_Toc232835890)

[4.11 Display Shopping Cart (Entry Sheet - Optional) 25](#_Toc232835891)

[4.12 Create Goods Receipt 26](#_Toc232835892)

[4.13 Display Shopping Cart (Goods Receipt - Optional) 28](#_Toc232835893)

[4.14 Create Supplier Invoice 29](#_Toc232835894)

[4.15 Display Shopping Cart (Invoice - Optional) 30](#_Toc232835895)

## Purpose

Overview

Guided buying in SAP Ariba Buying creates a simple, smart, and elegant purchasing experience that increases user engagement across all spend areas. It serves as a central place where all buyers can shop across all goods and services. It enables procurement and individual line-of-business (LoB) owners to specify procurement policies and inform and guide users whenever there appear to be policy conflicts. Central Procurement offers a centralized requisitioning process across industries with a deep integration into the customer's landscape. It connects guided buying in SAP Ariba Buying capability to the customer’s ERP or SAP S/4HANA Cloud Public Edition systems, and exchanges business documents to ensure end-to-end business processes into finance and logistics that run in the connected systems. The integration allows the transfer and updates of the requisition between the two as well as necessary master data.

Guided buying in SAP Ariba Buying creates a simple, smart, and elegant purchasing experience that increases user engagement across all spend areas. It serves as a central place where all buyers can shop across all goods and services. It enables procurement and individual line-of-business (LoB) owners to specify procurement policies and inform and guide users whenever there appear to be policy conflicts. Central procurement offers a centralized requisitioning process across industries with a deep integration into the customer's landscape. It connects Guided Buying in SAP Ariba Buying to the customer’s ERP or SAP S/4HANA Cloud Public Edition systems, and exchanges business documents to connect buying to finance and logistics and ensure end-to-end business processes. The integration allows transferring and updating requisition data and master data between the two systems.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/5b3f4932d23bd2821ec7f7cd908a2d27)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA HUB system | Any SAP S/4HANA system 2020 and higher. The SAP S/4HANA system acts as a hub system when it’s connected to multiple back-end systems. |
| Back-end system | Any ERP system from release ERP 6.06 releases and above, with add-on HUBERPI, is considered as the back-end system.Any SAP S/4HANA 1709 and higher, with add-on HUBS4IC, is considered as back-end system. |
| Guided Buying with SAP Ariba Buying | Your system administrator provides you with access to Guided Buying with SAP Ariba Buying. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Administrator (optional) | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

|  |
| --- |
| Note The role administrator was an optional role if you want to display fields Telephone, Fax, Street 2 and Street 3 in the delivery address of purchase requisition items on Hub system, you can use Process Purchase Requisitions (V2) (F1048A) and adapt the user interface (UI) of this app with key user adaptation. For details, refer to the [Making UI Changes (Object Pages)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/54270a390b194c3e97be2424592c3352.html?locale=en-US) of the [Adapting the UI](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/d868950a1e8c4b0f9b9453176939a19b.html?locale=en-US) section. |

### Master Data, Organizational Data, and Other Data

Master data in your system landscape

- The initial set of master data such as account assignment category, material group, purchasing organization, and purchasing group, existing in the back-end system, should also exist and be in sync with the Hub system and the SAP Ariba Buying system.
- Organizational data of back-end systems, such as the purchasing organization and purchasing groups, should exist in the Hub and the SAP Ariba Buying system.

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 18J - Requisitioning | Complete the Create Purchase Requisition step |
| 1XI - Central Requisitioning | Complete the Preliminary Steps in the test script to define the company code, plant, material group, etc. |

### Preliminary Steps

This step is valid only if you want to purchase an inventory item.

1. Log on to SAP Ariba (with guided buying capability enabled) using your administrator credentials.
2. On the dashboard, navigate to Manage > Core Administration > Feature Manager > Feature Availability Status to check below feature was enable or not. If not please enable them.
    - GB-10579
    - InventoryReservation
3. On the dashboard, naviagte to Manage > Core Administration > Customization Manager > Parameters to check below parameters was enable or not. If not, enable them.
    - Application.Common.EnablePlantBasedDefaultingForSAP
    - Application.Purchasing.EnableInventoryReservation
    - Application.Procure.S4Hana.SendGuidedBuyingInventoryReservationRequestsToS4HANA
    - Application.Purchasing.S4Hana.SendMaterialIDAsStandardFieldInGBRequests

#### Configure Automatic Creation of Reservation for Inventory Items (Optional)

This step is valid only if you want to purchase an inventory item.

|  |
| --- |
| Note As a prerequisite, the requested item needs to have an open, unrestricted stock. You can check this using the Fiori app Display Stock Overview. Log on as a Warehouse Clerk. |

Purpose

In this procedure, you configure the automatic creation of reservations for a purchasing group and material group combination.

Procedure

Option 1 – SAP S/4HANA Cloud Public Edition as a Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Logon to the SAP Fiori launchpad as a Configuration Expert. |  |  |
| 2 | Access App | Open the Settings for Creation of Reservation (F2278) app. |  |  |
| 3 | Maintain Values | Under General Settings section, enter the following details:Rules: <Goods Issue (03)>Movement Type: <GI for cost center (201)>Under the Requisition Identifiers section, enter the purchasing group and material group combination that you want enabled for automatic creation of reservation:Purchasing Group: Enter the purchasing group of the inventory item<002>Material Group: Enter the material group of the inventory item<L001>Auto-Reservation: ONCheck Unrestricted Stock Only: If the checkbox is selected, then the checking rule is bypassed and availability is determined based on only the stock that is available for unrestricted use.Choose Save. |  |  |

Option 2 – SAP ERP as a Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP ERP GUI as Configuration Expert. |  |  |
| 2 | Open Settings for Creation of Reservation | Input transaction code SPROAccess the transaction using the following navigation path.IMG Path: > SAP Customizing Implementation Guide M > Materials Management > Purchasing > Central Procurement > Setting in connecte4d systems > Central Purchase Requisitions > Reservation > Define settings for Creation of Reservation . |  |  |
| 3 | Maintain Values | Under General Settings section, enter the following details:Requisition Scenario: <Self-Service Procurement>Movement Type: < GI for cost center (201)>Checking Rule: <03>UnrestrictedStock: <Check Unrestricted Stock Only>Choose Save. |  |  |
| 4 | OpenMaterial Group and Purchasing Group for Reservation | Access the transaction using the following navigation path.IMG Path: > SAP Customizing Implementation Guide M > Materials Management > Purchasing > Central Procurement > Setting in connecte4d systems > Central Purchase Requisitions > Reservation > Define > Material Group and Purchasing Group for Reservation |  |  |
| 5 | Maintain Values | Under General Settings section, add new entry by the following details:Material Group: <L002 >PGr: <001>Checking Rule: <03>Auto Reserv: <Allow>Choose Save. |  |  |

#### Create Catalogs for Inventory Items (Optional)

This step is valid only if you want to purchase an inventory item.

Purpose

In this procedure, the supplier or buyer will create the catalogs for inventory items, which can be purchased via SAP Ariba Buying (with guided buying capability enabled).

Procedure

Both supplier and buyer can create the catalog for inventory items by first preparing the Catalog Interchange Format (CIF) file. For more detailed information about CIF, refer to [Topics about CIF catalogs](https://help.sap.com/viewer/43cc25c2fa9d4789b058784e816a2af8/LATEST/en-US/dd8ab5cbf0181014b2b3f8e513c6b6ee.html).

Suppliers can create and publish catalogs via Ariba Network for Suppliers, refer to the instructions on [How to create and publish catalogs](https://help.sap.com/viewer/1e9220c0f83d42d097418c387d3bea9b/LATEST/en-US/ddaf99d2f01810148790eb55a113e8aa.html).

Buyers can import local catalogs for SAP Ariba Procurement solutions, refer to the instructions on [How to import local catalogs](https://help.sap.com/viewer/c9b2518a80f1409aae8660cd58612a65/LATEST/en-US/6a6064a8c1da1014922ef287e2d82c26.html).

#### Set Up Pro-Rata VAT New Tax Codes

Use

For , if it is relevant for you, you can configure tax codes especially for pro-rata VAT (partially deductible and non-deductible VAT). To achieve this, you must perform the following steps.

Procedure

1. Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration.

Navigate to Manage Your Solution (F1241) → Configure Your Solution. You can search for a configuration step. In the search result, select the configuration item and go to the next screen. Select the configuration step and choose Configure.

SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following configuration activities:

| Configuration Activity | Instruction | Comments |
| --- | --- | --- |
| Define Tax Codes for Sales and Purchases | Create pro-rata tax codes that can trigger the automatic split of deductible and non-deductible portion |  |
| Define Pro Rata Coefficients | Define pro rata coefficients | Based on this configuration, the system can then automatically split the input VAT into deductible and nondeductible portions when an incoming invoice is posted, using the coefficient that is valid for the company code and the tax code on the relevant date. |
| Automatic Account Determination | Assign accounts for your new tax codes | Required when you create tax codes |
| Define Enhanced Tax Box Structure | Ensure your new tax codes are reported in the VAT return | Required when you create tax codes |

1. For each of the activities, choose Open Documentation to see more details about each configuration activity.
2. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system.
3. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration.

## Overview Table

The Guided Buying for Central Procurement with SAP Ariba Buying (3EN) scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Result |
| --- | --- | --- | --- |
| [Open Guided Buying App](#unique_13) [page ] 12 | Employee | Custom tile created in the set-up instructions (refer to the section [Open Guided Buying App](#unique_13) [page ] 12) | Guided Buying with SAP Ariba Buying logon screen is displayed.Note The user will automatically be logged on to Guided Buying if single sign-on for SAP Ariba is configured. |
| [Create Shopping Cart](#unique_14) [page ] 13 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is created and transferred to the SAP S/4HANA HUB system. |
| [Approve Shopping Cart](#unique_15) [page ] 16 | Approver | Guided Buying with SAP Ariba Buying | Shopping cart is approved. |
| [Create Reservation (Automated)](#unique_16) [page ] 17 | Automated step | Automated step | Reservation is created in the backend system |
| [Display Shopping Cart (Resesrvation)](#unique_17) [page ] 18 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with reservation ID. |
| [Post Goods Movement (Reservation)](#unique_18) [page ] 18 | Warehouse Clerk | Post Goods Movement |  |
| [Display Shopping Cart (Purchase Requisition)](#unique_19) [page ] 20 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with back-end PR creation status. |
| [Create Purchase Order (Automated)](#unique_20) [page ] 21 | Automated step | Automated step | PO is created from PR in the back-end system. |
| [Create Purchase Order (Manually, Optional)](#unique_21) [page ] 21 | Purchaser | Manual in back-end system | PO is created from PR in the back-end system. |
| [Display Shopping Cart (Purchase Order)](#unique_22) [page ] 23 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with back-end PO number. |
| [Create Goods Receipt](#unique_23) [page ] 26 | Warehouse Clerk | Post goods receipt for purchase order in back end system |  |
| [Display Shopping Cart (Goods Receipt - Optional)](#unique_24) [page ] 28 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with GR number in Guided Buying with SAP Ariba Buying. |
| [Create Supplier Invoice](#unique_25) [page ] 29 | Accounts Payable Accountant | Create supplier invoice in back-end system | Invoice is created in the back-end system. |
| [Display Shopping Cart (Invoice - Optional)](#unique_26) [page ] 30 | Employee | Guided Buying with SAP Ariba Buying | Shopping cart is updated with invoice number in Guided Buying with SAP Ariba Buying. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Open Guided Buying App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you open SAP Ariba Guided Buying.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee. |  |  |
| 2 | Go to Menu Path | For example, choose Purchase Requisition Processing > Guided_Buying (created in the set-up instructions, refer to the section Create Guided Buying App).Note The user will automatically be logged on to Guided Buying if single sign-on for SAP Ariba is configured. |  |  |

### Create Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you see the newly created shopping cart in Guided Buying with SAP Ariba Buying.

Procedure

Option 1 – Create Shopping Cart for a Non-Catalog Item

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to Guided Buying with SAP Ariba Buying as an Employee . |  |  |
| 2 | Go to Menu Path | On the right-side of the navigation pane, choose Request a non-catalog item. You can select the form that you published to create a shopping cart. |  |  |
| 3 | Maintain the Values | On this page, you can choose either the Goods or the Services tab.For a Goods request:The field names and the example values are:Product Name: <Laptop>Category: <footware>Description: <Description>Quantity: <10>Unit of Measure: <Each>Price: <10> per <1> each.If you want to create a shopping cart with the form you've published, go to the Shop tab, select the Line item form app that you've published, and enter the information required by the form.When you add a catalog or ad-hoc item to the shopping cart, if the Category value is a commodity code that is mapped as limit, the This is a limit item. checkbox is displayed.When you add a limit item to a request, you need to enter a value for the following fields that are displayed at the line item level:Expected valueOverall limitStart dateEnd dateOn the Checkout screen, you can change the value of the following fields that are displayed at the line item level:Expected valueOverall limitStart dateEnd date |  |  |
| 4 | Add to Cart and Check Out | Choose Add to Cart and in the dialog box, please choose Checkout. |  |  |
| 5 | Maintain Parameters | On the checkout screen, maintain the required parameters.Note The values given are example values.DataTitle: <Laptop>Need-by Date: <Today+1>Vendor: <Your Backend Supplier>AccountingAccount Assignment: <K> <Cost Center>Account Type: <Cost Center>Bill To: <Your Backend Plant>G/L Account: <Your Backend Account>Cost Center: <Your Backend Cost Center>ShippingPlant: <Your Backend Plant>Purchasing Group: <Your Backend Purchasing Group>Deliver To: <Buyer name>OthersCommodity Code: <footware>Item Category: <Material>Payment Terms: <Net45>Purch Org: <Your Backend Purchasing Organization> |  |  |
| 6 | Send Request | Choose Submit and Done. | A success message is displayed. |  |
| 7 | Note Down the PR Number and the ERP Reference ID | Note down the PR number and the ERP Reference ID. | PR<XXXX>: Requisition has been submitted in SAP S/4HANA.ERP Reference ID: <XXXXXXXX>. |  |

Option 2 – Create Shopping Cart for Inventory Items

|  |
| --- |
| Note In order to test with an inventory item, you need to first complete the [Configure Automatic Creation of Reservation for Inventory Items (Optional)](#unique_9) [page ] 6 and [Create Catalogs for Inventory Items (Optional)](#unique_10) [page ] 8 chapters as mentioned under [Preliminary Steps](#unique_8) [page ] 6. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. |  |  |
| 2 | Search for the inventory item | On the upper pane, search for an inventory item which is configured in preliminary steps, |  |  |
| 3 | Maintain Values | Maintain the required parameters.Quantity: 1 |  |  |
| 4 | Add to Cart and Checkout | Choose Add to Cart and in the dialog box, choose Checkout. |  |  |
| 5 | Maintain Parameters | In the checkout screen, maintain the required parameters.Note The values given are example values.DataTitle: <Free text>Need-by Date: <Today+1>AccountingAccount Assignment: <K><Cost Center>Account Type: <Cost Center>Bill To: <Your Backend Plant>G/L Account: <Your Backend Account>Cost Center: <Your Backend Cost Center>ShippingPlant: <Your Backend Plant>Purchasing Group: <Your Backend Purchasing Group>Deliver To: <Employee name>OthersPurch Org: <Your Backend Purchasing Organization> |  |  |
| 6 | Send Request | Choose Submit and Done. | A message appears informing you that you've sent your request for approval. |  |
| 7 | Note PR number | Note the number. For example, PR<XXXX>. | PR<XXXX> status: Submitted |  |
| 8 | Note the ERP Reference ID | Note the ERP Reference ID number. (This is the PR number created in the SAP S/4HANA Buyer system.) |  |  |

### Approve Shopping Cart

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Approver logs on to the SAP Ariba Buying system to approve the shopping cart.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Approver. |  |  |
| 2 | Go to Menu Path | Choose the SAP logo on the top-left corner. |  |  |
| 3 | Approve Requests | Choose Approve requests. |  |  |
| 4 | To Approve | On the Approve requests screen, select the To approve tab. |  |  |
| 5 | Select PR for Approval | Search for PRXXXX, which was created in the previous step. |  |  |
| 6 | Approve PR | Choose Approve. |  |  |
| 7 | Comments for Approval | In the Approve Request dialog box, enter comments and choose Approve. |  |  |
| 8 | Repeat Steps | Repeat steps 1 to 7 for all the other approvers. |  | The status of PRXXXX changes from Submitted to Approved in the external system. |

### Create Reservation (Automated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with an inventory item.

In this activity, the reservation will be created automatically in the back-end system.

Prerequisites

Automatic reservation creation is configured for a purchasing group and material group combination of your inventory item, as mentioned in the [Preliminary Steps](#unique_8) [page ] 6.

Procedure

The reservation will be created automatically in the SAP S/4HANA Cloud Public Edition system.

### Display Shopping Cart (Resesrvation)

Purpose

This step is valid only if you're testing with inventory item.

In this activity, you check the shopping cart to see the updated resesrvation ID from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Display Shopping Cart | On the Recently Viewed left navigation panel, click the shopping cart that you had created in the earlier step. | Shopping cart is displayed with details. |  |
| 3 | Reservation Number Updated in PR | Under the History tab, in the summary column, you see a message with reservation ID. | Make a note of the reservation ID. |  |

### Post Goods Movement (Reservation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you're testing with an inventory item.

In this activity, you post the goods in the back-end system.

Procedure

Case 1: ERP as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the back-end ERP system. |  |  |
| 2 | Open Post Goods Movement | Create the goods receipt with the transaction code MIGO.Choose Goods Issue, and Reservation, enter the back-end Reservation ID that you've obtained in the previous step. |  |  |
| 5 | Post | Enter all required data, for example, Qty in Delivery Note, Item OK, and so on. Then, choose Post. | A dialog box appears with the material document number.Note down this number. |  |

Case 2: SAP S/4HANA as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Open Post Goods Movement | Open Post Goods Movement (MIGO). |  |  |
| 3 | Search for reservation | Choose A07 Goods Issue, and R09 Reservation, input the reservation ID <reservation ID> that you've noted down in the previous step and choose Enter. |  |  |
| 4 | Check Delivery Quantity | Under Quantity, check the delivery quantity, enter all necessary entries, for example Storage Location, Item OK, and so on. |  |  |
| 5 | Post | Choose Post. | A message dialog box appears with the Material Document number.Note This material document number will not be updated in guided buying with SAP Ariba Buying. |  |

### Display Shopping Cart (Purchase Requisition)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the employee checks the shopping cart to see the updated purchanse requisition ID from the back end system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Employee. |  |  |
| 2 | Display Shopping Cart | On the Recently Viewed navigation panel on the left, choose the shopping cart that you've created before. |  |  |
| 3 | ERP ID Number Updated in PR | Under the History tab, in the Summary column, you see a message with a PR number and a requisition ID to inform you that the requisition has been successfully replicated to the back end system from the hub.Make a note of the back end Purchase Requisition ID. |  |  |

### Create Purchase Order (Automated)

Purpose

A purchase order is automatically created from the purchase requisition.

Prerequisites

- You have maintained a customizing entry in the back-end system which enables the automatic creation of purchase orders. First, you create a purchase requisition in Guided Buying with SAP Ariba Buying system, from there it's replicated to the back-end system and a purchase order is automatically generated.
- The purchase order is not created automatically if a purchase order has already been created for any one of the items in purchase requisition.
- The automatic creation of purchase orders is not allowed if any of the items listed in purchase requisition fails to create a purchase order.
- The existing configuration for automatic creation of purchase orders in ERP with transaction ME59 is applicable.

#### Create Purchase Order (Manually, Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the purchaser creates a purchase order (PO) in the back-end system. This step can be carried out only if an automatic PO is not created from purchase requisition (PR).

Procedure

Case 1: ERP as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the respective back-end system to which the employee belongs as a Purchaser |  |  |
| 2 | Assign Source of Supply | Search for the back-end PR ID that you've obtained in the previous step, and assign the sources of supply with the transaction code ME57. |  |  |
| 3 | Change Account Assignment or Assign Source of Supply | Search for the back-end PR ID that you've obtained in the previous step, and change the account assignment or assign the source of supply with the transaction code ME57.Note If you’re creating a PO of service, please add the service number in the PO in this step. | If you create a purchase requisition with account assignment U, the PO creation process will be triggered after you change the account assignment from U to K. |  |
| 4 | Create Purchase Order | Create the standard PO with reference to previous PR ID with the transaction code ME21N. | A purchase order is created in the back-end system. |  |

Case 2: SAP S/4HANA as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Find your Purchase Requisition | Open Assign and Process Purchase Requisitions (ME57).Make the following entries:Purchase Requisition: <Your back-end purchase requisition ID that you 've obtained in the previous step>Assigned Purchase Requisitions: <Select>Choose Execute. |  |  |
| 3 | Change Account Assignment | On the Assign and Process Purchase Requisitions screen, choose your purchase requisition and make the following entries:AcctAssCat: change from U to KOpen Item Detail, choose Account Assignment, and make the following entries:Cost Center: <your cost center>Choose Save. | If you create a purchase requisition with account assignment U, the PO creation process is triggered after you change the account assignment from U to K. |  |
| 4 | Assign Supply for your Back-End Purchase Requisition | On the Assign and Process Purchase Requisitions screen, choose your purchase requisition and choose Edit Items.Open Item Detail, go to the Source of Supply tab and make the following entries:Fixed Supplier: <your supplier>Choose Save. |  |  |
| 5 | Create Purchase Order | Go to Purchase Order Processing and open the Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) app.In the Search field, enter the PR number that you've obtained in section [Create Shopping Cart](#unique_14) [page ] 13. Choose Go.Select the purchase requisition in which the assigned supplier is displayed and choose Create Purchase Order.Select the Purchase Order Type with standard PO and choose Save. | A purchase order is created in the back-end system. |  |

### Display Shopping Cart (Purchase Order)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the employee checks the shopping cart to see the updated purchase order (PO) number from the back end system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Employee. |  |  |
| 2 | Display Shopping Cart | On the Recently Viewed navigation panel on the left, choose the shopping cart that you've created earlier. |  |  |
| 3 | PO Number Updated in PR | Under the History tab, in the Summary column, you see a message with the PO number, for example:PRXXXX : Ordered in SAP S/4HANA. ERP Order IDs: [XXXXXXXX].Make a note of the back-end Purchase Order ID. |  |  |
| 4 | PR Status Changed | The PR status is changed from Ordering to Ordered. |  |  |

### Create Service Entry Sheet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you post the service entry sheet in the back-end system. This step is only required when you've chosen a service request in section [Create Shopping Cart](#unique_14) [page ] 13.

Procedure

Case 1: ERP as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the back-end ERP system. |  |  |
| 2 | Open Display Entry Sheet | Create the goods receipt with Transaction Code Ml81n.Choose Other Purchase Order and search by purchase order ID.Choose Create Entry Sheet. |  |  |
| 3 | Release Service Entry Sheet | Add Service No. and Quantity. Make sure the data is the same as the data in the purchase order.Hit Enter until you see a green flag in the menu bar.Click the flag to release and save the service entry sheet. | The status of service entry sheet changes to Accepted. |  |

Case 2: SAP S/4HANA as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Open Manage Service Entry Sheets | Choose the app Manage Service Entry Sheets - Lean Services (F2027). | . |  |
| 3 | Search for Purchase Requisition | Enter the purchase order number that you’ve noted down in the previous step and choose Enter (or you can select your purchase requisition from the list). |  |  |
| 4 | Check Delivery Quantity | Under Items, enter Delivered as <same as open quantity>. |  |  |
| 5 | Post | Choose Post.A dialog box displays the material document number. Note down this number. |  |  |

### Display Shopping Cart (Entry Sheet - Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is valid only if you’re testing with a lean service procurement. In this activity, the employee checks the shopping cart in guided buying to see the updated entry sheet number from the back end system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Employee. |  |  |
| 2 | Display Shopping Cart | On the Recently Viewed navigation panel on the left, choose the shopping cart that you’ve created in the previous step. |  |  |
| 3 | Entry sheet number updated in PR | In the History tab, in the Summary column, you see a message with the XXX number.Check whether the entry sheet created in the backend system and the number updated are the same. |  |  |

### Create Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt to the back-end system.

Procedure

Case 1: ERP as a Back-End System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the back-end ERP system. |  |  |
| 2 | Open Confirm Receipt of Goods | Create the goods receipt with the transaction code MIGO.Choose Goods Receipt and then choose Purchase Order, enter the back-end PO ID that you've obtained in the previous step. |  |  |
| 5 | Post | Enter all required data, for example, Qty in Delivery Note, Item OK, and so on. Then, choose Post. | A dialog box appears with the material document number.Note down this number. |  |

Case 2: SAP S/4HANA as a Back-End System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Open Confirm Receipt of Goods | Choose Post Goods Receipt for Purchasing Document (F0843). |  |  |
| 3 | Search for Purchase Requisition | Enter the PO number that you've obtained in the previous step and choose Enter. Alternatively, you can select your purchase requisition from the list. |  |  |
| 4 | Check Delivery Quantity | Under Items, enter Delivered as <same as open quantity>. |  |  |
| 5 | Post | Choose Post. | A dialog box displays the material document number.Note down this number. |  |

Case 3: Post the Goods Receipt in Guided Buying with SAP Ariba Buying

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Employee. | The Guided Buying Home page is displayed. |  |
| 2 | Open Your Requests | Choose the Your Requests tab. |  |  |
| 3 | To Receive | On the Your Requests tab, choose the To Receive tab. |  |  |
| 4 | Submit Goods Receipt | Find the Purchase Order number which was created in Guided Buying with SAP Ariba Buying, and enter the following: Accepted: <enter the quantity you want to receive, for example 10> Final Receipt: <select the checkbox if all quantities are accepted> Choose Submit. |  |  |

### Display Shopping Cart (Goods Receipt - Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the shopping cart in guided buying to see the updated GR number from the back end system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Employee. |  |  |
| 2 | Display Shopping Cart | On the Recently Viewed navigation panel on the left, choose the shopping cart that you've created in the previous step. |  |  |
| 3 | GR Number Updated in PR | Under the History tab, in the Summary column, you see a message with the GR number, for example:PRXXXX: Received in SAP S/4HANA.ERP Receipt IDs:[XXXXXXXX]. | Check that the GR created in the back end system and the number updated are the same. |  |

### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the accountant creates a supplier invoice in the back-end system.

Procedure

Case 1: ERP as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the ERP back-end system. |  |  |
| 2 | Open the Create Supplier Invoice | Create a supplier invoice for the back-end PO that you've obtained in the previous step with transaction code MIRO. |  |  |
| 3 | Post the Invoice | Enter all the necessary data of the invoice and choose Post. | The invoice is created. |  |

Case 2: SAP S/4HANA as back-end system

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Open the Create Supplier Invoice App | Choose Create Supplier Invoice (F0859). |  |  |
| 3 | Enter General Data | If purchase orders with local currencies have been created in your system, make the following entries:Transaction: <Invoice>Company Code: <Your Company Code>Invoice Date: <Today>Posting Date: <Today>Gross Invoice Amount : <Value in PO Calculate Tax>Invoice Party: <Your Supplier Number>Reference: <Reference Invoice Number from Invoicing Party> |  |  |
| 4 | Enter Purchase Order References | On the Purchase Order References tab, make the following entries (use the back-end PO ID that you 've obtained in the previous step).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: PO number |  |  |
| 5 | Check the Purchase Order Items Data | Check the Amount, the Quantity, and the Tax Code. |  |  |
| 6 | Post Invoice | Choose Post. | The invoice is created. |  |

### Display Shopping Cart (Invoice - Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the shopping cart in guided buying to see the updated invoice number from the back end system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Guided Buying with SAP Ariba Buying as an Employee. |  |  |
| 2 | Display Shopping Cart | On the Recently Viewed navigation panel on the left, choose the shopping cart that you've created in the previous step. |  |  |
| 3 | Invoice Number Updated in PR | On the History tab, in the Summary column, you see a message with the invoice number. For example:PRXXXX : Invoiced in SAP S/4HANA.ERP Invoice IDs: [XXXXXXXX] | Check if the invoice created in back end system and the number updated are the same. |  |

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
- related-to :: [[10-procurement/test-script-guided-buying-capability-with-sap-ariba-buying-2nv-ae-836]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3EN_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 49,469 chars in the whole document
