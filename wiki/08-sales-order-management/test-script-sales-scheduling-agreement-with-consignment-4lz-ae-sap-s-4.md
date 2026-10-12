---
id: 08-sales-order-management/test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4
title: "Test Script: Sales Scheduling Agreement with Consignment (4LZ_AE) - SAP S/4HANA Cloud Public Edition (4LZ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script for scope item 4LZ_AE: consignment scheduling agreements, fill-up, issue, pick-up, return, corrections, EDI checks."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-consignment]
aliases: [4LZ_S4CLD2608_BPD_EN_AE]
keywords: [Customer Consignment, consignment scheduling agreements, customer consignment stock, consignment fill-up, consignment issue, consignment pick-up, consignment returns, correction delivery, external agent correction, delivery schedules]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LZ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1035
topic: 08-sales-order-management/customer-consignment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Scheduling Agreement with Consignment (4LZ_AE) - SAP S/4HANA Cloud Public Edition (4LZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Consignment** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Scheduling Agreement with Consignment (4LZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232855293)

[2 Prerequisites 5](#_Toc232855294)

[2.1 System Access 5](#_Toc232855295)

[2.2 Roles 5](#_Toc232855296)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232855297)

[2.4 Business Conditions 8](#_Toc232855298)

[2.5 Preliminary Steps 8](#_Toc232855299)

[2.5.1 Maintain Customer-Material Info Record (Optional) 8](#_Toc232855300)

[2.5.2 Set Initial Stock for Material 9](#_Toc232855301)

[2.5.3 Create Condition Records (Optional) 10](#_Toc232855302)

[3 Overview Table 11](#_Toc232855303)

[4 Test Procedures 15](#_Toc232855304)

[4.1 Scheduling Agreement Consignment Fill-up 15](#_Toc232855305)

[4.1.1 Create Sales Scheduling Agreements for Consignment 15](#_Toc232855306)

[4.1.2 Maintain Planning Delivery Schedule Instruction (Optional) 17](#_Toc232855307)

[4.1.3 Check Incoming Delivery Schedules in AIF (Message Dashboard) - EDI relevant 18](#_Toc232855308)

[4.1.4 Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional) 19](#_Toc232855309)

[4.1.5 Update Scheduling Agreement for JIT Delivery Schedule Manually (Optional) 20](#_Toc232855310)

[4.1.6 Generate Planning Delivery Schedule (Optional) 21](#_Toc232855311)

[4.1.7 Check Planning Delivery Schedule (Optional) 22](#_Toc232855312)

[4.1.8 Create Outbound Delivery 23](#_Toc232855313)

[4.1.9 Pick Goods 24](#_Toc232855314)

[4.1.10 Post Goods Issue 25](#_Toc232855315)

[4.1.11 Check Stock Overview 26](#_Toc232855316)

[4.1.12 Send Advance Shipping Notice- EDI Relevant(Automatically) 27](#_Toc232855317)

[4.1.13 Check Advanced Shipping Notification in AIF (Message Dashboard) - EDI Relevant 28](#_Toc232855318)

[4.2 Consignment Issue 29](#_Toc232855319)

[4.2.1 Create Consignment Issue Order with Reference to Scheduling Agreement 29](#_Toc232855320)

[4.2.2 Display Consignment Issue Orders (Optional) 29](#_Toc232855321)

[4.2.3 Create Consignment Issue Order with Reference to Scheduling Agreement Manually 30](#_Toc232855322)

[4.2.4 Create Delivery (Automatically) 31](#_Toc232855323)

[4.2.5 Post Goods Issue 32](#_Toc232855324)

[4.2.5.1 Option 1: Without Scheduling 32](#_Toc232855325)

[4.2.5.2 Option 2: With Scheduling 33](#_Toc232855326)

[4.2.6 Check Stock Overview 34](#_Toc232855327)

[4.2.7 Create Customer Invoice 35](#_Toc232855328)

[4.2.8 Send Invoice – EDI Relevant 37](#_Toc232855329)

[4.2.9 Check Invoice in AIF (Message Dashboard) - EDI relevant 37](#_Toc232855330)

[4.3 Consignment Pick-Up 38](#_Toc232855331)

[4.3.1 Create Consignment Pick-Up Order with Reference to Scheduling Agreement 38](#_Toc232855332)

[4.3.2 Create Return Delivery (Automatically) 40](#_Toc232855333)

[4.3.3 Receive Returned Goods 40](#_Toc232855334)

[4.3.4 Post Goods Receipt 41](#_Toc232855335)

[4.3.5 Check Stock Overview 42](#_Toc232855336)

[4.4 Consignment Return 43](#_Toc232855337)

[4.4.1 Create Consignment Return Order with Reference to Scheduling Agreement 43](#_Toc232855338)

[4.4.2 Create Return Delivery (Automatically) 44](#_Toc232855339)

[4.4.3 Receive Returned Goods 45](#_Toc232855340)

[4.4.4 Post Goods Receipt 46](#_Toc232855341)

[4.4.4.1 Option 1: Without Scheduling 46](#_Toc232855342)

[4.4.4.2 Option 2: With Scheduling 47](#_Toc232855343)

[4.4.5 Check Stock Overview 48](#_Toc232855344)

[4.4.6 Release Consignment Return Order for Billing 49](#_Toc232855345)

[4.4.7 Create Credit Memo 50](#_Toc232855346)

[4.4.8 Send Credit Memo – EDI Relevant 52](#_Toc232855347)

[4.4.9 Check Credit Memo in AIF (Message Dashboard) - EDI relevant 52](#_Toc232855348)

[4.5 Correction Delivery 53](#_Toc232855349)

[4.6 External Agent Correction 54](#_Toc232855350)

[4.6.1 Create External Agent Correction Order with Reference to Scheduling Agreement 54](#_Toc232855351)

[4.6.2 Create Correction Outbound Delivery (Automatically) 56](#_Toc232855352)

[5 Appendix 57](#_Toc232855353)

[5.1 Process Integration 57](#_Toc232855354)

[5.1.1 Preceding Processes 57](#_Toc232855355)

[5.1.2 Succeeding Processes 57](#_Toc232855356)

## Purpose

Overview

Customer Consignment is a specific logistics business where the supplier maintains a stock of material at a customer’s location. Consignment goods are stored at the customer location but owned by your company. The customer isn’t obliged to pay for these goods until they remove them from consignment stock. Otherwise, the customer can return consignment goods that aren’t required.

Consignment offers the partners several advantages. Customers store the consignment goods at their own warehouses. Customers can access the goods in the consignment warehouse at any time. They’re billed for the actual quantity taken when they’re removed from the warehouse.

Goods that aren’t required can be returned from the consignment stock to the central warehouse.

In some cases, goods are returned to the customer consignment stock after the consignment issue has already taken place.

This scope item uses scheduling agreements that can be run with or without an external service provider.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning), no Serial No.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | RM129 | RAW129,PD |  |
| Sold-To Party | 33100003 | Customer domestic 03 |  |
| Ship-To Party | 33100003 | Customer domestic 03 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Special Stock Partner | 33100003 | Customer domestic 03 | Enter the special stock partner in the relevant customer master record on the partner screen using the partner function SB, or enter the partner function SB manually in the document header or in the relevant items if a special stock partner is required. |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Outbound |
| Storage Location | 331R | Storage Location Returns | Return |
| Shipping Point | 3310 | Shipping Point 3310 | Outbound |
| Shipping Point | 331R | Shipping Point 331R | Return |
| Shipping Point | 331C | Shipping Point 331C | Consignment |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either run through the Procurement of Direct Materials process or create stock using FLP tile Post Goods Movement (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the master data script Create New Open MM Posting Period. Posting period is up to date. |

### Preliminary Steps

#### Maintain Customer-Material Info Record (Optional)

Purpose

This process shows you how to maintain the customer-material info record to run through this scope item.

If the customer-material info record already exists, or you want to maintain the customer material manually when creating the scheduling agreement, please skip the step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Materials (F2499). |  |  |
| 3 | Access the Creation of Customer Material | Choose Create. | The Customer Material screen displays. |  |
| 4 | Enter Basic Customer-Material Information Value Mappings | Make the following entries:Customer: 33100003Product: TG11Sales Organization: 3310Distribution Channel: 10Customer Material Description: RM129 | Basic customer-material information is maintained. |  |
| 5 | Save | Choose Save. | The Customer Material is successfully saved. |  |

#### Set Initial Stock for Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). It only displays this way if it was your last transaction. So, the action for the user should be to select Reference Document for MIGO Transaction > Other. | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : TG11 |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A |  |  |
| 7 | Save Your Entries | Choose Post. |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Scheduling Agreement Consignment Fill-Up

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Scheduling Agreements for Consignment](#unique_11) [page ] 15 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | The scheduling agreement is created.Document type: LK/Sched. Agr. w/ Csgmt. |
| [Maintain Planning Delivery Schedule Instruction (Optional)](#unique_12) [page ] 17 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Maintain planning delivery schedule instruction. |
| [Check Incoming Delivery Schedules in AIF (Message Dashboard) - EDI relevant](#unique_13) [page ] 18 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | The message (Forecast Delivery Schedule and/or JIT Delivery Schedule) is checked in dashboard. |
| [Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional)](#unique_14) [page ] 19 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manually maintain the forecast delivery schedule. |
| [Update Scheduling Agreement for JIT Delivery Schedule Manually (Optional)](#unique_15) [page ] 20 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manually maintain the JIT delivery schedule. |
| [Generate Planning Delivery Schedule (Optional)](#unique_16) [page ] 21 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manully generate planning delivery schedule. |
| [Check Planning Delivery Schedule (Optional)](#unique_17) [page ] 22 | Internal Sales Representative | Display Sales Scheduling Agreements (VA33) | Check planning delivery schedule. |
| [Create Outbound Delivery](#unique_18) [page ] 23 | Shipping Specialist | My Sales Order Schedule Lines - Due for Delivery (VL10E) | The outbound delivery is created.Document type: LF/Outbound Delivery |
| [Pick Goods](#unique_19) [page ] 24 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. |
| [Post Goods Issue](#unique_20) [page ] 25 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | An advanced shipping notification is sent to the Buyer system.The goods issue is posted. |
| [Check Stock Overview](#unique_21) [page ] 26 | Shipping Specialist | Stock - Multiple Materials (F1595) | The delivered quantity is added to the consignment stock. |
| [Send Advance Shipping Notice- EDI Relevant(Automatically)](#unique_22) [page ] 27 | ASN is automatically sent to the Buyer system. |  |  |
| [Check Advanced Shipping Notification in AIF (Message Dashboard) - EDI Relevant](#unique_23) [page ] 28 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | The message (ASN) is checked in dashboard. |

Table 2: Consignment Issue

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| Create Consignment Issue Order with Reference to Scheduling Agreement |  |  |  |
| Display Consignment Issue Orders (Optional) |  |  |  |
| [Create Consignment Issue Order with Reference to Scheduling Agreement](#unique_24) [page ] 29 | Internal Sales Representative |  | The consignment issue order is created.Document type: ED/CsgmtIssueSchedAgr |
| Create Delivery (Automatically) |  |  |  |
| Post Goods Issue |  |  |  |
| [Option 1: Without Scheduling](#unique_25) [page ] 32 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Option 2: With Scheduling](#unique_26) [page ] 33 | Shipping Specialist | Schedule Goods Issue for Deliveries (F2259) | The goods issue for deliveries is posted. |
| [Check Stock Overview](#unique_27) [page ] 34 | Shipping Specialist | Stock - Multiple Materials (F1595) | The customer consignment stock is reduced by the goods issue. |
| [Create Customer Invoice](#unique_28) [page ] 35 | Billing Clerk | Create Billing Documents (F0798) | Invoice is created and sent from the SAP S/4HANA system (supplier side) to the buyer system.Document type: F2/Customer Invoice |
| [Send Invoice – EDI Relevant](#unique_29) [page ] 37 | Supplier Invoice is automatically sent to the buyer system. |  |  |
| [Check Invoice in AIF (Message Dashboard) - EDI relevant](#unique_30) [page ] 37 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | The message (Invoice) is checked in dashboard. |

Table 3: Consignment Pick-Up

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Pick-Up Order with Reference to Scheduling Agreement](#unique_31) [page ] 38 | Internal Sales Representative | Manage Sales Orders (F1873). | The consignment pick-up order is created.Document type: KAZU/CsgmtPickUpSchedAgr |
| [Create Return Delivery (Automatically)](#unique_32) [page ] 40 |  |  |  |
| [Receive Returned Goods](#unique_33) [page ] 40 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The material is received. |
| [Post Goods Receipt](#unique_34) [page ] 41 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The goods receipt is posted. |
| [Check Stock Overview](#unique_35) [page ] 42 | Shipping Specialist | Stock - Single Material (F1076). | The delivered quantity is posted from the consignment stock into the free available stock. |

Table 4: Consignment Return

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Consignment Return Order with Reference to Scheduling Agreement](#unique_36) [page ] 43 | Internal Sales Representative | Manage Sales Orders (F1873). | The consignment return order is created.Document type: KRZU/CsgmtReturnSchedAgr |
| [Create Return Delivery (Automatically)](#unique_37) [page ] 44 |  |  |  |
| [Receive Returned Goods](#unique_33) [page ] 40 | Shipping Specialist. | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Receipt](#unique_34) [page ] 41 |  |  |  |
| [Option 1: Without Scheduling](#unique_38) [page ] 46 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted. |
| [Option 2: With Scheduling](#unique_39) [page ] 47 | Shipping Specialist | Schedule Goods Issue for Deliveries (F2259) | The goods receipt for return for deliveries is posted. |
| [Check Stock Overview](#unique_40) [page ] 48 | Shipping Specialist | Stock - Single Material (F1076). | The received quantity is added to the customer consignment stock. |
| [Release Consignment Return Order for Billing](#unique_41) [page ] 49 | Internal Sales Representative | Manage Customer Returns (F1708). | The billing block is removed. |
| [Create Credit Memo](#unique_42) [page ] 50 | Billing Clerk | Create Billing Documents (F0798) | Billing is carried out.Document type: CBRE/Credit Memo for Returns |

Table 5: Correction Delivery

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Correction Delivery](#unique_43) [page ] 53 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32). | The outbound delivery is created.Document type: LFKO/Correction Delivery |

Table 6: External Agent Coreection

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create External Agent Correction Order with Reference to Scheduling Agreement](#unique_44) [page ] 54 | Internal Sales Representative | Manage Sales Orders (F1873) | The consignment issue order is created.Document type: EDKO/CsgmtCorrSchedAgr |
| [Create Correction Outbound Delivery (Automatically)](#unique_45) [page ] 56 |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Scheduling Agreement Consignment Fill-up

|  |
| --- |
| Note Considering internal integrated testing, you have to perform some steps stipulated in test script BMR in the corresponding buyer system, interactively with the steps in this test script of 4LZ in supplier system as below. |

| SEQUENCE | System | Scope Item | Chapter |
| --- | --- | --- | --- |
| 1 | Buyer & Supplier client | BMR and 4LZ | Preliminary steps |
| 2 | Buyer client | BMR | 4.3.1 Creating Scheduling Agreement w/ Release doc - Standard |
| 3 | Supplier client | 4LZ | [Create Sales Scheduling Agreements for Consignment](#unique_11) [page ] 15 |
| 4 | Buyer client | BMR | 4.3.2 Maintaining Delivery Schedule |
| 5 | Buyer client | BMR | 4.3.4 Releasing Scheduling Agreement |
| 6 | Buyer client | BMR | 4.3.5 Checking Scheduling Agreement Releases |
| 7 | Buyer client | BMR | 4.3.6 Sending Forcast & JIT Delivery Schedule – EDI relevant |
| 8 | Buyer client | BMR | 4.3.7 Checking Forecast and JIT Delivery Schedule in AIF (Message Dashboard) |
| 9 | Supplier client | 4LZ | [Check Incoming Delivery Schedules in AIF (Message Dashboard) - EDI relevant](#unique_13) [page ] 18 |

#### Create Sales Scheduling Agreements for Consignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Scheduling agreement for Consignment is used to transfer goods from plant stock to customer consignment stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Scheduling Agreements (F3515). |  |  |
| 3 | Navigate to Create Scheduling Agreement Screen | On the Manage Sales Scheduling Agreements screen, choose Create Scheduling Agreements. |  |  |
| 4 | Enter Data | On the Create Scheduling Agreements screen, make the following entries and choose Continue:Sched. Agreemt Type: LKSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Sched. Agr. w/ Csgmt: Overview screen, make the following entries:Sold-To Party:33100003Ship-To Party: 33100003Customer Reference: Purchase scheduling agreement number from customerMaterial Number: TG11Customer Material: RM129 |  |  |
| 6 | Optional:Enter External Service Provider | If there are external agents providing external service for this customer:On the Create Sched. Agr. w/ Csgmt: Overview screen, choose More -> Goto -> Header -> Partner and make the following entries:SP Forwarding Agent: xxxSB Special Stock Partner: xxxChoose Back. |  |  |
| 7 | Optional:Maintain MRP for DS type | If this Sales Scheduling Agreement is JIT relevant, which means incoming inbound JIT Delivery Schedule from buyer can be received and update this sales scheduling agreement:Choose More ->Goto -> Header -> Sales, under Sales tab, and make the following entries:MRP for DS type: change from defaulted setting E(JIT delivery schedules are not used) to A or B |  |  |
| 8 | Save Document | Choose Save.Make a note of the scheduling agreement number: __________.If you have created a scheduling agreement with the same data in your system and you use material TG11 and customer 33100003, the following warning may appear:There is already a scheduling agreement with this same data.To skip this warning, choose Enter. |  |  |

#### Maintain Planning Delivery Schedule Instruction (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain planning delivery schedule instruction.

|  |
| --- |
| Note The step is only relevant if you want to create planning delivery schedule according to forecast delivery schedule. Planning delivery schedule is only relevant to the forecast delivery schedule which is based on week or month. . |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Change Sched. Agr. w/ Csgmt xxxxxxxx: Overview screen, choose the Item line, and choose Display Item Details. |  |  |
| 5 | Enter Planning Delivery Schedule Instruciton | On the Change Sched. Agr. w/ Csgmt xxxxxxxx: Item Data screen, choose Call Control Parameter and make the following entries:PlanDS instruction: SAP1Information No planning delivery schedule in item 0000xxappears, choose Enter. |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Check Incoming Delivery Schedules in AIF (Message Dashboard) - EDI relevant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The forecast delivery schedule or JIT delivery schedule has been created and released from Buyer System and send via EDI to the Supplier. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The forecast delivery schedule or JIT delivery schedule has been created and released from Buyer System.

This step is only relevant to EDI relevant delivery schedules.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR). |  |  |
| 3 | Choose Date And Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Create.Choose the line of /SDSAR, Inbound Scheduling Agreement Processing and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding scheduling agreement number in Buyer system.Double-click the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

#### Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to manually create the forecast delivery schedule in predefined scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Choose Forecast Delivery Schedule | On the Change Sched.Agr. w/ Csgmt xxxxxxxx : Overview screen, choose the line Item and choose Fore. DlSch. |  |  |
| 5 | Enter the Forecast Delivery Schedule | On the Change Sched.Agr. w/ Csgmt xxxxxxxx : Item Data screen, make the following entries and choose Enter.Dlv. Schedule: 0 (Del.sched.no. must be different from the previous one, so in case of existing ones choose previous no. +1)Dlv. Sched. Date: <Today>Date Type: WDate: <Today>Order Quantity: <20>Create similar entries for next 3 weeks. |  |  |
| 6 | Save Document | Choose Save to save your changes. |  |  |

#### Update Scheduling Agreement for JIT Delivery Schedule Manually (Optional)

Note that you can only maintain the JIT delivery schedule horizon in the JIT delivery schedule header screen. When working with JIT delivery schedules, make sure that the MRP for DS type indicator in the header sales screen is not set to "E" (no JIT delivery schedules). The system proposes this indicator from the sales document type when you create a scheduling agreement.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to manually create the JIT delivery schedule in predefined scheduling agreement.

JIT delivery schedule is an optional step. How schedule lines are handled in MRP is depending on the predefined settings. In this scenario following settings are predefined: within the JIT delivery schedule horizon the JIT delivery schedule is relevant for MRP, and delivery-outside the JIT delivery horizon the forecast delivery schedule is relevant for MRP and delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Choose JIT Delivery Schedule | On the Change Sched.Agr. w/ Csgmt xxxxxxxx : Overview screen, choose the line Item and choose JIT DlSch. |  |  |
| 5 | Enter the Forecast Delivery Schedule | On the Change Sched.Agr. w/ Csgmt xxxxxxxx : Item Data screen, make the following entries and choose Enter.DIv.schedule:99Dlv. sched.date: <Today>Order Quantity: 2Add additional schedule lines and choose Enter.Order Quantity: 3Order Quantity: 4 |  |  |
| 6 | Save Document | Choose Save to save your changes. |  |  |

#### Generate Planning Delivery Schedule (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate planing delivery schedule manually.

Prerequisite

Planning delivery schedule instruction has been set. Forecast delivery schedule has been created manually with date type week or month. For delivery schedule generated via EDI, planning delivey schedule will generate automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Change Sched.Agr. w/ Csgmt xxxxxxxx : Overview screen, choose the Item line, and choose Display Item Details. |  |  |
| 5 | Enter Planning Delivery Schedule Instruction | On the Change Sched.Agr. w/ Csgmt xxxxxxxx : Item Data screen, choose Planning Delivery Schedule, and choose Generate plan. Dlv.sched. |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Check Planning Delivery Schedule (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to check planning delivery schedule.

Prerequisite

Planning delivery schedule is generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Display Sales Scheduling Agreements (VA33). |  |  |
| 3 | Choose Scheduling Agreement | On the Display Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Display Sched.Agr. w/ Csgmt xxxxxxxx : Overview screen, choose the item line, and choose Display Item Details. |  |  |
| 5 | Enter Planning Delivery Schedule Instruction | On the Display Sched.Agr. w/ Csgmt xxxxxxxx : Item Data screen, choose Planning Delivery Schedule. |  |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an outbound delivery for the previously received delivery schedule (scheduling agreement consignment).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open My Sales Order Schedule Lines - Due for Delivery (VL10E). | The Sales Order Schedule Lines screen displays. |  |
| 3 | Search Scheduling Agreement | On the Sales Order Schedule Lines screen, make the following entries and choose Continue:Shipping Point: 3310Selection Date: <Shipping date>CalcRuleDefltDlvCrDt: <Blank>On the Sales Order s tab:SD Document: <Scheduling Agreement number created previously>Choose Execute. |  |  |
| 4 | Create Delivery | On the Activities Due for Shipping “Sales Order Schedule Lines” screen, choose Sales Sched. Agr. No. created in previous step, and choose Dialog. |  |  |
| 5 | Save Delivery | Choose Save, make a note of the delivery number. | Creation of a delivery is triggered. |  |

#### Pick Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and providing the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Picking screen, make the following entry:Shipping Point: 3310 |  |  |
| 5 | Set Only Picking without WM | Choose Only Picking without WM and choose Execute. |  |  |
| 6 | Select Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Delivery [number] Change: Overview screen, choose the Picking tab. Enter the quantity in the Picked Qty field.The picking status is set to complete if the picked quantity and the delivery quantity is equal. To solve deviations in quantity, choose More > Edit > Copy Picked Quantity as Deliv. Quantity. | The picked quantities are entered. |  |
| 8 | Save Document | Choose Save. | The delivery is saved. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue in the dialog box, choose today’s date and choose Continue. | The goods issue is posted. |  |

Financial Postings

As transfer from plant stock to consignment stock does not result in a change of stock owner, no accounting document is created.

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are now in the customer's consignment stock. The stock overview reflects this transfer of products. This process step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter material numbers used in the scheduling agreement consignment fill-up.Customer: Enter the customer used in scheduling agreement.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomer: You may need to adapt column settings. For example, Customer. |  |

#### Send Advance Shipping Notice- EDI Relevant(Automatically)

Purpose

This process step shows you how ASN automatically sent to the buyer system.

Prerequisites

Goods issued must have been posted in the SAP S/4HANA system (supplier side).

This step is only relevant to EDI-related deliveries schedules.

Procedure

This step is automatically generated.

#### Check Advanced Shipping Notification in AIF (Message Dashboard) - EDI Relevant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The advanced shipping notification is sent via EDI to the buyer. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The Outbound Delivery has been post goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR). |  |  |
| 3 | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search. In the Result List, choose the line of /LEEDI and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding delivering number.Double choose the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

### Consignment Issue

#### Create Consignment Issue Order with Reference to Scheduling Agreement

Purpose

A consignment issue order is automatically created with reference to scheduling agreement consignment.

Prerequisites

A delivery note from external agent has been sent to the SAP S/4HANA system (supplier side).

Precedure

This step is automatically generated.

#### Display Consignment Issue Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you see newly created consignment issue order in SAP S/4HANA supplier system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. |  |  |
| 2 | Open Display Sales Orders | Open the Display Sales Orders - VA03 (VA03) tile. |  |  |
| 3 | Enter search criteria | Enter Delivery note from EDL or customer in the Purchase Order No. field and choose Search. Then double-click the entry with purchase order number in the popup window. |  |  |
| 4 | Display sales order | Sales order should be displayed with correct data. Make a note of the sales order ID. | You can see all the sales order details. |  |
| 5 | Status Overview | On the Display CsgmtIssueSchedAgr xxxxx Overview screen, choose Status Overview. In the Status Overview tree structure in the last line, check if the status is Complete Item Data. |  |  |

#### Create Consignment Issue Order with Reference to Scheduling Agreement Manually

Note: This chapter is only used for internal testing purpose, normally the Consignment Issue Order is automatically generated via inbound delivery note from external agent or customer.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a delivery by external agent , document type ED , on the basis of the external agent delivery note. You do this in the same way as creating a [sales order](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/f564b65334e6b54ce10000000a174cb4.html) with reference to the scheduling agreement.

Or at regular intervals, the customer reports either how many products have been sold, or consumed, or how many products are in the current stock (inventory).A corresponding order is entered, documenting the issue from the consignment stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). |  |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create and then choose Create Sales Order - VA01. |  |  |
| 4 | Enter Order Type | On the Create Sales Documents screen, make the following entries and choose Create with Reference:Order Type: EDSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Refered Scheduling Agreement | On the Create with Reference dialog box, make the following entry and choose Copy:SchedAgree: <the sales scheduling agreement number created previously with Doc Type : LK> |  |  |
| 6 | Enter Material Data | On the Create CsgmtIssueSchedAgr : Overview screen, make the following entries:Sold-to Party:Ship-to Party:Cust. Reference: <the customer purchase order number>On the Items tab, make the following entries:Material: TG11 <defaulted from Scheduling Agreement)Order Quantity: <the required quantity>, for example, 5PC |  |  |
| 7 | Save Document | Choose Save.CsgmtIssueSchedAgr xxxxx has been saved (delivery xxxxxxxxx created).Make a note of the delivery number__________. | The consignment issue order is created. |  |

#### Create Delivery (Automatically)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you save the delivery by external agent document, the system automatically creates an immediate delivery.

Procedure

This step is automatically generated.

#### Post Goods Issue

##### Option 1: Without Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue for this delivery to reduce the consignment stock on record and increase the cumulative quantity issued by the external agent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries - VL06O screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute:Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods issue is posted. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

##### Option 2: With Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the posting of goods issue for deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. |  |
| 3 | Create Scheduling Job | Choose Create and make at least the following entries:Start DateShipping Point: 331CYou can also choose Add More Scheduling Options.Choose Schedule. | The New Job screen displays.Depending on the scheduling options, the goods issue posting is started immediately or at a specific time, for one or more consignment deliveries.The Application Jobs screen displays. |  |
| 4 | View Job Log | On the Application Job screen, choose Go to refresh the status. If you scheduled the job for immediate start, the job should start and finish immediately. Once the job status is updated, navigate to the job log via the column Log. | The goods issue is posted. |  |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred from the customer's consignment stock and are no longer owned by the company. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter material numbers used in the scheduling agreement consignment fill-up.Customer: Enter the customer used in scheduling agreement.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomer: You may need to adapt column settings, for example, Customer. |  |

#### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as <Sold-to Party>, <Sales Document ID>, or <Sales Document Category>.In the SD Document field, enter outbound delivery no. .In the SD Document Category filter, choose Delivery. | A list of delivery-related billing due list items is displayed. |  |
| 4 | Make Billing Settings | Choose the cog symbol on the bottom right-hand corner of the screen.Make sure that Display Billing Documents After Creation is switched on. If not, switch it on.Check that Automatically Post Billing Documents is switched on. If not, switch it on.Choose OK. | The Billing Settings is dialog displays and you make your settings. |  |
| 5 | Select Billing Due List Item | Select a row and set a check mark next to the billing due list item that you want to create a billing document for. | The appropriate billing due list item is selected. |  |
| 6 | Create and Display Invoice | Choose the Create button at the bottom of the screen.In the pop-up Create Billing Documents screen, enter the following data and choose OK,Billing Type: Invoice (F2)Billing Date: Today | The system generates a draft customer invoice with ID TMPxxxxxxx and displays the invoice details in the Manage Billing Documents app. |  |
| 7 | Save Billing Document | In the Billing Document screen, click button Save. The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | Display Print Preview | Choose Preview at the bottom of the screen. | A preview of the invoice document in PDF form is displayed. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 10100003 | 41000000 Rev Domestic Prod22000000Output Tax (MWS)21030000 (optional) Freight Clrg MMOnly posted if you enter freight costs in sales order. | none |

#### Send Invoice – EDI Relevant

Purpose

This process step shows you how to sent invoice to the Buyer system.

Prerequisites

Billing Document must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

#### Check Invoice in AIF (Message Dashboard) - EDI relevant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer invoice is sent via EDI to the buyer. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The billing document has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR). |  |  |
| 3 | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search. In the Result List, choose the line of /SDEDI, Outbound Invoice Processing and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding billing number created in previous step.Double choose the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

### Consignment Pick-Up

#### Create Consignment Pick-Up Order with Reference to Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer can return goods that are not required or sold to the central warehouse. The consignment pick-up triggers the return of goods from the customer’s custody, or from the external agent (if, for example, you have delivered too much) use document type KAZU (consignment pick-up).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Order - VA01. | The Create Sales Document screen is displayed. |  |
| 3 | Enter Order Type | On the Create Sales Documents screen, make the following entries and choose Create with Reference:Order Type: KAZUSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Refered Scheduling Agreement | On the Create with Reference dialog box, make the following entry and choose Copy:SchedAgree: <the sales scheduling agreement number created previously> |  |  |
| 5 | Enter Material Data | On the Create CsgmtPickUpSchedAgr screen, make the following entries:Sold-to Party: 33100003Ship-to Party: 33100003Customer Reference: <Enter the Customer Purchase Order Number>Order Reason: for example, 101 Poor QualityOn the Items tab, make the following entries:Material: TG11 <defaulted from Scheduling Agreement)Order Quantity: Enter the Required Quantity(for example, 2 PC) |  |  |
| 6 | Save Document | Choose Save.The system issues an information message: Enter either a correction delivery/ES agtconsignment issue correctionChoose Contunue (Enter).CsgmtPickUpSchedAgr xxxxxxxx has been saved (delivery xxxxxxxx created).Make a note of the delivery. number__________. |  |  |

#### Create Return Delivery (Automatically)

Purpose

When you save the ConsignPick-up document, the system automatically creates an immediate delivery.

Procedure

This step is automatically generated.

#### Receive Returned Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and providing the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Pickingscreen, make the following entry:Shipping Point: 331R |  |  |
| 5 | Set Only Picking Without WM | Choose Only Picking without WM and choose Execute. |  |  |
| 6 | Select Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Received Quantity | On the Delivery [number] Change: Overview screen, choose the Picking tab. Enter the quantity in the Picked Qty field.The picking status is set to complete if the picked quantity and the delivery quantity is equal. To solve deviations in quantity, choose More > Edit > Copy Picked Quantity as Deliv. Quantity. |  |  |
| 8 | Save Document | Choose Save. | The delivery is saved. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt. When the goods receipt is posted, the transfer from the consignment stock is carried out at the same time as the direct posting into the free stock of the return storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Make Entries | Choose For Goods Issue. Make the following entry and choose ExecuteShipping Point: 331R |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods receipt is posted. |  |

Financial Postings

A transfer from consignment stock to plant stock does not result in an owner change of stock, no accounting document is created.

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred again to customer's consignment stock. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter the material numbers used in the consignment pick-up order.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity has been posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomerYou may need to adapt column settings. For example, Customer. |  |

### Consignment Return

#### Create Consignment Return Order with Reference to Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods that have been consumed or sold by the customer may be returned to the consignment stock. In this case, the customer communicates the returning quantity. Or from the customer to the external agent, use document type KRZU (consignment returns) to create returns with reference to the scheduling agreement.

A return order with the following follow-on documents is generated:

- A returns delivery with subsequent goods receipt
- A credit note for returns

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Open Create Sales Orders - VA01 (VA01). | The Create Sales Document screen is displayed. |  |
| 3 | Enter Order Type | On the Create Sales Documents screen, make the following entries and choose Create with Reference:Order Type: KRZUSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Refered Scheduling Agreement | On the Create with Reference dialog box, make the following entry and choose Copy:SchedAgree: <the sales scheduling agreement number created previously> |  |  |
| 5 | Enter Material Data | On the Create CsgmtReturnSchedAgr: Overview screen, make the following entries and choose Continue (Enter):Sold-To Party: 33100003Ship-To Party: 33100003Cust. Reference: Enter the customer purchase order number.On the Items tab, make the following entries:Material: TG11 <defaulted from Scheduling Agreement)Order Quantity: Enter the required quantity (for example, 2 PC)>Check that the Billing Block is set. |  |  |
| 6 | Save Document | Choose Save.CsgmtReturnSchedAgr xxxxxxxx has been saved (delivery xxxxxxxxx created)Make a note of the delivery number___________. | The customer return order is created. |  |

#### Create Return Delivery (Automatically)

Purpose

When you save the Consign Return document, the system automatically creates an immediate delivery.

Procedure

This step is automatically generated.

#### Receive Returned Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and providing the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Pickingscreen, make the following entry:Shipping Point: 331C |  |  |
| 5 | Set Only Picking Without WM | Choose Only Picking without WM and choose Execute. |  |  |
| 6 | Select Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Received Quantity | On the ConsiReturn Delivery [number] Change: Overview screen, choose the Picking tab. Enter the quantity in the Picked Qty field.The picking status is set to complete if the picked quantity and the delivery quantity is equal. To solve deviations in quantity, choose More > Edit > Copy Picked Quantity as Deliv. Quantity. |  |  |
| 8 | Save Document | Choose Save. | The delivery is saved. |  |

#### Post Goods Receipt

##### Option 1: Without Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt. When the goods receipt is posted, the consignment stock is consequently increased.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point: 331C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods receipt is posted. |  |

Post Goods Issue

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

##### Option 2: With Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the posting of goods receipts for return deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. |  |
| 3 | Create Scheduling Job | Choose New and make at least the following entries:Start Date: <Start Date>Shipping Point: 331CYou can also choose Add More Scheduling Options.Choose Schedule. | The New Job screen displays.Depending on the scheduling options, the goods issue posting is started immediately or at a specific time, for one or more consignment deliveries.The Application Jobs screen displays. |  |
| 4 | View Job Log | On the Application Job screen, choose Go to refresh the status. If you scheduled the job for immediate start, the job should start and finish immediately. Once the job status is updated, navigate to the job log via the Log column. | The goods issue is posted. |  |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred from the customer's consignment stock and no longer owned by the company. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter the material numbers used in the scheduling agreement consignment fill-up.Customer: Enter the customer used in sales document.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomerYou may need to adapt column settings. For example, Customer. |  |

#### Release Consignment Return Order for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The consignment return order has been created with a billing block to be removed manually. This is done to add a check of the credit memo to ensure that the entries are correct.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Navigate to Display Return Order Screen | On the Manage Cutomer Returns screen, enter the respective order number created in previous step in the Customer Returns field and choose Go.Choose the return order line that displays. |  |  |
| 4 | Navigate to Change Return Order Screen | Choose Change. |  |  |
| 5 | Remove Billing Block | On the Change CsgmtReturnSchedAgr xxxxxxxx : Overview screen, remove the billing block. | The billing block is removed. |  |
| 6 | Save Document | Choose Save. | The sales order is saved. |  |

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as <Sold-to Party>, <Sales Document ID>, or <Sales Document Category>, in the search field.In the SD Document field, enter outbound delivery no. .In the SD Document Category filter, choose Returns Delivery for Order. | A list of delivery-related billing due list items is displayed. |  |
| 4 | Make Billing Settings | Choose the cog symbol on the bottom right-hand corner of the screen.Make sure that Display Billing Documents After Creation is switched on. If not, switch it on.Check that Automatically Post Billing Documents is switched on. If not, switch it on.Choose OK. | The Billing Settings dialog displays, and you can make your settings. |  |
| 5 | Select Billing Due List Item | Select a row and set a check mark next to the billing due list item that you want to create a billing document for. | The appropriate billing due list item is selected. |  |
| 6 | Create and Display Invoice | Choose Create at the bottom of the screen.Choose Billing type Credit Memo for Returns (CBRE), and maintain Billing Date, for example, <Current Date>, then press OK. | The system generates a draft customer invoice with ID TMPxxxxxxx and displays the invoice details in the Manage Billing Documents app. |  |
| 7 | Save Billing Document | On the Billing Document screen, click Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | Display Print Preview | Choose Preview at the bottom of the screen. | A preview of the credit memo document in PDF form is displayed. |  |

Financial Postings

| Material | Credited Accounts | Debited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33100003 | 41000000 Rev Domestic Prod22000000 Output Tax (MWS)21030000 (optional) Freight Clrg MMOnly posted if you enter freight costs in sales order | none |

#### Send Credit Memo – EDI Relevant

Purpose

This process step shows you how to send credit memo to the Buyer system.

Prerequisites

Credit memo Document must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

#### Check Credit Memo in AIF (Message Dashboard) - EDI relevant

Purpose

The customer credit memo is sent via EDI to the buyer. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The credit memo document has been created.

Procedure

Table 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR) |  |  |
| 3 | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search. In the Result List, choose the line of /SDEDI, Outbound Invoice Processing and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding billing number created in previous step.Double choose the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

### Correction Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

In the case of returns, cumulative quantities are not updated automatically! You correct cumulative delivered quantities manually for [returns](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/f920bf53d25ab64ce10000000a174cb4.html) .

You correct cumulative quantities in scheduling agreements:

In case of [returns](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/f920bf53d25ab64ce10000000a174cb4.html)

When there has been a processing error

When there has been a [year change](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/ed20bf53d25ab64ce10000000a174cb4.html)

When you are [transferring initial quantities](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/8120bf53d25ab64ce10000000a174cb4.html) from a legacy system into the SAP System

To do this, you create a correction delivery within the delivery schedule itself. This delivery is not relevant for requirements planning, shipping, goods issue, or billing.

Correct cumulative quantities only when the customer has not posted goods receipt.

Purpose

If the system should adjust the cumulative delivered quantity, you will need to create a correction delivery (document type LFKO ).This process step shows you how to correct cumulative delivered quantities (deliveries to the external agent), create a [correction delivery](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/f320bf53d25ab64ce10000000a174cb4.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Choose Forecast Delivery Schedule | On the Change Sched. Agr. w/ Csgmt xxxxxxxx : Overview screen, choose the line Item and choose Fore. DlSch. |  |  |
| 5 | Enter the Forecast Delivery Schedule | On the Change Sched. Agr. w/ Csgmt xxxxxxxx : Item Data screen, choose Corr. Delivery on the Forecast D[elivery Schedule](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/3721bf53d25ab64ce10000000a174cb4.html) tabstrip.Make the following entries in the dialog box Create Correction Deliveryand choose Copy Data (E nter ).Delivery d ate:e.g. <Today>For help on deciding where you want to position the correction delivery, choose Display . The system lists delivery dates in chronological order.Corr.quantity: <1 PC>Enter a negative correction quantity by placing a minus sign after the quantity |  |  |
| 6 | Save Document | Choose Save to save your changes.Sched. Agr. w/ Csgmt xxxxxxx has been saved (delivery xxxxxxxx created). |  |  |

Result

When you save the correction delivery, the system updates the cumulative quantities in the delivery schedule.

To display correction deliveries, choose Deliveries on the delivery schedule tabstrip, or Environment -> Display document flow .

### External Agent Correction

#### Create External Agent Correction Order with Reference to Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the system should adjust the cumulative quantity issued by the external agent, you will need to create an external agent correction (document type EDKO ). This process step shows you how tocreate with reference to the scheduling agreement, using document type EDKO, to correct cumulative quantities issued by the external agent.When you save the document, the system automatically creates a delivery. No changes are made to stock.

For positive corrections, use item category EDK (proposed as default for materials with item category group NORM). Use item category EDK1 for negative corrections.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). |  |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create and then choose Create Sales Order - VA01. | The Create Sales Document screen displays. |  |
| 4 | Enter Order Type | On the Create Sales Documents screen, make the following entries and choose Create with Reference:Order Type: EDKOSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Refered Scheduling Agreement | On the Create with Reference dialog box, make the following entry and choose Copy:SchedAgree: <the sales scheduling agreement number created previously> |  |  |
| 6 | Enter Material Data | On the Create CsgmtCorrSchedAgr screen, make the following entries and choose Continue (Enter):Sold-To Party: 33100003Ship-To Party: 33100003Cust. Reference: Enter the customer purchase order number.On the Items tab, make the following entries:Material: TG11 <defaulted from Scheduling Agreement)Order Quantity: <Enter the required quantity (for example, 2 PC)> |  |  |
| 7 | Save Document | Choose Save.CsgmtCorrSchedAgr xxxxx has been saved (delivery xxxxxxxx created)Make a note of the delivery number___________. | The customer return order is created. |  |

#### Create Correction Outbound Delivery (Automatically)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you save the External Agent Correction Order document, the system automatically creates an immediate delivery.

Procedure

This step is automatically generated.

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| BD6 - Basic Credit Management - Set Credit Limit (Optional) | In this process, a credit limit is set for the selected customer.Complete all the activities regarding set of credit limit described in the test script of the scope item BD6 - Basic Credit Management. Credit limit can’t be checked for consignment fill-up. Only consignment issue will update credit values, but also won’t check the credit limit of the customer. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 -Accounts Receivable | In this activity, you post the incoming payment.Complete all activities described in the test script of scope item J59 -Accounts Receivable (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items) using the master data from this document. |
| BKK - Sales Order Fulfillment Monitoring | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.Using the master data from this document, complete all the activities described in the Business Process Documentation of scope item BKK - Sales Order Fulfillment Monitoring (Chapters Review Sales Documents blocked for billing, Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents). |

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
> Flagged while digesting this document, not verified: Stock overview expected results are inconsistent within the script: the Overview Table says consignment pick-up posts the quantity from consignment stock into free available stock (and 4.3.4 says the same), but 4.3.5 Check Stock Overview says the goods are transferred again to the customer's consignment stock.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Consignment issue stock check: the Overview Table says customer consignment stock is reduced by the goods issue, while step 4.2.6 states the expected result as the delivered quantity being posted into the consignment stock; for consignment return, 4.4.5 purpose says goods are transferred from consignment stock and no longer owned, while the Overview Table says the received quantity is added to customer consignment stock.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Financial postings for the consignment return goods receipt (Option 1, Without Scheduling) show debit 51600000 Consptn Trde Gds / credit 13600000 Inventory TradingGd, identical to the consignment issue goods issue, whereas the consignment pick-up goods receipt states no accounting document is created because ownership does not change.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-customer-consignment-1iu-ae-sap-s-4hana-cloud-public-editi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 92,196 chars in the whole document
