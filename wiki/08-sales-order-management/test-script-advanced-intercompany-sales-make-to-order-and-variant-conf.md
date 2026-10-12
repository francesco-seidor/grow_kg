---
id: 08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf
title: "Test Script: Advanced Intercompany Sales – Make-to-Order and Variant Config (7DM_AE) (7DM_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script (7DM_AE): advanced intercompany sales with make-to-order and variant configuration, prerequisites to value chain monitoring."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/advanced-intercompany-sales, topic/intercompany-make-to-order]
aliases: [7DM_S4CLD2608_BPD_EN_AE]
keywords: [Advanced Intercompany Sales, variant configuration, make-to-order production, intercompany invoicing, stock in transit, value chain monitoring, outbound delivery, billing documents, supplier invoices, financial postings]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DM_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1210
topic: 08-sales-order-management/advanced-intercompany-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Advanced Intercompany Sales – Make-to-Order and Variant Config (7DM_AE) (7DM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Advanced Intercompany Sales** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Intercompany Sales – Make-to-Order and Variant Config (7DM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860053)

[1.1 Main Abbreviations Used in the Document 4](#_Toc232860054)

[2 Prerequisites 5](#_Toc232860055)

[2.1 System Access 5](#_Toc232860056)

[2.2 Roles 5](#_Toc232860057)

[2.3 Master Data and Organizational Data, and Other Data 6](#_Toc232860058)

[2.4 Additional Manual Configuration 9](#_Toc232860059)

[2.5 Business Conditions 9](#_Toc232860060)

[2.6 Preliminary Steps 10](#_Toc232860061)

[2.6.1 Initial Stock Posting for the Material in BoM 10](#_Toc232860062)

[2.6.2 Create Condition Records (Optional) 11](#_Toc232860063)

[2.6.3 Maintain SSCUI Assign Item Categories (Optional) 11](#_Toc232860064)

[2.6.4 BRF+ Settings for Delivery Documents 12](#_Toc232860065)

[2.6.5 Enable Advanced Intercompany Sales - Make-to-Order and Variant Process Config 13](#_Toc232860066)

[2.6.6 Assign Transit Plant to Company Code 14](#_Toc232860067)

[3 Overview Table 15](#_Toc232860068)

[4 Test Procedures 17](#_Toc232860069)

[4.1 Create Sales Order with Configurable Material (Single Level) 17](#_Toc232860070)

[4.2 Process Sales Order Approval (Optional) 21](#_Toc232860071)

[4.3 Create Pro Forma F5 Invoice (Optional) 21](#_Toc232860072)

[4.4 Manufacturing Steps Production Order Processing 22](#_Toc232860073)

[4.5 Create Delivery 24](#_Toc232860074)

[4.6 Perform Picking 25](#_Toc232860075)

[4.7 Post Goods Issue 26](#_Toc232860076)

[4.8 Confirm Transfer of Control Dates 28](#_Toc232860077)

[4.9 Create Pro Forma F8 Invoice (Optional) 30](#_Toc232860078)

[4.10 Create Intercompany Invoice 31](#_Toc232860079)

[4.11 Display Intercompany Supplier Invoice 33](#_Toc232860080)

[4.12 Create F2 Invoice 34](#_Toc232860081)

[4.13 Update Text in Billing Document (Optional) 35](#_Toc232860082)

[4.14 Monitor Intercompany Sales Value Chain 37](#_Toc232860083)

[4.14.1 Display Intercompany Sales Value Chain 37](#_Toc232860084)

[4.14.2 Display Intercompany Purchase Order 39](#_Toc232860085)

[4.14.3 Display Intercompany Sales Order 40](#_Toc232860086)

[4.14.4 Display Intercompany Supplier Invoice 41](#_Toc232860087)

[4.15 Schedule Resolution of Value Chain Issues (Optional) 42](#_Toc232860088)

## Purpose

Overview

This scope item enables advanced variant configuration (Make-to-Order Production with Variant Configuration (1YT)) in advanced intercompany sales. It partially combines those functions and requires the following scope items as business conditions:

- Advanced Intercompany Sales Processing (5D2)
- Make-to-Order Production with Variant Configuration (1YT)

Key Process Flow

- Create Sales Order with Configurable Product (Single Level)
- Manufacturing Steps:
    - Run MRP
    - Create Planned Order
    - Create Production Order
    - Confirm Assembly Activities
    - Post Goods Receipt (to Sales Order Stock)
- Create Outbound Delivery
- Post Stock Transfer (Valuated Stock in Transit) from Delivering to Selling Company and from Selling Company to Customer
- Create Intercompany Billing Document
- Create Supplier Invoice
- Create Customer Invoice
- Use Value Chain Monitor to Track Postings

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
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | General Ledger | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data and Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

In our example the Sales Organization 3310 is selling the product CM-FL-V00 to the domestic Customer 33100002 in United Arab Emirates. The goods are directly shipped to the customer from the plant 1710 in US (which is owned by the US Delivering Company 1710). Meanwhile, Stock in Transit that is owned by the Selling Company 3310 is assigned to the plant 3310 of the Selling Company 3310. The Delivering Sales Organization 1710 will create an intercompany invoice towards the Selling Company 3310, while the Customer’s Company 3310 will receive a supplier invoice from the Delivering Company 1710.

You can either use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | CM-FL-V00 | Configurable Forklifter | Please refer to Set-Up Instructions of the scope item 5D2, chapter Enhance Material Master in Selling Company Code to maintain the field, for example, Stor. Location for Ext. Proc. with value 171APlease refer to Set-Up Instructions of the scope item 5D2, chapter Maintain Standard Purchase Info Record with value, for example, BP 17411710, Pur. Org 1010 |
| Material | SF-FL-COMB | FORKLIFTER BASE MODEL COMBUSTION | Initial stock posting required |
| Material | SF-FL-CWEIGHT | COUNTERWEIGHT 1000KG | Initial stock posting required |
| Material | SF-FL-ELECTRIC | FORKLIFTER BASE MODEL ELECTRICAL | Initial stock posting required |
| Material | SF-FL-TIRE-CUSH | CUSHION TIRE ASSEMBLY | Initial stock posting required |
| Material | SF-FL-TIRE-PNEU | PNEUMATIC TIRE ASSEMBLY | Initial stock posting required |
| Material | SF-FL-FORK-S | FORK (1.200 MM) | Initial stock posting required |
| Material | SF-FL-FORK-M | FORK (1.800 MM) | Initial stock posting required |
| Material | SF-FL-FORK-L | FORK (2.400 MM) | Initial stock posting required |
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
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |
| 2NI | Create Application Group and Characteristic Display - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for scope item Advanced Intercompany Sales (5D2). These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/cdc21d75bc156982be95178cc2d7dbc7)

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in company codes 1710 and 3310 respectively. |
| IYT - Make-to-Order Production with Variant Configuration | Please ensure scope item 1YT has been activated in your system. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | Please ensure scope item BJE has been activated in your system. |
| 5D2 - Advanced Intercompany Sales | Please ensure scope item 5D2 has been activated in your system. |

### Preliminary Steps

Before this scope item can be tested, the following preliminary steps must be met.

#### Initial Stock Posting for the Material in BoM

Purpose

This process step shows you how to post initial stock for BoM materials of CM-FL-V00.

|  |
| --- |
| Note Alternatively, you can run the procurement scope items. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other - XXX (your user name) screen displays. |  |
| 3 | Enter Details | Choose Goods Receipt and Others on top of the screen.In the Detail Data section, make the following entries and press Enter. Select Next Item icon to add entries.On the Where tab:Goods Movement Type: 561 (Init.entry of stBal.)Plant: 1710Storage Location: 171BOn the Quantity tab:Quantity: <Quantity>, for example, 100On the Material tab:Material: <BOM Material>, see the Bill of Material Structure for CM-FL-V00 in the chapter Master Data, Organizational Data, and Other Data for a detailed materials list.Select Item OK, and choose Check. | A message displays: The Document is OK. |  |
| 4 | Post | Confirm the message that the batch has been created and choose Post. | A message displays: Material document XXXXXXXX posted. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition |

#### Maintain SSCUI Assign Item Categories (Optional)

Purpose

If you want to use Item Category CBTN when creating OR order. Please refer to the following settings to extend the possibility of Item Category CBTN within Sales Order OR with configuration item category group 0002 via SSCUI Assign Item Categories (102807) for this combination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on the SAP Fiori launchpad as an Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item | Enter the following filters:Application Area: SalesSub Application Area: Sales Order Management and ProcessingIn the items table, select the item with item name: Sales Documents. | The Configure Your Solution - Sales Documents screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Assign Item Categories (102807) configuration steps. |  |  |
| 6 | Add Item Category CBTN | Make the following entries and choose Save:SaTy: ORItCGr: 0002MltCa: CBTN | This combination supports sales order OR with item category 0002 of FoC Config. at Mat CBTN. |  |

#### BRF+ Settings for Delivery Documents

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

#### Enable Advanced Intercompany Sales - Make-to-Order and Variant Process Config

Purpose

Advanced intercompany sales make-to-order and variant process is disabled for the standard document types and item categories by pre-delivered configuration. The pre-delivered configuration must be enabled through SSCUI. Only with this configuration enabled, the Advanced Intercompany Sales process is activated.

|  |
| --- |
| Note If the configuration is already available, this step can be skipped. |

Prerequisite

All the above settings and configurations have been completed.

Procedure

All the above settings and configurations have been completed.

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
2. Access the Manage Your Solution App by opening the title.
3. Select Configure Your Solution on Manager Your Solution screen. The Configure Your Solution screen displays.

|  |
| --- |
| Note Select Set Local Version to create country-/region-dependent settings for the intended local version. |

1. Enter Enable Value Chain Types for Combination of Document Type and Item Category in the searching input box and choose enter. The list of Configuration Items is displayed.
2. Choose the Logistics in Configuration Item area, the Configuration Your Solution – Integration with Value Chain Management screen displays.
3. Choose Configure of the Enable Value Chain Types for Combination of Document Type and Item Category, the Enable Value Chain Types for Combination of..: Change screen displays.
4. Select Enable for Combination of Document Type and Item Category from the list below if you want to enable Advanced Intercompany Sales Process for Make-to-Order and Variant Process.

| Sales Order Type | Item Category | Enabled |
| --- | --- | --- |
| OR | CBTC | X |
| OR | CBTN | X |
| CBFD | CBTN | X |

#### Assign Transit Plant to Company Code

Procedure

All the above settings and configurations have been completed.

1. Raise a pre-approved incident using the component XX-S4C-OPR-SRV.
2. Attach this excel with the following data:
    - Assign Transit Plant to Company Code:

| Company Code | Transit Plant |
| --- | --- |
| 1010 |  |
| 1710 |  |

1. Send it to SAP.
2. SAP Cloud Operation will implement How to Guide by considering the customer data above.
3. Test the advanced intercompany sales make-to-order and variant process in quality or test system. Release BCP project to transport the expert configuration to production system once the testing is confirmed.

## Overview Table

The scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction\App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order with Configurable Material (Single Level)](#unique_17) [page ] 17 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Process Sales Order Approval (Optional)](#unique_18) [page ] 21 |  |  | Sales order is approved. |
| [Create Pro Forma F5 Invoice (Optional)](#unique_19) [page ] 21 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F5 type is created. |
| [Manufacturing Steps Production Order Processing](#unique_20) [page ] 22 |  |  |  |
| [Create Delivery](#unique_21) [page ] 24 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Perform Picking](#unique_22) [page ] 25 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Material is picked. |
| [Post Goods Issue](#unique_23) [page ] 26 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Confirm Transfer of Control Dates](#unique_24) [page ] 28 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Transfer of Control Dates are confirmed. |
| [Create Pro Forma F8 Invoice (Optional)](#unique_25) [page ] 30 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F8 type is created. |
| [Create Intercompany Invoice](#unique_26) [page ] 31 | Billing Clerk | Create Billing Documents (F0798) | Billing with IV2 type is created. Intercompany Supplier Invoice is created automatically. |
| [Display Intercompany Supplier Invoice](#unique_27) [page ] 33 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Intercompany Supplier Invoice displays. |
| [Create F2 Invoice](#unique_28) [page ] 34 | Billing Clerk | Create Billing Documents (F0798) | Billing with F2 type is created. |
| [Update Text in Billing Document (Optional)](#unique_29) [page ] 35 | Billing Clerk | Change Billing Documents (VF02) | Change Billing Documents displays. |
| Monitor Intercompany Sales Value Chain |  |  |  |
| [Display Intercompany Sales Value Chain](#unique_30) [page ] 37 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Display Intercompany Purchase Order](#unique_31) [page ] 39 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Display Intercompany Sales Order](#unique_32) [page ] 40 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Display Intercompany Supplier Invoice](#unique_33) [page ] 41 | Internal Sales Representative | Monitor Value Chains (F4854) | Monitor Value Chains displays. |
| [Schedule Resolution of Value Chain Issues (Optional)](#unique_34) [page ] 42 | Internal Sales Representative | Schedule Mass Resolution of Value Chain Issues (F6868) | Application Jobs displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Order with Configurable Material (Single Level)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales order in the selling company, then goods will be directly delivered to the customer from the affiliate company/plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order VA01 . | The Sales Order screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330Choose Continue. | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | Sold-to Party: 33100002Cust. Reference: PO numberDeliver.Plant: <Delivery Plant in another company code>, for example, 1710Plant: <Delivery Plant in another company code>, for example, 1710 |  |  |
| 6 | Enter Characteristic Value | There are two optional ways to configure the characteristic value for the material. You can choose to execute step 6 or 7.In the All Items section, enter the following value and press Enter.Material Number: CM-FL-V00Quantity: for example, 1 PCOn the Variant Configuration screen, select value for characteristics below and choose Done.Lifter Model: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Wheel Type: <Cushion Tires, Pneumatic Tires>Fork Size: <Small, Normal, Large> (If customer-material info record is maintained as described in preliminary step, Small displays as default value.)Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity (Ah) : <50, 80, 140>Note Only when the Power Source is Electrical, can this field be seen.Variant condition: AVC_CWEIGHT by defaultNet Value: Varies according to characteristic value chosenThe combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Normal or LargeVariant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Variant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeCombination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity(Ah): 50 or 80 or 140 (140 only available when fork size is L)Variant condition: AVC_LARGEFORK or AVC_SMALLFORK auto added according to chosen fork sizeOn the Review Availability Check Result screen, choose Apply. | If you choose the following combination, a material variant FG-FL-MV-V00 is hit. Material variant will not be covered in this scope item, and there is another scope item 21D to handle it.Lifter Model: STDPower Source: COMBWheel Type: CFork Size: MCounterweight: 2.000kg |  |
| 7 | Fast Entry of Characteristic Value (Alternative) | Choose Configuration tab and choose Product Fork Lifter for Char. Display. Choose Selection, and the characteristics Lifer Model, Power Source, Wheel Type, Fork Size, Counterweight and Battery Capacity then display in the columns of All Items section.Enter the following entries in All Items section.Material Number: CM-FL-V00Quantity: for example, 1 PCPress Enter. Combustion is defaulted for Power Source.Enter value for Lifer Model, Power Source, Wheel Type, Fork Size, Counterweight, and Battery Capacity.Lifter Model: HVY, STDPower Source: COMB, ELECWheel Type: C, PFork Size: S, M, L (If customer-material info record is maintained as described in preliminary step, S displays as default value.)Counterweight (KG): 1.000, 2.000, 5.000Battery Capacity(Ah): 50, 80, 140Press Enter after entering value for each characteristic and value entered is replaced by value description in each field. Allowed combinations of characteristic values are the same as step 6.Note To change value for characteristics, instead of choosing F4 search help button, manually enter the new value in the field directly. |  |  |
| 8 | Check Pricing | Double-click sales order item and select Condition tab. Pricing of variant components displays.Check the condition value of condition type PPR0.CounterweightThe condition value for Counterweight is calculated by the formula below.Condition value = Sales order quantity * Amount (Unit price) * Char. Value for Counterweight/1000For example, if choose Char. Value 5000KG for Counterweight in Step 6, then Condition value = Sales Quotation quantity * Amount * 5000/1000Small ForkIf choose Char. Value S for Fork Size in step 6, then a minus value for SMALLFORK displays.Large ForkIf choose Char. Value L for Fork Size in step 6, then a value for LARGEFORK displays.Choose Back. |  |  |
| 9 | Enter Tax Departure Country | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 10 | Tax Country/Region | In the Billing section, input country abbeviation that is consistent to Sales Organization.For example, if Sales Organization is 3310, then make the following entry:Tax Departure C / R: AE |  |  |
| 11 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 12 | Check Transit Plant | Choose the line item and choose Display Item Details. Choose Shipping tab, check the value of the field Transit Plant, for example, 3310. | The right Transit Plant displays. |  |
| 13 | Save | Choose Save. | A sales order is created.Make a note of the sales order number. |  |
| 14 | Check Intercompany Purchase Order | Execute the step [Display Intercompany Purchase Order](#unique_31) [page ] 39 to check the Intercompany Purchase Order automatically created by the above sales order. | Intercompany Purchase Order is automatically created successfully. |  |
| 15 | Check Intercompany Sales Order | Execute the step [Display Intercompany Sales Order](#unique_32) [page ] 40 to check the intercompany sales order automatically created by the above sales order. | Intercompany Sales Order is automatically created successfully. |  |

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

### Manufacturing Steps Production Order Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create stock (Sales order stock) for material finished goods CM-FL-V00 .

Procedure

To produce the material and get it into Sales Order stock, execute the following steps described in the Business Process Documentation Test Script of the scope item Make-to-Order Production - Finished Goods Sales and Final Assembly (BJE_US).

| Master Data | Sample Value |
| --- | --- |
| Material | CM-FL-V00 |
| Plant | 1710 |
| Storage Location | 171A |
| Area of Responsibility Production Supervisor | Plant 1 US (1710) MTO VC -Valuated (YB3) |

Refer to Chapter Production Planning in scope item 1YT.

| Step | Step description | Note |
| --- | --- | --- |
| STEP 1 | Material Requirements Planning for Sales Order |  |
| STEP 2 | Create Production Order (CO01) |  |
| STEP 3 | Release Production Orders (CO05N) |  |
| STEP 4 | Pick Components (Picking List) |  |
| STEP 5 | Confirm Assembly Activities |  |
| STEP 6 | Posting Goods Receipt for Production Order | Please make sure finished goods CM-FL-V00 to be posted into storage location 171A. |

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

|  |
| --- |
| Note If error message shows Delivery cannot be created due to running process in ValChainMgm, please log on VCM to monitor Sales Order status. |

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
| 5 | Confirm Internal Transfer of Control Dates and Times | On the top menu, choose Menu > Goto > Header > Shipment , check the field Planned Dates and Time at the screen block Internal Transfer of Control Dates, input new actual date and time in the field Actual Date and Time to reflect the actual case, for example, current System Date and Time.Note This field controls when the goods movement will be posted from Stock in Transit of the delivering company to the selling company. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement one day later than then this date and time. | Internal Transfer of Control Dates are confirmed. |  |
| 6 | Confirm External Transfer of Control Dates | At the screen block External Transfer of Control Dates, check the field Planned Dates and Time, input new actual date and time in the field Actual Date and Time to reflect the actual case, for example, current System Date and Time.Note This field controls when the goods movement will be posted from Stock in Transit of the selling company to customer. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, system will post the goods movement immediately when Goods Issue is posted on the Outbound Delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system will post the goods movement one day later than this date and time. | External Transfer of Control Dates are confirmed. |  |

Financial Posting

Post Goods Issue from Issuing SiT in delivering company

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000 Inventory - Consumption - Trading Goods | 13600000 Inventory - Trading Goods | 51600000 Consumption - Trading Goods |

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
| Trading Good (HAWA) | 51600000 Inventory - Consumption - Trading Goods | 13600000 Inventory - Trading Goods | 51600000 Consumption - Trading Goods |

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
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose the button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Intercompany Invoice (IV2) and maintain billing date, for example current date, then choose button OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________.Note The intercompany supplier invoice is only created automatically by VCM when the intercompany customer invoice has been transferred and released to FI. | The system generates an invoice for billing. |  |
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
| 5 | Select item(s) for billing | Select the row(s) of the SD document created previously and choose Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain the billing date, for example the current date. Then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

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
> Flagged while digesting this document, not verified: Purpose lists only 5D2 and 1YT as required business conditions, but the Business Conditions table also requires scope item BJE (Make-to-Order Production - Finished Goods Sales and Final Assembly) to be activated.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Post Goods Issue expected result says goods issue is posted to Stock in Transit of the delivering company, 'for example, 3310', although 3310 is the selling company and the delivering company is 1710.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-advanced-intercompany-sales-5d2-ae-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 71,946 chars in the whole document
