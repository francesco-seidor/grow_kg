---
id: 10-procurement/test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1
title: "Test Script: Supply Chain Automation with SAP Business Network (5I2_AE) (5I2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5I2 (AE): subcontracting, scheduling agreements, multi-tier and consignment with SAP Business Network."
cluster: 10-procurement
tags: [kb/procurement, topic/business-network-supply-chain-collaboration]
aliases: [5I2_S4CLD2608_BPD_EN_AE]
keywords: [Supply Chain Collaboration with SAP Business Network, subcontracting, serial number management, batch-managed material, packing instruction, scheduling agreements, multi-tier subcontracting, sap business network, consignment purchase order, purchase order approval]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5I2_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1102
topic: 10-procurement/business-network-supply-chain-collaboration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Supply Chain Automation with SAP Business Network (5I2_AE) (5I2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5I2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supply Chain Collaboration with SAP Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Supply Chain Automation with SAP Business Network (5I2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232857260)

[2 Prerequisites 6](#_Toc232857261)

[2.1 Additional Manual Configuration 6](#_Toc232857262)

[2.2 System Access 6](#_Toc232857263)

[2.3 Roles 7](#_Toc232857264)

[2.4 Master Data, Organizational Data, and Other Data 8](#_Toc232857265)

[2.5 Business Conditions 9](#_Toc232857266)

[2.6 Preliminary Steps 10](#_Toc232857267)

[2.6.1 Opening New MM Posting Period 10](#_Toc232857268)

[2.6.2 Activate Flexible Workflow for Purchase Orders 10](#_Toc232857269)

[2.6.3 Configure Flexible Workflow for Purchase Order 12](#_Toc232857270)

[3 Overview Table 15](#_Toc232857271)

[4 Test Procedures 23](#_Toc232857272)

[4.1 Subcontracting without Serial Number Management 23](#_Toc232857273)

[4.1.1 Create Purchase Order 23](#_Toc232857274)

[4.1.2 Approve Purchase Order (Optional) 24](#_Toc232857275)

[4.1.3 Display Purchase Order as a Supplier in SAP Business Network 25](#_Toc232857276)

[4.1.4 Confirm Purchase Order as a Supplier in SAP Business Network (Optional) 26](#_Toc232857277)

[4.1.5 Check Purchase Order Confirmation (Optional) 27](#_Toc232857278)

[4.1.6 Create Outbound Delivery for Subcontracting Purchase Order 28](#_Toc232857279)

[4.1.7 Change Outbound Delivery for Subcontracting Purchase Order 29](#_Toc232857280)

[4.1.8 Post Goods Issue 30](#_Toc232857281)

[4.1.9 Display Components Inventory as a Supplier in SAP business Network (Optional) 31](#_Toc232857282)

[4.1.10 Display Shipments for Components as a Supplier in SAP Business Network 32](#_Toc232857283)

[4.1.11 Create a Component Receipt as a Supplier in SAP Business Network 32](#_Toc232857284)

[4.1.12 Check Updated Proof of Delivery in Outbound Delivery Document 33](#_Toc232857285)

[4.1.13 Create Shipping Notification as a Supplier in SAP Business Network 34](#_Toc232857286)

[4.1.14 Check Inbound Delivery for Purchase Order (Optional) 36](#_Toc232857287)

[4.1.15 Set Up the Putaway of Goods for Inbound Delivery 37](#_Toc232857288)

[4.1.16 Post Goods Receipt 38](#_Toc232857289)

[4.1.17 Check Goods Receipt Details (Optional) 39](#_Toc232857290)

[4.1.18 Post Subsequent Stock Adjustment (Optional) 40](#_Toc232857291)

[4.1.19 Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network 41](#_Toc232857292)

[4.1.20 Display Invoice Status Change as a Supplier in SAP Business Network 43](#_Toc232857293)

[4.2 Subcontracting with Serial Number Management 43](#_Toc232857294)

[4.2.1 Create Purchase Order 43](#_Toc232857295)

[4.2.2 Approve Purchase Order (Optional) 45](#_Toc232857296)

[4.2.3 Display Purchase Order as a Supplier in SAP Business Network 46](#_Toc232857297)

[4.2.4 Confirm Purchase Order as a Supplier in SAP Business Network (Optional) 47](#_Toc232857298)

[4.2.5 Check Purchase Order Confirmation (Optional) 48](#_Toc232857299)

[4.2.6 Create Outbound Delivery for Subcontracting Purchase Order 49](#_Toc232857300)

[4.2.7 Pick Delivery Item and Post Goods Issue 50](#_Toc232857301)

[4.2.8 Display Shipments for Components as a Supplier in SAP Business Network 51](#_Toc232857302)

[4.2.9 Create a Component Receipt as a Supplier in SAP Business Network 52](#_Toc232857303)

[4.2.10 Check Updated Proof of Delivery in Outbound Delivery Document 53](#_Toc232857304)

[4.2.11 Create Shipping Notification as a Supplier in SAP Business Network 54](#_Toc232857305)

[4.2.12 Check Inbound Delivery for Purchase Order (Optional) 55](#_Toc232857306)

[4.2.13 Set Up the Putaway of Goods for Inbound Delivery 56](#_Toc232857307)

[4.2.14 Post Goods Receipt 57](#_Toc232857308)

[4.2.15 Check Goods Receipt Details (Optional) 58](#_Toc232857309)

[4.2.16 Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network 59](#_Toc232857310)

[4.2.17 Display Invoice Status Change as a Supplier in SAP Business Network 60](#_Toc232857311)

[4.3 Subcontracting with Batch-Managed Material 61](#_Toc232857312)

[4.3.1 Create Purchase Order 61](#_Toc232857313)

[4.3.2 Approve Purchase Order (Optional) 63](#_Toc232857314)

[4.3.3 Display Purchase Order as a Supplier in SAP Business Network 64](#_Toc232857315)

[4.3.4 Confirm Purchase Order as a Supplier in SAP Business Network (Optional) 65](#_Toc232857316)

[4.3.5 Check Purchase Order Confirmation (Optional) 66](#_Toc232857317)

[4.3.6 Create Outbound Delivery for Subcontracting Purchase Order 67](#_Toc232857318)

[4.3.7 Pick Delivery Item and Post Goods Issue 68](#_Toc232857319)

[4.3.8 Display Shipments for Components as a Supplier in SAP Business Network 69](#_Toc232857320)

[4.3.9 Create a Component Receipt as a Supplier in SAP Business Network 70](#_Toc232857321)

[4.3.10 Check Updated Proof of Delivery in Outbound Delivery Document 71](#_Toc232857322)

[4.3.11 Create Shipping Notification as a Supplier in SAP Business Network 72](#_Toc232857323)

[4.3.12 Check Inbound Delivery for Purchase Order (Optional) 73](#_Toc232857324)

[4.3.13 Set Up the Putaway of Goods for Inbound Delivery 74](#_Toc232857325)

[4.3.14 Post Goods Receipt 75](#_Toc232857326)

[4.3.15 Check Goods Receipt Details (Optional) 76](#_Toc232857327)

[4.3.16 Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network 77](#_Toc232857328)

[4.3.17 Display Invoice Status Change as a Supplier in SAP Business Network 78](#_Toc232857329)

[4.4 Subcontracting with Packing Instruction 79](#_Toc232857330)

[4.4.1 Create Purchase Order 79](#_Toc232857331)

[4.4.2 Approve Purchase Order (Optional) 81](#_Toc232857332)

[4.4.3 Display Purchase Order as a Supplier in SAP Business Network 82](#_Toc232857333)

[4.4.4 Confirm Purchase Order as a Supplier in SAP Business Network (Optional) 83](#_Toc232857334)

[4.4.5 Check Purchase Order Confirmation (Optional) 84](#_Toc232857335)

[4.4.6 Create Shipping Notification with Handling Unit as a Supplier in SAP Business Network 85](#_Toc232857336)

[4.4.7 Check Inbound Delivery for Purchase Order (Optional) 86](#_Toc232857337)

[4.4.8 Set Up the Putaway of Goods for Inbound Delivery 87](#_Toc232857338)

[4.4.9 Post Goods Receipt 88](#_Toc232857339)

[4.4.10 Check Goods Receipt Details (Optional) 89](#_Toc232857340)

[4.4.11 Create a Supplier Invoice linked to a Scheduling Agreement in SAP Business Network 90](#_Toc232857341)

[4.4.12 Display Invoice Status Change as a Supplier in SAP Business Network 91](#_Toc232857342)

[4.5 Scheduling Agreement with SAP Business Network 92](#_Toc232857343)

[4.5.1 Create Scheduling Agreement 92](#_Toc232857344)

[4.5.2 Maintain Delivery Schedule 94](#_Toc232857345)

[4.5.3 Release Scheduling Agreement 96](#_Toc232857346)

[4.5.4 Display Scheduling Agreement as a Supplier in SAP Business Network 97](#_Toc232857347)

[4.5.5 Create Shipping Notification as a Supplier in SAP Business Network 98](#_Toc232857348)

[4.5.6 Get Inbound Delivery Number 99](#_Toc232857349)

[4.5.7 Set Up the Putaway of Goods for Inbound Delivery 100](#_Toc232857350)

[4.5.8 Post Goods Receipt 101](#_Toc232857351)

[4.5.9 Check Goods Receipt Details (Optional) 102](#_Toc232857352)

[4.5.10 Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network 103](#_Toc232857353)

[4.5.11 Display Invoice Status Change as a Supplier in SAP Business Network 104](#_Toc232857354)

[4.6 Multi-Tier Subcontracting 105](#_Toc232857355)

[4.6.1 Create Purchase Order 105](#_Toc232857356)

[4.6.2 Approve Purchase Order (Optional) 107](#_Toc232857357)

[4.6.3 Display Purchase Order as a Main Supplier in SAP Business Network 108](#_Toc232857358)

[4.6.4 Display Purchase Order as a Multi-Tier Supplier in SAP Business Network 109](#_Toc232857359)

[4.6.5 Confirm Purchase Order as a Main Supplier in SAP Business Network (Optional) 110](#_Toc232857360)

[4.6.6 Check Order Confirmation as a Multi-Tier Supplier in SAP Business Network (Optional) 111](#_Toc232857361)

[4.6.7 Check Purchase Order Confirmation (Optional) 112](#_Toc232857362)

[4.6.8 Create Shipping Notification as a Main Supplier in SAP Business Network 113](#_Toc232857363)

[4.6.9 Display Shipping Notification as a Multi-Tier Supplier in SAP Business Network 114](#_Toc232857364)

[4.6.10 Set Up the Putaway of Goods for Inbound Delivery 115](#_Toc232857365)

[4.6.11 Post Goods Receipt 116](#_Toc232857366)

[4.6.12 Check Goods Receipt Details (Optional) 117](#_Toc232857367)

[4.6.13 Create Supplier Invoice with PO/GR Relation as a Main Supplier in SAP Business Network 118](#_Toc232857368)

[4.6.14 Display Invoice Status Change as a Supplier in SAP Business Network 119](#_Toc232857369)

[4.7 Purchase Order with Item Type Consignment 120](#_Toc232857370)

[4.7.1 Create Purchase Order 120](#_Toc232857371)

[4.7.2 Approve Purchase Order (Optional) 122](#_Toc232857372)

[4.7.3 Display Purchase Order as a Supplier in SAP Business Network 123](#_Toc232857373)

[4.7.4 Confirm Purchase Order as a Supplier in SAP Business Network (Optional) 124](#_Toc232857374)

[4.7.5 Check Purchase Order Confirmation (Optional) 125](#_Toc232857375)

## Purpose

Overview

This scope item handles several supply chain processes as an integrated end-to-end solution. It includes SAP S/4HANA Cloud Public Edition and SAP Business Network for Supply Chain.

Subcontracting

Subcontract purchase requisitions are generated either through the material requirements planning (MRP) process or manually by requestors. These requisitions are then converted into subcontract purchase orders. Purchase orders require approval based on predefined parameters before they're issued to subcontractors. Once approved, outbound deliveries are created, and goods

(e.g. components and/ or raw materials) are picked and shipped to subcontractors. After the delivery of the finished materials, goods receipts are created. The consumption of sent the previously provided components is recorded when the value-added finished materials are received. This process subsequently initiates invoicing. The integrated Subcontracting processes focuses on externally produced materials (make-to-stock).

Scheduling Agreements

Scheduling agreements are long-term contracts with suppliers for the supply of materials under predetermined conditions. These conditions are valid for a specific period and a defined total purchase quantity. You can use scheduling agreements either with release documentation.

Customizing controls this through an indicator when you define the document type for scheduling agreements. For agreements with release documentation, use the LPA document type.

SA schedule lines are created with reference to a purchase scheduling agreement either through the material requirements planning process (MRP) or manually by requesters. Once the SA release has been carried out, an SA delivery schedule (forecast/JIT) is issued and communicated to the supplier. Based on the SA delivery schedule, the supplier delivers the requested goods and notifies about the upcoming delivery by sending an ASN. After the ASN has been converted into an inbound delivery, the goods receipt is posted, and the logistics invoice verification is carried out.

Multi-Tier Collaboration

Multi-Tier Collaboration lets you work with multiple trading partners across various processes, systems, and geographies in real time. It enhances transparency by sharing purchase orders, order confirmations, and advance ship notifications with multiple suppliers. This feature allows supply chain partners to access copies of orders, confirmations, and ship notices, with financial fields masked. They can also create component receipts upon receiving shipments. OEM buyers can manage their copy documents and view component shipments and receipts from tiered suppliers.

Advanced Packaging with Handling Units

Customers need standardized packaging for the materials and products they order and receive from suppliers. Without support for Handling Units during the creation of advanced shipping notifications, materials may be packed arbitrarily. This makes it challenging for customers to streamline their receiving and put-away processes. In this scenario, the replication of packaging instructions as well as the creation of ASNs with packaging data (specified in the replicated PI) is described.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/5I2_S4CLD2602_BPD_EN_AE.docx) ). |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/2893032ca60c113e17c8c127eb09bdd1)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Business Network Discovery | Accessible via SAP Business Network Discovery discovery.ariba.com with the SAP Business Network Buyer and Supplier accounts. Your system administrator provides you with logon data.Note In a multi-tier subcontracting scenario, you'll need two supplier accounts. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to [How to Create a Business Role for the Administrator](https://help.sap.com/docs/SAP_S4HANA_CLOUD/55a7cb346519450cb9e6d21c1ecd6ec1/8fa28e0107984d42a99b9eea67856cea.html) in the SAP S/4HANA Cloud Public Edition product assistance.

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
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_MANAGER |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

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
| Purchase Organization | 3310 | Purchase Organization 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor/Supplier | 3330008533300001 | Vendor domestic United States Ariba |  |
| Material | SG23 | SEMI23,PD,Subcontracting |  |
| Material | SG27 | SEMI23, PD, Subcontracting with serial numbers |  |
| Material | RM129 |  |  |
| Material | RM128 |  |  |

For more information on creating master data objects, refer to the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J60 - Accounts Payable | Update BP master data with payment method T.Review and execute Invoice payment preparation section |

To run through this scope item, the materials must be available in stock. You can create stock using the Manage Stock(F1062__sap_mmimtype_manage) app or the Transfer Stock - In-Plant(F1061) app in the SAP Fiori launchpad.

### Preliminary Steps

#### Opening New MM Posting Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This is an external process. |

Information on material stock and certain valuation data such as total stock value, total stock, evaluation elements class, price control indicator, and price unit are held by financial posting period. The period must be set up at the beginning of each new posting period to ensure that values and goods movement are posted to the correct period. Usually, only the current posting period is open for posting. All other posting periods are closed.

To close an MM posting period, and open a new posting period, run the procedure described in the Create New Open MM Posting Period - MDS (BNZ) master data script.

#### Activate Flexible Workflow for Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This procedure describes how to activate the flexible workflow for purchase orders.

Prerequisites

To carry out the following activity, a business user with a business role must exist. The business role must contain the business catalog SAP_CORE_BC_COM (Communication Management), for example, the business role Administrator (SAP_BR_ADMINISTRATOR) is required.

Additionally, the business role Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT) must be assigned to the user

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Your Solution (F1241) app. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 4 | Search for Application Area | On the Configure Your Solution: Realize Phase screen, set the following search filters:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement | A search result list is displayed. |  |
| 5 | Select Configuration Item | From the search result list, select the Purchase Order Processing configuration item. | The Configure Your Solution - Purchase Order Processing screen is displayed. |  |
| 6 | Select Configuration Step | On the Configure Your Solution - Purchase Order Processing screen, in the Configuration Steps section, choose Configure for the Activate Flexible Workflow for Purchase Orders configuration step. | The Document Types Purchase order Change screen is displayed. |  |
| 7 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: Select the checkbox. | The scenario-based workflow is active for standard purchase orders.If you’re asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue.Choose Save. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
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

This procedure describes how to configure workflows to optimize the approval process for purchase orders.

|  |
| --- |
| Note Before you start this procedure, ensure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access App | Open the Manage Workflows for Purchase Orders (F2872) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Purchase Order | Choose Create. On the New Workflow screen, enter a workflow name in the Workflow Name field, for example, Test Workflow for Purchase Order.Select the Start Conditions tab. In the Only start the workflow if all of the following preconditions are met: field, select Purchasing group of purchase order is from the dropdown list and enter 001.Choose Create Alternative Preconditions and enter the following data:In the Only start the workflow if all of the following preconditions are met: field, select Total net amount of purchase order is greater than from the dropdown list and enter the following data:Amount: 100Currency: AEDSelect the Steps tab. Choose Create.On the New Step screen, select the Header tab. In the Step Type field, select Release of Purchase Order from the dropdown list.Select the Recipients tab and select the following settings:Assignment By: RoleRole: Manager of Workflow InitiatorStep to be completed by: One of the recipientsChoose Create > Save . | The workflow for a purchase order is created. |  |
| 4 | Activate Workflow Item | On the Workflow Details screen, select the workflow item that you've created and choose Activate. | The workflow item is activated. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Subcontracting without Serial Number Management

The scope of the Subcontracting without Serial Number Management section consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_12) [page ] 23 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | A subcontracting purchase order is created. |
| [Approve Purchase Order (Optional)](#unique_13) [page ] 24 | Purchasing Manager | My Inbox (F0862) | The subcontracting purchase order is approved. |
| [Display Purchase Order as a Supplier in SAP Business Network](#unique_14) [page ] 25 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected subcontracting purchase order are displayed. |
| [Confirm Purchase Order as a Supplier in SAP Business Network (Optional)](#unique_15) [page ] 26 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The subcontracting purchase order is confirmed. |
| [Check Purchase Order Confirmation (Optional)](#unique_16) [page ] 27 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system aligns with the status in SAP Business Network. |
| [Post Goods Issue](#unique_17) [page ] 30 | Shipping Specialist | Change Outbound Delivery (VL02N) | The goods issue is posted. |
| [Display Shipments for Components as a Supplier in SAP Business Network](#unique_18) [page ] 32 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | A list of delivery items with reference to the purchase order is displayed. |
| [Create a Component Receipt as a Supplier in SAP Business Network](#unique_19) [page ] 70 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) |  |
| [Check Updated Proof of Delivery in Outbound Delivery Document](#unique_20) [page ] 33 | Shipping Specialist | Display Outbound Delivery - Proof of Delivery (VLPODA) |  |
| [Create Shipping Notification as a Supplier in SAP Business Network](#unique_21) [page ] 34 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The shipping notification is created. |
| [Check Inbound Delivery for Purchase Order (Optional)](#unique_22) [page ] 36 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system aligns with the status in SAP Business Network. |
| [Set Up the Putaway of Goods for Inbound Delivery](#unique_23) [page ] 37 | Receiving Specialist | Change Inbound Delivery (VL32N) | The putaway of material is set up. |
| [Post Goods Receipt](#unique_24) [page ] 38 | Warehouse Clerk | Post Goods Receipt for Inbound Delivery (F2502) | After the goods ordered through a purchase order arrived at the warehouse, the goods receipt for a purchase order is posted. |
| [Check Goods Receipt Details (Optional)](#unique_25) [page ] 39 | Warehouse Clerk | Material Documents Overview (F1077) | The goods receipt details are reviewed. |
| [Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network](#unique_26) [page ] 41 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice with PO/GR relation is created and submitted to SAP Business Network. |
| [Display Invoice Status Change as a Supplier in SAP Business Network](#unique_27) [page ] 43 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The invoice of the subcontracting purchase order is either in status Sent or Approved. |

Subcontracting with Serial Number Management

The scope of the Subcontracting with Serial Number Management section consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_28) [page ] 43 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | A subcontracting purchase order is created. |
| [Approve Purchase Order (Optional)](#unique_29) [page ] 45 | Purchasing Manager | My Inbox (F0862) | The subcontracting purchase order is approved. |
| [Display Purchase Order as a Supplier in SAP Business Network](#unique_30) [page ] 46 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected subcontracting purchase order are displayed. |
| [Confirm Purchase Order as a Supplier in SAP Business Network (Optional)](#unique_31) [page ] 47 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The subcontracting purchase order is confirmed. |
| [Check Purchase Order Confirmation (Optional)](#unique_32) [page ] 48 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system aligns with the status in SAP Business Network. |
| [Create Outbound Delivery for Subcontracting Purchase Order](#unique_33) [page ] 49 | Purchaser | Display Subcontracting Stocks by Supplier (ME2ON) | A delivery document for the subcontracting purchase order is created. |
| [Pick Delivery Item and Post Goods Issue](#unique_34) [page ] 50 | Shipping Specialist | Change Outbound Delivery (VL02N) | The outbound delivery for a subcontracting purchase order is changed and the goods issue is posted.. |
| [Display Shipments for Components as a Supplier in SAP Business Network](#unique_35) [page ] 51 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | A list of delivery items with reference to the purchase order is displayed. |
| [Create a Component Receipt as a Supplier in SAP Business Network](#unique_36) [page ] 52 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) |  |
| [Check Updated Proof of Delivery in Outbound Delivery Document](#unique_37) [page ] 53 | Shipping Specialist | Display Outbound Delivery - Proof of Delivery (VLPODA) |  |
| [Create Shipping Notification as a Supplier in SAP Business Network](#unique_38) [page ] 54 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The shipping notification is created. |
| [Check Inbound Delivery for Purchase Order (Optional)](#unique_39) [page ] 55 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system aligns with the status in SAP Business Network. |
| [Set Up the Putaway of Goods for Inbound Delivery](#unique_40) [page ] 56 | Receiving Specialist | Change Inbound Delivery (VL32N) | The putaway of material is set up. |
| [Post Goods Receipt](#unique_41) [page ] 57 | Warehouse Clerk | Post Goods Receipt for Inbound Delivery (F2502) | After the goods ordered through a purchase order arrived at the warehouse, the goods receipt for a purchase order is posted. |
| [Check Goods Receipt Details (Optional)](#unique_42) [page ] 58 | Warehouse Clerk | Material Documents Overview (F1077) | The goods receipt details are reviewed. |
| [Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network](#unique_43) [page ] 59 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice with PO/GR relation is created and submitted to SAP Business Network. |
| [Display Invoice Status Change as a Supplier in SAP Business Network](#unique_44) [page ] 60 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The invoice of the subcontracting purchase order is either in status Sent or Approved. |

Subcontracting with Batch-Managed Material

The scope of the Subcontracting with Batch-Managed Material section consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_45) [page ] 61 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | A subcontracting purchase order is created. |
| [Approve Purchase Order (Optional)](#unique_46) [page ] 63 | Purchasing Manager | My Inbox (F0862) | The subcontracting purchase order is approved. |
| [Display Purchase Order as a Supplier in SAP Business Network](#unique_47) [page ] 64 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected subcontracting purchase order are displayed. |
| [Confirm Purchase Order as a Supplier in SAP Business Network (Optional)](#unique_48) [page ] 65 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The subcontracting purchase order is confirmed. |
| [Check Purchase Order Confirmation (Optional)](#unique_49) [page ] 66 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system aligns with the status in SAP Business Network. |
| [Create Outbound Delivery for Subcontracting Purchase Order](#unique_50) [page ] 67 | Purchaser | Display Subcontracting Stocks by Supplier (ME2ON) | A delivery document for the subcontracting purchase order is created. |
| [Pick Delivery Item and Post Goods Issue](#unique_51) [page ] 68 | Shipping Specialist | Change Outbound Delivery (VL02N) | The outbound delivery for a subcontracting purchase order is changed and the goods issue is posted.. |
| [Display Shipments for Components as a Supplier in SAP Business Network](#unique_52) [page ] 69 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | A list of delivery items with reference to the purchase order is displayed. |
| [Check Updated Proof of Delivery in Outbound Delivery Document](#unique_53) [page ] 71 | Shipping Specialist | Display Outbound Delivery - Proof of Delivery (VLPODA) |  |
| [Create Shipping Notification as a Supplier in SAP Business Network](#unique_54) [page ] 72 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The shipping notification is created. |
| [Check Inbound Delivery for Purchase Order (Optional)](#unique_55) [page ] 73 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system aligns with the status in SAP Business Network. |
| [Set Up the Putaway of Goods for Inbound Delivery](#unique_56) [page ] 74 | Receiving Specialist | Change Inbound Delivery (VL32N) | The putaway of material is set up. |
| [Post Goods Receipt](#unique_57) [page ] 75 | Warehouse Clerk | Post Goods Receipt for Inbound Delivery (F2502) | After the goods ordered through a purchase order arrived at the warehouse, the goods receipt for a purchase order is posted. |
| [Check Goods Receipt Details (Optional)](#unique_58) [page ] 76 | Warehouse Clerk | Material Documents Overview (F1077) | The goods receipt details are reviewed. |
| [Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network](#unique_59) [page ] 77 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice with PO/GR relation is created and submitted to SAP Business Network. |
| [Display Invoice Status Change as a Supplier in SAP Business Network](#unique_60) [page ] 78 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The invoice of the subcontracting purchase order is either in status Sent or Approved. |

Subcontracting with Packing Instruction

The scope of the Subcontracting with Packing Instruction section consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_61) [page ] 79 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | A subcontracting purchase order is created. |
| [Approve Purchase Order (Optional)](#unique_62) [page ] 81 | Purchasing Manager | My Inbox (F0862) | The subcontracting purchase order is approved. |
| [Display Purchase Order as a Supplier in SAP Business Network](#unique_63) [page ] 82 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected subcontracting purchase order are displayed. |
| [Confirm Purchase Order as a Supplier in SAP Business Network (Optional)](#unique_64) [page ] 83 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The subcontracting purchase order is confirmed. |
| [Check Purchase Order Confirmation (Optional)](#unique_65) [page ] 84 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |
| [Create Shipping Notification with Handling Unit as a Supplier in SAP Business Network](#unique_66) [page ] 85 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The shipping notification is created. The status of the purchase order is changed to Shipped. |
| [Check Inbound Delivery for Purchase Order (Optional)](#unique_67) [page ] 86 | Receiving Specialist | Manage Purchase Orders (F0842A) | The Handling Unit Information is displayed. |
| [Set Up the Putaway of Goods for Inbound Delivery](#unique_68) [page ] 87 | Receiving Specialist | Change Inbound Delivery (VL32N) | The inbound delivery has been saved. |
| [Post Goods Receipt](#unique_69) [page ] 88 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt for inbound delivery is posted. |
| [Check Goods Receipt Details (Optional)](#unique_70) [page ] 89 | Warehouse Clerk | Material Documents Overview (F1077) | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |
| [Create a Supplier Invoice linked to a Scheduling Agreement in SAP Business Network](#unique_71) [page ] 90 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition. |
| [Display Invoice Status Change as a Supplier in SAP Business Network](#unique_72) [page ] 91 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice is released for payment. |

Scheduling Agreement with SAP Business Network

The scope of the Scheduling Agreement with SAP Business Network section consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Scheduling Agreement](#unique_73) [page ] 92 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A new scheduling agreement is created. |
| [Maintain Delivery Schedule](#unique_74) [page ] 94 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The scheduling agreement is updated with the delivery schedule. |
| [Release Scheduling Agreement](#unique_75) [page ] 96 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The release document is immediately issued to the supplier. The document status changes to Sent. |
| [Display Scheduling Agreement as a Supplier in SAP Business Network](#unique_76) [page ] 97 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected scheduling agreement are displayed. |
| [Create Shipping Notification as a Supplier in SAP Business Network](#unique_77) [page ] 98 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The shipping notification is created. The status of the purchase order is changed to Shipped. |
| [Get Inbound Delivery Number](#unique_78) [page ] 99 | Purchaser | Display Scheduling Agreement (ME33L) | In the Supplier Confirmations table, the inbound delivery number is displayed. |
| [Set Up the Putaway of Goods for Inbound Delivery](#unique_79) [page ] 100 | Receiving Specialist | Change Inbound Delivery (VL32N) | The inbound delivery is saved. |
| [Post Goods Receipt](#unique_80) [page ] 101 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt for the inbound delivery is posted. |
| [Check Goods Receipt Details (Optional)](#unique_81) [page ] 102 | Warehouse Clerk | Material Documents Overview (F1077) | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |
| [Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network](#unique_82) [page ] 103 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition. |
| [Display Invoice Status Change as a Supplier in SAP Business Network](#unique_83) [page ] 104 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The component receipt for a ship notice is created. |

Multi-Tier Subcontracting

The scope of the Scheduling Agreement with SAP Business Network section consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_84) [page ] 105 | Purchaser | Create Purchase Order - Advanced (ME21N) | A new subcontracting purchase order is created. |
| [Approve Purchase Order (Optional)](#unique_85) [page ] 107 | Purchaser | My Inbox (F0862) | The subcontracting purchase order is approved. |
| [Display Purchase Order as a Main Supplier in SAP Business Network](#unique_86) [page ] 108 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected subcontracting purchase order are displayed. |
| [Display Purchase Order as a Multi-Tier Supplier in SAP Business Network](#unique_87) [page ] 109 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected subcontracting purchase order are displayed. |
| [Confirm Purchase Order as a Main Supplier in SAP Business Network (Optional)](#unique_88) [page ] 110 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The status of the subcontracting purchase order is changed to Confirmed. |
| [Check Order Confirmation as a Multi-Tier Supplier in SAP Business Network (Optional)](#unique_89) [page ] 111 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) |  |
| [Check Purchase Order Confirmation (Optional)](#unique_90) [page ] 112 | Purchaser | Manage Purchase Orders (F0842A) | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |
| [Create Shipping Notification as a Main Supplier in SAP Business Network](#unique_91) [page ] 113 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The shipping notification is created. The status of the purchase order is changed to Shipped. |
| [Display Shipping Notification as a Multi-Tier Supplier in SAP Business Network](#unique_92) [page ] 114 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The line item details of the selected purchase order are displayed. |
| [Display Invoice Status Change as a Supplier in SAP Business Network](#unique_83) [page ] 104 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The component receipt for a ship notice is created. |
| [Check Purchase Order Confirmation (Optional)](#unique_90) [page ] 112 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt for the inbound delivery is posted. |
| [Check Goods Receipt Details (Optional)](#unique_93) [page ] 117 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt for the inbound delivery is posted. |
| [Create Supplier Invoice with PO/GR Relation as a Main Supplier in SAP Business Network](#unique_94) [page ] 118 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition. |
| [Display Invoice Status Change as a Supplier in SAP Business Network](#unique_95) [page ] 119 | Supplier in SAP Business Network | [supplier.ariba.com](https://supplier.ariba.com/) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Subcontracting without Serial Number Management

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a subcontracting purchase order in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Basic Data | On the Purchase Order screen, enter the following data in the Basic Data section:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300080Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310 |  |  |
| 5 | Enter Purchase Order Item | Select the Items tab. In the Purchase Order Items section, choose Create.Enter the following data according to your business requirements:ExampleItem Category: Subcontracting(L)Material: SG23Plant: 3310Order Quantity: 10 PCNet Order Price: 20AEDTax: <Input Tax Code> or <Input Tax Code> | A purchase order item is created. |  |
| 6 | Enter Supplier Confirmation Control | Select the newly created purchase order item to view detailed information.On the Purchase Order Item screen, select the Supplier Confirmation Control tab.In the Confirmation Control field, Select Confirmations 1 from the dropdown list. | The confirmation control is set for the purchase order item. |  |
| 7 | Save Purchase Order | Choose Apply > Order . | A new subcontracting purchase order is created. The system message Purchase Order has been saved is displayed.Note Make a note of the purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve and release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval (for Purchasing Group 001 and Purchasing Group 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchasing Manager role. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for the subcontracting purchase order you've created and select it.Note Purchase orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |  |
| 4 | Approve the Purchase Order | Choose Approve.In the Submit Decision dialog box, enter the approval reason if needed. Then, choose Submit. | The subcontracting purchase order is approved. |  |

#### Display Purchase Order as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order in the SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |

#### Confirm Purchase Order as a Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm a subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Confirm Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Order Confirmation > Confirm Entire Order .Enter the following data:Confirmation #: Subcon-01 | The Confirming PO screen is displayed. |  |
| 4 |  | On the Confirming PO screen, choose Next > Submit . | The status of the subcontracting purchase order is changed to Confirmed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order that you've created, enter the required search criteria and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network. | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |  |

#### Create Outbound Delivery for Subcontracting Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create an outbound delivery for a subcontracting purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Display Subcontracting Stocks by Supplier (ME2ON) app. | The Subcontracting Cockpit screen is displayed. |  |
| 3 | Search for Purchasing Documents | On the Subcontracting Cockpit screen, enter the following data:Supplier: 33300080With requirements from subcontracting Purchase Requisitions: Select the checkbox.With external receipts from Purchase Requisitions: Select the checkbox.With external receipts from Purchase Orders: Select the checkbox.Choose Execute. | A search result table is displayed. |  |
| 4 | Select Line Items of Subcontracting Purchase Order | For the following material descriptions, expand the Requirements via SC Orders entry by selecting the symbol in the Show/Hide column:Material RM13Material RM14In the Document Number column, find the line items of your subcontracting purchase order. To select the relevant entries, use Ctrl and select the checkbox in the Table selection menu column (1. column) of each line item.Choose Create Delivery. | The Create Delivery for Subcontracting Purchase Orders screen is displayed. |  |
| 5 | Create Delivery for Subcontracting Purchase Order | On the Create Delivery for Subcontracting Purchase Orders screen, go to the Stor. Loc. column. For each line item, enter 171C in the Stor. Loc. column field.To select the relevant entries, use Ctrl and select the checkbox in the Table selection menu column (1. column) of each line item.Choose Create Document.Note down your delivery number. | A delivery document for the subcontracting purchase order is created. |  |

#### Change Outbound Delivery for Subcontracting Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to change the outbound delivery for a subcontracting purchase order in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed. |  |
| 3 | Search for Outbound Delivery | In the Outbound Delivery field, enter the outbound delivery number.Choose Continue. | The Outbound Delivery <Outbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Change Outbound Delivery | Select the Picking tab.For the delivery item, enter the quantity in the Picked Qty column that equals the quantity displayed in the Deliv. Qty column.Choose Save. | The outbound delivery for a subcontracting purchase order is changed. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post the goods issue in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed. |  |
| 3 | Search for Outbound Delivery | In the Outbound Delivery field, enter the outbound delivery number.Choose Continue. | The Outbound Delivery <Outbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Post Goods Issue | Choose Post Goods Issue. | The goods issue is posted. |  |

#### Display Components Inventory as a Supplier in SAP business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display components inventory to the supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Check Components Inventory | Choose Fulfillment > Extended Collaboration > Components Inventory | A list of customers with reference to the component with their quantity respectively is displayed. |  |

#### Display Shipments for Components as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display shipments for components sent to the supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Check Components Shipment | Choose Fulfillment > Extended Collaboration > Components Shipment . | A list of delivery items with reference to the purchase order is displayed. |  |

#### Create a Component Receipt as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a component receipt for a ship notice as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Check Components Shipment | Choose Fulfillment > Extended Collaboration . |  |  |
| 3 | Check Component Shipments | On the Extended Collaboration screen, select the Components Shipment tab. | The Component Ship Notices table is displayed. |  |
| 4 | Select Your Ship Notice | In the Component Ship Notices table, select the checkbox for the row of your ship notice number and choose Create Component Receipt. | The Create Receipt screen is displayed. |  |
| 5 | Create Component Receipt for Your Ship Notice | In the Receipt # field, enter a receipt number and choose Next. | The Review screen is displayed. |  |
| 6 | Review Component Receipt | Review the component receipt of your ship notice and choose Submit. | The Extended Collaboration screen is displayed.Go to the Component Ship Notices table. For your ship notice, the status in the Receipt Status column is Fully Received. |  |

#### Check Updated Proof of Delivery in Outbound Delivery Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the updated proof of delivery in the outbound delivery document in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open the Display Outbound Delivery - Proof of Delivery (VLPODA) app. | The Proof of Delivery – Display Outbound Delivery screen is displayed. |  |
| 3 | Check the Outbound Delivery | In the Outbound Delivery field, enter the number of the purchase order.Choose Continue. | The Proof of Delivery - Delivery for Subcon. <Outbound Delivery Number> screen is displayed. |  |
| 4 | Review Updated POD | On the Overview POD tab, go to the All Items table.In the Itm column, double-click on the item number. | The Proof of Delivery - Delivery for Subcon. <Outbound Delivery Number>: Item Details screen is displayed. |  |
| 5 | Check POD Relevance Status | On the Processing tab, go to the Item status section. Check whether the POD field is marked with A.Note The following status values exist:--: Not ReleventA: Not Yet ProcessedB: Partially ProcessedC: Completely ProcessedChoose Exit. |  |  |

#### Create Shipping Notification as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a shipping notification in SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order that you've created in chapter and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order. | The Purchase Order: <Purchase Order Number> screen is displayed. |  |
| 4 | Create Shipping Notification | On the Purchase Order: <Purchase Order Number> screen, choose Create Ship Notice.Enter the following data according to your business requirements:ExamplePacking Slip ID: SLIP ##Actual Shipping Date: <Today>Actual Delivery Date: <Today> |  |  |
| 5 | Add Serial Numbers | At the line item level, select the Add Details link.In the Serial Number field, enter a unique serial number.Choose OK. | The serial numbers are added to the material. |  |
| 6 |  | Choose OK > Next > Submit > Done . | The shipping notification is created.The status of the purchase order is changed to Shipped. |  |

#### Check Inbound Delivery for Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check if an inbound delivery was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Select Purchase Order Item | Select the Items tab.From the Purchase Order Items table, select a row to view the purchse order item details. | The Purchase Order Item screen is displayed. |  |
| 6 | Display Supplier Confirmations | Select the Supplier Confirmations tab. | In the Delivery column, the Inbound Delivery Number is displayed.Note If the Delivery column is not visible, choose Settings (  ). In the Vieww Settings dialog box, select the Delivery checkbox and choose OK. |  |

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
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post the goods receipt after the goods ordered through a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Post | Choose Post. | The system message Goods receipt for inbound delivery <Inbound Delivery Number> posted (material document <Material Document Number>) is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the details of a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Warehouse Clerk. | SAP Fiori launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open the Material Documents Overview (F1077) app. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | To search for a goods receipt material document, enter the following search criteria according to your business requirements:Plant: 3310Purchase Order: <Purchase Order Number>Choose Go. | A search result table with material documents and material document items is displayed. |  |
| 4 | Select Goods Receipts Material Document | To view a material document, select a row from the search result table. | The Material Document <Material Document Number> screen is displayed. |  |
| 5 | Check Goods Receipts Details | Review the information displayed on the General Information and the Items tab.The value of the Number of Reversed Items field should be 0 of 1. |  |  |
| 6 | Display Process Flow | Select the Process Flow tab. | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |  |

#### Post Subsequent Stock Adjustment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post a subsequent stock adjustment to align the actual consumption with the stock level of the provided components in SAP S/4HANA.

A subsequent stock adjustment would be required if, for example, the recorded consumption (quantity of the provided components posted in the goods receipt issue) does not reflect the real or physical consumption during the production of the final product.

|  |
| --- |
| Example 2 PCs of component RM13 have been posted in the goods issue (according to the quantity listed in the component list of the purchase order line item). But the physical consumption was higher than expected (for example 3 PCs) due to a component with insufficient quality. |

Posting a subsequent stock adjustment is only possible if the corresponding purchase order item has already been posted in the goods receipt ([Post Goods Receipt](#unique_24) [page ] 38) and if the supplier did not report or add the actual consumption of consumed components during the creation of the advance shipping notice (ASN) in SAP Business Network ([Create Shipping Notification as a Supplier in SAP Business Network](#unique_21) [page ] 34).

|  |
| --- |
| Note The procedure is also possible for Batch and SERNR-managed items. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as an Inventory Manager . | SAP Fiori launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open the Post Subsequent Adjustment (F5476) app. | The Post Subsequent Adjustment screen is displayed. |  |
| 3 | Search for the Purchase Document | In the Purchasing Document field, enter a purchase order number.Note To search for a specific purchase order number, you can use the Value Help (  ). | The purchasing document is displayed. |  |
| 4 | Select the Line Item of the Purchasing Document | Go to the Items tab and select the line item 10. | The Goods Receipt Item screen is displayed. |  |
| 5 | Perform the Stock Adjustment for the Related Components | Go to the Components tab and enter the following data according to your business requirements:ExampleTo reflect the additional consumption of 1 PC, select Overconsumption from the dropdown list in the Goods Movement column.To reflect the reduced consumption of 1 PC, choose Underconsumption from the dropdown list in the Goods Movement column.In the Batch column, enter a batch number.Note To search for a specific batch number, you can use the Value Help (  ).In the Quantity column, enter a value greater than 0.Choose Apply. | A stock adjustment for the related components is performed. |  |
| 6 | Post the Subsequent Stock Adjustment | To post the subsequent stock adjustment, choose Post. | The subsequent stock adjustment is posted. A new material document is created, reflecting the additional or reduced consumption of the component stock provided to the subcontractor. |  |

#### Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the supplier invoice with PO/GR relation against the purchase order to be invoiced as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Pick the purchase order to be invoiced | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Invoice > Standard Invoice.If a supplier invoice needs to be created for a service entry sheet, select the service entry sheet under the selected purchase order and choose Create Invoice > Standard Invoice. | The Create Invoice screen is displayed. |  |
| 4 | Enter Supplier Invoice Data | On the Create Invoice screen, enter the following data according to your business requirements:Example Summary section:Invoice Number: <Invoice Number>Tax section:Category: Sales TaxRate (%): 0%Choose Update > Next. | The Invoice Submission screen is displayed. |  |
| 5 | Post Supplier Invoice | On the Invoice Submission screen, review the supplier invoice details and choose Submit.If the system requires a Remit To ID, naviagte to the Invoice Header section of the supplier invoice. Choose View/Edit Addresses. In the View/Edit Addresses dialog box, enter 1000 in the Remit To ID field. Choose OK > Update. | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition system. |  |

#### Display Invoice Status Change as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the updated status of the invoice that you've created for your subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Main Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Invoices search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Invoices screen is displayed with a search result list. |  |
| 3 | Display Invoice and Check Invoice Status | From the search result list, select the Invoice Number of the invoice you've created for your subcontracting purchase order.In the Invoice Status column, the status is displayed as either Sent or Approved. |  |  |

### Subcontracting with Serial Number Management

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a subcontracting purchase order in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Basic Data | On the Purchase Order screen, enter the following data in the Basic Data section:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300080Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310 |  |  |
| 5 | Enter Purchase Order Item | Select the Items tab. In the Purchase Order Items section, choose Create.Enter the following data according to your business requirements:ExampleItem Category: Subcontracting(L)Material: SG23Plant: 3310Order Quantity: 10 PCNet Order Price: 20AEDTax: <Input Tax Code> or <Input Tax Code> | A purchase order item is created. |  |
| 6 | Enter Supplier Confirmation Control | Select the newly created purchase order item to view detailed information.On the Purchase Order Item screen, select the Supplier Confirmation Control tab.In the Confirmation Control field, Select Confirmations 1 from the dropdown list. | The confirmation control is set for the purchase order item. |  |
| 7 | Save Purchase Order | Choose Apply > Order . | A new subcontracting purchase order is created. The system message Purchase Order has been saved is displayed.Note Make a note of the purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve and release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval (for Purchasing Group 001 and Purchasing Group 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchasing Manager role. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for the subcontracting purchase order you've created and select it.Note Purchase orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |  |
| 4 | Approve the Purchase Order | Choose Approve.In the Submit Decision dialog box, enter the approval reason if needed. Then, choose Submit. | The subcontracting purchase order is approved. |  |

#### Display Purchase Order as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order in the SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |

#### Confirm Purchase Order as a Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm a subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Confirm Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Order Confirmation > Confirm Entire Order .Enter the following data:Confirmation #: Subcon-01 | The Confirming PO screen is displayed. |  |
| 4 |  | On the Confirming PO screen, choose Next > Submit . | The status of the subcontracting purchase order is changed to Confirmed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order that you've created, enter the required search criteria and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network. | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |  |

#### Create Outbound Delivery for Subcontracting Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create an outbound delivery for a subcontracting purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Display Subcontracting Stocks by Supplier (ME2ON) app. | The Subcontracting Cockpit screen is displayed. |  |
| 3 | Search for Purchasing Documents | On the Subcontracting Cockpit screen, enter the following data:Supplier: 33300080With requirements from subcontracting Purchase Requisitions: Select the checkbox.With external receipts from Purchase Requisitions: Select the checkbox.With external receipts from Purchase Orders: Select the checkbox.Choose Execute. | A search result table is displayed. |  |
| 4 | Select Line Items of Subcontracting Purchase Order | For the following material descriptions, expand the Requirements via SC Orders entry by selecting the symbol in the Show/Hide column:Material RM33Material RM34In the Document Number column, find the line items of your subcontracting purchase order. To select the relevant entries, use Ctrl and select the checkbox in the Table selection menu column (1. column) of each line item.Choose Create Delivery. | The Create Delivery for Subcontracting Purchase Orders screen is displayed. |  |
| 5 | Create Delivery for Subcontracting Purchase Order | On the Create Delivery for Subcontracting Purchase Orders screen, go to the Stor. Loc. column. For each line item, enter 171C in the Stor. Loc. column field.To select the relevant entries, use Ctrl and select the checkbox in the Table selection menu column (1. column) of each line item.Choose Create Document.Note down your delivery number. | A delivery document for the subcontracting purchase order is created. |  |

#### Pick Delivery Item and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to enter the results of the picking process for a particular delivery. The picking process involves taking goods from a storage location, and staging the right quantity in a picking area, where the goods are prepared for shipping. The goods issue is posted in the SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Outbound Deliveries (F0867A) app. | The Manage Outbound Deliveries screen is displayed. |  |
| 3 | Search for Outbound Delivery | In the Outbound Delivery field, enter the outbound delivery document number.Choose Continue. | The Outbound Delivery <Outbound Delivery Number> Delivery Header screen is displayed. |  |
| 4 | Pick Delivery Item | Select the Picking tab.For the delivery item, enter the quantity in the Picking Quantity column that equals the quantity displayed in the Delivered Quantity column.Choose View Output. | The outbound delivery for a subcontracting purchase order is changed. |  |
| 5 | Add Items to Delivery | From the Serial Numbers section, click Add Multiple.The Select Serial Numbers for Materials pop-up is displayed.Under the Items section, select the check-boxes for the items to be added to the delivery, and choose OK.Choose Apply. | The selected items are added to the delivery. |  |
| 6 |  | Repeat step 5 for other item types in the delivery. |  |  |
| 7 | Save | Choose Save. | The outbound delivery is updated and saved. |  |
| 8 | Post Good Issue | On the Delivery Header screen, choose Post GI. | The goods issue is posted. |  |

#### Display Shipments for Components as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display shipments for components sent to the supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Check Components Shipment | Choose Fulfillment > Extended Collaboration > Components Shipment . | A list of delivery items with reference to the purchase order is displayed. |  |

#### Create a Component Receipt as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a component receipt for a ship notice as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Check Components Shipment | Choose Fulfillment > Extended Collaboration . |  |  |
| 3 | Check Component Shipments | On the Extended Collaboration screen, select the Components Shipment tab. | The Component Ship Notices table is displayed. |  |
| 4 | Select Your Ship Notice | In the Component Ship Notices table, select the checkbox for the row of your ship notice number and choose Create Component Receipt. | The Create Receipt screen is displayed. |  |
| 5 | Create Component Receipt for Your Ship Notice | In the Receipt # field, enter a receipt number and choose Next. | The Review screen is displayed. |  |
| 6 | Review Component Receipt | Review the component receipt of your ship notice and choose Submit. | The Extended Collaboration screen is displayed.Go to the Component Ship Notices table. For your ship notice, the status in the Receipt Status column is Fully Received. |  |

#### Check Updated Proof of Delivery in Outbound Delivery Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the updated proof of delivery in the outbound delivery document in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open the Display Outbound Delivery - Proof of Delivery (VLPODA) app. | The Proof of Delivery – Display Outbound Delivery screen is displayed. |  |
| 3 | Check the Outbound Delivery | In the Outbound Delivery field, enter the number of the purchase order.Choose Continue. | The Proof of Delivery - Delivery for Subcon. <Outbound Delivery Number> screen is displayed. |  |
| 4 | Review Updated POD | On the Overview POD tab, go to the All Items table.In the Itm column, double-click on the item number. | The Proof of Delivery - Delivery for Subcon. <Outbound Delivery Number>: Item Details screen is displayed. |  |
| 5 | Check POD Relevance Status | On the Processing tab, go to the Item status section. Check whether the POD field is marked with A.Note The following status values exist:--: Not ReleventA: Not Yet ProcessedB: Partially ProcessedC: Completely ProcessedChoose Exit. |  |  |

#### Create Shipping Notification as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a shipping notification in SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order that you've created in chapter and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order. | The Purchase Order: <Purchase Order Number> screen is displayed. |  |
| 4 | Create Shipping Notification | On the Purchase Order: <Purchase Order Number> screen, choose Create Ship Notice.Enter the following data according to your business requirements:ExamplePacking Slip ID: SLIP ##Actual Shipping Date: <Today>Actual Delivery Date: <Today> |  |  |
| 5 | Add Serial Numbers | At the line item level, select the Add Details link.In the Serial Number field, enter a unique serial number.Choose OK. | The serial numbers are added to the material. |  |
| 6 | Add Component Consumption | At the line item level, select the Add Details link.In the Consumed Components table, add the consumed quantity in the Quantity field, and enter Batch (for batch-managed materials).Choose OK > Next > Submit > Done . | The shipping notification is created.The status of the purchase order is changed to Shipped. |  |

#### Check Inbound Delivery for Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check if an inbound delivery was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Select Purchase Order Item | Select the Items tab.From the Purchase Order Items table, select a row to view the purchse order item details. | The Purchase Order Item screen is displayed. |  |
| 6 | Display Supplier Confirmations | Select the Supplier Confirmations tab. | In the Delivery column, the Inbound Delivery Number is displayed.Note If the Delivery column is not visible, choose Settings (  ). In the Vieww Settings dialog box, select the Delivery checkbox and choose OK. |  |

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
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post the goods receipt after the goods ordered through a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Post | Choose Post. | The system message Goods receipt for inbound delivery <Inbound Delivery Number> posted (material document <Material Document Number>) is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the details of a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Warehouse Clerk. | SAP Fiori launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open the Material Documents Overview (F1077) app. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | To search for a goods receipt material document, enter the following search criteria according to your business requirements:Plant: 3310Purchase Order: <Purchase Order Number>Choose Go. | A search result table with material documents and material document items is displayed. |  |
| 4 | Select Goods Receipts Material Document | To view a material document, select a row from the search result table. | The Material Document <Material Document Number> screen is displayed. |  |
| 5 | Check Goods Receipts Details | Review the information displayed on the General Information and the Items tab.The value of the Number of Reversed Items field should be 0 of 1. |  |  |
| 6 | Display Process Flow | Select the Process Flow tab. | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |  |

#### Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the supplier invoice with PO/GR relation against the purchase order to be invoiced as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Pick the purchase order to be invoiced | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Invoice > Standard Invoice.If a supplier invoice needs to be created for a service entry sheet, select the service entry sheet under the selected purchase order and choose Create Invoice > Standard Invoice. | The Create Invoice screen is displayed. |  |
| 4 | Enter Supplier Invoice Data | On the Create Invoice screen, enter the following data according to your business requirements:Example Summary section:Invoice Number: <Invoice Number>Tax section:Category: Sales TaxRate (%): 0%Choose Update > Next. | The Invoice Submission screen is displayed. |  |
| 5 | Post Supplier Invoice | On the Invoice Submission screen, review the supplier invoice details and choose Submit.If the system requires a Remit To ID, naviagte to the Invoice Header section of the supplier invoice. Choose View/Edit Addresses. In the View/Edit Addresses dialog box, enter 1000 in the Remit To ID field. Choose OK > Update. | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition system. |  |

#### Display Invoice Status Change as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the updated status of the invoice that you've created for your subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Main Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Invoices search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Invoices screen is displayed with a search result list. |  |
| 3 | Display Invoice and Check Invoice Status | From the search result list, select the Invoice Number of the invoice you've created for your subcontracting purchase order.In the Invoice Status column, the status is displayed as either Sent or Approved. |  |  |

### Subcontracting with Batch-Managed Material

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a subcontracting purchase order in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Basic Data | On the Purchase Order screen, enter the following data in the Basic Data section:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300080Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310 |  |  |
| 5 | Enter Purchase Order item | Select the Items tab. In the Purchase Order Items section, choose Create.Enter the following data according to your business requirements:ExampleItem Category: Subcontracting(L)Material: SG24Plant: 3310Order Quantity: 10 CCMNet Order Price: 0.15AEDNote In the Scheduled Lines section, note down the quantities for each component as they have to be entered in [Pick Delivery Item and Post Goods Issue](#unique_51) [page ] 68. | A purchase order item is created. |  |
| 6 | Enter Supplier Confirmation Control | Select the newly created purchase order item to view detailed information.On the Purchase Order Item screen, select the Supplier Confirmation Control tab.In the Confirmation Control field, Select Confirmations 1 from the dropdown list. | The confirmation control is set for the purchase order item. |  |
| 7 | Save Purchase Order | Choose Apply > Order . | A new subcontracting purchase order is created. The system message Purchase Order has been saved is displayed.Note Make a note of the purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve and release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval (for Purchasing Group 001 and Purchasing Group 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchasing Manager role. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for the subcontracting purchase order you've created and select it.Note Purchase orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |  |
| 4 | Approve the Purchase Order | Choose Approve.In the Submit Decision dialog box, enter the approval reason if needed. Then, choose Submit. | The subcontracting purchase order is approved. |  |

#### Display Purchase Order as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order in the SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |

#### Confirm Purchase Order as a Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm a subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Confirm Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Order Confirmation > Confirm Entire Order .Enter the following data:Confirmation #: Subcon-01 | The Confirming PO screen is displayed. |  |
| 4 |  | On the Confirming PO screen, choose Next > Submit . | The status of the subcontracting purchase order is changed to Confirmed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order that you've created, enter the required search criteria and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network. | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |  |

#### Create Outbound Delivery for Subcontracting Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create an outbound delivery for a subcontracting purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Display Subcontracting Stocks by Supplier (ME2ON) app. | The Subcontracting Cockpit screen is displayed. |  |
| 3 | Search for Purchasing Documents | On the Subcontracting Cockpit screen, enter the following data:Supplier: 33300080With requirements from subcontracting Purchase Requisitions: Select the checkbox.With external receipts from Purchase Requisitions: Select the checkbox.With external receipts from Purchase Orders: Select the checkbox.Choose Execute. | A search result table is displayed. |  |
| 4 | Select Line Items of Subcontracting Purchase Order | For the following material descriptions, expand the Requirements via SC Orders entry by selecting the symbol in the Show/Hide column:Material RM09Material RM19In the Document Number column, find the line items of your subcontracting purchase order. To select the relevant entries, use Ctrl and select the checkbox in the Table selection menu column (1. column) of each line item.Choose Create Delivery. | The Create Delivery for Subcontracting Purchase Orders screen is displayed. |  |
| 5 | Create Delivery for Subcontracting Purchase Order | On the Create Delivery for Subcontracting Purchase Orders screen, go to the Stor. Loc. column. For each line item, enter 171C in the Stor. Loc. column field.Enter the batch number for each component.To select the relevant entries, use Ctrl and select the checkbox in the Table selection menu column (1. column) of each line item.Choose Create Document.Note down your delivery number. | A delivery document for the subcontracting purchase order is created. |  |

#### Pick Delivery Item and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to enter the results of the picking process for a particular delivery. The picking process involves taking goods from a storage location, and staging the right quantity in a picking area, where the goods are prepared for shipping. The goods issue is posted in the SAP S/4HANA .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed. |  |
| 3 | Search for Outbound Delivery | In the Outbound Delivery field, enter the outbound delivery number.Choose Continue. | The Outbound Delivery <Outbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Pick Delivery Item | Select the Picking tab.For the delivery item, enter the quantity in the Picked Qty column that equals the quantity displayed in the Deliv. Qty column.Note Add correct quantities for each purchase order that you've created.Choose Save. | The outbound delivery for a subcontracting purchase order is changed. |  |
| 5 | Post Goods Issue | On the Change Outbound Delivery (Original) screen, choose Post Goods Issue (Original). | The goods issue is posted. |  |

#### Display Shipments for Components as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display shipments for components sent to the supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Check Components Shipment | Choose Fulfillment > Extended Collaboration > Components Shipment . | A list of delivery items with reference to the purchase order is displayed. |  |

#### Create a Component Receipt as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a component receipt for a ship notice as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Check Components Shipment | Choose Fulfillment > Extended Collaboration . |  |  |
| 3 | Check Component Shipments | On the Extended Collaboration screen, select the Components Shipment tab. | The Component Ship Notices table is displayed. |  |
| 4 | Select Your Ship Notice | Note Ensure to enter correct quantities and relevant batch numbers in the Consumed Components table.In the Component Ship Notices table, select the checkbox for the row of your ship notice number and choose Create Component Receipt. | The Create Receipt screen is displayed. |  |
| 5 | Create Component Receipt for Your Ship Notice | In the Receipt # field, enter a receipt number and choose Next. | The Review screen is displayed. |  |
| 6 | Review Component Receipt | Review the component receipt of your ship notice and choose Submit. | The Extended Collaboration screen is displayed.Go to the Component Ship Notices table. For your ship notice, the status in the Receipt Status column is Fully Received. |  |

#### Check Updated Proof of Delivery in Outbound Delivery Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the updated proof of delivery in the outbound delivery document in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open the Display Outbound Delivery - Proof of Delivery (VLPODA) app. | The Proof of Delivery – Display Outbound Delivery screen is displayed. |  |
| 3 | Check the Outbound Delivery | In the Outbound Delivery field, enter the number of the purchase order.Choose Continue. | The Proof of Delivery - Delivery for Subcon. <Outbound Delivery Number> screen is displayed. |  |
| 4 | Review Updated POD | On the Overview POD tab, go to the All Items table.In the Itm column, double-click on the item number. | The Proof of Delivery - Delivery for Subcon. <Outbound Delivery Number>: Item Details screen is displayed. |  |
| 5 | Check POD Relevance Status | On the Processing tab, go to the Item status section. Check whether the POD field is marked with A.Note The following status values exist:--: Not ReleventA: Not Yet ProcessedB: Partially ProcessedC: Completely ProcessedChoose Exit. |  |  |

#### Create Shipping Notification as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a shipping notification in SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order. | The Purchase Order: <Purchase Order Number> screen is displayed. |  |
| 4 | Create Shipping Notification | On the Purchase Order: <Purchase Order Number> screen, choose Create Ship Notice.Enter the following data according to your business requirements:ExamplePacking Slip ID: SLIP ##Actual Shipping Date: <Today>Actual Delivery Date: <Today> |  |  |
| 5 | Add Batch Information | In the Order Items section, enter the following data according to your business requirements:ExampleSupplier Batch ID: Batch ##Production Date: <Today>Expiry Date: <Today> + 1 yearChoose OK. | The batch number is added to the material. |  |
| 6 | Add Component Consumption | At the line item level, select the Add Details link.In the Consumed Components table, add the consumed quantity in the Quantity field, and enter Batch on component level (for batch-managed materials).Choose OK > Next > Submit > Done . | The shipping notification is created.The status of the purchase order is changed to Shipped. |  |

#### Check Inbound Delivery for Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check if an inbound delivery was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Select Purchase Order Item | Select the Items tab.From the Purchase Order Items table, select a row to view the purchse order item details. | The Purchase Order Item screen is displayed. |  |
| 6 | Display Supplier Confirmations | Select the Supplier Confirmations tab. | In the Delivery column, the Inbound Delivery Number is displayed.Note If the Delivery column is not visible, choose Settings (  ). In the Vieww Settings dialog box, select the Delivery checkbox and choose OK. |  |

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
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post the goods receipt after the goods ordered through a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Post | Choose Post. | The system message Goods receipt for inbound delivery <Inbound Delivery Number> posted (material document <Material Document Number>) is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the details of a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Warehouse Clerk. | SAP Fiori launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open the Material Documents Overview (F1077) app. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | To search for a goods receipt material document, enter the following search criteria according to your business requirements:Plant: 3310Purchase Order: <Purchase Order Number>Choose Go. | A search result table with material documents and material document items is displayed. |  |
| 4 | Select Goods Receipts Material Document | To view a material document, select a row from the search result table. | The Material Document <Material Document Number> screen is displayed. |  |
| 5 | Check Goods Receipts Details | Review the information displayed on the General Information and the Items tab.The value of the Number of Reversed Items field should be 0 of 3. |  |  |
| 6 | Display Process Flow | Select the Process Flow tab. | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |  |

#### Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the supplier invoice with PO/GR relation against the purchase order to be invoiced as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Pick the purchase order to be invoiced | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Invoice > Standard Invoice.If a supplier invoice needs to be created for a service entry sheet, select the service entry sheet under the selected purchase order and choose Create Invoice > Standard Invoice. | The Create Invoice screen is displayed. |  |
| 4 | Enter Supplier Invoice Data | On the Create Invoice screen, enter the following data according to your business requirements:Example Summary section:Invoice Number: <Invoice Number>Tax section:Category: Sales TaxRate (%): 0%Choose Update > Next. | The Invoice Submission screen is displayed. |  |
| 5 | Post Supplier Invoice | On the Invoice Submission screen, review the supplier invoice details and choose Submit.If the system requires a Remit To ID, naviagte to the Invoice Header section of the supplier invoice. Choose View/Edit Addresses. In the View/Edit Addresses dialog box, enter 1000 in the Remit To ID field. Choose OK > Update. | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition system. |  |

#### Display Invoice Status Change as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the updated status of the invoice that you've created for your subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Main Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Invoices search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Invoices screen is displayed with a search result list. |  |
| 3 | Display Invoice and Check Invoice Status | From the search result list, select the Invoice Number of the invoice you've created for your subcontracting purchase order.In the Invoice Status column, the status is displayed as either Sent or Approved. |  |  |

### Subcontracting with Packing Instruction

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a subcontracting purchase order in the SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Basic Data | On the Purchase Order screen, enter the following data in the Basic Data section:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300085Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310 |  |  |
| 5 | Enter Purchase Order item | Select the Items tab. In the Purchase Order Items section, choose Create.Enter the following data according to your business requirements:ExampleItem Category: <Blank>Material: TG0011Plant: 3310Order Quantity: 10 PCNet Order Price: 0.15AED | A purchase order item is created. |  |
| 6 | Enter Supplier Confirmation Control | Select the newly created purchase order item to view detailed information.On the Purchase Order Item screen, select the Supplier Confirmation Control tab.In the Confirmation Control field, Select Confirmations 1 from the dropdown list. | The confirmation control is set for the purchase order item. |  |
| 7 | Save Purchase Order | Choose Apply > Order . | A new subcontracting purchase order is created. The system message Purchase Order has been saved is displayed.Note Make a note of the purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve and release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval (for Purchasing Group 001 and Purchasing Group 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchasing Manager role. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for the subcontracting purchase order you've created and select it.Note Purchase orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |  |
| 4 | Approve the Purchase Order | Choose Approve.In the Submit Decision dialog box, enter the approval reason if needed. Then, choose Submit. | The subcontracting purchase order is approved. |  |

#### Display Purchase Order as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order in the SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |

#### Confirm Purchase Order as a Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm a subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Confirm Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Order Confirmation > Confirm Entire Order .Enter the following data:Confirmation #: Subcon-01 | The Confirming PO screen is displayed. |  |
| 4 |  | On the Confirming PO screen, choose Next > Submit . | The status of the subcontracting purchase order is changed to Confirmed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order that you've created, enter the required search criteria and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network. | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |  |

#### Create Shipping Notification with Handling Unit as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a shipping notification in SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order. | The Purchase Order: <Purchase Order Number> screen is displayed. |  |
| 4 | Create Shipping Notification | On the Purchase Order: <Purchase Order Number> screen, choose Create Ship Notice.Enter the following data according to your business requirements:ExamplePacking Slip ID: SLIP ##Actual Shipping Date: <Today>Actual Delivery Date: <Today> |  |  |
| 5 | Add Serial Number | At the line item level, select the Add Details link.In the Serial Number field, enter a unique serial number.Choose OK. | A serial number is added to the material. |  |
| 6 | Add Packing Instruction | Choose Pack Items.The items are automatically assigned.Choose Next > Next . | The Confirm Packing Plan screen is displayed. |  |
| 7 | Add Component Consumption | At the line item level, select the Add Details link.In the Consumed Components table, add the consumed quantity in the Quantity field and enter Batch (for bacth-managed materials).Choose OK > Next > Submit > Done . | The shipping notification is created. The status of the purchase order is changed to Shipped. |  |

#### Check Inbound Delivery for Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check if an inbound delivery was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Select Purchase Order Item | Select the Items tab.From the Purchase Order Items table, select a row to view the purchse order item details. | The Purchase Order Item screen is displayed. |  |
| 6 | Display Supplier Confirmations | Select the Supplier Confirmations tab. | In the Delivery column, the Inbound Delivery Number is displayed.Note If the Delivery column is not visible, choose Settings (  ). In the Vieww Settings dialog box, select the Delivery checkbox and choose OK. |  |
| 7 | Display Handling Unit | Select the Handling Unit tab. | The Handling Unit Information is displayed. |  |

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
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post the goods receipt after the goods ordered through a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Post | Choose Post. | The system message Goods receipt for inbound delivery <Inbound Delivery Number> posted (material document <Material Document Number>) is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the details of a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Warehouse Clerk. | SAP Fiori launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open the Material Documents Overview (F1077) app. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | To search for a goods receipt material document, enter the following search criteria according to your business requirements:Plant: 3310Purchase Order: <Purchase Order Number>Choose Go. | A search result table with material documents and material document items is displayed. |  |
| 4 | Select Goods Receipts Material Document | To view a material document, select a row from the search result table. | The Material Document <Material Document Number> screen is displayed. |  |
| 5 | Check Goods Receipts Details | Review the information displayed on the General Information and the Items tab.The value of the Number of Reversed Items field should be 0 of 1. |  |  |
| 6 | Display Process Flow | Select the Process Flow tab. | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |  |

#### Create a Supplier Invoice linked to a Scheduling Agreement in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure explains how to create a supplier invoice linked to a scheduling agreement in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Pick the purchase order to be invoiced | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Invoice > Standard Invoice.If a supplier invoice needs to be created for a service entry sheet, select the service entry sheet under the selected purchase order and choose Create Invoice > Standard Invoice. | The Create Invoice screen is displayed. |  |
| 4 | Enter Supplier Invoice Data | On the Create Invoice screen, enter the following data according to your business requirements:Example Summary section:Invoice Number: <Invoice Number>Tax section:Category: Sales TaxRate (%): 0%Choose Update > Next. | The Invoice Submission screen is displayed. |  |
| 5 | Post Supplier Invoice | On the Invoice Submission screen, review the supplier invoice details and choose Submit.If the system requires a Remit To ID, naviagte to the Invoice Header section of the supplier invoice. Choose View/Edit Addresses. In the View/Edit Addresses dialog box, enter 1000 in the Remit To ID field. Choose OK > Update. | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition. |  |

#### Display Invoice Status Change as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the updated status of the invoice that you've created for your subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Main Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Invoices search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Invoices screen is displayed with a search result list. |  |
| 3 | Display Invoice and Check Invoice Status | From the search result list, select the Invoice Number of the invoice you've created for your subcontracting purchase order.In the Invoice Status column, the status is displayed as either Sent or Approved. |  |  |

### Scheduling Agreement with SAP Business Network

#### Create Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a scheduling agreement in SAP S/4HANA Cloud Public Edition, and also describes how to create the Scheduling Agreement for the Consignment type (optional).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Scheduling Agreements (F2179) app. | The Manage Purchase Scheduling Agreements screen is displayed. |  |
| 3 | Create Scheduling Agreement | Choose Create. | The New Purchase Scheduling Agreement screen is displayed. |  |
| 4 | Enter Header Data | On the New Purchase Scheduling Agreement screen, enter the following data in the Basic Data section:Supplier: 33300001Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310Agreement Type: From the dropdown menu, select SA with Release Doc (LPA).Valid Start: <Default Today>Valid End: <MM/DD/YYYY>In the Payment Terms section, enter the following data:Select a document currency. |  |  |
| 5 | Enter Scheduling Agreement Item(Optional) E Scheduling Agreement with Consignment type | Select the Items tab. Choose Create.Enter the following data according to your business requirements:ExampleItem Category: <Blank>Material: RM129Plant: 3310Tax Code: <Input Tax Code>Tax Date: <Default Today>Order Quantity: 10 PC(Optional): For the Scheduling Agreement for the Consignment type:ExampleItem Category: K <Consignment>Material: RM128Plant: 1710Tax Code: I1Tax Date: <Default Today>Order Quantity: 200In the Output Control section, enter the following data:Creation Profile: 0001 | A scheduling agreement item is created. |  |
| 6 | Enter Supplier Confirmation Control | Select the newly created scheduling agreement item to view detailed information.On the Scheduling Agreement Item screen, select the Handling tab.In the Confirmation Control field, Select Confirmations 1 from the dropdown list. | The confirmation control is set for the scheduling agreement item. |  |
| 7 | Enter the Scheduling control | On the Scheduling Control tab, enter the following data:Firm Zone: 1Trade Off Zone: 1 | The Scheduling Control is set. |  |
| 8 | Save | Go back to the New Purchase Scheduling Agreement header view and choose Create. | A new scheduling agreement is created. |  |

#### Maintain Delivery Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create delivery schedules for scheduling agreements when they haven't been maintained during the agreement's creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Scheduling Agreements (F2179) app. | The Manage Purchase Scheduling Agreements screen is displayed. |  |
| 3 | Find Scheduling Agreement Number | Find the scheduling agreement number using the search filter criteria, such as:Supplier: 33300001Purchasing Org.: 3310Agreement Type: From the dropdown menu, select SA with Release Doc (LPA)..Choose Go. | In the search results list, the purchase scheduling agreement is displayed. |  |
| 4 | Select Scheduling Agreement | Select the scheduling agreement from the search results list to go to the details page. | The scheduling agreement is displayed in Display mode. |  |
| 5 | Maintain Delivery Schedule | Choose Edit.On the Items tab, select an item for which you want to create a delovery schedule. | The Purchase Scheduling Agreement Item screen is displayed. |  |
| 6 |  | Go to the Schedule Lines section and choose Create.Enter the following data according to your business requirements:Data Type: <Day Format>Delivery Date: <Today>Delivery Time: <Time Format>Scheduled Quantity: <10>To add a schedule line, choose Apply twice. | The Purchase Scheduling Agreement Item screen is displayed. |  |
| 7 | Save | Choose Save. | The scheduling agreement is updated with the delivery schedule. |  |

#### Release Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to release a scheduling agreement in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Scheduling Agreements (F2179) app. | The Manage Purchase Scheduling Agreements screen is displayed. |  |
| 3 | Find Scheduling Agreement Number | Find the scheduling agreement number using the search filter criteria, such as:Supplier: 33300001Purchasing Org.: 3310Agreement Type: From the dropdown menu, select SA with Release Doc (LPA).. | In the search results list, the purchase scheduling agreement is displayed. |  |
| 4 | Option 1: Release at Schedule Agreement Level | Select the scheduling agreement and choose one of the following options:Release > Release: Forecast and JIT ScheduleRelease > Forecast ScheduleRelease > JIT ScheduleIn the Release: Forecast and JIT Schedule dialog box, choose Release. | The Purchase Scheduling Agreement Item screen is displayed. |  |
| 5 | Option 2: Release at Schedule Agreement Item Level | Select the scheduling agreement and choose the chevron.Go to the Items tab.Select an item and choose one of the following options:Release > Generate Forecast Schedule > Release > OKRelease > Generate JIT Schedule > Release > OK | The release document is immediately issued to the supplier. The document status changes to Sent. |  |

#### Display Scheduling Agreement as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the scheduling agreement in the SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Scheduling Agreement Number | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the scheduling agreement number and start the search. | A search results list is displayed. |  |
| 3 | Displayed Scheduling Agreement Line Items | From the search results list, select the Scheduling Agreement Number.On the Scheduling Agreement: <Scheduling Agreement> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected scheduling agreement are displayed. |  |

#### Create Shipping Notification as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a shipping notification in SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order. | The Purchase Order: <Purchase Order Number> screen is displayed. |  |
| 4 | Create Shipping Notification | On the Purchase Order: <Purchase Order Number> screen, choose Create Ship Notice.Enter the following data according to your business requirements:ExamplePacking Slip ID: SLIP ##Actual Shipping Date: <Today>Actual Delivery Date: <Today> |  |  |
| 5 | Add Batch Information | In the Order Items section, enter the following data according to your business requirements:ExampleSupplier Batch ID: Batch ##Production Date: <Today>Expiry Date: <Today> + 1 yearChoose OK. | The batch number is added to the material. |  |
| 6 | Add Component Consumption | At the line item level, select the Add Details link.In the Consumed Components table, add the consumed quantity in the Quantity field, and enter Batch on component level (for batch-managed materials).Choose OK > Next > Submit > Done . | The shipping notification is created.The status of the purchase order is changed to Shipped. |  |

#### Get Inbound Delivery Number

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to get the inbound delivery number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Display Scheduling Agreement (ME33L) app. | The Display Scheduling Agreement screen is displayed. |  |
| 3 | Display Scheduling Agreement Item | In the Agreement field, enter the scheduling agreement number. Choose Overview. | The Display Scheduling Areement: Item Overview screen is displayed. |  |
| 4 | Get Inbound Delivery Number | In the Outline Agreement Items table, select the agreement item and choose Item > Confirmations > Overview . | The Display Scheduling Areement: Item <Agreement Item Number> screen is displayed.In the Supplier Confirmations table, the inbound delivery number is displayed. |  |

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
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post the goods receipt after the goods ordered through a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Post | Choose Post. | The system message Goods receipt for inbound delivery <Inbound Delivery Number> posted (material document <Material Document Number>) is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the details of a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Warehouse Clerk. | SAP Fiori launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open the Material Documents Overview (F1077) app. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | To search for a goods receipt material document, enter the following search criteria according to your business requirements:Plant: 3310Purchase Order: <Scheduling AGreement>Choose Go. | A search result table with material documents and material document items is displayed. |  |
| 4 | Select Goods Receipts Material Document | To view a material document, select a row from the search result table. | The Material Document <Material Document Number> screen is displayed. |  |
| 5 | Check Goods Receipts Details | Review the information displayed on the General Information and the Items tab.The value of the Number of Reversed Items field should be 0 of 1. |  |  |
| 6 | Display Process Flow | Select the Process Flow tab. | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |  |

#### Create Supplier Invoice with PO/GR Relation as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the supplier invoice with PO/GR relation against the purchase order to be invoiced as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Pick the purchase order to be invoiced | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Invoice > Standard Invoice.If a supplier invoice needs to be created for a service entry sheet, select the service entry sheet under the selected purchase order and choose Create Invoice > Standard Invoice. | The Create Invoice screen is displayed. |  |
| 4 | Enter Supplier Invoice Data | On the Create Invoice screen, enter the following data according to your business requirements:Example Summary section:Invoice Number: <Invoice Number>Tax section:Category: Sales TaxRate (%): 0%Choose Update > Next. | The Invoice Submission screen is displayed. |  |
| 5 | Post Supplier Invoice | On the Invoice Submission screen, review the supplier invoice details and choose Submit.If the system requires a Remit To ID, naviagte to the Invoice Header section of the supplier invoice. Choose View/Edit Addresses. In the View/Edit Addresses dialog box, enter 1000 in the Remit To ID field. Choose OK > Update. | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition system. |  |

#### Display Invoice Status Change as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the updated status of the invoice that you've created for your subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Main Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Invoices search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Invoices screen is displayed with a search result list. |  |
| 3 | Display Invoice and Check Invoice Status | From the search result list, select the Invoice Number of the invoice you've created for your subcontracting purchase order.In the Invoice Status column, the status is displayed as either Sent or Approved. |  |  |

### Multi-Tier Subcontracting

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a subcontracting purchase order in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Basic Data | On the Purchase Order screen, enter the following data in the Basic Data section:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300001Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310 |  |  |
| 5 | Enter Purchase Order Item | Select the Items tab. In the Purchase Order Items section, choose Create.Enter the following data according to your business requirements:ExampleItem Category:Material: RM13Plant: 3310Order Quantity: 10 PC: 20AEDTax: <Input Tax Code> or <Input Tax Code> | A purchase order item is created. |  |
| 6 | Enter the Partner Function | In the Partner section, choose Create.Enter the following data according to your business requirements:ExamplePartner Function: CS (Multi-Tier Supplier)Partner: 33300001 (Multi-Tier Supplier) |  |  |
| 7 | Enter Supplier Confirmation Control | Select the newly created purchase order item to view detailed information.On the Purchase Order Item screen, select the Supplier Confirmation Control tab.In the Confirmation Control field, Select Confirmations 1 from the dropdown list. | The confirmation control is set for the purchase order item. |  |
| 8 | Save Purchase Order | Choose Apply > Order. | A new subcontracting purchase order is created. The system message Purchase Order has been saved is displayed.Note Make a note of the purchase order number. |  |
| 9 | (Optional) | To post goods receipts into subcontractor stock for multi-tier purchase order line items, maintain two fields in the Create Purchase Order - Advanced (ME21N) app.To do so, open the Create Purchase Order - Advanced (ME21N) app and select the same purchase order. Go to the Delivery Address tab. In the Supplier field, enter the multi-tier supplier ID. Select the SC (Subcontractor) checkbox. |  |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve and release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval (for Purchasing Group 001 and Purchasing Group 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchasing Manager role. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for the subcontracting purchase order you've created and select it.Note Purchase orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |  |
| 4 | Approve the Purchase Order | Choose Approve.In the Submit Decision dialog box, enter the approval reason if needed. Then, choose Submit. | The subcontracting purchase order is approved. |  |

#### Display Purchase Order as a Main Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the subcontracting purchase order in the SAP Business Network as a main supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Main Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |

#### Display Purchase Order as a Multi-Tier Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the subcontracting purchase order in the SAP Business Network as a multi-tier supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Multi-Tier Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, go to the Fulfillment tab. From the dropdown menu, select ExTended Collaboration. | The ExTended Collaboration screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |

#### Confirm Purchase Order as a Main Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm a subcontracting purchase order as a main supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Confirm Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Order Confirmation > Confirm Entire Order .Enter the following data:Confirmation #: Subcon-01 | The Confirming PO screen is displayed. |  |
| 4 |  | On the Confirming PO screen, choose Next > Submit . | The status of the subcontracting purchase order is changed to Confirmed. |  |

#### Check Order Confirmation as a Multi-Tier Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the copy of a confirmed subcontracting purchase order in the SAP Business Network as a multi-tier supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, go to the Fulfillment tab. From the dropdown menu, select Extended Collaboration. | The Extended Collaboration screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |
| 4 | Display Order Confirmation | On the details page of the purchase order, go to the Order History tab. In the History section, review the copy of the confirmed subcontracting purchase order. | The Purchase Order screen is displayed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order that you've created, enter the required search criteria and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network. | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |  |

#### Create Shipping Notification as a Main Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a shipping notification in SAP Business Network as a main supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order. | The Purchase Order: <Purchase Order Number> screen is displayed. |  |
| 4 | Create Shipping Notification | On the Purchase Order: <Purchase Order Number> screen, choose Create Ship Notice.Enter the following data according to your business requirements:ExamplePacking Slip ID: SLIP ##Actual Shipping Date: <Today>Actual Delivery Date: <Today> |  |  |
| 5 | Add Batch Information | In the Order Items section, enter the following data according to your business requirements:ExampleSupplier Batch ID: Batch ##Production Date: <Today>Expiry Date: <Today> + 1 yearChoose OK. | The batch number is added to the material. |  |
| 6 | Add Component Consumption | At the line item level, select the Add Details link.In the Consumed Components table, add the consumed quantity in the Quantity field, and enter Batch on component level (for batch-managed materials).Choose OK > Next > Submit > Done . | The shipping notification is created.The status of the purchase order is changed to Shipped. |  |

#### Display Shipping Notification as a Multi-Tier Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the shipping notification in the SAP Business Network as a multi-tier supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Multi-Tier Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, go to the Fulfillment tab. From the dropdown menu, select ExTended Collaboration. | The ExTended Collaboration screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected purchase order are displayed. |  |

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
| # | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| # | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| # | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| # | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post the goods receipt after the goods ordered through a purchase order arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Receiving Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Post | Choose Post. | The system message Goods receipt for inbound delivery <Inbound Delivery Number> posted (material document <Material Document Number>) is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the details of a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Warehouse Clerk. | SAP Fiori launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open the Material Documents Overview (F1077) app. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | To search for a goods receipt material document, enter the following search criteria according to your business requirements:Plant: 3310Purchase Order: <Purchase Order Number>Choose Go. | A search result table with material documents and material document items is displayed. |  |
| 4 | Select Goods Receipts Material Document | To view a material document, select a row from the search result table. | The Material Document <Material Document Number> screen is displayed. |  |
| 5 | Check Goods Receipts Details | Review the information displayed on the General Information and the Items tab.The value of the Number of Reversed Items field should be 0 of 1. |  |  |
| 6 | Display Process Flow | Select the Process Flow tab. | In the Process Flow chart, the Material Document and the Accounting Document are displayed. |  |

#### Create Supplier Invoice with PO/GR Relation as a Main Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the supplier invoice with PO/GR relation against the purchase order to be invoiced as a main supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Pick the purchase order to be invoiced | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Invoice > Standard Invoice.If a supplier invoice needs to be created for a service entry sheet, select the service entry sheet under the selected purchase order and choose Create Invoice > Standard Invoice. | The Create Invoice screen is displayed. |  |
| 4 | Enter Supplier Invoice Data | On the Create Invoice screen, enter the following data according to your business requirements:Example Summary section:Invoice Number: <Invoice Number>Tax section:Category: Sales TaxRate (%): 0%Choose Update > Next. | The Invoice Submission screen is displayed. |  |
| 5 | Post Supplier Invoice | On the Invoice Submission screen, review the supplier invoice details and choose Submit.If the system requires a Remit To ID, naviagte to the Invoice Header section of the supplier invoice. Choose View/Edit Addresses. In the View/Edit Addresses dialog box, enter 1000 in the Remit To ID field. Choose OK > Update. | The supplier invoice is submitted to SAP Business Network. It is routed to the buyer's SAP S/4HANA Cloud Public Edition system. |  |

#### Display Invoice Status Change as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the updated status of the invoice that you've created for your subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Main Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Invoices search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Invoices screen is displayed with a search result list. |  |
| 3 | Display Invoice and Check Invoice Status | From the search result list, select the Invoice Number of the invoice you've created for your subcontracting purchase order.In the Invoice Status column, the status is displayed as either Sent or Approved. |  |  |

### Purchase Order with Item Type Consignment

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchase order with Item type Consignment in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Basic Data | On the Purchase Order screen, enter the following data in the Basic Data section:Purchasing Doc. Type: Standard PO (NB)Supplier: 10300001Company Code: 1010Purchasing Group: 001Purchasing Org.: 1010 |  |  |
| 5 | Enter Purchase Order Item | Select the Items tab. In the Purchase Order Items section, choose Create.Enter the following data according to your business requirements:ExampleItem Category: KMaterial: RM128Plant: 1010Order Quantity: 10 PCNet Order Price: 20AEDTax: <Input tax code> | A purchase order item is created. |  |
| 6 | Enter Supplier Confirmation Control | Select the newly created purchase order item to view detailed information.On the Purchase Order Item screen, select the Supplier Confirmation Control tab.In the Confirmation Control field, Select Confirmations 1 from the dropdown list. | The confirmation control is set for the purchase order item. |  |
| 7 | Save Purchase Order | Choose Apply > Order . | A new subcontracting purchase order is created. The system message Purchase Order has been saved is displayed.Note Make a note of the purchase order number. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve and release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval (for Purchasing Group 001 and Purchasing Group 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchasing Manager role. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for the subcontracting purchase order you've created and select it.Note Purchase orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |  |
| 4 | Approve the Purchase Order | Choose Approve.In the Submit Decision dialog box, enter the approval reason if needed. Then, choose Submit. | The subcontracting purchase order is approved. |  |

#### Display Purchase Order as a Supplier in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the purchase order in the SAP Business Network as a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Display Purchase Order Line Items | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, go to the Line Items section.To display the line item details, select the Show Item Details link. | The line item details of the selected subcontracting purchase order are displayed. |  |

#### Confirm Purchase Order as a Supplier in SAP Business Network (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to confirm a subcontracting purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | On the Home screen, select the Orders and Releases search category in the search bar.In the search field, enter the purchase order number of the subcontracting purchase order and start the search. | The Orders and Releases screen is displayed with a search result list. |  |
| 3 | Confirm Purchase Order | From the search result list, select the Order Number of your subcontracting purchase order.On the Purchase Order: <Purchase Order Number> screen, choose Create Order Confirmation > Confirm Entire Order .Enter the following data:Confirmation #: Consig 01 | The Confirming PO screen is displayed. |  |
| 4 |  | On the Confirming PO screen, choose Next > Submit . | The status of the subcontracting purchase order is changed to Confirmed. |  |

#### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the purchase order confirmation in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | To search for the subcontracting purchase order that you've created, enter the required search criteria and choose Go. | A search result list with purchase orders is displayed. |  |
| 4 | Select Purchase Order | From the search result list, select the subcontracting purchase order you newly created. | The Standard PO <Purchase Order Number> screen is displayed. |  |
| 5 | Open Confirmations | Expand the Item Details section, and go to the Confirmations tab. Check if the entry in the Reference column has the same confirmation as the order confirmation in SAP Business Network. | The status of the purchase order confirmation in SAP S/4HANA Cloud Public Edition aligns with the status in SAP Business Network. |  |

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
> Flagged while digesting this document, not verified: Multi-tier overview table lists Approve Purchase Order under role Purchaser, while the procedure and the other scenarios use Purchasing Manager.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Multi-tier overview table lists Create Purchase Order via ME21N, but the detailed procedure creates the PO in Manage Purchase Orders (F0842A) and uses ME21N only for an optional step.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Subcontracting without serial numbers overview table omits several procedure steps (create/change outbound delivery) and references inconsistent page numbers, so overview and detailed procedures may differ in scope.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-mrp-change-request-integration-with-sap-business-network-6]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5I2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 219,235 chars in the whole document
