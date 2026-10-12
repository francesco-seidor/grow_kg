---
id: 10-procurement/test-script-automation-of-source-to-pay-with-sap-business-network-42k
title: "Test Script: Automation of Source-to-Pay with SAP Business Network (42K_AE) (42K_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 42K: source-to-pay with SAP Business Network, covering material, service, enhanced limit and ERS procurement."
cluster: 10-procurement
tags: [kb/procurement, topic/business-network-purchase-to-pay]
aliases: [42K_S4CLD2608_BPD_EN_AE]
keywords: [Purchase-to-Pay Automation with SAP Business Network, source-to-pay automation, sap business network, material procurement, service procurement, enhanced limit purchase order, quick enablement of suppliers, quote automation, evaluated receipt settlement, payment proposals]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42K_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-995
topic: 10-procurement/business-network-purchase-to-pay
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Automation of Source-to-Pay with SAP Business Network (42K_AE) (42K_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42K_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchase-to-Pay Automation with SAP Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Automation of Source-to-Pay with SAP Business Network (42K_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232854380)

[2 Prerequisites 6](#_Toc232854381)

[2.1 Additional Manual Configuration 6](#_Toc232854382)

[2.2 System Access 6](#_Toc232854383)

[2.3 Roles 6](#_Toc232854384)

[2.4 Master Data, Organizational Data, and Other Data 7](#_Toc232854385)

[2.5 Business Conditions 9](#_Toc232854386)

[2.6 Preliminary Steps 9](#_Toc232854387)

[2.6.1 Open New MM Posting Period 9](#_Toc232854388)

[2.6.2 Configure Workflow for Supplier Quotation 9](#_Toc232854389)

[2.6.3 Configure Workflow for Lean Services/Enhanced Limit 11](#_Toc232854390)

[2.6.4 Activate Flexible Workflow for Purchase Orders 12](#_Toc232854391)

[2.6.5 Configure Flexible Workflow for Purchase Order 13](#_Toc232854392)

[3 Overview Table 16](#_Toc232854393)

[4 Test Procedures 21](#_Toc232854394)

[4.1 Material Procurement 21](#_Toc232854395)

[4.1.1 Create Request for Quotation 21](#_Toc232854396)

[4.1.2 Submit Price Quote (as a Supplier in SAP Business Network Discovery) 22](#_Toc232854397)

[4.1.3 Display Supplier Quotation (Optional) 23](#_Toc232854398)

[4.1.4 Award Quote 24](#_Toc232854399)

[4.1.5 Approve Supplier Quotation (Optional) 25](#_Toc232854400)

[4.1.6 Create Purchase Order from Supplier Quotation 26](#_Toc232854401)

[4.1.7 Display Automatically Created Info Record from Award 27](#_Toc232854402)

[4.1.8 Display Automatically Created Purchase Order 28](#_Toc232854403)

[4.1.9 Create Purchase Order with Advanced App (Optional) 29](#_Toc232854404)

[4.1.10 Approve Purchase Order (Optional) 30](#_Toc232854405)

[4.1.11 Display Purchase Order (as a Supplier in SAP Business Network) 31](#_Toc232854406)

[4.1.12 Change Purchase Order (Optional) 32](#_Toc232854407)

[4.1.13 Create Confirmation (as a Supplier in SAP Business Network (Optional)) 33](#_Toc232854408)

[4.1.14 Update Unit Price of Line Item in Purchase Order (as a Supplier in SAP Business Network (Optional)) 34](#_Toc232854409)

[4.1.15 Check Purchase Order Confirmation (Optional) 35](#_Toc232854410)

[4.1.16 Change Confirmation (as a Supplier in SAP Business Network (Optional)) 36](#_Toc232854411)

[4.1.17 Check Purchase Order Confirmation (Optional) 37](#_Toc232854412)

[4.1.18 Create Shipping Notification (as a Supplier in SAP Business Network (Optional)) 38](#_Toc232854413)

[4.1.19 Check Inbound Delivery for Purchase Order (Optional) 39](#_Toc232854414)

[4.1.20 Set Up the Putaway of Goods for Inbound Delivery 40](#_Toc232854415)

[4.1.21 Post Goods Receipt for Inbound Delivery 41](#_Toc232854416)

[4.1.22 Check Goods Receipt Details (Optional) 42](#_Toc232854417)

[4.1.23 Display Goods Receipt (as a Supplier in SAP Business Network) 43](#_Toc232854418)

[4.1.24 Return Goods Receipt for Purchasing Document 44](#_Toc232854419)

[4.1.25 Display Goods Return (as a Supplier in SAP Business Network) 45](#_Toc232854420)

[4.1.26 Cancel Goods Return for Purchasing Document 46](#_Toc232854421)

[4.1.27 Create Supplier Invoice with PO/GR Relation (as a Supplier in SAP Business Network) 47](#_Toc232854422)

[4.1.28 Supplier Invoice Cancellation (Optional) 49](#_Toc232854423)

[4.1.28.1 Check Status of Supplier Invoice 49](#_Toc232854424)

[4.1.28.2 Cancel Supplier Invoice (as a Supplier in SAP Business Network) 49](#_Toc232854425)

[4.1.28.3 Review Supplier Invoice Cancellation 50](#_Toc232854426)

[4.1.29 Create Supplier Invoice with PO/GR Relation (as a Supplier in SAP Business Network) 51](#_Toc232854427)

[4.1.30 Release Supplier Invoice for Payment (Optional) 52](#_Toc232854428)

[4.1.31 Display Invoice Status Change (as a Supplier in the SAP Business Network) 53](#_Toc232854429)

[4.1.32 Single Invoice Payment 54](#_Toc232854430)

[4.1.32.1 Schedule Payment Proposals 54](#_Toc232854431)

[4.1.32.2 Revise Payment Proposal 56](#_Toc232854432)

[4.1.32.3 Release Payment Proposal 58](#_Toc232854433)

[4.1.32.4 Approval by First Approver 59](#_Toc232854434)

[4.1.33 Bank Payment Approval (Optional based on Cash Management) 60](#_Toc232854435)

[4.1.33.1 Approval by First Approver 61](#_Toc232854436)

[4.1.33.2 Approval by Second Approver 62](#_Toc232854437)

[4.1.34 Send Payment Advice to Supplier 63](#_Toc232854438)

[4.1.35 Check the Remittance Advice of the Paid Payment Advice (as a Buyer in SAP Business Network) 64](#_Toc232854439)

[4.1.36 Cancel Payment Advice 65](#_Toc232854440)

[4.1.36.1 Send Payment Advice Cancellation 67](#_Toc232854441)

[4.1.37 Display Canceled Payment Advice 67](#_Toc232854442)

[4.1.38 Check the Remittance Advice of the Canceled Payment Advice (as a Supplier in SAP Business Network) 68](#_Toc232854443)

[4.2 Service Procurement 69](#_Toc232854444)

[4.2.1 Create Lean Services Purchase Order with Advanced App (Optional) 69](#_Toc232854445)

[4.2.2 Approve Purchase Order (Optional) 71](#_Toc232854446)

[4.2.3 Display Purchase Order (as a Supplier in SAP Business Network) 72](#_Toc232854447)

[4.2.4 Create Confirmation (as a Supplier in SAP Business Network (Optional)) 73](#_Toc232854448)

[4.2.5 Update Unit Price of Line Item in Purchase Order (as a Supplier in SAP Business Network (Optional)) 74](#_Toc232854449)

[4.2.6 Check Purchase Order Confirmation (Optional) 75](#_Toc232854450)

[4.2.7 Create Service Entry Sheet (as a Supplier in SAP Business Network (Optional)) 76](#_Toc232854451)

[4.2.8 Check Service Entry Sheet (Optional) 77](#_Toc232854452)

[4.2.9 Update Service Entry Sheet (as a Supplier in SAP Business Network (Optional) 78](#_Toc232854453)

[4.2.10 Check Service Entry Sheet Update (Optional) 79](#_Toc232854454)

[4.2.11 Cancel Service Entry Sheet (as a Supplier in SAP Business Network (Optional)) 80](#_Toc232854455)

[4.2.12 Check Service Entry Sheet Cancellation (Optional) 81](#_Toc232854456)

[4.2.13 Create Service Entry Sheet (as a Supplier in SAP Business Network (Optional)) 82](#_Toc232854457)

[4.2.14 Release Service Entry Sheet 83](#_Toc232854458)

[4.2.15 Create Supplier Invoice with SES Relation (as a Supplier in SAP Business Network) 84](#_Toc232854459)

[4.2.16 Display Invoice 85](#_Toc232854460)

[4.3 Enhanced Limit Purchase Order 86](#_Toc232854461)

[4.3.1 Create Enhanced Limit Purchase Order 86](#_Toc232854462)

[4.3.2 Approve Purchase Order (Optional) 88](#_Toc232854463)

[4.3.3 Display Purchase Order (as a Supplier in SAP Business Network) 89](#_Toc232854464)

[4.3.4 Create Confirmation (as a Supplier in SAP Business Network (Optional)) 90](#_Toc232854465)

[4.3.5 Check Purchase Order Confirmation (Optional) 91](#_Toc232854466)

[4.3.6 Create Service Entry Sheet (as a Supplier in SAP Business Network) 91](#_Toc232854467)

[4.3.7 Check Service Entry Sheet (Optional) 93](#_Toc232854468)

[4.3.8 Release Service Entry Sheet 94](#_Toc232854469)

[4.3.9 Create Supplier Invoice (as a Supplier in SAP Business Network) 94](#_Toc232854470)

[4.3.10 Release Supplier Invoice for Payment (Optional) 95](#_Toc232854471)

[4.3.11 Display Invoice Status Change (as a Supplier in SAP Business Network) 96](#_Toc232854472)

[4.4 Quick Enablement of Suppliers 97](#_Toc232854473)

[4.4.1 Allow Quick Enablement of Suppliers (as a Buyer in SAP Business Network) 97](#_Toc232854474)

[4.4.2 Add Business Partners to the Communication System 98](#_Toc232854475)

[4.4.3 Add Business Partner to the Output Parameter Determination of a Purchase Order 99](#_Toc232854476)

[4.4.4 Add or Update Supplier Email Address 100](#_Toc232854477)

[4.4.5 Create Purchase Order 101](#_Toc232854478)

[4.4.6 Register Supplier 102](#_Toc232854479)

[4.4.7 Display Purchase Order (as a Supplier in SAP Business Network) 103](#_Toc232854480)

[4.4.8 Check Supplier Data (as a Buyer in SAP Business Network) 104](#_Toc232854481)

[4.5 Quick Enablement of Suppliers through Quote Automation 105](#_Toc232854482)

[4.5.1 Allow Quick Enablement of Suppliers (as a Buyer in SAP Business Network) 105](#_Toc232854483)

[4.5.2 Add Business Partners to the Communication System 106](#_Toc232854484)

[4.5.3 Add or Update Supplier Email Address 107](#_Toc232854485)

[4.5.4 Create Request for Quotation 108](#_Toc232854486)

[4.5.5 Register Supplier 110](#_Toc232854487)

[4.5.6 Submit Price Quote (as a Supplier in SAP Business Network Discovery) 111](#_Toc232854488)

[4.5.7 Check Supplier Data (as a Buyer in SAP Business Network) 112](#_Toc232854489)

[4.6 Material Procurement with Evaluated Receipt Settlement 112](#_Toc232854490)

[4.6.1 Create Purchase Order with Advanced App (Optional) 112](#_Toc232854491)

[4.6.2 Approve Purchase Order (Optional) 114](#_Toc232854492)

[4.6.3 Display Purchase Order (as a Supplier in SAP Business Network) 115](#_Toc232854493)

[4.6.4 Post Goods Receipt for Purchasing Document 116](#_Toc232854494)

[4.6.5 Set Up Evaluated Receipt Settlement (ERS) 117](#_Toc232854495)

[4.6.6 Check Supplier Invoice List (Optional) 118](#_Toc232854496)

[4.6.7 Display Invoice (as a Supplier in SAP Business Network) 119](#_Toc232854497)

## Purpose

Overview

This scope item lets you integrate SAP S/4HANA Cloud Public Edition with SAP Business Network for Procurement to connect with suppliers and automate purchase order and payment processing for the procurement of direct or indirect materials and project-based service processes. You can send electronic purchase orders or payment advices to your suppliers and receive electronic order confirmations, advance shipping notices, and invoices from them through SAP Business Network for Procurement.

Digitized collaboration with your suppliers in SAP Business Network for Procurement and the integrated SAP Business Network Commerce Automation helps you speed up procurement to payment processes and to reduce manual process steps, reducing the cost of transactions with your suppliers.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/28d163d9921898cfeda96ba174105572)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Business Network Discovery | Access on [discovery.ariba.com](https://discovery.ariba.com) with the SAP Business Network Buyer and Supplier accounts. Your system administrator provides you with logon data. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor / Supplier | 33300085 | Vendor domestic United Arab Emirates Ariba |  |
| Material | TG0011 | Trading Good for Regular Procurement (PD planning) |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |
| BNG | Free Goods Processing |
| BNM | Free Goods Processing |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J60 - Accounts Payable | Update BP master data with payment method T.Review and complete chapter Invoice Payment Preparation . |
| J78 - Advanced Cash Operations | You have completed the following chapters of the test script:Maintain Payment Approver for Bank AccountsApproval of Bank Transfer |

To run through this scope item, the materials must be available in stock. You can create stock using the Manage Stock (F1062__sap_mmimtype_manage) app or the Transfer Stock - In-Plant (F1061) app in the SAP Fiori launchpad.

### Preliminary Steps

#### Open New MM Posting Period

|  |
| --- |
| Note This is an external process. |

Information on material stock and certain valuation data such as total stock value, total stock, evaluation elements class, price control indicator, and price unit are held by financial posting period. The period must be set up at the beginning of each new posting period to ensure that values and goods movement are posted to the correct period. Usually, only the current posting period is open for posting. All other posting periods are closed.

To close an MM posting period, and open a new posting period, run the procedure described in the Create New Open MM Posting Period - MDS (BNZ) master data script.

#### Configure Workflow for Supplier Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to configure workflows to optimize the approval process for supplier quotations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access App | Open the Manage Workflows for Supplier Quotations (F2704) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Supplier Quotation | Choose Create. On the New Workflow screen, enter a workflow name in the Workflow Name field, for example, Test Workflow for Supplier Quotation.Select the Start Conditions tab. In the Only start the workflow if all of the following preconditions are met: field, select Quotation Document Type from the dropdown list and enter RSI.Select the Steps tab. Choose Create.On the New Step screen, select the Header tab. In the Step Type field, select Release of Supplier Quotation from the dropdown list.Select the Recipients tab and select the following settings:Assignment By: UserUser: Open the Value Help (  ), enter the PURCHASING_MANAGER employee ID in the search field, and choose Go. In the Items section, select an user ID, and choose OK.Step to be completed by: One of the recipientsChoose Create > Save . | The workflow for a supplier quotation is created. |  |
| 4 | Activate Workflow Item | On the Workflow Details screen, select the workflow item that you've created and choose Activate. | The workflow item is activated. |  |

#### Configure Workflow for Lean Services/Enhanced Limit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to configure workflows to optimize the approval process for service entry sheets.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open the Manage Workflows for Service Entry Sheets - Lean Services (F3173) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Supplier Quotation | Choose Create. On the New Workflow screen, enter a workflow name in the Workflow Name field, for example, Automatic Release of Service Entry Sheet.Select the Steps tab. Choose Create.On the New Step screen, select the Header tab. In the Step Type field, select Automatic Release of Service Entry Sheet from the dropdown list.Note The recipients are determined automatically.Choose Create > Save. | The workflow for a supplier quotation is created. |  |
| 4 | Activate Workflow Item | On the Workflow Details screen, select the workflow item that you've created and choose Activate. | The workflow item is activated. |  |

#### Activate Flexible Workflow for Purchase Orders

Use

This procedure describes how to activate the flexible workflow for purchase orders.

Prerequisites

To carry out the following activity, a business user with a business role must exist. The business role must contain the business catalog SAP_CORE_BC_COM (Communication Management), for example, the business role SAP_BR_ADMINISTRATOR (Administrator) is required.

Additionally, the business role SAP_BR_BPC_EXPERT must be assigned to the user

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Your Solution (APS_BCT_SPRO) app. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 4 | Search for Application Area | On the Configure Your Solution: Realize Phase screen, set the following search filters:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement | A search result list is displayed. |  |
| 5 | Select Configuration Item | From the search result list, select the Purchase Order Processing configuration item. | The Configure Your Solution - Purchase Order Processing screen is displayed. |  |
| 6 | Select Configuration Step | On the Configure Your Solution - Purchase Order Processing screen, in the Configuration Steps section, choose Configure for the Activate Flexible Workflow for Purchase Orders configuration step. | The Document Types Purchase order Change screen is displayed. |  |
| 7 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: Select the checkbox. | The scenario-based workflow is active for standard purchase orders.If you’re asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue.Choose Save. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). |  |  |
| 3 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: Select the checkbox. | The scenario-based workflow is active for standard purchase orders.If you’re asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue.Choose Save. |  |

#### Configure Flexible Workflow for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you configure your release conditions for Purchase Order Approval.

|  |
| --- |
| Note Before you start this procedure, ensure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access App | Open the Manage Workflows for Purchase Orders (F2872) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Supplier Quotations | Choose Create. On the New Workflow screen, enter a workflow name in the Workflow Name field, for example, Test Workflow for Purchase Order.Select the Start Conditions tab. In the Only start the workflow if all of the following preconditions are met: field, select Purchasing group of purchase order is from the dropdown list and enter 001.Choose Create Alternative Preconditions and enter the following data:In the Only start the workflow if all of the following preconditions are met: field, select Total net amount of purchase order is greater than from the dropdown list and enter the following data:Amount: 100Currency: USDSelect the Steps tab. Choose Create.On the New Step screen, select the Header tab. In the Step Type field, select Release of Purchase Order from the dropdown list.Select the Recipients tab and select the following settings:Assignment By: RoleRole: Manager of Workflow InitiatorStep to be completed by: One of the recipientsChoose Create > Save . | The workflow for a purchase order is created. |  |
| 4 | Activate Workflow Item | On the Workflow Details screen, select the workflow item that you've created and choose Activate. | The workflow item is activated. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |
| --- |
| Note Only the mandatory chapters that need to be edited manually are displayed in the overview. |

The scope of the section Material Procurement consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Request for Quotation](#unique_14) [page ] 21 | Purchaser | Manage RFQs (F2049) | The workflow for automatic approval of the request for quotation is triggered. After approval, the request for quotation is published. |
| [Submit Price Quote (as a Supplier in SAP Business Network Discovery)](#unique_15) [page ] 22 | Supplier in SAP Business Network Discovery | [discovery.ariba.com](https://discovery.ariba.com/) | The price quote is submitted. |
| [Award Quote](#unique_16) [page ] 24 | Purchaser | Manage Supplier Quotations (F1991) | The automatically created supplier quotation is awarded. |
| [Create Purchase Order from Supplier Quotation](#unique_17) [page ] 26 | Purchaser | Manage Supplier Quotations (F1991) | A purchase order from an automatically created supplier quotation. |
| [Display Automatically Created Info Record from Award](#unique_18) [page ] 27 | Purchasing Manager | Manage Supplier Quotations (F1991) | The automatically created info record is displayed. |
| [Display Automatically Created Purchase Order](#unique_19) [page ] 28 | Purchaser | Manage RFQs (F2049) | The automatically created purchase order is displayed. |
| [Display Purchase Order (as a Supplier in SAP Business Network)](#unique_20) [page ] 31 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The purchase order is displayed. |
| [Set Up the Putaway of Goods for Inbound Delivery](#unique_21) [page ] 40 | Receiving Specialist | Change Inbound Delivery (VL32N) | The putaway of material for inbound delivery is set up. |
| [Post Goods Receipt for Inbound Delivery](#unique_22) [page ] 41 | Warehouse Clerk | Post Goods Receipt for Inbound Delivery (F2502) | The goods receipt for inbound delivery is posted. |
| [Display Goods Receipt (as a Supplier in SAP Business Network)](#unique_23) [page ] 43 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The goods receipt is displayed. |
| [Return Goods Receipt for Purchasing Document](#unique_24) [page ] 44 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for purchasing document is returned. |
| [Display Goods Return (as a Supplier in SAP Business Network)](#unique_25) [page ] 45 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The goods return is displayed. |
| [Return Goods Receipt for Purchasing Document](#unique_24) [page ] 44 | Warehouse Clerk | Post Goods Movement (MIGO) | The previous purchasing document is cancelled for return. |
| [Create Supplier Invoice with PO/GR Relation (as a Supplier in SAP Business Network)](#unique_26) [page ] 47 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice/credit memo is created. |
| [Display Invoice Status Change (as a Supplier in the SAP Business Network)](#unique_27) [page ] 53 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The invoice status change is displayed. |
| [Schedule Payment Proposals](#unique_28) [page ] 54 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | The invoices to be paid are selected and payment proposals are scheduled. The SAP S/4HANA Cloud Public Edition system is updated with the information about the outgoing payment. |
| [Revise Payment Proposal](#unique_29) [page ] 56 | Accounts Payable Accountant | Revise Payment Proposals (F0771) | The payment proposals for the invoices to be paid are revised. |
| [Release Payment Proposal](#unique_30) [page ] 58 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | The payment proposals for the invoices to be paid are released. |
| [Approval by First Approver](#unique_31) [page ] 59 | Accounts Payable Manager | Approve Bank Payments (F0673A) | The payment proposals are approved by the first approver. |
| [Approval by Second Approver](#unique_32) [page ] 62 | Cash Manager | Approve Bank Payments (F0673A) | The payment proposals are approved by the second approver. |
| [Send Payment Advice to Supplier](#unique_33) [page ] 63 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | The payment advice is sent to the supplier in SAP Business Network. |
| [Check the Remittance Advice of the Paid Payment Advice (as a Buyer in SAP Business Network)](#unique_34) [page ] 64 | Buyer in SAP Business Network | [buyer.ariba.com](https://buyer.ariba.com/) | The remittance advice of the paid payment advice is checked. |
| [Cancel Payment Advice](#unique_35) [page ] 65 | Accounts Payable Accountant | Reset Cleared Items (F2223) | The payment advice is cancelled. |
| [Display Canceled Payment Advice](#unique_36) [page ] 67 | Accounts Payable Accountant | Manage Journal Entries (F0717A) | The cancelled payment advice is displayed. |
| [Check the Remittance Advice of the Canceled Payment Advice (as a Supplier in SAP Business Network)](#unique_37) [page ] 68 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The remittance advice of the cancelled payment advice is checked. |

The scope of the section Service Procurement consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Display Purchase Order (as a Supplier in SAP Business Network)](#unique_38) [page ] 72 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The purchase order is displayed. |
| [Release Service Entry Sheet](#unique_39) [page ] 83 | Purchasing Manager | My Inbox - All Items (F0862) | The service entry sheet is released. |
| [Create Supplier Invoice with SES Relation (as a Supplier in SAP Business Network)](#unique_40) [page ] 84 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice/credit memo is created. |
| [Display Invoice](#unique_41) [page ] 85 | Purchaser | Change Purchase Order - Advanced (ME22N) | The invoice document is displayed. |

The scope of the section Enhanced Limit Purchase Order consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Enhanced Limit Purchase Order](#unique_42) [page ] 86 | Purchaser | Manage Purchase Orders (F0842A) | The enhanced limit purchase order is created. |
| [Display Purchase Order (as a Supplier in SAP Business Network)](#unique_43) [page ] 89 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The purchase order is displayed. |
| [Create Service Entry Sheet (as a Supplier in SAP Business Network)](#unique_44) [page ] 91 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The service entry sheet is created. |
| [Release Service Entry Sheet](#unique_45) [page ] 94 | Purchasing Manager | My Inbox - All Items (F0862) | The service entry sheet is released. |
| [Create Supplier Invoice (as a Supplier in SAP Business Network)](#unique_46) [page ] 94 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice is created against the purchase order to be invoiced. |
| [Display Invoice Status Change (as a Supplier in SAP Business Network)](#unique_47) [page ] 96 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The status change of the purchase order is displayed. |

The scope of the section Quick Enablement of Suppliers consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Allow Quick Enablement of Suppliers (as a Buyer in SAP Business Network)](#unique_48) [page ] 97 | Buyer in SAP Business Network | [buyer.ariba.com](https://buyer.ariba.com/) | The quick enablement of suppliers is allowed. |
| [Add Business Partners to the Communication System](#unique_49) [page ] 98 | Administrator | Communication Systems (F1762) | Business Partners are added as allowed partners to the communication system for the quick enablement. |
| [Add Business Partner to the Output Parameter Determination of a Purchase Order](#unique_50) [page ] 99 | Administrator | Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) | Business partners are added as key fields to the output parameter determination of a purchase order for the quick enablement. |
| [Add or Update Supplier Email Address](#unique_51) [page ] 100 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | The email address of the supplier is added or updated. |
| [Create Purchase Order](#unique_52) [page ] 101 | Purchaser | Create Purchase Order - Advanced (ME21N) | A new purchase order is created. |
| [Register Supplier](#unique_53) [page ] 102 | New account on SAP Business Network | After you received a registration email from the SAP Business Network, select the link in the email to activate your account. | A new supplier is registered in the SAP Business Network. |
| [Display Purchase Order (as a Supplier in SAP Business Network)](#unique_54) [page ] 103 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The purchase order is displayed. |
| [Check Supplier Data (as a Buyer in SAP Business Network)](#unique_55) [page ] 104 | Buyer in SAP Business Network | [buyer.ariba.com](https://buyer.ariba.com/) | The data of the newly added supplier is checked. |

The scope of the section Quick Enablement of Suppliers through Quote Automation consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Allow Quick Enablement of Suppliers (as a Buyer in SAP Business Network)](#unique_56) [page ] 105 | Buyer in SAP Business Network | [buyer.ariba.com](https://buyer.ariba.com/) | The quick enablement of suppliers is allowed. |
| [Add Business Partners to the Communication System](#unique_57) [page ] 106 | Administrator | Communication Systems (F1762) | Business partners are added as allowed partners to the communication system for the quick enablement. |
| [Add or Update Supplier Email Address](#unique_58) [page ] 107 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | The email address of the supplier is added or updated. |
| [Create Request for Quotation](#unique_59) [page ] 108 | Purchaser | Manage RFQs (F2049) | The workflow for automatic approval of the request for quotation is triggered. After approval, the request for quotation is published. |
| [Register Supplier](#unique_60) [page ] 110 | New account on SAP Business Network | After you received a registration email from the SAP Business Network, select the link in the email to activate your account. | A new supplier is registered in the SAP Business Network. |
| [Submit Price Quote (as a Supplier in SAP Business Network Discovery)](#unique_61) [page ] 111 | Supplier in SAP Business Network Discovery | [discovery.ariba.com](https://discovery.ariba.com/) | The price quote is submitted. |
| [Check Supplier Data (as a Buyer in SAP Business Network)](#unique_62) [page ] 112 | Buyer in SAP Business Network | [buyer.ariba.com](https://buyer.ariba.com/) | The data of the newly added supplier is checked. |

The scope of the section Material Procurement with Evaluated Receipt Settlement consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order with Advanced App (Optional)](#unique_63) [page ] 112 | Purchaser | Create Purchase Order - Advanced (ME21N) | A new purchase order is created. |
| [Approve Purchase Order (Optional)](#unique_64) [page ] 114 | Purchasing Manager | My Inbox - All Items (F0862) | The purchase order is approved. |
| [Display Purchase Order (as a Supplier in SAP Business Network)](#unique_65) [page ] 115 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The purchase order is displayed. |
| [Set Up Evaluated Receipt Settlement (ERS)](#unique_66) [page ] 117 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | After the goods ordered by a purchase order arrived at the warehouse, the goods receipt is posted. |
| [Check Supplier Invoice List (Optional)](#unique_67) [page ] 118 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs (F1683) | Created goods movements can be settled without receipt of an invoice. The system can create and post the appropriate invoices itself. ERS is especially effective if you create settlement documents periodically. |
| [Display Invoice (as a Supplier in SAP Business Network)](#unique_68) [page ] 119 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The invoice is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Material Procurement

#### Create Request for Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a request for quotation (RFQ) from an existing purchase requisition, and send it to SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage RFQs (F2049) app. | The Manage RFQs screen is displayed. |  |
| 3 | Access New Request for Quotation Screen | On the Manage RFQs screen, choose Create, and from the dropdown list, choose Ext. Price Request. | The New Request for Quotation screen is displayed. |  |
| 4 | Create New Request for Quotation | On the New Request for Quotation screen, enter the required data.On the General Information tab, enter the following data:RFQ Description: <Short description or the title of the RFQ>Note This field is mandatory.Language Key: To select a language key, choose the value help.Quotation Deadline: todayPurchasing Group: 001Purch. Organization: 3310Company Code: 3310On the Delivery and Payment Terms tab, enter the following data:Currency: AEDOn the Items tab, select the newly created RFQ Item and enter the following data:Material: TG0011Material Group: L001Plant: 3310Requested Quantity: 20Delivery date: today + 1 monthInfo Record Update: Select the checkbox.Choose Apply. You’ll return to the New Request for Quotation screen.On the Bidders tab, choose Create, and add one or more bidders, for example, Supplier: 33300085Choose Create. | The new request for quotation is created. |  |
| 5 | Publish Request for Quotation | On the Request for Quotation screen, choose Publish. | The workflow for automatic approval of the request for quotation is triggered. After approval, the request for quotation is published. |  |

#### Submit Price Quote (as a Supplier in SAP Business Network Discovery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to enter your bids as a supplier in SAP Business Network Discovery.

|  |
| --- |
| Note SAP Business Network will wait for the quotation deadline (as set in [Create Request for Quotation](#unique_59) [page ] 108) to pass by before the bid is actually forwarded to the buyer. For example, after entering the bid, you have to wait until the quotation deadline you entered in the RFQ has passed (that would typically be the next day if you set the quotation deadline to today) before you can continue with the test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). |  |  |
| 2 | Display Automated RFQ Overview | Choose Discovery > Matched and Invited Leads .Search for the relevant RFQ and open it. | An overview list of the existing RFQs is displayed. |  |
| 3 | Create Response | Choose Quote all. | The list of all item parts of the RFQ is displayed. |  |
| 4 | Submit Response | For each of the items, enter the following data according to your business requirements:ExamplePrice: 1Shipping cost: 5Choose Submit. | The quote was submitted. |  |

#### Display Supplier Quotation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA Cloud Public Edition system and display the automatically created supplier quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage RFQs (F2049). | The Manage RFQs screen is displayed with a list of existing Request for Quotations items. |  |
| 3 | Search for RFQ | Choose Go.Enter the RFQ number of the RFQ you've created in [Create Request for Quotation](#unique_14) [page ] 21. | In the searach results list, your RFQ is displayed. |  |
| 4 | Open RFQ | Selet the RFQ and open it. |  |  |
| 5 | Display Supplier Quotation | Go to the Quotation tab and view the price quote that was created in [Submit Price Quote (as a Supplier in SAP Business Network Discovery)](#unique_15) [page ] 22. | The price quote is displayed in the Supplier Quotation column. |  |

#### Award Quote

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA Cloud Public Edition system and award the automatically created supplier quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Acccess App | Open the Manage Supplier Quotations (F1991) app. | The Manage Supplier Quotations screen is displayed. |  |
| 3 | Search for Supplier Quotations | To search for a specific supplier quotation, enter the required search criteria. Choose Go. | A search result list with supplier quotations is displayed. |  |
| 4 | Award Supplier Quotation | Select the supplier quotation. Choose Award.To confirm the Send dialog box, choose OK. |  |  |

#### Approve Supplier Quotation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve a supplier quotation.

Prerequisites

It is required that you completed the procedure described in [Configure Workflow for Supplier Quotation](#unique_9) [page ] 9.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox (F0862) app. | The My Inbox screen is displayed. |  |
| 3 | Select Supplier Quotation | To search for a specific supplier quotation, enter the required search criteria in the Search field. Choose Go. | The Supplier Quotation xxx is displayed. |  |
| 4 | Approve the Supplier Quotation | Choose Approve. If needed, enter the approval reason. Choose Submit. |  |  |

#### Create Purchase Order from Supplier Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchase order from an automatically created supplier quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Supplier Quotations (F1991) app. | The Manage Supplier Quotations screen is displayed. |  |
| 3 | Search for Supplier Quotation | In the RFQ field, enter a supplier quotation ID and choose Go. | A search results list is displayed. |  |
| 4 | Display Supplier Quotation | From the search results list, select a supplier quotation. | The supplier quotation is displayed. |  |
| 5 | Create Purchase Order | Choose Follow-On Document > Create Purchase Order > Order . | You've created a purchase order from an automatically created supplier quotation. |  |

#### Display Automatically Created Info Record from Award

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the automatically created info record from award in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Supplier Quotations (F1991) app. | The Manage Supplier Quotations screen is displayed. |  |
| 3 | Search for Supplier Quotation | To search for a specific supplier quotation, enter the required search criteria. Choose Go. | The Supplier Quotation xxx is displayed. |  |
| 4 | Display the Automatically Created Info Record | Select the supplier quotation and open it.Go to the Items tab.On the Items tab, choose Purchasing Info Record. | The automatically created info record is displayed. |  |

#### Display Automatically Created Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the automatically created purchase order in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage RFQs (F2049) app. | The Manage RFQs screen is displayed. |  |
| 3 | Search for RFQ | To search for the RFQ created in [Create Request for Quotation](#unique_14) [page ] 21, enter the required search criteria. Choose Go. | The RFQ xxx is displayed. |  |
| 4 | Display Automatically Created Purchase Order | Select the RFQ and open it. | The automatically created purchase order is displayed.On the Process Flow tab, the Purchase Order No. is displayed. |  |
| 5 | Display More Information about Automatically Created Purchase Order | Open the My Inbox (F0862) app. To display more details, search for the above created Purchase Order No.. |  |  |

#### Create Purchase Order with Advanced App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order Data | In the Header section, enter the following data:Order Type: Standard OrderSupplier: 33300085Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310In the Items section, enter the following data:Material: TG0011Quantity: 100 PCDelivery Date: Today + 1 monthNet Price: 30AEDPlant: 3310Storage Location: 331AIn the Item Details section, enter the following data:On the Confirmations tab, select Conf. Control for confirmations.On the Texts tab, choose Item text to be able to enter specific text for the purchase order on the item details level.Note The following restrictions apply:On the Invoice tab, don't select the ERS checkbox. Otherwise, it won't be possible to create an invoice in SAP Business Network Supplier.On the Delivery tab, don't select the Deliv. Compl. checkbox. Otherwise, it's not possible to create an advanced shipping notification (ASN) in SAP Business Network Supplier for this purchase order.On the Delivery tab, if you enter a value in the Overdeliv. Tol. field, it's not possible to create an advanced shipping notification (ASN) with a higher quantity than requested in this purchase order.If material is batch-managed, you can define the batch number on the Material Data tab. If material is managed with serial numbers, you can define serial numbers to be ordered on the Delivery Schedule tab. |  |  |
| 4 | Attach File to Purchase Order | Choose Services for Object > Create Attachment. Select a file that you want to attach and choose Ok. | A file is attached to a purchase order. |  |
| 5 | Check Purchase Order for Completeness | Choose Check. | If no error dialog box is displayed, the purchase order is complete.If an error dialog box is displayed, review the data of the purchase order, and correct all errors. |  |
| 6 | Save Purchase Order | To save the purchase order, choose Save. | A new purchase order is created. The system message Standard PO created under the number 450000XXXX is displayed.Note Make a note of this purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve a purchase order.

|  |
| --- |
| Note Purchase orders with a net value of 500 USD (global release amount is configured in USD, and converted to the country/region currency amount), or more require an approval (for Purchasing Group 001 and 003). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchasing Manager. |  |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen with a list of already created purchase orders that need to be approved is displayed. |  |
| 3 | Select Purchase Order | To search for a specific purchase order, enter the required search criteria.From the search result list, select a purchase order. | The Purchase Order xxx is displayed.Purchase orders without follow-on documents (w/o status Follow-On Documents), and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Approve the Purchase Order | Choose Approve.If required, enter the approval reason. Choose Submit. |  |  |

#### Display Purchase Order (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select the Purchase Order | Choose Orders > Orders and Releases . Select a Purchase Order ID. | The purchase order is displayed. |  |

#### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed.A list of already created Purchase Orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of a purchase order.On the Purchase Order screen choose Edit. | The Edit Purchase Order xxx screen is displayed. The purchase order is opened in Change mode. |  |
| 4 | Change Purchase Order | Change certain field values of the purchase order according to your business requirements. | The purchase order values are changed. |  |
| 5 | Follow Up on Error Messages | If an error or warning message is displayed, a correction of the purchase order data is necessary. If no message is displayed, the purchase order is complete. |  |  |
| 6 | Save Purchase Order | To save the purchase order, choose Order. | The purchase order is saved. The system message Purchase Order xxx updated. is displayed. |  |

#### Create Confirmation (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Confirm Entire Order . Enter the following data:Supplier Reference:: PO Confirmation for MaterialEst. Delivery Date: <Delivery Date>Choose Next > Submit . | The status of the purchase order is changed to Confirmed. |  |
| 5 | Return to Orders and Releases | To return to the list of purchase orders, choose Done. | The list of purchase orders is displayed. |  |

#### Update Unit Price of Line Item in Purchase Order (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to update the unit price of a line item in a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | On the Home screen, choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Update Line Items .On the Confirming PO screen, enter the following data according to your business requirements:Order Confirmation Header section:Confirmation #: Conf (<Today>)Est. Shipping Date: <Today>Est. Delivery Date: <Today>Line Items section:Confirm: Enter the purchase order quantity.Choose Details. Edit the value of the Unit Price field according to your business requirements.Note If the price difference exceeds the price tolerance limit, the purchase order confirmation will not be processed.Choose OK.On the Confirming PO screen, choose Next > Submit . | The status of the purchase order is changed to Confirmed. |  |
| 5 | Return to Search Results List | To return to the search results list of purchase orders, choose Done. | The search results list is displayed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the purchase order confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen, a list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of the purchase order you created in previous step. | The Standard PO XXX screen is displayed. |  |
| 4 | Open Confirmations | Expand the Item Details section, and go to the Supplier Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network.If you've updated the unit price of a line item in the purchase order as described in [Update Unit Price of Line Item in Purchase Order (as a Supplier in SAP Business Network (Optional))](#unique_76) [page ] 34, review the Expected Value field. | The purchase order confirmation is displayed. |  |

#### Change Confirmation (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the supplier changes the confirmation date in the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane.In the Data Range field, enter Last 24 Hours.Choose Search. | A seach result list of new purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Confirm Entire Order .Enter the following data:Est. Shipping Date: TomorrowEst. Delivery Date: TomorrowChoose Next > Submit . | The status of the purchase order is changed to Confirmed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure you can check the purchase order confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen displayed.A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of a purchase order number you created in [Create Purchase Order from Supplier Quotation](#unique_17) [page ] 26. | The Standard PO XXX screen is displayed. |  |
| 4 | Open Confirmations | Expand the Item Details section. Go to Confirmations. Check the value in the Reference column, to see if the date corresponds with the confirmation date (tomorrow) that you entered for the order confirmation in the SAP Business Network. | The purchase order confirmation is displayed. |  |
| 5 | Check Attached File | Choose Attachment. | The file attached to the puchase order confirmation is displayed. |  |

#### Create Shipping Notification (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a shipping notification in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane.In the Data Range field, enter Last 24 Hours.Choose Search. | A search result list of new purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order displayed. |  |
| 4 | Create Shipping Notification | Choose Create Ship Notice.Enter the following data according to your business requirements:Packing Slip ID: SLIP ##Shipping Date: TodayDelivery Date: TodayTo add attachments, select Choose File in the Header section. Select a file from your computer and choose Add Attachment.Note For the batch-managed materials, enter the batch number in the Supplier Bacth ID field at the item level.Choose Next > Submit . | The status of the purchase order is changed to Shipped. |  |
| 5 | Finish Procedure | Choose Done. | The search result list of purchase orders is displayed again. |  |

#### Check Inbound Delivery for Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to can check if an inbound delivery was created for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed with a list of already created purchase orders. |  |
| 3 | Select Purchase Order | Select the row of the pruchase order you created in [Create Purchase Order from Supplier Quotation](#unique_17) [page ] 26. | The Standard PO XXX screen is displayed. |  |
| 4 | Display Inbound Delivery Number | Expand the Item Details section, and go to the Supplier Confirmations tab. | In the Inb Delivery column, the inbound delivery number is displayed. |  |

#### Set Up the Putaway of Goods for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to set up the putaway of material. When material is put away in the warehouse, it is generally transferred from the goods receipt interim storage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Receiving Specialist. |  |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post a goods receipt, after the goods ordered by a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Access App | Open the Post Goods Receipt for Inbound Delivery (F2502) app.Note If the inbound delivery contains materials with serial numbers, open the Change Inbound Delivery (VL32N) app for goods receipt. | The Post Goods Receipt for Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The inbound delivery is automatically displayed. |  |
| 4 | Enter Delivery Note | On the General Information tab, enter a delivery note in the Delivery Note field. |  |  |
| 5 | Select Item | On the Items tab, select the items for which a goods receipt is to be posted. For each of the selected items, choose Unrestricted-Use from the dropdown list in the Stock Type column. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system message Document created: Material Document <Material Document Number> is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the goods receipt fact sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Material Documents Overview (F1077) app. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | To search for a specific material document, enter the following search criteria:Plant: 3310Purchase Order: <xxx>Choose Go. | On the Material Document Overview screen, the relevant material documents, and material document items are displayed. |  |
| 4 | Select Material Document for Goods Receipt | To view a specfic material document, select the respectiv row. | The list of the material documents, and the goods receipt details are displayed. |  |
| 5 | Check Goods Receipts Details | Check the follwoing fields:StatusGeneral DataMaterial Document Items | The number of reversed items should be 0. In the General Data section, the correct Posting Date, Document Date and the Delivery Note are displayed. |  |
| 6 | Display Document Flow | Go to the Process Flow section. | The Document Flow shows the Purchase Order and the Material Document as a flow chart. |  |

#### Display Goods Receipt (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the goods receipt as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select the Goods Receipt | Choose Orders > Orders and Releases .Select the Receipt Number ID to the corresponding purchase order. | The goods receipt is displayed. |  |

#### Return Goods Receipt for Purchasing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to return goods to the supplier, if they’re defect.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Access App | Open the Post Goods Movement (MIGO) app. | The Goods Receipt Purchase Order screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the following data:Trans./Event: Return DeliveryReference Document: Material DocumentMaterial Document Number: <Material Document Number>Note Use the material document number that has beeen created by posting the goods receipt described i [Post Goods Receipt for Inbound Delivery](#unique_22) [page ] 41.Choose Search (  ).Enter filter criteria based on your requirement. Choose Execute. Double click on the Material document you are searching for. | The data of the goods return are displayed. |  |
| 4 | Enter Quantity | On the Quantity tab, enter the return quantity on the item level in the Qty in Unit of Entry field, for example, 3 PC. |  |  |
| 5 | Check Movement Type and Choose Reason for Movement | On the Where tab, enter the following data:Movement Type: 122Storage Location:331A(for example)Reason for Movement: 0001 |  |  |
| 6 | Select Item | To adopt the item in the document, select the Item OK checkbox. |  |  |
| 7 | Check Document | Choose Check. | The system message Document is OK is displayed. |  |
| 8 | Post Document | Choose Post. | The material document is posted. The system message Material document XXXXXXX posted is displayed. |  |

#### Display Goods Return (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the goods return document as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Search for Purchase Order | Choose Orders > Orders and Releases .Open the Search Filters pane.In the Data Range field, enter Last 24 Hours.Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Check Goods Return Document | In the Related Documents section, select the Material Document Number for the goods return. If not all documents are displayed, choose More. | The Material Document Number for the goods return document is displayed. |  |

#### Cancel Goods Return for Purchasing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to cancel the previous material document for return.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Access App | Open the Post Goods Movement (MIGO) app. | The Goods Receipt Purchase Order screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the following data:Trans./Event: CancellationReference Document: Material DocumentMaterial Document Number: <Material Document Number>Note The material document number was created in [Return Goods Receipt for Purchasing Document](#unique_24) [page ] 44.Choose Execute. | The data of the goods return are displayed. |  |
| 4 | Select Item | To adopt the item in the document, select the Item OK checkbox |  |  |
| 5 | Check Document | Choose Check. | The system message Document is OK is displayed. |  |
| 6 | Post Document | Choose Post. | The material document is posted. The system message Material document XXXXXXX posted is displayed. |  |

#### Create Supplier Invoice with PO/GR Relation (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to select the purchase order to be invoiced and create the supplier invoice against it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order to be Invoiced | Choose Orders > Orders and Releases.Select the purchase order to be invoiced and choose Create Invoice > Standard Invoice.Note To process a service entry sheet, select the desired service entry sheet of the selected purchase order and create the invoice respectively. | The Create Invoice screen is displayed. |  |
| 3 | Enter Invoice Header Data | In the Invoice # field, enter the invoice number.To add an attachment at header level, choose Add Attachment. Select a file from your computer and choose Add to Header > Add Attachment. |  |  |
| 4 | Enter Taxes | In the Tax section, select Line Item Actions > Tax. In the Rate (%) field, enter 0%. Choose Update.If you are asked to enter data in the Tax Category field, please choose Sales Tax. |  |  |
| 5 | Post Supplier Invoice | Choose Next.On the Invoice Submission screen, review the invoice details. Choose Submit. | The supplier invoice is submitted to SAP Business Network. It is also routed to the buyer's SAP S/4HANA Cloud Public Edition system.If the system requires a Remit To ID, choose Invoice Header > View/Edit Addresses. In the Remit To ID field, enter 1000. |  |

#### Supplier Invoice Cancellation (Optional)

##### Check Status of Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the status of the supplier invoice in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Accounts Payable Accountant. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for Supplier Invoices | On the Supplier Invoice List screen, enter the required search criteria to search for a specific supplier invoice. Choose Go. | In the Invoices table, the supplier invoice is displayed. |  |

##### Cancel Supplier Invoice (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to select the purchase order to be invoiced and create the supplier invoice against it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Supplier Invoice to Be Cancelled | Choose Invoices > Invoices .Select your supplier invoice. | The Detail View screen is displayed. |  |
| 3 | Cancel Supplier Invoice | Choose More > Cancel .Approve your cancellation. | The supplier invoice is cancelled. |  |

##### Review Supplier Invoice Cancellation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to review the cancellation of the supplier invoice in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for Supplier Invoices | On the Supplier Invoice List screen, enter the required search criteria to search for a specific supplier invoice. Choose Go. | In the Invoices table, the supplier invoice is displayed. |  |
| 4 | Check Supplier Invoice Status | In the Status column, review whether the supplier invoice is in status Reversed. | The supplier invoice is in status Reversed (received from SAP Business Network). |  |

#### Create Supplier Invoice with PO/GR Relation (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to select the purchase order to be invoiced and create the supplier invoice against it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order to be Invoiced | Choose Orders > Orders and Releases.Select the purchase order to be invoiced and choose Create Invoice > Standard Invoice.Note To process a service entry sheet, select the desired service entry sheet of the selected purchase order and create the invoice respectively. | The Create Invoice screen is displayed. |  |
| 3 | Enter Invoice Header Data | In the Invoice # field, enter the invoice number.To add an attachment at header level, choose Add Attachment. Select a file from your computer and choose Add to Header > Add Attachment. |  |  |
| 4 | Enter Taxes | In the Tax section, select Line Item Actions > Tax. In the Rate (%) field, enter 0%. Choose Update.If you are asked to enter data in the Tax Category field, please choose Sales Tax. |  |  |
| 5 | Post Supplier Invoice | Choose Next.On the Invoice Submission screen, review the invoice details. Choose Submit. | The supplier invoice is submitted to SAP Business Network. It is also routed to the buyer's SAP S/4HANA Cloud Public Edition system.If the system requires a Remit To ID, choose Invoice Header > View/Edit Addresses. In the Remit To ID field, enter 1000. |  |

#### Release Supplier Invoice for Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to release the supplier invoice for payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for Blocked Supplier Invoices | On the Supplier Invoice List, search for your invoice that is in status Blocked for Payment. | If an invoice has been blocked for payment, the Blocked for Payment: Yes system message is displayed. |  |
| 4 | Release the Invoice | Choose Release. | The invoice is released. |  |

#### Display Invoice Status Change (as a Supplier in the SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the updated invoice status as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display Invoice | Choose Outbox > Invoices .Select the invoice related to the purchase order created in [Create Purchase Order from Supplier Quotation](#unique_17) [page ] 26. | The invoice is displayed. |  |
| 3 | Check Invoice Status | The invoice is in status Sent, or Approved. |  |  |
| 4 | Check Supplier Invoice Attachment | If you've attached a document during the supplier invoice creation, go to the Attachment section and check whether the attachment is available. | The attachment is displayed. |  |

#### Single Invoice Payment

Purpose

This section describes how to post payment using the automatic payment program

Prerequisites

Invoices have been posted and are open for payment.

The payment methods to be used have been defined in the Business Partner Master Data. For more information, see the test script of scope item [Accounts Payable (J60)](https://me.sap.com/processnavigator/SolP/J60), chapter Complete Supplier Master Data.

##### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to select the invoices to be paid. When a vendor has been paid directly via an online banking system, you then manually add the information to the SAP S/4HANA Cloud Public Edition system.

Prerequisite

An open invoice is available. For more information, see the [Business Conditions](#unique_7) [page ] 9.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Create Automatic Payment Parameter | To create an automatic payment parameter, choose Create Parameter, and enter the following data:Run Date: <today's date>Identification: <any five character description, such as SPAY1>Choose Create. | The Automatic Payment Parameters screen is displayed. |  |
| 4 | Data Entry | In the Basic section, enter the following data:Posting Date: <today's date>Docs Entered Up To: <today's date>Enable the Additional Log toggle.In the Payment Controls section, enter the following data:Company Code: 3310Note You can use the Value Help ().Next Payment Date: <today's date + 40 days>Note Adjust the date according to payment terms.Payment Method: T, FNote You can use the Value Help ().Note Verify that the payment method is valid in the supplier master record.In the Open Item Section section, enter the following data:Supplier: 33300085Note You can use the Value Help ().If you need to execute a payment for a single invoice, choose Document Number (BKPF-BELNR) from the dropdown list of the Free Selection 1 and enter a document number.Note You can use the Value Help ().Choose Save. | The system message Parameter has been saved is displayed. The status changes to Parameter Created. |  |
| 5 | Schedule Proposal | Choose Schedule > Proposal. | The Schedule Proposal popup window is displayed. |  |
| 6 | Data Entry | On the Schedule Proposal popup window, enter the following data:Start Date: <today's date>Start Immediately: Select the checkbox.Choose Schedule. | The system message Proposal is created is displayed.The status changes to Proposal Created. |  |
| 7 | View Proposal | On the Manage Automatic Payments screen, select the Proposal Processed tab. | A list of processed proposal items is displayed. |  |
| 8 | View Log for Outgoing Payment | On the Manage Automatic Payments screen, select the Proposal Processed tab.In the Log column of your payment run, choose Notes ().Note If the Log column isn’t displayed, choose Settings (). Select the Log checkbox, and choose OK. | The log displays the program's selection. The SAP S/4HANA Cloud Public Edition system is updated with the information about the outgoing payment. |  |

##### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be paid.

|  |
| --- |
| Caution Make sure that there are no other Payment Run Identification Proposals pending to be executed that might be using the same supplier as proposal created in [Schedule Payment Proposals](#unique_28) [page ] 54. If such a payment proposals exist, it must be processed, or deleted. Otherwise no payment proposal is generated for your proposal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Revise Payment Proposals (F0771) app. | The Revise Payment Proposals screen is displayed. |  |
| 3 | Display All Payment Proposals | To display all payment proposals, choose Go. | A list of all payment proposals is displayed. |  |
| 4 | Select a Payment Proposal | To display a specific payment proposal, select the row of a payment proposal, for example, SPAY1. | The Schedule Payment Proposal screen is displayed. |  |
| 5 | Edit Payment Proposal | On the Payments tab, select the rows to edit. Choose Edit Payment. | The Edit Payment dialog box is displayed. |  |
| 6 | Change Field Values of Payment Proposal | To change the payment proposal, update the values of the respective fields according to your business requirements:Payment Method: <Payment Method>House Bank: <House Bank>Account ID: <Account ID>Payee Bank:<Payee Bank>Due Date: <Due Date>To continue, choose OK. |  |  |
| 7 | Process Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You can unblock, or reallocate these payments, and pay them according to your business requirements. |  |  |

##### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to release a payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Display All Payment Proposals | To display all payment proposals, choose Go. | A list of all payment proposals is displayed. |  |
| 4 | Process PaymentProposal | Go to the Proposal Processed tab. |  |  |
| 5 | Select Payment Proposal | Select the row of the payment proposal scheduled in [Schedule Payment Proposals](#unique_28) [page ] 54, for example, SPAY1. | The Schedule Payment dialog box is displayed. |  |
| 6 | Schedule Payment | To schedule a payment, enter the following data:Start Date: <Today's date>Start immediately: Select the checkbox.Choose Schedule. | The system message Payment has been scheduled is displayed. The status changes to Payment Posted. In the log the number of postings, or payments that generated is displayed. |  |
| 7 | View Payment Status | Go to the Payment Processed tab. | The status changes to Payment posted. |  |
| 8 | View Log Postings | Select the row of your Identification payment run. In the Log column, choose Notes.Note If the Log column is not displayed, choose Settings. Select the Log field, and choose OK. | In the log the number of postings that generated is displayed. |  |
| 9 | Close Log Details | Choose OK. | The Log Details dialog box is closed. |  |
| 10 | Payments and Exceptions | In the Open column, choose the Navigation Right Arrow (  ). | A summary of payments and exceptions for the payment run are displayed. |  |
| 11 | Select Information View | You can sort how the information is displayed by Payment Method, Country/Region, and so on. Select the view that suits your needs in the field below Summary. | The information is sorted by your selection. |  |
| 12 | Payments | Choose Payments, or Exceptions. | Details are displayed for generated payments, or exceptions (for example, payment document, payment order, included items, and so on). |  |
| 13 | Payments Navigation | To display line item details of the payment, choose the Navigation Right Arrow (  ) in the Open column.When you are done, choose Back to exit this view. | Payment item details are displayed. |  |

##### Approval by First Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how a payment batch is approved by the first approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Accounts Payable Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Approve Bank Payments (F0673A) app. | The Approve Bank Payments screen is displayed. |  |
| 3 | Review Tab | Go to the For Review tab. |  |  |
| 4 | Review Payment Batch and Items | Review the payment batch and items, to ensure that the batches are correct. |  |  |
| 5 | Select Batch to be Approved | Select the payment batch for approval.If more than one batch needs to be approved, choose Multi-Select. Then select the checkbox for the batches to approve. |  |  |
| 6 | Choose Submit | To submit your changes, choose one of the following options:If you approved only one payment batch, choose Submit.If you approved multiple payment batches, choose Approve Batch. | The Confirm dialog box is displayed. |  |
| 7 | Enter a Note | In the Confirm dialog box, enter the following data:Digital Signature Password: <Logon password for first approver>Note: <Note>Choose OK. | The first approval step is executed. To review it, go to the Processed tab. |  |

#### Bank Payment Approval (Optional based on Cash Management)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In SAP S/4HANA Cloud Public Edition, a SAP Bank Communication Management batch should be approved by two approvers. After the approval process is done, the payment medium is created automatically.

No matter the source of BCM batch, payment run of suppliers/customers, or payment run of bank transfer, the BCM batch should go through the approval process.

|  |
| --- |
| Note If you have implemented outgoing payment with SAP Bank Communication Management approval process (an additional license is required for SAP Bank Communication Management), the approval process is required. |

|  |
| --- |
| Note For more information, see the test script of scope item [Advanced Cash Operations (J78)](https://me.sap.com/processnavigator/SolP/J78). |

Prerequisite

SAP Bank Communication Management batches are created successfully for the payment run of bank transfer.

The approvers’ user ID are maintained on the Payment Signatories tab for the bank account master data. For more information, see the test script of scope item [Advanced Cash Operations (J78)](https://me.sap.com/processnavigator/SolP/J78), chapter Maintain Payment Approver for Bank Accounts.

Procedure

|  |
| --- |
| Note In the test script of scope item [Advanced Cash Operations (J78)](https://me.sap.com/processnavigator/SolP/J78), complete all procedures of chapter Approval of Bank Transfer. |

##### Approval by First Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how a payment batch is approved by the first approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Accounts Payable Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Approve Bank Payments (F0673A) app. | The Approve Bank Payments screen is displayed. |  |
| 3 | Review Tab | Go to the For Review tab. |  |  |
| 4 | Review Payment Batch and Items | Review the payment batch and items, to ensure that the batches are correct. |  |  |
| 5 | Select Batch to be Approved | Select the payment batch for approval.If more than one batch needs to be approved, choose Multi-Select. Then select the checkbox for the batches to approve. |  |  |
| 6 | Choose Submit | To submit your changes, choose one of the following options:If you approved only one payment batch, choose Submit.If you approved multiple payment batches, choose Approve Batch. | The Confirm dialog box is displayed. |  |
| 7 | Enter a Note | In the Confirm dialog box, enter the following data:Digital Signature Password: <Logon password for first approver>Note: <Note>Choose OK. | The first approval step is executed. To review it, go to the Processed tab. |  |

##### Approval by Second Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how a payment batch is approved by the second approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Approve Bank Payments (F0673A) app. | The Approve Bank Payments screen is displayed. |  |
| 3 | Review Tab | Go to the For Review tab. |  |  |
| 4 | Review Payment Batch and Items | Review the payment batch and items, to ensure that the batches are correct. |  |  |
| 5 | Select Batch to be Approved | Select the payment batch for approval.If more than one batch needs to be approved, choose Multi-Select. Then select the checkbox for the batches to approve. |  |  |
| 6 | Choose Submit | To submit your changes, choose one of the following options:If you approved only one payment batch, choose Submit.If you approved multiple payment batches, choose Approve Batch. | The Confirm dialog box is displayed. |  |
| 7 | Enter a Note | In the Confirm dialog box, you can enter a note.Choose OK. | The first approval step is executed. To review it, go to the Processed tab. |  |

#### Send Payment Advice to Supplier

Purpose

A payment advice is automatically generated and sent to buyer and supplier via SAP Business Network.

Prerequisites

Payments have been approved. The Ariba Network Supplier Account ID is created for vendor 33300085

|  |
| --- |
| Note Only execute the following procedure, if the payment advice was not sent to SAP Business Network automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments screen is displayed. |  |
| 3 | Search for a Payment | To search for a specific payment, set the relevant search filters and choose Go. | A search result table is displayed. |  |
| 4 | Select a Payment | Choose the Payments Processed tab. In the search result table, find the payment you want to view by its value in the Identification column.To open a payment, choose Details (  ). | The Paying Company Code: <Paying Company Code> screen is displayed. |  |
| 5 | View Details of Payment | On the Paying Company Code: <Paying Company Code> screen, navigate to the Payments tab.To view detailed information about the payment, choose Details (  ). | The Payment: <Document Number> screen is displayed. |  |
| 6 | Output Items | On the Payment: <Document Number> screen, navigate to the Output Items tab. |  |  |
| 7 | Review the Output Type | On the Output Items tab, check if the status of the PAYM_ADV_EDI output type is Completed. |  |  |
| 8 | Resend Output Item of the Payment | If the status of the PAYM_ADV_EDI output type is not Completed, select the checkbox of the table entry with the PAYM_ADV_EDI output type and choose Resend. | For the table entry with the PAYM_ADV_EDI output type, the status is set to Completed. |  |
| 9 | Finish the Procedure | Choose Back twice. |  |  |

#### Check the Remittance Advice of the Paid Payment Advice (as a Buyer in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the remittance advice of the paid payment advice as a buyer in SAP Business Network.

Prerequisite

The payment advice was approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Buyer on [https://buyer.ariba.com/](https://buyer.ariba.com/). |  |  |
| 2 | View Remittance | Choose Payments > Remittances . | The Remittances screen is displayed.In the Remittances table, the remittance advice for the paid payment advice is displayed with the status Paid. |  |
| 3 | View Details of Remittance Advice | In the Remittances table, select the relevant remittance by clicking on the transaction number to view all details. | The Remittance Advice: <Transaction Number> (Paid) screen is displayed. |  |

#### Cancel Payment Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to cancel the already created payment advice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Reset Cleared Items (F2223) app. | The Reset Cleared Items screen is displayed. |  |
| 3 | Search for Clearing Journal Entry | On the Reset Cleared Items screen, enter the following search criteria:ExampleClearing Journal Entry: Enter the number of the clearing document that you got in [Release Payment Proposal](#unique_30) [page ] 58.Company Code: 3310Fiscal Year of Clearing Journal Entry: 2017To start the search, choose Go. | A search result list is displayed. |  |
| 4 | Select Clearing Journal Entry | From the search result list, select a clearing journal entry. | The Clearing Entry screen is displayed. |  |
| 5 | Reset or Reset and Reverse Clearing Journal Entry | On the Clearing Entry screen, choose Reset or Reset and Reverse as required. | Depending on your selection, one of the following results is expected:If you chose Reset, the system message Success - Clearing <Journal Entry Number> reset is displayed.If you chose Reset and Reverse, the Reverse Journal Entry dialog box is displayed. |  |
| 6 | Enter Details for Reverse Journal Entry | In the Reverse Journal Entry dialog box, enter the following data:ExampleReversal Reason: Select a reason from the dropdown list.Posting Date: MM/dd/yyyyPeriod: <Period>Choose OK. | A message is displayed mentioning that clearing has been reset.The system message Document <Journal Entry Number> was posted in company code <Company Code>. |  |

##### Send Payment Advice Cancellation

Purpose

The payment cancellation is automatically sent to the other system.

Prerequisites

The payment advice needs to be available and canceled by the user.

Procedure

This step is automatically generated.

#### Display Canceled Payment Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the canceled payment advice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Journal Entries (F0717A) app. | The Manage Journal Entries screen is displayed. |  |
| 3 | Search for Journal Entry | On the Manage Journal Entries screen, enter the journal entry of the payment created in [Single Invoice Payment](#unique_89) [page ] 54.Choose Go. | A search result list is displayed. |  |
| 4 | Manage Journal Entry | From the search result list, select a journal entry by clicking on the journal entry number. Choose Manage Journal Entry. | The details of the journal entry are displayed. |  |
| 5 | Choose Line Items | In the Line Items section, select a Posting View Item. | The details of the posting view item are displayed. In the Output Details section, it’s displayed whether the payment advice cancellation (PAYM_ADV_CANCELLATION) is successfully sent or not. |  |
| 6 | Show Application Log | In the Output Details section, select an entry. Then choose Show Application Log. | The application log displays all the processing details of the message. |  |

#### Check the Remittance Advice of the Canceled Payment Advice (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the remittance advice of the canceled payment advice as a supplier in SAP Business Network.

Prerequisite

The payment advice was canceled in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [https://supplier.ariba.com/](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | View Remittance | Choose Payments > Remittances. | The Remittances screen is displayed.In the Remittances table, the remittance advice for the canceled payment advice is displayed with the status Canceled. |  |
| 3 | View Details of Remittance Advice | In the Remittances table, select the relevant remittance by clicking on the transaction number to view all details. | The Remittance Advice: <Transaction Number> (Canceled) screen is displayed. |  |

### Service Procurement

#### Create Lean Services Purchase Order with Advanced App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a lean services purchase order.

Using the advanced app, you are able to see the confirmation and inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | In the Header section, enter the following data:Order Type: Standard OrderSupplier: 33300085Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310Payment Terms: 0003In the Items section, enter the following data:Item - 10Account Assignment Category: KShort Text : Software DevelopmentQuantity: 100 HRDelivery date: Today + 1 monthNet Price: 30 AEDPlant: 3310Service Start Date : First day of the current monthService End Date : Last day of the next monthIn the Item Details - Material Data section, enter the following data:Material group : P001Product Type Group : 2 (service)In the Item Details - Invoice section, enter the following data:Select Invoice ReceiptSelect GR based IVIn the Item Details - Account Assignment section, enter the following data:G/L Account: 65001000Cost Center: 33101101In the Item Details - Confirmations section, enter the following data:Conf Control: Confirmations |  |  |
| 4 | Check Purchase Order for Completeness | Choose Check. | If a dialog box is displayed, you need to correct the errors of the purchase order. Continue with step 5.If no dialog box is displayed, the purchase order is complete. Continue with step 6. |  |
| 5 | Correct Errors | Choose Display Messages. Check the entries for errors and correct them. | Errors of the purchase order are corrected. |  |
| 6 | Save Purchase Order | Choose More > Purchase Order > Save. | A new purchase order is created. The system message Standard PO created under the number 450000XXXX is displayed. Make a note of the purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure you approve a purchase order.

|  |
| --- |
| Note Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country currency amount), or more require an approval (for Purchasing Group 001 and 003). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Approve Purchase Order | Open the My Inbox (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders that need to be approved is displayed. |  |
| 3 | Select Purchase Order | To search for a specific purchase order, enter the required search criteria, for example, the purchase order number. | The Purchase Order xxx is displayed.Purchase orders without follow-on documents (w/o status Follow-On Documents), and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Approve the Purchase Order | Choose Approve.If required, enter the approval reason. Choose Submit. |  |  |

#### Display Purchase Order (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select the Purchase Order | Choose Orders > Orders and Releases . Select the Purchase Order ID. | The purchase order is displayed. |  |

#### Create Confirmation (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Confirm Entire Order . Enter the following data:Supplier Reference:: PO Confirmation for MaterialEst. Delivery Date: <Delivery Date>Choose Next > Submit . | The status of the purchase order is changed to Confirmed. |  |
| 5 | Return to Orders and Releases | To return to the list of purchase orders, choose Done. | The list of purchase orders is displayed. |  |

#### Update Unit Price of Line Item in Purchase Order (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to update the unit price of a line item in a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | On the Home screen, choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Update Line Items .On the Confirming PO screen, enter the following data according to your business requirements:Order Confirmation Header section:Confirmation #: Conf (<Today>)Est. Shipping Date: <Today>Est. Delivery Date: <Today>Line Items section:Confirm: Enter the purchase order quantity.Choose Details. Edit the value of the Unit Price field according to your business requirements.Note If the price difference exceeds the price tolerance limit, the purchase order confirmation will not be processed.Choose OK.On the Confirming PO screen, choose Next > Submit . | The status of the purchase order is changed to Confirmed. |  |
| 5 | Return to Search Results List | To return to the search results list of purchase orders, choose Done. | The search results list is displayed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen, a list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of the purchase order you created in previous step. | The Standard PO XXX screen is displayed. |  |
| 4 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network.If you've updated the unit price of a line item in the purchase order as described in [Update Unit Price of Line Item in Purchase Order (as a Supplier in SAP Business Network (Optional))](#unique_96) [page ] 74, review the Expected Value field. | The purchase order confirmation is displayed. |  |

#### Create Service Entry Sheet (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a service entry sheet as a supplier in SAP Business Network.

|  |
| --- |
| Note This is only relevant for lean services purchase orders. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed |  |
| 4 | Create Service Sheet | Choose Create Service Sheet.In the Header section, enter the following data:Service Sheet #: SE1Servcie Sheet Date: TodayService Start Date: Today + 5Service End Date: Today + 10 (Enter the day before the delivery date in the purchase order.)Approver: TSApprover Mail ID: TStest@sap.comTo add an attachment at header level, choose Add Attachment. Select a file from your computer and choose Add Attachment.In the Service Line Items section, enter the following data:Service Start Date: Enter the same value as in the Header section.Service End Date: Enter the same value as in the Header section.Choose Save > Next > Submit . | The status of the purchase order is changed to Serviced. |  |

#### Check Service Entry Sheet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure decribes how to check a service entry sheet in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets - Lean Services (F2027) app.If an approval workflow is already configured, please follow the approval process. | The Manage Service Entry Sheets screen displayed. |  |
| 3 | Select Service Entry Sheet | Select the row for a service entry sheet number that you've created in [Create Service Entry Sheet (as a Supplier in SAP Business Network (Optional))](#unique_98) [page ] 76. | The Service Entry Sheet Details screen is displayed. |  |

#### Update Service Entry Sheet (as a Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to update a rejected service entry sheet as a supplier in SAPBusiness Network. These steps are applicable only if a manual workflow for LeanServices/Enhanced Limit has been configured, and the service entry sheet has beenmanually rejected in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display the Service Entry Sheet | Choose Fulfillment > Service Sheets. | A search results list with service entry sheets is displayed.To expand the search results list, choose View All in Order. |  |
| 3 | Update Service Entry Sheet | Select a service entry sheet.Select the Edit and Resubmit button.Update some of the fields in the Header section according to your business requirements:ExampleService Start Date: Today + 5Service End Date: Today + 10 (Enter the day before thedelivery date in the purchase order.)Choose Save > Next > Submit. | The service entry sheet is updated. |  |

#### Check Service Entry Sheet Update (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure decribes how to check a service entry sheet in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets - Lean Services (F2027) app.If an approval workflow is already configured, please follow the approval process. | The Manage Service Entry Sheets screen displayed. |  |
| 3 | Select Service Entry Sheet | Select the row for a service entry sheet number that you've created in [Create Service Entry Sheet (as a Supplier in SAP Business Network (Optional))](#unique_98) [page ] 76. | The Service Entry Sheet Details screen is displayed. |  |

#### Cancel Service Entry Sheet (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to cancel an approved service entry sheet as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display the Service Entry Sheet | Choose Fulfillment > Service Sheets . | A search result list with service entry sheets is displayed.To expand the search result list, choose View All in Order. |  |
| 3 | Cancel Service Entry Sheet | Select a service entry sheet. | The Detail View screen is displayed. |  |
| 4 | Cancel Service Entry Sheet | Choose More > Cancel .Approve your cancellation. | The service entry sheet is cancelled. |  |

#### Check Service Entry Sheet Cancellation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check a service entry sheet cancellation in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad of your SAP S/4HANA Cloud Public Edition system as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets - Lean Services (F2027) app. | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Cancelled Service Entry Sheet | To search for a cancelled service entry sheet, enter the required search criteria, for example, the service entry sheet number. | The service entry sheet is displayed with status Deleted. |  |
| 4 | Access App | Open the Change Purchase Order - Advanced (ME22N) app. | The Display Purchase Orders screen is displayed. |  |
| 5 | Select Purchase Order | Choose Other Purchase Order. Enter a purchase order number. Choose Other Document. | The purchase order is displayed. |  |
| 6 | Check Availability of Service Entry Sheet | Choose Item Details > Purchase Order History. | The service entry sheet with quantity and cost equal 0 is added as a new line.A new service entry sheet can be created for the particular purchase order. |  |

#### Create Service Entry Sheet (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a service entry sheet as a supplier in SAP BusinessNetwork.

|  |
| --- |
| Note This is only relevant for lean services purchase orders. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, chooseLast 24 Hours from the dropdown list. Choose Search. | A list of newly created purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed |  |
| 4 | Create Service Sheet | Choose Create Service Sheet.In the Header section, enter the following data:Service Sheet #: SE1Servcie Sheet Date: TodayService Start Date: Today + 5Service End Date: Today + 10 (Enter the day before thedelivery date in the purchase order.)Approver: TSApprover Mail ID: TStest@sap.comSelect field Final ServiceSheet.Note If youselect the field Final ServiceSheet, it is not possible to createfurther service sheets for the same service lineitems.In the Service Line Items section, enter the following data:Service Start Date: Enter the same value as in the Headersection.Service End Date: Enter the same value as in the Headersection.Choose Save > Next > Submit. | The status of the purchase order is changed to Serviced. |  |

#### Release Service Entry Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to release a service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Acccess App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created service entry sheets that need to be approved is displayed. |  |
| 3 | Select Service Entry Sheet | To search for a specific purchase order, enter the required search criteria, for example, the purchase order number. | A search result list with the service entry sheets for the entered purchase order number is displayed. |  |
| 4 | Approve the Service Entry Sheet | Choose Release.If required, enter an approval reason. Choose Submit. |  |  |

#### Create Supplier Invoice with SES Relation (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to select the purchase order to be invoiced and create the supplier invoice against it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order to be Invoiced | Choose Orders > Orders and Releases .Select the purchase order to be invoiced and choose Create Invoice > Standard Invoice.Note To process a service entry sheet, select the desired service entry sheet of the selected purchase order and create the invoice respectively. | The Create Invoice screen is displayed. |  |
| 3 | Enter Invoice Header Data | In the Invoice # field, enter the invoice number. |  |  |
| 4 | Enter Taxes | On the Tax tab, enter 0% in the Rate (%) field. Choose Update.If you are asked to enter data in the Category field, please choose Sales Tax. |  |  |
| 5 | Post Supplier Invoice | Choose Next.On the Invoice Submission screen, review the invoice details. Choose Submit. | The supplier invoice is submitted to SAP Business Network. It is also routed to the buyer's SAP S/4HANA Cloud Public Edition system.If the system requires a Remit To ID, choose Invoice Header > View/Edit Addresses. In the Remit To ID field, enter 1000. |  |

#### Display Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the invoice that was created in the Ariba Supplier system in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Purchase Order - Advanced (ME22N) app. | The Change Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Chhoose Other Purchase Order and enter the purchase order number. Choose Other Document. | The ppurchase order is displayed. |  |
| 4 | Display Invoice | Choose Item Detailes > Purchase Order History.In the Material Document column, the invoice number is displayed. To open the invoice, select the invoice number. | The invoice document is displayed. |  |

### Enhanced Limit Purchase Order

#### Create Enhanced Limit Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create an enhanced limit purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori Launchpad as Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Enter Purchase Order Data | Choose Create.On the General Information tab, in the Basic Data section, enter the following data:Purchase Order Type: Standard PO (NB)Supplier: 33300085Currency: AEDOn the General Information tab, in the Organization section, enter the following data:Purchasing Group: 001Purchasing Organization: 3310Company Code: 3310Expected Value: 10000 AEDOverall Limit: 12000 AEDAccount Assignment Category: Cost Center(K)Product Type Group: Service (2)Note If Materials (1) is entered as product type group, based on the invoice a purchase order can directly be created without a service entry sheet.Plant: 3310To see further details of the line item, choose  . The Purchase Order Item screen is displayed.On the Supplier Confirmation Control tab, enter the following data:Confirmation control: Confirmation (Select the checkbox.)On the Process Flow tab, enter the following data:Goods receipt: Set (Select the checkbox.)On the Schedule Flow tab, select the checkbox for Schedule Line Item - 1, and enter the following data:Start of Performance Period: <Today - 10 Days>End of Performance Period: <Today + 10 Days>On the Account Assignment tab, select the checkbox for Account Assgmt No. - 1, and enter the following data:G/L Account: 65001000To see further details of the account assignment, choose  . The Purchase Order Item Account Assignment screen is displayed.On the General Information tab, enter the following data:Cost Center: 33101101Note You can add attachments at the item or at the header level. These attachments are then available in SAP Business Network Supplier. |  |  |
| 4 | Create Enhanced Limit Purchase Order | Choose Apply > Apply > Order . | If no error message is displayed, the enhanced limit purchase order is complete.If a dialog box is displayed, a correction of the entries must be made to correct the purchase order. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve a purchase order.

|  |
| --- |
| Note Purchase orders with a net value of 500 USD (global release amount is configured in USD, and converted to the country/region currency amount), or more require an approval (for Purchasing Group 001 and 003). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchasing Manager. |  |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen with a list of already created purchase orders that need to be approved is displayed. |  |
| 3 | Select Purchase Order | To search for a specific purchase order, enter the required search criteria.From the search result list, select a purchase order. | The Purchase Order xxx is displayed.Purchase orders without follow-on documents (w/o status Follow-On Documents), and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Approve the Purchase Order | Choose Approve.If required, enter the approval reason. Choose Submit. |  |  |

#### Display Purchase Order (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display the Purchase Order | Choose Orders > Orders and Releases , and select the respective Purchase Order ID. | The purchase order is displayed. |  |

#### Create Confirmation (as a Supplier in SAP Business Network (Optional))

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how the supplier confirms the purchase order in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, choose Last 24 Hours from the dropdown list. Choose Search. | A search result list with purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Confirm Purchase Order | Choose Create Order Confirmation > Confirm Entire Order . In the Confirmation # field, enter PO Confirmation for Service.Choose Next > Submit . | The status of the purchase order is changed to Confirmed. |  |
| 5 | Return to Orders and Releases | To return to the list of purchase orders, choose Done. | The search result list of purchase orders is displayed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | On the Manage Purchase Orders screen, a list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Select the row of the purchase order you created in [Create Enhanced Limit Purchase Order](#unique_42) [page ] 86. | The Standard PO XXX screen is displayed. |  |
| 4 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation number as the order confirmation number in the SAP Business Network. | The purchase order confirmation is displayed. |  |

#### Create Service Entry Sheet (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how the supplier creates a service entry sheet in SAP BusinessNetwork that won’t be sent to SAP S/4 HANA Cloud.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Orders > Orders and Releases .Open the Search Filters pane. In the Date Range field, chooseLast 24 Hours from the dropdown list. Choose Search. | A list of new purchase orders is displayed. |  |
| 3 | Display Purchase Order | To display a purchase order, select the respective purchase order number. | The purchase order is displayed. |  |
| 4 | Create Service Sheet | Choose Create Service Sheet and enter the following data:Service Sheet #: SE1Service Sheet Date:<Today>Service Start Date:<Today + 5>Service End Date:<Today + 10> (One daybefore the delivery date of the purchase order)Service Description: Software DevelopmentApprover:TSApprover Mail ID:TStest@sap.comNote If you select the fieldFinal Service Sheet, it is notpossible to create further service sheets for the sameservice line items.In the Service Entry Sheet Lines section, choose Add > Add Unplanned Item. Enter the following data:Qty: 1 HURPrice: 800AEDStart Date: <Today + 5>End Date: <Today + 10>Choose Save > Next > Submit. | The status of the purchase order is changed to Serviced. |  |

#### Check Service Entry Sheet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure decribes how to check a service entry sheet in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets - Lean Services (F2027) app.If an approval workflow is already configured, please follow the approval process. | The Manage Service Entry Sheets screen displayed. |  |
| 3 | Select Service Entry Sheet | Select the row for a service entry sheet number that you've created in [Create Service Entry Sheet (as a Supplier in SAP Business Network (Optional))](#unique_98) [page ] 76. | The Service Entry Sheet Details screen is displayed. At the header level, the attachment is displayed. |  |

#### Release Service Entry Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure you release a service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created service entry sheets that need to be approved is displayed. |  |
| 3 | Select Service Entry Sheet | To search for a specific purchase order, enter the required search criteria, for example, the purchase order number. | A search result list with service entry sheets for the entered purchase order number is displayed. |  |
| 4 | Release the Service Entry Sheet | Choose Release.If required, enter an approval reason. Choose Submit. |  |  |

#### Create Supplier Invoice (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to select the purchase order to be invoiced and create the supplier invoice against it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select the Purchase Order to Be Invoiced | Choose Orders > Orders and Releases . Select the purchase order to be invoiced and choose Create Invoice > Standard Invoice . | The Create Invoice screen is displayed. |  |
| 3 | Enter Invoice Header Data | In the Invoice # field, enter the invoice number. |  |  |
| 4 | Enter Taxes | On the Tax tab, enter 0% in the Rate (%) field. Choose Update.If you are asked to enter data in the Category field, please choose Sales Tax. | The Invoice Submission screen is displayed. |  |
| 5 | Post Invoice | On the Invoice Submission screen, review the invoice details and choose Submit. | The invoice is submitted to SAP Business Network. It’s routed to the buyer's SAP S/4HANA Cloud Public Edition system.If the system requires a Remit To ID, choose Invoice Header > View/Edit Addresses, and enter the value 1000 in the Remit To ID field. |  |

#### Release Supplier Invoice for Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to release a supplier invoice for payment in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad of your SAP S/4HANA Cloud Public Edition system as a Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for Blocked Supplier Invoices | On the Supplier Invoice List sscreen, search for your invoice that is in status Blocked for Payment. | If an invoice has been blocked for payment, a Blocked for Payment: Yes system message is displayed. |  |
| 4 | Release the Invoice | Choose Release. | The invoice is released. |  |

#### Display Invoice Status Change (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the status of the update of the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display Invoice | Choose Invoices > Invoices .Select the invoice related to the previously created purchase order number. | The supplier invoice is displayed. |  |
| 3 | Check Invoice Status | The invoice status should be Sent, or Approved. |  |  |

### Quick Enablement of Suppliers

The following chapters describe the process for quick enablement of a supplier, triggered by a purchase order.

For a supplier who is available in SAP S/4HANA Cloud Public Edition, but not in SAP Business Network, the process triggers onboarding of the supplier to SAP Business Network, so that the supplier can be used in a commerce automation process.

Some steps have to be processed before a purchase order can be sent to SAP Business Network. For example, you need to add or update the supplier email address that then triggers the invitation and registration process for the supplier in SAP Business Network.

|  |
| --- |
| Note The steps in this section are optional and must be performed only once for the respective supplier. If your business partner has been added to the communication system and to the output parameter determination of a purchase order and if the respective e-mail address has been added to the supplier master data, you can skip the complete section. |

#### Allow Quick Enablement of Suppliers (as a Buyer in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to allow quick enablement of suppliers through purchase orders, payment proposals, CC invoices, and invoices without purchase order as a buyer in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Buyer on [https://buyer.ariba.com](https://buyer.ariba.com). |  |  |
| 2 | Allow Quick Enablement | Choose Profile > Settings > Transactions > Default Transaction Rules . In the Quick Enablement Rules section, select the Allow Quick Enablement checkbox.Choose Save. | The quick enablement of suppliers is allowed. |  |

#### Add Business Partners to the Communication System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to add business partners as allowed partners to the communication system for the quick enablement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Access App | Open the Communication Systems (F1762) app. | The Communication Systems screen is displayed. |  |
| 3 | Search Communication System | To search for a communication system, set the relevant search filters, and choose Go. | A list of communication systems is displayed. |  |
| 4 | Select Communication System | Select a communication system and navigate to the Business Partners tab. Choose Add (  ). | The Add Business Partner popup window is displayed. |  |
| 5 | Add Business Partner to Communication System | In the Add Business Partner popup window, select a business partner. Choose Select . | The business partner is added to the communication system for the quick enablement. |  |

#### Add Business Partner to the Output Parameter Determination of a Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to add business partners as key fields to the output parameter determination of a purchase order for the quick enablement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Access App | Open the Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app. | The Output Parameter Determination screen is displayed. |  |
| 3 | Determination Step: Channel | In the Select Business Rules section, enter the following data:Show Rules for: From the dropdown list, select Purchase Order.Determination Step: From the dropdown list, select Channel. | After a short processing time, all details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules for Channel | In the Maintain Business Rules section, choose Edit. In the Table Contents section, search for the table row with the value EDI in the Channel column.In that table row, select the value of the Recipient column.Choose Change > Insert Include Condition . Enter a business partner as recipient.To confirm the entered value, choose OK. |  |  |
| 5 | Activate Channel | In the Maintain Business Rules section, choose Activate (Ctrl + A). | The system message Objects saved and activated is displayed. |  |

#### Add or Update Supplier Email Address

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to add or update the email address of the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Supplier Master Data (F1053A) app. | The Manage Supplier Master Data screen is displayed. |  |
| 3 | Search for Business Partner | To search for the supplier, enter a business partner ID.Tip You can use the value help (  ), to select the correct data.Choose Go. | In the search result list, the supplier is displayed. |  |
| 4 | Select Supplier | To add or update the data of the supplier, select the supplier. | The Supplier screen is displayed. |  |
| 5 | Select Supplier Address | On the Supplier screen, choose Address > Address Details .Select the address that has the value Yes in the Standard column. | The Address Details screen is displayed. |  |
| 6 | Add or Update Email Address | On the Address Details screen, choose Communication > Email .Add or update an email address. In the Standard column, select the checkbox.Choose Apply > Save . | The email address is added or updated, and is set as standard. |  |

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori Launchpad as Purchaser. |  |  |
| 2 | Access App | Open the Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order Data | On the Create Purchase Order screen, enter the following data:Order Type: Standard OrderVendor: <Vendor Number for Quick Enablement>Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310 |  |  |
| 4 | Enter Purchase Order Item Data | For Item 10, enter the following data:Material: TG0011Quantity: 10 PCDelivery date: Today + 1 monthNet Price: 17.55AEDPlant: 3310Storage Location: 331AConf Control: Confirmations |  |  |
| 5 | Check Purchase Order for Completeness | Choose Check. | If no error dialog box is displayed, the purchase order is complete .If an error dialog box is displayed, correct the data of the purchase order. |  |
| 6 | Correct Issues | Choose Display Messages.Check for errors and correct the data. |  |  |
| 7 | Save Purchase Order | To save the purchase order, choose More > Purchase Order > Save. | A new purchase order is created. The system message Standard PO created under the number 450000XXXX is displayed.Make a note of the purchase order number. |  |

#### Register Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to register a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive Registration Email | After you received a registration email from SAP Business Network, select the link in the email to activate your account. |  |  |
| 2 | Register Supplier | Enter a temporary ID and a secure code. If you're asked to check for existing accounts, continue with the creation of a new account.Tip Note down the user name and password that you entered. | An activation email is sent to you. |  |
| 3 | Confirm Activation | Confirm the activation as described in the activation email. | An SAP Business Network registration confirmation email is sent to you. |  |
| 4 | Check Registration Data | Check if the SAP Business Network registration confirmation email provides you with the following information for your supplier:Company NameUser NameAriba Network ID (ANID)Logon URL | You registered a supplier in Ariba Network. |  |

#### Display Purchase Order (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display the Purchase Order | Choose Orders > Orders and Releases , and select the respective Purchase Order ID. | The purchase order is displayed. |  |

#### Check Supplier Data (as a Buyer in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the data of the new supplier as a buyer in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Buyer on [https://buyer.ariba.com](https://buyer.ariba.com). | The Home screen is displayed. |  |
| 2 | Check Supplier Settings in the Buyer Account | Choose Supplier Enablement > Active Relationships. | The newly created supplier is listed with the Ariba Network ID (ANID) that you received in the SAP Business Network registration confirmation email. |  |
| 3 | Check Supplier Data | Select the supplier, and choose More Actions > Edit. | The supplier number from SAP S/4HANA Cloud Public Edition is displayed in the Vendor ID field. |  |

### Quick Enablement of Suppliers through Quote Automation

The following chapters describe the process for quick enablement of a supplier, triggered by a request for quotation.

For a supplier who is available in SAP S/4HANA Cloud Public Edition, but not in SAP Business Network, the process triggers onboarding of the supplier to SAP Business Network, so that the supplier can be used in a commerce automation process.

Some steps have to be processed before a request for quotation can be sent to SAP Business Network. For example, you need to add or update the supplier email address that then triggers the invitation and registration process for the supplier in SAP Business Network.

|  |
| --- |
| Note The steps in this section are optional and must be performed only once for the respective supplier. If your business partner has been added to the communication system and if the respective e-mail address has been added to the supplier master data, you can skip the complete section. |

#### Allow Quick Enablement of Suppliers (as a Buyer in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to allow quick enablement of suppliers through purchase orders, payment proposals, CC invoices, and invoices without purchase order as a buyer in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Buyer on [https://buyer.ariba.com](https://buyer.ariba.com). |  |  |
| 2 | Allow Quick Enablement | Choose Profile > Settings > Transactions > Default Transaction Rules . In the Quick Enablement Rules section, select the Allow Quick Enablement checkbox.Choose Save. | The quick enablement of suppliers is allowed. |  |

#### Add Business Partners to the Communication System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to add business partners as allowed partners to the communication system for the quick enablement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Access App | Open the Communication Systems (F1762) app. | The Communication Systems screen is displayed. |  |
| 3 | Search Communication System | To search for a communication system, set the relevant search filters, and choose Go. | A list of communication systems is displayed. |  |
| 4 | Select Communication System | Select a communication system and navigate to the Business Partners tab. Choose Add (  ). | The Add Business Partner popup window is displayed. |  |
| 5 | Add Business Partner to Communication System | In the Add Business Partner popup window, select a business partner. Choose Select . | The business partner is added to the communication system for the quick enablement. |  |

#### Add or Update Supplier Email Address

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to add or update the email address of the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Supplier Master Data (F1053A) app. | The Manage Supplier Master Data screen is displayed. |  |
| 3 | Search for Business Partner | To search for the supplier, enter a business partner ID.Tip You can use the value help (  ), to select the correct data.Choose Go. | In the search result list, the supplier is displayed. |  |
| 4 | Select Supplier | To add or update the data of the supplier, select the supplier. | The Supplier screen is displayed. |  |
| 5 | Select Supplier Address | On the Supplier screen, choose Address > Address Details .Select the address that has the value Yes in the Standard column. | The Address Details screen is displayed. |  |
| 6 | Add or Update Email Address | On the Address Details screen, choose Communication > Email .Add or update an email address. In the Standard column, select the checkbox.Choose Apply > Save . | The email address is added or updated, and is set as standard. |  |

#### Create Request for Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a request for quotation (RFQ) from an existing purchase requisition, and send it to SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage RFQs (F2049) app. | The Manage RFQs screen is displayed. |  |
| 3 | Access New Request for Quotation Screen | On the Manage RFQs screen, choose Create, and from the dropdown list, choose Ext. Price Request. | The New Request for Quotation screen is displayed. |  |
| 4 | Create New Request for Quotation | On the New Request for Quotation screen, enter the required data.On the General Information tab, enter the following data:RFQ Description: <Short description or the title of the RFQ>Note This field is mandatory.Language Key: To select a language key, choose the value help.Quotation Deadline: todayPurchasing Group: 001Purch. Organization: 3310Company Code: 3310On the Delivery and Payment Terms tab, enter the following data:Currency: AEDOn the Items tab, select the newly created RFQ Item and enter the following data:Material: TG0011Material Group: L001Plant: 3310Requested Quantity: 20Delivery date: today + 1 monthInfo Record Update: Select the checkbox.Choose Apply. You’ll return to the New Request for Quotation screen.On the Bidders tab, choose Create, and add one or more bidders, for example, Supplier: 33300085Choose Create. | The new request for quotation is created. |  |
| 5 | Publish Request for Quotation | On the Request for Quotation screen, choose Publish. | The workflow for automatic approval of the request for quotation is triggered. After approval, the request for quotation is published. |  |

#### Register Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to register a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive Registration Email | After you received a registration email from SAP Business Network, select the link in the email to activate your account. |  |  |
| 2 | Register Supplier | Enter a temporary ID and a secure code. If you're asked to check for existing accounts, continue with the creation of a new account.Tip Note down the user name and password that you entered. | An activation email is sent to you. |  |
| 3 | Confirm Activation | Confirm the activation as described in the activation email. | An SAP Business Network registration confirmation email is sent to you. |  |
| 4 | Check Registration Data | Check if the SAP Business Network registration confirmation email provides you with the following information for your supplier:Company NameUser NameAriba Network ID (ANID)Logon URL | You registered a supplier in Ariba Network. |  |

#### Submit Price Quote (as a Supplier in SAP Business Network Discovery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to enter your bids as a supplier in SAP Business Network Discovery.

|  |
| --- |
| Note SAP Business Network will wait for the quotation deadline (as set in [Create Request for Quotation](#unique_59) [page ] 108) to pass by before the bid is actually forwarded to the buyer. For example, after entering the bid, you have to wait until the quotation deadline you entered in the RFQ has passed (that would typically be the next day if you set the quotation deadline to today) before you can continue with the test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). |  |  |
| 2 | Display Automated RFQ Overview | Choose Discovery > Matched and Invited Leads .Search for the relevant RFQ and open it. | An overview list of the existing RFQs is displayed. |  |
| 3 | Create Response | Choose Quote all. | The list of all item parts of the RFQ is displayed. |  |
| 4 | Submit Response | For each of the items, enter the following data according to your business requirements:ExamplePrice: 1Shipping cost: 5Choose Submit. | The quote was submitted. |  |

#### Check Supplier Data (as a Buyer in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the data of the new supplier as a buyer in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Buyer on [https://buyer.ariba.com](https://buyer.ariba.com). | The Home screen is displayed. |  |
| 2 | Check Supplier Settings in the Buyer Account | Choose Supplier Enablement > Active Relationships. | The newly created supplier is listed with the Ariba Network ID (ANID) that you received in the SAP Business Network registration confirmation email. |  |
| 3 | Check Supplier Data | Select the supplier, and choose More Actions > Edit. | The supplier number from SAP S/4HANA Cloud Public Edition is displayed in the Vendor ID field. |  |

### Material Procurement with Evaluated Receipt Settlement

#### Create Purchase Order with Advanced App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order Data | In the Header section, enter the following data:Order Type: Standard OrderPayment Terms: 0004Vendor: 33300085Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310In the Items section, enter the following data:Material: TG0011Quantity: 100 PCDelivery Date: Today + 1 monthNet Price: 30AEDPlant: 3310Storage Location: 331AIn the Item Details section, enter the following data:On the Invoice tab, select the ERS checkbox, the Inv. Receipt Checkbox, and the GR-Bsd IV checkbox.Conf Control: Don't select any value from the dropdown list. |  |  |
| 4 | Check Purchase Order for Completeness | Choose Check. | If no error dialog box is displayed, the purchase order is complete.If an error dialog box is displayed, review the data of the purchase order, and correct all errors. |  |
| 6 | Save Purchase Order | To save the purchase order, choose More > Purchase Order > Save. | A new purchase order is created. The system message Standard PO created under the number 450000XXXX is displayed.Note Make a note of this purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve a purchase order.

|  |
| --- |
| Note Purchase orders with a net value of 500 USD (global release amount is configured in USD, and converted to the country/region currency amount), or more require an approval (for Purchasing Group 001 and 003). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchasing Manager. |  |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen with a list of already created purchase orders that need to be approved is displayed. |  |
| 3 | Select Purchase Order | To search for a specific purchase order, enter the required search criteria.From the search result list, select a purchase order. | The Purchase Order xxx is displayed.Purchase orders without follow-on documents (w/o status Follow-On Documents), and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Approve the Purchase Order | Choose Approve.If required, enter the approval reason. Choose Submit. |  |  |

#### Display Purchase Order (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display the Purchase Order | Choose Orders > Orders and Releases , and select the respective Purchase Order ID. | The purchase order is displayed. |  |

#### Post Goods Receipt for Purchasing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post a goods receipt, after the goods ordered by a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open the Post Goods Receipt for Purchasing Document (F0843) app. | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Search Purchasing Document | In the Purchasing Document field, enter the purchase order number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The purchase order is displayed. |  |
| 4 | Enter Delivery Note | On the General Information tab, enter a delivery note in the Delivery Note field. |  |  |
| 5 | Select Item | On the Items tab, select the items for which a goods receipt is to be posted. For each of the selected items, choose Unrestricted-Use from the dropdown list in the Stock Type column. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system message Document created: Material Document <Material Document Number> is displayed. |  |

#### Set Up Evaluated Receipt Settlement (ERS)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Created goods movements can be settled without receipt of an invoice. The system can create and post the appropriate invoices itself. ERS is especially effective if you create settlement documents periodically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Schedule Supplier Invoice Jobs (F1683) app. | The Application Jobs screen is displayed. |  |
| 3 | Create Application Job | Choose Create. | The New Job: Automatic Delivery Cost Settlement (ERS) screen is displayed. |  |
| 4 | Set Up ERS | In the Template Selection section, enter the following data:Job Template: Select Evaluated Receipt Settlement from the dropdown list.Job Name: Evaluated Receipt Settlement (ERS)Choose Step 2.In the Scheduling Options section, choose one of the following options:Start Immediately: Select the checkbox.Start Immediately: Don't select the checkbox. Instead, enter a strat date and start time.Choose Step 3.In the Parameters section, enter the following data according to your business requirements:ExampleCompany Code: 3310Plant: 3310Document Year of Goods Receipt: <Current Year>Supplier: 33300085Purchasing Document: Enter the purchase order number from the purchase order that you've created in [Create Purchase Order with Advanced App (Optional)](#unique_63) [page ] 112.Test Run: Select the checkbox.Choose Check. |  |  |
| 5 | Schedule the Job without Test Run | Deselect the Test Run checkbox.Choose Schedule. | It may take several minutes until the job is in status Finished. |  |
| 6 | Check the Result | On the Application Jobs screen, find the job that you've created. Choose Results. | On the <Document ID>, the detailed log is displayed. The corresponding document number and FI document number are created. |  |

#### Check Supplier Invoice List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to review the document created in [Set Up Evaluated Receipt Settlement (ERS)](#unique_66) [page ] 117 and get the generated credit memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for Document | On the Supplier Invoices List screen, enter the following data:Invoicing Party : 33300085Company Code: 3310Choose Go. | A search results list with invoices is displayed. |  |
| 4 | Display Invoice Details | Select the invoice number with ERS entry type that you've created. | The invoice details are displayed. |  |

#### Display Invoice (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the invoice as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Display Invoice | Choose Invoices > Invoices .Select the invoice related to the purchase order created in [Set Up Evaluated Receipt Settlement (ERS)](#unique_66) [page ] 117. | The invoice is displayed. |  |

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
- related-to :: [[10-procurement/test-script-automated-purchase-to-pay-with-sap-ariba-commerce-automati]]
- related-to :: [[10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business]]
- related-to :: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]
- related-to :: [[10-procurement/test-script-integration-of-procurement-with-external-suppliers-2ej-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42K_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 195,543 chars in the whole document
