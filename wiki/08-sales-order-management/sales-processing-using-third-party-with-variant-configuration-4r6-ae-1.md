---
id: 08-sales-order-management/sales-processing-using-third-party-with-variant-configuration-4r6-ae-1
title: Sales Processing using Third-Party with Variant Configuration (4R6_AE) (4R6_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 4R6: third-party sales order with variant-configurable material, prerequisites, preliminary steps and follow-ups."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/third-party-sales]
aliases: [4R6_S4CLD2608_BPD_EN_AE]
keywords: [Third-Party Sales Processing, third-party sales, variant configuration, sales order creation, purchasing info record, purchase price conditions, business roles, master data, item categories, purchase requisition to order]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R6_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1045
topic: 08-sales-order-management/third-party-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Processing using Third-Party with Variant Configuration (4R6_AE) (4R6_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R6_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Third-Party Sales Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sales Processing using Third-Party with Variant Configuration (4R6_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sales Processing using Third-Party with Variant Configuration (4R6_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855408)

[2 Prerequisites 4](#_Toc232855409)

[2.1 System Access 4](#_Toc232855410)

[2.2 Roles 4](#_Toc232855411)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232855412)

[2.4 Business Conditions 7](#_Toc232855413)

[2.5 Preliminary Steps 8](#_Toc232855414)

[2.5.1 Extend Purchasing View for Configuration Material 8](#_Toc232855415)

[2.5.2 Create Purchasing Info Record 9](#_Toc232855416)

[2.5.3 Create Purchasing Price 9](#_Toc232855417)

[2.5.4 Create Characteristic 11](#_Toc232855418)

[2.5.5 Enhance Class 11](#_Toc232855419)

[2.5.6 Enhance Dependencies in the Configuration Profile 12](#_Toc232855420)

[3 Overview Table 14](#_Toc232855421)

[4 Test Procedures 15](#_Toc232855422)

[4.1 Create Sales Order with Configurable Material for 3rd Party Process 15](#_Toc232855423)

[5 Appendix 18](#_Toc232855424)

[5.1 Succeeding Processes 18](#_Toc232855425)

[5.2 Process the following step to finish the order 18](#_Toc232855426)

[5.3 Relevant Processes 19](#_Toc232855427)

## Purpose

Overview

With this process, the standard sales order automatically creates a purchase requisition for the materials to be delivered by third-party vendors.

The purchase requisition is transferred into a purchase order and sent to the vendor.

Once vendors have sent a shipping notification, a statistical goods receipt can be posted. Once this has taken place, customer invoices can be created and issued based on the goods receipt quantities.

After the shipping notification, the invoice receipt is posted based on the invoice sent from vendor.

You can also run the process without shipping notifications. In that case, you can create the customer billing document based on the invoice from the vendor.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER |  |  |  |
| Accounts Payable AccountantAccounts Payable Accountant - Procurement | SAP_BR_AP_ACCOUNTANT SAP_BR_AP_ACCOUNTANT_PROCUREMT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

Manufacturing / Trading

Production Plant

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | CM-FL-V00-3P | Forklift for 3rd Party |  |
| Material | SF-FL-COMB | Forklift Base Combustion Model |  |
| Material | SF-FL-TIRE-CUSH | Forklift Cushion Tire |  |
| Material | SF-FL-ELECTRIC | Forklift Base Electrical Model |  |
| Material | SF-FL-TIRE-PNEU | Forklift Pneumatic Tire |  |
| Material | SF-FL-CWEIGHT | Forklift Counterweight Plate |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

This is a super BOM list for configurable materials. Not all components necessarily used in production order.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| CM-FL-V00-3P | 0 | KMAT | PC | Forklift for 3rd Party |  |

Sales Center

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Organization | 3310 |  | National |
| Distribution Channel | 10 |  | Direct Sales |
| Customer | 33100003 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 2NI | Create Application Group and Characteristic Display - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period (BNZ) master data script. Posting Period is up to date. |
| 22T - Set Up Configurable Model Using Variant Configuration | If you are going to execute 22T with Setup Configurable Model using Variant Configuration Sample Master Data, you must have completed the preliminary step in 22T for CM-FL-V01 material to enable the material for production and sales and distribution process. |

### Preliminary Steps

#### Extend Purchasing View for Configuration Material

Purpose

This section will guide you to create the purchase view for the configuration material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Material . | The Create Material (MM01) displays.. |  |
| 3 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: CM-FL-V00-3PIndustry sector: M | The Select View(s) view displays. |  |
| 4 | Choose Views | In the Select View(s) window, select Purchasing and choose Continue. |  |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant: <Plant code> for example 3310 | The Create Material (Configurable Materials) view displays.You get the following system message at the bottom of the view: The material already exists and will be extended. |  |
| 6 | Save | Choose Save. |  |  |

|  |
| --- |
| Note If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: KMAT - Configurable materials |

#### Create Purchasing Info Record

Purpose

In this activity, you create a Purchase Info Record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose the Create Purchasing Info Record tile. | The Create Info Record: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Supplier: 33300001Material:CM-FL-V00-3PPurchasing Organization:3310Plant: 3310 | The Create Info Record: General Data screendisplays. |  |
| 4 | Enter General Information | Choose Purch.Org. Data 1. | The Create Info Record: Purch. Organization Data 1 screen displays. |  |
| 5 | EnterPurchasing Data | Make the following entries:Delivery Time in Days: 2 DaysPurchasing Group: 002Standard Quantity: 1Tol. Underdl. 10Tol. Overdl : 10Tax Code: V1Net Price : 2200 | Purchasing Data is added. |  |
| 6 | Save your data | Choose Save. | A purchasing info record is saved. |  |

#### Create Purchasing Price

Purpose

In this activity, you create a purchase price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Create Price Conditions. | The Create Condition Records displays. |  |
| 3 | Enter Data | Make the following entries:Condition Type : PPR0. |  |  |
| 4 | Choose Key Combination | Choose Material info Record (Plant-Specific).And choose Enter. |  |  |
| 5 | EnterPurchasing Data | Make the following entries:Supplier : 33300001Material: CM-FL-V00-3PPurch. Organization: 3310Plant: 3310Info Record Category: 0Amount: 2200Exclusion: |  |  |
| 6 | Save your data | Choose Save. | A purchasing info record is saved. |  |

Repeat the step from step 4 to step 7 to create the variant price. For detail input data, please follow below table:

| Condition Type | Key Combination | Supplier | Material | Purch. Org | Info Record Category | Variant | Amount |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PVA0 | Info Record: Variant | 33300001 | CM-FL-V00-3P | 3310 | 0 | AVC_CWEIGHT | 130 |
| PVA0 | Info Record: Variant | 33300001 | CM-FL-V00-3P | 3310 | 0 | AVC_LARGEFORK | 100 |
| PVA0 | Info Record: Variant | 33300001 | CM-FL-V00-3P | 3310 | 0 | AVC_SMALLFORK | -80 |

#### Create Characteristic

Purpose

In this activity, you create the MM characteristic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose the Manage Characteristics tile. | The Characteristics screen displays. |  |
| 3 | Enter Data | Make the following entries:Characteristic: AVC_CR_MMCOMVKOND_VXX |  |  |
| 4 | Maintain Basic Data | Make the following entries:Description: Variant Condition KeyStatus: ReleasedData Type: Character FormatNumber of Chars: 20Case Sensitive: <Selected> |  |  |
| 5 | Enter Additional Data | Make the following entries:Table Name: MMCOMField Name: VKONDNot Ready for input: <Selected>No Display: <Selected> |  |  |
| 6 | Save your data | Choose Save. | Characteristic AVC_CR_MMCOMVKOND_VXX is saved. |  |

#### Enhance Class

Purpose

In this activity, you will enhance the existing class.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose the Manage Classes tile. | The Class screen displays. |  |
| 3 | Enter Data | Make the following entries:Class : AVC_CL_REFCSTC_VXXClass Type:300 |  |  |
| 4 | Maintain Char. Data | Add the following entries:Char. : AVC_CR_MMCOMVKOND_VXX |  |  |
| 5 | Save your data | Choose Save. | Class AVC_CL_REFCSTC_VXX is saved. |  |

#### Enhance Dependencies in the Configuration Profile

Purpose

In this activity, you will enhance the existing dependencies in the configuration profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose the VC Modeling Environment tile. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter Data | Make the following entries:Material : CM-FL-V00-3PClass Type: 300 |  |  |
| 4 | Find dependencies | Expand the object structure tree and find dependencies AVC_OD_CALCPRICECWEIGHT_VXX: |  |  |
| 5 | Choose dependencies | Double click dependencies AVC_OD_CALCPRICECWEIGHT_VXX. Choose Editor and choose Change. |  |  |
| 6 | Update dependencies | Make the following entries:Enter Dependencies as :$self.AVC_CR_SDCOMVKOND_VXX = 'AVC_CWEIGHT',$set_pricing_factor($self, AVC_CR_SDCOMVKOND_VXX, 'AVC_CWEIGHT',AVC_CR_COUNTERWEIGHT_VXX / 1000),$self.AVC_CR_MMCOMVKOND_VXX = 'AVC_CWEIGHT',$set_pricing_factor($self, AVC_CR_MMCOMVKOND_VXX, 'AVC_CWEIGHT',AVC_CR_COUNTERWEIGHT_VXX / 1000). |  |  |
| 7 | Save your data | Choose Save. | Configuration model changes have been saved. |  |

Repeat the step from step 5 to step 8 to update the dependencies. For detail input data, please follow below table:

| Dependency | Constraints |
| --- | --- |
| AVC_OD_CALC01_V00 | $self.AVC_CR_SDCOMVKOND_VXX = 'AVC_LARGEFORK'if AVC_CR_FORKSIZE_VXX = 'L',$self.AVC_CR_MMCOMVKOND_VXX = 'AVC_LARGEFORK'if AVC_CR_FORKSIZE_VXX = 'L'. |
| AVC_OD_CALC02_V00 | $self.AVC_CR_SDCOMVKOND_VXX = 'AVC_SMALLFORK'if AVC_CR_FORKSIZE_VXX = 'S',$self.AVC_CR_MMCOMVKOND_VXX = 'AVC_SMALLFORK'if AVC_CR_FORKSIZE_VXX = 'S'. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order with Configurable Material for 3rd Party Process](#unique_15) [page ] 15 | Internal Sales Representative | Manage Sales Orders (F1873) |  |

## Test Procedures

### Create Sales Order with Configurable Material for 3rd Party Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how a customer buys a forklifter with an individual configuration which is not available on stock and has therefore to be produced individually(at the supplier who could do the production for the VC material).

For selling a material variant of the forklifter which have been produced upfront to selling to customers (make-to-stock), please refer to the scope item 21D.

Characteristics of the forklifter can be configured in an additional screen or directly in the sales order line item. Both ways are described in the test procedures.

|  |
| --- |
| Note In order to process successfully the edocuments for export in EDOC tool, it is necessary to add the destination country in the following SSCUI ID 102473 - Assign Document Types to Billing Types. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders (F1873) screen, select Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order: Initial Screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and press Enter:Sold To party: 33100003Ship To party: 33100003Cust. Reference: Reference number Enter a customer purchase order number as referenceRep. Deliv. Date: <Current date + 5 days> |  |  |
| 6 | Enter Material and Characteristic Value | In the Sales section, enter the following value and choose Enter.Material Number:CM-FL-V00-3PQuantity: for example, 1 PCThe Billing Plan not covered currently.ItCa (Item category): CB1CNoteYou can manually maintain the item category to CB2C if the item is for 3rd party sales order without shipping notification.You can manually maintain the item category to CB3C if the item is free of charge for 3rd party sales order with shipping notification.You can manually maintain the item category to CB4C if the item is free of charge for 3rd party sales order without shipping notification.On the Variant Configuration screen, select value for characteristics below and choose Done.Lifter Model: <Standard>Power Source:<Combustion, Electrical>Wheel Type: Cushion TiresCounterweight: 1.000kgFork Size: Normal |  |  |
| 7 | Maintain Purchase Group - Optional | Make the following entry as below:Purchase group: 001And choose Enter. |  |  |
| 8 | Save Document | Choose Save Document. Make a note of the sales order number: __________. | The order is saved.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable(J59) | Complete the following activities:Posting a Customer Invoice in AccountingOverdue ReceivablesDisplay Customer BalancesManage Customer Line Items |
| Event-Based Production Cost Posting(3F0) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Periodic closing BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html.If you are still using period-end posting, you may need to refer to non-standard Scope Item Period-End Closing – Plant(BEI). |

### Process the following step to finish the order

Purpose

This process step shows you how to process the following step to finish the step with different item category.

Procedure

Optional A: When the sales order creation with item category CB1C or CB3C.

| Test Procedure No. of BD3 | Test Procedure |
| --- | --- |
| 4.8 | Display List of Purchase Requisitions to be Assigned |
| 4.9 | Convert Assigned Requisitions into Purchase Orders |
| 4.17 | Post Statistical Goods Receipt |
| 4.18 | Create Billing Document |
| 4.21 | Create Supplier Invoice |

Optional B: When the sales order creation with item category CB2C or CB4C.

| Test Procedure No. of BDK | Test Procedure |
| --- | --- |
| 4.9 | Display List of Purchase Requisitions to be Assigned |
| 4.10 | Convert Assigned Requisitions to Purchase Orders |
| 4.15 | Create Supplier Invoice |
| 4.17 | Create Billing Document |

|  |
| --- |
| Note In case the Purchase Order send via EDI to the supplier, please check the (EDI, optional) steps in BD3 or BDK, depending on which item category you are using. |

|  |
| --- |
| Note After executing Step Convert Assigned Requisitions into Purchase Orders you can check if the configuration from the sales order has been successfully transferred to the purchase order. In Manage Purchase Orders App, you can click Configuration button on the Standard PO screen to check if the characteristic values from step Create Sales Order have been transferred. |

### Relevant Processes

If the following processes are enabled in your system, you can also test these business processes for the configurable material described in this test script.

| Process |
| --- |
| 1F1 - Debit Memo Processing |
| 1EZ - Credit Memo Processing |
| BKL - Invoice Correction Process with Credit Memo |
| BDQ - Invoice Correction Process with Debit Memo |
| 7TZ - Credit and Debit Memo Processing with Variant Configuration |

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
- related-to :: [[08-sales-order-management/sales-processing-using-third-party-with-shipping-notification-bd3-ae-t]]
- related-to :: [[08-sales-order-management/sales-processing-using-third-party-without-shipping-notification-bdk-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R6_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,909 chars in the whole document
