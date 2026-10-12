---
id: 08-sales-order-management/test-script-advanced-intercompany-sales-5d2-ae-sap-s-4hana-cloud-publi
title: "Test Script: Advanced Intercompany Sales (5D2_AE) - SAP S/4HANA Cloud Public Edition (5D2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5D2 Advanced Intercompany Sales (AE): prerequisites, test steps by role, postings, value chain monitoring."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/advanced-intercompany-sales]
aliases: [5D2_S4CLD2608_BPD_EN_AE]
keywords: [Advanced Intercompany Sales, sales kits, sales order creation, intercompany invoicing, outbound delivery, goods issue, transfer of control dates, value chain monitoring, stock in transit, value chain issue resolution]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5D2_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1074
topic: 08-sales-order-management/advanced-intercompany-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Advanced Intercompany Sales (5D2_AE) - SAP S/4HANA Cloud Public Edition (5D2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5D2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Advanced Intercompany Sales** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Intercompany Sales (5D2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856319)

[1.1 Main Abbreviations Used in the Document 4](#_Toc232856320)

[2 Prerequisites 5](#_Toc232856321)

[2.1 System Access 5](#_Toc232856322)

[2.2 Roles 5](#_Toc232856323)

[2.3 Master Data and Organizational Data, and Other Data 6](#_Toc232856324)

[2.4 Additional Manual Configuration 8](#_Toc232856325)

[2.5 Business Conditions 8](#_Toc232856326)

[2.6 Preliminary Steps 8](#_Toc232856327)

[2.6.1 Create Condition Records (Optional) 9](#_Toc232856328)

[2.6.2 Preliminary Steps BRF+ Settings for Delivery Documents 10](#_Toc232856329)

[2.6.2.1 BRF+ Settings for Delivery Documents 10](#_Toc232856330)

[3 Overview Table 11](#_Toc232856331)

[4 Test Procedures 13](#_Toc232856332)

[4.1 Create Sales Order 13](#_Toc232856333)

[4.2 Process Sales Order Approval (Optional) 17](#_Toc232856334)

[4.3 Create Pro Forma F5 Invoice (Optional) 17](#_Toc232856335)

[4.4 Create Delivery 18](#_Toc232856336)

[4.5 Perform Picking 19](#_Toc232856337)

[4.6 Post Goods Issue 20](#_Toc232856338)

[4.7 Confirm Transfer of Control Dates 22](#_Toc232856339)

[4.8 Create Pro Forma F8 Invoice (Optional) 24](#_Toc232856340)

[4.9 Create Intercompany Invoice 26](#_Toc232856341)

[4.10 Display Intercompany Supplier Invoice 27](#_Toc232856342)

[4.11 Create F2 Invoice 28](#_Toc232856343)

[4.12 Update Text in Billing Document (Optional) 30](#_Toc232856344)

[4.13 Monitor Intercompany Sales Value Chain 31](#_Toc232856345)

[4.13.1 Display Intercompany Sales Value Chain 31](#_Toc232856346)

[4.13.2 Display Intercompany Purchase Order 33](#_Toc232856347)

[4.13.3 Display Intercompany Sales Order 34](#_Toc232856348)

[4.13.4 Display Intercompany Supplier Invoice 35](#_Toc232856349)

[4.14 Schedule Resolution of Value Chain Issues (Optional) 36](#_Toc232856350)

## Purpose

Overview

This scope item enables you to sell from stock and manage intercompany sales transactions seamlessly between affiliated organizations. A new process creates an additional purchase order in the selling company and a sales order in the delivery company.

This process utilizes valuated stock in transit (VSIT) to support several key functions. It allows for profitability reporting for both affiliated companies and ensures a seamless change of control between affiliates and the customer. Additionally, it supports event-based revenue recognition and provides detailed insights through the material ledger and cost component split. The process also includes integrated product and trade compliance checks and is fully integrated into transportation management, including the management of freight costs.

Sales Kits Sales Process

In addition to the standard sales process, this scope item also supports sales kits in the advanced intercompany sales. It partially combines the functions and requires the following scope item as the business condition:

- Sales Order Processing for Sales Kits (31Q)

Prerequisites

Please refer to scope item 31Q, Chapter Preliminary Steps to create material master data, condition records and BOM definition etc,. before starting this process testing.

Currently, only the following Sales Kits (LUMF, CPFH, DISH, ERLA) are in this scope item’s scope.

Scope of Sales Kits in Advanced Intercompany Sales Business

1. Inventory-Controlled Items:

Only inventory-controlled items are included in the intercompany business.

Inventory-controlled items will integrate into the Transit Plant and associated processes (FIN integration), including Purchase Order, Intercompany Order, Outbound Delivery, Intercompany Invoice, Customer Invoice, and Stock in transit postings.

1. Non-Inventory-Controlled Items:

Non-inventory-controlled items will solely integrate into the Transit Plant to ensure financial availability of the Sales Kit within the selling company. These items will appear only in the Outbound Delivery and Customer Invoice as they do not impact material valuation or stock movements (no movement type assigned). They are not included in the intercompany business.

1. Profitability Segment Logic for CPFH and DISH:

CPFH and DISH will continue employing existing profitability segment logic, propagating from main to sub with FIN integration at the Transit Plant. This ensures consistent support for standard plants and subitems, with no deviations supported in current processes.

Summary

The selling organization offers Sales Kits, consisting of both inventory and non-inventory-controlled goods, to external customers. However, the intercompany business exclusively involves inventory-controlled goods. Delivery of the Sales Kit to the external customer is managed by the delivering organization. Intercompany billing, which involves transactions between affiliated companies where the delivering company invoices the selling company, pertains only to inventory-controlled goods ordered through the Purchasing document.

|  |
| --- |
| Note Scope item 5D2 does not support the following scenarios:Non-stock itemsNon sales kit structures, for example, configuration with subitemOrder related / milestone billing and free of charge w/o billing documentThird-party order processingMixed scenarios (aICO and classical ICO) within a single sales kit. The sales order cannot be saved in this case. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

### Main Abbreviations Used in the Document

| Abbreviation | Explanation |
| --- | --- |
| SiT | Stock in Transit |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/5D2_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | General Ledger | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data and Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

In our example the Sales Organization 3310 is selling the product TG12 to the domestic Customer 33100002 in United Arab Emirates. The goods are directly shipped to the customer from the plant 1710 in US (which is owned by the US Delivering Company 1710). Meanwhile, Stock in Transit that is owned by the Selling Company 3310 is assigned to the plant 3310 of the Selling Company 3310. The Delivering Sales Organization 1710 will create an intercompany invoice towards the Selling Company 3310, while the Customer’s Company 3310 will receive a supplier invoice from the Delivering Company 1710.

You can either use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Material which is used to be provided to the customer. |
| Material for Sales Kits | SDBOMERLAHDSDBOMERLAIT01SDBOMERLAIT02SDBOMLUMFHDSDBOMLUMFIT01SDBOMLUMFIT02SDBOMCPFHHDSDBOMCPFHIT01SDBOMCPFHIT02SDBOMDISHHDSDBOMDISHIT01SDBOMDISHIT02 | SD BOM Header ERLASD BOM ERLA Item01SD BOM ERLA Item02SD BOM Header LUMFSD BOM LUMF Item01SD BOM LUMF Item02SD BOM Header CPFHSD BOM CPFH Item01SD BOM CPFH Item02SD BOM Header DISHSD BOM DISH Item01SD BOM DISH Item02 |  |
| Customer | 33100002 | Domestic UAE Customer 2 |  |
| Intercompany Payer | 33403310 | In the US Delivering Company 1710’s view, this ID represents the Customer Company 3310 as a customer. It acts as the payer in both the sales order and the intercompany invoice in the US Delivering Company1710. |  |
| Intercompany Supplier | 17401710 | In the Customer Company 3310’s view, this ID represents the US Delivering Company 1710 as a vendor. It acts as the invoicing party in both the purchase order and the supplier invoice in the Customer Company 3310. |  |
| Intercompany Plant Customer | 33413310 | In the US Delivering Company 1710’s view, this ID represents the plant 3310 as a customer. It acts as the sold-to-party in both the sales order and the intercompany invoice US Delivering Company 1710. |  |
| Intercompany Plant Supplier | 17411710 | In the Customer Company 3310’s view, this ID represents the plant 1710 as a vendor. It acts the vendor in the purchase order and in the supplier invoice in the Customer Company 3310. |  |
| Selling Company’s Sales Organization | 3310 | Sales organization in selling company 3310 and is responsible for creating invoice to customer. |  |
| Delivering Company’s Sales Organization | 1710 | Sales organization in delivering company 1710 and is responsible for creating intercompany invoice. |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Master Data Script Reference

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/cdc21d75bc156982be95178cc2d7dbc7)

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in company codes 1710 and 3310 respectively. |

### Preliminary Steps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Please refer to test script Create New Open MM Posting Period - MDS - MDS (BNZ) to open new posting period in company codes 1710 and 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material: TG12Material for Sales Kits: In chapter Sales Bill of Material Structure, the material that specified with inventory should be included.Plant: <Supply Plant in affiliate company>, for example, 1710 | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select an initial stock to add, for example:Storage Location: <Storage Location in the affiliate supply plant>, for example, 171A | A dialog displays.The Storage Location, Stock Type and Current Quantity display according to the previous step entries. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition |

#### Preliminary Steps BRF+ Settings for Delivery Documents

##### BRF+ Settings for Delivery Documents

Purpose

This process step shows you how to define the system determination of output parameters for printing a delivery document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Output Type | In the Select Business Rule section, make the following entries:Show Rules for: Outbound DeliveryDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules | Expand the Maintain Business Rules section. Choose Edit. In the Table Contents, choose Insert New Row and enter the following entries:Output Type: DELIVERY_NOTE | The relevant form is added.Insert after the line the last Sender Country mentioned in the list and insert before the lines with no Sender Country mentioned. |  |
| 5 | Activate | Choose Activate. | Rules are activated. |  |

## Overview Table

The scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction\App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_13) [page ] 13 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Process Sales Order Approval (Optional)](#unique_14) [page ] 17 |  |  | Sales order is approved. |
| [Create Pro Forma F5 Invoice (Optional)](#unique_15) [page ] 17 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F5 type is created. |
| [Create Delivery](#unique_16) [page ] 18 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Perform Picking](#unique_17) [page ] 19 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is picked. |
| [Post Goods Issue](#unique_18) [page ] 20 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Confirm Transfer of Control Dates](#unique_19) [page ] 22 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Transfer of Control Dates are confirmed. |
| [Create Pro Forma F8 Invoice (Optional)](#unique_20) [page ] 24 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F8 type is created. |
| [Create Intercompany Invoice](#unique_21) [page ] 26 | Billing Clerk | Create Billing Documents (F0798) | Billing with IV2 type is created. Intercompany Supplier Invoice is created automatically. |
| [Display Intercompany Supplier Invoice](#unique_22) [page ] 27 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Intercompany Supplier Invoice displays. |
| [Create F2 Invoice](#unique_23) [page ] 28 | Billing Clerk | Create Billing Documents (F0798) | Billing with F2 type is created. |
| [Update Text in Billing Document (Optional)](#unique_24) [page ] 30 | Billing Clerk | Change Billing Documents (VF02) | Change Billing Documents displays. |
| Monitor Intercompany Sales Value Chain |  |  |  |
| [Display Intercompany Sales Value Chain](#unique_25) [page ] 31 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Display Intercompany Purchase Order](#unique_26) [page ] 33 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Display Intercompany Sales Order](#unique_27) [page ] 34 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Display Intercompany Supplier Invoice](#unique_28) [page ] 35 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Schedule Resolution of Value Chain Issues (Optional)](#unique_29) [page ] 36 | Internal Sales Representative | Schedule Mass Resolution of Value Chain Issues (F6868) | Application Jobs displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales order in the selling company, then goods will be directly delivered to the customer from the affiliate company/plant.

Part 1: Create Sales Order with General Trading Material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order VA01 . | The Sales Order screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330Choose Continue. | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | Sold-to Party: 33100002Cust. Reference: PO numberDeliver.Plant: <Delivery Plant in another company code>, for example, 1710Plant: <Delivery Plant in another company code>, for example, 1710Material: <material number>, for example, TG12.Order Quantity: <quantity>, for example, 10. |  |  |
| 6 | Enter Tax Departure Country | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region | In the Billing section, input country abbreviation that is consistent to Sales Organization.For example, if Sales Organization is 3310, then make the following entry:Tax Departure C / R: AE |  |  |
| 8 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check Transit Plant | Choose the line item and choose Display Item Details. Choose Shipping tab, check the value of the field Transit Plant, for example, 3310. | The right Transit Plant displays. |  |
| 10 | Save | Choose Save. | A sales order is created.Make a note of the sales order number. |  |
| 11 | Check Intercompany Purchase Order | Execute the step [Display Intercompany Purchase Order](#unique_26) [page ] 33 to check the Intercompany Purchase Order automatically created by the above sales order. | Intercompany Purchase Order is automatically created successfully. |  |
| 12 | Check Intercompany Sales Order | Execute the step [Display Intercompany Sales Order](#unique_27) [page ] 34 to check the intercompany sales order automatically created by the above sales order. | Intercompany Sales Order is automatically created successfully. |  |

Part 2: Create Sales Order with Sales Kits Material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Orders - VA01(VA01). |  |  |
| 4 | Enter the Order Data | On the Create Standard Order: Initial screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries:Sold to party: 33100002Ship to party: 33100002Customer Reference: <Customer Reference>Customer Reference Date: <Date>Material Number: <SDBOMERLAHD> or <SDBOMLUMFHD>Deliver.Plant: <Delivery Plant in another company code>, for example, 1710Plant: <Delivery Plant in another company code>, for example, 1710Order Quantity: <Quantity>Enter the item category TAQF or TAPF manually before BOM explosion if the item is free of charge during order creation.Note If you are using SDBOMERLAHD, SDBOMLUMFHD, or SDBOMCPFHHD, SDBOMDISHHD (for Cloud only) in testing, the sales BOM will explode and subitems will appear. However, the BOM expansion and material presentation on Sales to Customer documents and Internal Sales documents are different.In Sales to Customer documents (Sales Order, Outbound Delivery, Customer Invoice), main item and subitems are shown both.In Internal Sales documents (Purchase Order, Intercompany Order, Intercompany Invoice, Supplier Invoice, and Stock in Transit postings) only items with Inventory Management are shown.Consequently, these items must carry (internal) prices, regardless of whether the external price is charged on them or not.BOM TypePricing inInventory inThe section for Sales to Customer documents displaysThe section for Internal Sales document displaysSDBOMERLAHDMain itemMain itemMain item and subitems bothMain item onlySDBOMLUMFHDSubitemsSubitemsMain item and subitems bothSubitems onlySDBOMCPFHHDMain itemSubitemsMain item and subitems bothSubitems onlySDBOMDISHHDSubitemsMain itemMain item and subitems bothMain item only |  |  |
| 6 | Enter Tax Departure Country | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region | In the Billing section, input country abbreviation that is consistent to Sales Organization.For example, if Sales Organization is 1010, then make the following entry:Tax Departure C / R: DE |  |  |
| 8 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check Transit Plant | Choose the line item and choose Display Item Details. Choose Shipping tab, check the value of the field Transit Plant, for example, 1010. | The right Transit Plant displays. |  |
| 10 | Save | Choose Save. | A sales order is created.Make a note of the sales order number. |  |
| 11 | Check Intercompany Purchase Order | Execute the step [Display Intercompany Purchase Order](#unique_26) [page ] 33 to check the Intercompany Purchase Order automatically created by the above sales order. | Intercompany Purchase Order is automatically created successfully. |  |
| 12 | Check Intercompany Sales Order | Execute the step [Display Intercompany Sales Order](#unique_27) [page ] 34 to check the intercompany sales order automatically created by the above sales order. | Intercompany Sales Order is automatically created successfully. |  |

### Process Sales Order Approval (Optional)

Follow the procedure in Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This process step shows you how to review the sales orders that might be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the scope item Sell from Stock (BD9).

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
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Select billing type Pro Forma for Order (F5) and maintain billing date, for example, current date.Enter Intercompany Sales Order number in the input field Document which is created in the previous step.Press Enter. |  |  |
| 4 | Save | Choose Save. | The F5 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Billing Number and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx (F5) Display: Overview screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Pro Forma for Order xxxxxxxx ( F5) Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display PDF Document. | Preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries-From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 1710Planned Creation Date: <delivery selection date>Order: <sales order number created previously> | The Create Delivery: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to take goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Manage Outbound Deliveries screen, make the following entry:1710 |  |  |
| 5 | Select the Only Picking without WM Checkbox and Choose Execute | Choose Only Picking without WM.Choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Outbound Delivery xxx Change: Overview screen, choose Picking and enter quantity in the Picked Qty field.Picking status is set to Completely processed if picked quantity and delivery quantity are equal.Deviations in quantity can be solved by the Copy Picked Quantity as Delivery Quantity function. |  |  |
| 8 | Save Document | Choose Save. |  |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entry and choose Execute.Shipping Point: 1710 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue.Select today’s date in the dialog box.Choose Continue. | The goods issue is posted to Stock in Transit of delivering company, for example, 3310. The other follow-on good movements are posted or scheduled for later posting according to the Transfer of Control Dates. |  |
| 5 | Check Status of Advanced Intercompany Sales Value Chain | Execute the step Display Intercompany Sales Value Chain to check the status of the Advanced Intercompany Sales Value Chain. | The status of the Advanced Intercompany Sales Value Chain is correct. The other follow-on good movements are posted or scheduled for later posting successfully according to the Transfer of Control Dates. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen is displayed. |  |
| 3 | Issue Delivery Output | Choose For Goods Issue.Make the following entries and choose Execute.Shipping Point: 1710On the Display Outbound Delivery, enter the Delivery number, and choose Continue.On the Delivery xxxxxxxxxxx Display: Overview:choose More > Extras > Delivery > Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_NOTE, and choose Display PDF Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Goods | 13600000 Inventory - Trading Goods | none |

### Confirm Transfer of Control Dates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm transfer of control dates. Normally the transfer of control dates is confirmed by API or TM integration based on Incoterms.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose List Outbound Deliveries.Make the following entries and choose Execute.Shipping Point/Receiving Pt: 1710 | List of Outbound Deliveries screen displays. |  |
| 4 | Change Outbound Deliveries | Mark the relevant delivery and choose Change Outbound Deliveries. | Outbound Delivery <Outbound Delivery> Change: Overview screen displays. |  |
| 5 | Confirm Internal Transfer of Control Dates and Times | On the top menu, choose Menu > Goto > Header > Shipment , check the field Planned Dates and Time at the screen block Internal Transfer of Control Dates, input new actual date and time in the field Actual Date and Time to reflect the actual case, for example, current System Date and Time.Note This field controls when the goods movement will be posted from Stock in Transit of the delivering company to the selling company. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement one day later than this date and time. | Internal Transfer of Control Dates are confirmed. |  |
| 6 | Confirm External Transfer of Control Dates | At the screen block External Transfer of Control Dates, check the field Planned Dates and Time, input new actual date and time in the field Actual Date and Time to reflect the actual case, for example, current System Date and Time.Note This field controls when the goods movement will be posted from Stock in Transit of the selling company to customer. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement one day later than this date and time. | External Transfer of Control Dates are confirmed. |  |

Financial Posting

Post Goods Issue from Issuing SiT in delivering company

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem | 13600000 Inventory - Trading Goods | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem |

Post Goods Receipt to storage location in selling company 3310

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading Good | 21120000 Goods Received/Invoice Received | none |

Post Goods Issue from storage location in selling company 3310

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory - Trading | 13600000 Inventory - Trading Goods | none |

Post Goods Issue from SiT to Customer in selling company 3310

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem | 13600000 Inventory - Trading Goods | 54083000 Inventory Change - Cost of own Goods sold w/C.Elem |

### Create Pro Forma F8 Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma invoice in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Pro Forma Invoice for Delivery (F8) and maintain billing date, for example, current date.Enter Delivery Number.Choose Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Billing Number, and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoicexxxxxxxx Display: Overview screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Invoice xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Invoice Change: Output screen, select the output entry and choose Display PDF Document. | Preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create intercompany invoice in delivering company code. In background, intercompany supplier invoice is created automatically in the selling company code by Value Chain Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings on the bottom bar and make the following entries:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary, for example, the Delivery Number, press Enter. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously with intercompany sold-to party and choose the button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Intercompany Invoice (IV2) and maintain billing date, for example current date, then choose button OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________.Note The intercompany supplier invoice is only created automatically by VCM when the intercompany customer invoice has been transferred and released to FI. | The system generates an invoice for billing. |  |
| 8 | Check Intercompany Supplier Invoice | Execute the step Display Intercompany Supplier Invoice to know the number of the intercompany supplier invoice. |  |  |

Financial Posting

In all the scenarios related to a sales flow, whatever billing document is created (customer invoice, debit note, credit note, intercompany invoice, etc.) the journal entry type is determined according to the following rule:

- If the Dest. Country/Region is Italy, the FI document type is W1 IT Local Cust. Sales.
- If the Dest. Country/Region is within European Union, the FI document type is W2 IT EU Cust. Sales.
- If the Dest. Country/Region is outside European Union, the FI document type is W3 IT EXEU Cust. Sales.

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 Receivables affiliated Companies | 41001500 Revenue Affiliate - Product | 41001500 Revenue Affiliate - Product |

### Display Intercompany Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the intercompany supplier invoice automatically created by the IV2 invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen displays. |  |
| 3 | Search Intercompany Supplier Invoice | Enter the intercompany supplier invoice number in the field Invoice Document No. or enter the intercompany invoice number in the field Reference, which is noted down in the previous step. Choose Go. | The supplier invoice is listed out. |  |
| 4 | Display Intercompany Supplier Invoice | Choose the line item of the intercompany supplier invoice. | The Supplier Invoice screen displays. |  |
| 5 | Display Journal Entry | Choose Journal Entries, and the Display Process Flow – Accounts Payable screen displays.Choose the node Journey Entry, and the Journal Entry dialog box displays.Expand Related Applications, and choose Display Journal Entries. | The Display Document: Data Entry View screen displays. |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 21120000 Goods Received/Invoice Received | 21300000 Company Code 1710 as Business Partner | none |

### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create customer invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings on the bottom bar and make the following entries:Set the billing date and type in before billing: ONCreate a separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after the creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary, for example, the Delivery Number. Then press Enter. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select the row(s) of the SD document created previously with customer sold-to party and choose Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain the billing date, for example the current date. Then choose OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Rcvbls Domestic | 41000000 Revenue Domestic – Product22000000 Output Tax (MWS) | none |

### Update Text in Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to update text in a billing document.

Procedure

Update Text in Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Billing Documents (VF02). | The Change Billing Documents screen displays. |  |
| 3 | Enter the Billing Number | On the Change Billing Documents screen, enter the respective billing document number created in the previous step.Choose Enter. | The billing document displays. |  |
| 4 | Update Text (Optional) | In the Edit mode, you can add, delete, and update these texts. | The relevant text is added, deleted, or updated. |  |
| 5 | Save your Changes | Save your changes by choosing Save in the footer bar. | The billing document is saved. |  |

Display Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Billing Documents (VF03). | The Display Billing Documents screen displays. |  |
| 3 | Enter the Billing Number | On the Display Billing Documents screen, enter the respective billing document number and choose Continue. | The billing document displays. |  |
| 4 | Check Output Condition | On the Invoice xxxxxxxx (F2) Display: Overview of Billing Items screen, choose More > Goto > Header > Output . |  |  |
| 5 | Display PDF Document | On the Invoice xxxxxxxx (F2) Display: Output screen, select output item with output type BILLING_DOCUMENT and form template SDBIL_INVOICE_RU. Choose Display PDF Document. | Preview for PDF document displays. |  |

### Monitor Intercompany Sales Value Chain

#### Display Intercompany Sales Value Chain

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display advanced intercompany sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type: <Advanced Intercompany Sales>Note You can also enter other document number to search the Advanced Intercompany Process Chain, for example, Outbound Delivery number, Intercompany Invoice number and so on. | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Check the Status of the Advanced Intercompany Sales Value Chain Process | Check the value of the field Status on the screen, possible values could be from the list:Open: Value Chain is triggeredIn Process: Value Chain is in processingPending: Value Chain is pending for external processingProcessed with Errors: Error occurred when executing a process step by Value Chain ManagementReprocessing: Value Chain is under reprocessingCompleted: Value Chain is completed | The status of the intercompany sales value chain displays. |  |
| 7 | Display the Process Flow of the Advanced Intercompany Sales Value Chain Process | Choose Process Flow tab in Business Process screen, detailed process steps of Advanced Intercompany Sales value chain are displayed in a flow chart. Each process step is displayed as a node with the following data:Step Name, for example, Sales Order (SOSC)Business Document Number, for example, Sales Order (1234)Document Type, for example, Sales OrderDocument ID, for example, 1234Document Status, for example, CompletedNote Legend of the color of process node:Green: process step is CompletedRed: process step is in an ErrorGrey: process step is OpenOrange: process step is PendingBlue: process step is Scheduled | The Process Flow of the Advanced Intercompany Sales value chain process displays. |  |

#### Display Intercompany Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check intercompany purchase order of the advanced inter-company sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type : <Advanced Intercompany Sales> | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Display Intercompany Purchase Order | Locate the line item for the step “IC Purchase Order (POIC)” from the Documents list, click the line item. | The Document screen displays. |  |
| 7 | Note Down the Purchase Order Number | Note down the Purchase Order number on the top of the screen. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type: <Advanced Intercompany Sales> | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Display Intercompany Sales Order | Locate the line item for the step “IC Sales Order (SOIC)” from the Documents list, click the line item. | The Document screen displays. |  |
| 7 | Note Down the Sales Order Number | Note down the Sales Order number on the top of the screen. |  |  |

#### Display Intercompany Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display or check supplier invoice of the advanced intercompany sales value chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Value Chains (F4854). | The Monitor Value Chains screen displays. |  |
| 3 | Adapt Searching Filter | Choose Adapt Filters, and the Adapt Filters dialog box pops up. Select Initiating Document, Processing Stage and Process Type, and choose OK. | Searching field Process Type displays. |  |
| 4 | Search Value Chain Process | Make the following entries and choose Go:Initiating Document: * + Sales Order number.Process Type: <Advanced Intercompany Sales> | Business Processes that match the search criteria are listed out. |  |
| 5 | Display the Advanced Intercompany Value Chain Process | Click the line item from the Business Processes list. | The Business Process screen displays. |  |
| 6 | Display Intercompany Sales Order | Locate the line item for the step “IC Supplier Invoice (SIIC)” from the Documents list, click the line item. | The Document screen displays. |  |
| 7 | Note Down the Supplier Invoice Number | Note down the Supplier Invoice number on the top of the screen. |  |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Script is for the AE (UAE) localization with company 3310, but financial posting guidance refers to Italian FI document types W1/W2/W3, Part 2 sales order example uses sales org 1010/DE, and invoice form template SDBIL_INVOICE_RU is a Russian template; may disagree with other localized versions of 5D2.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5D2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 66,114 chars in the whole document
