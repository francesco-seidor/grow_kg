---
id: 08-sales-order-management/test-script-sales-scheduling-agreements-3nr-ae-sap-s-4hana-cloud-publi
title: "Test Script: Sales Scheduling Agreements (3NR_AE) - SAP S/4HANA Cloud Public Edition (3NR_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3NR_AE (UAE): sales scheduling agreement through delivery, goods issue, billing and EDI messages."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-scheduling-agreements-and-jit]
aliases: [3NR_S4CLD2608_BPD_EN_AE]
keywords: [Sales Scheduling Agreements and JIT Supply to Customer, sales scheduling agreements, forecast delivery schedule, jit delivery schedule, planning delivery schedule, edi message monitoring, outbound delivery, goods issue, billing documents, picking]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NR_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-965
topic: 08-sales-order-management/sales-scheduling-agreements-and-jit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Scheduling Agreements (3NR_AE) - SAP S/4HANA Cloud Public Edition (3NR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Scheduling Agreements and JIT Supply to Customer** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Scheduling Agreements (3NR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853466)

[2 Prerequisites 4](#_Toc232853467)

[2.1 System Access 4](#_Toc232853468)

[2.2 Roles 4](#_Toc232853469)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853470)

[2.4 Additional Manual Configuration 7](#_Toc232853471)

[2.5 Business Conditions 7](#_Toc232853472)

[2.6 Preliminary Steps 7](#_Toc232853473)

[2.6.1 Maintain Customer-Material Info Record (Optional) 7](#_Toc232853474)

[2.6.2 Set Initial Stock for Material 8](#_Toc232853475)

[2.6.3 Create Condition Records (Optional) 9](#_Toc232853476)

[3 Overview Table 10](#_Toc232853477)

[4 Test Procedures 12](#_Toc232853478)

[4.1 Create Sales Scheduling Agreement 12](#_Toc232853479)

[4.2 Maintain Planning Delivery Schedule Instruction (Optional) 13](#_Toc232853480)

[4.3 Check Incoming Delivery Schedules in AIF (Message Dashboard) - EDI relevant 14](#_Toc232853481)

[4.4 Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional) 15](#_Toc232853482)

[4.5 Update Scheduling Agreement for JIT Delivery Schedule Manually (Optional) 16](#_Toc232853483)

[4.6 Generate Planning Delivery Schedule (Optional) 17](#_Toc232853484)

[4.7 Check Planning Delivery Schedule (Optional) 18](#_Toc232853485)

[4.8 Create Delivery 19](#_Toc232853486)

[4.9 Execute Picking 20](#_Toc232853487)

[4.10 Post Goods Issue 21](#_Toc232853488)

[4.11 Send Advance Shipping Notice- EDI Relevant (Optional) 22](#_Toc232853489)

[4.12 Check Advanced Shipping Notice in AIF (Message Dashboard) - EDI Relevant (Optional) 23](#_Toc232853490)

[4.13 Create Preliminary Billing Document (Optional) 23](#_Toc232853491)

[4.14 Create Billing Document 25](#_Toc232853492)

[4.15 Send Invoice - EDI Relevant 26](#_Toc232853493)

[4.16 Check Invoice in AIF (Message Dashboard) - EDI relevant 27](#_Toc232853494)

[5 Appendix 28](#_Toc232853495)

[5.1 Process Integration 28](#_Toc232853496)

[5.2 Preceding Processes 28](#_Toc232853497)

[5.3 Succeeding Processes 28](#_Toc232853498)

## Purpose

Overview

The sales scheduling agreement is an outline agreement between the buyer and supplier. Forecast and JIT (Just-in-Time) delivery schedules are sent via EDI. These delivery schedules contain the delivery dates and quantities. The whole communication is based on cumulative quantities between buyer and supplier.

Planning delivery schedules can be generated to smooth the demand handed over to production.

The shipping specialist creates deliveries based on open quantities in the delivery outbound monitor.

After the completion of picking, the shipping specialist posts goods issue. This posting is the actual recording of the physical quantity that is being shipped to the customer.

With the goods issue posting, revenue is recognized and cost of goods sold is recorded in Financial Accounting.

Advanced shipping notifications are sent via EDI to the buyer.

Once goods are delivered, you can invoice the delivery. An EDI invoice message is sent to the buyer.

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
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
|  |  |  |  | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| NoteExternal Tax Calculation Partner Solution makes use of tax attributes from Business Place, Business Partner, Material and Service master data, as well as other attributes automatically determined by the system when the appropriate configuration is done.Information related to External Tax Calculation attributes is available in the master data script Create Master Data for Brazil (JD0) and in the scope item Invoice, Taxes and Complementary Postings (1J5).Please inform a valid EAN Code in material master data via app Change Material (MM02) using the role SAP_BR_PRODMASTER_SPECIALIST.This field is found in the Basic Data 1 view in Dimension/EANs session. It is mandatory to have an EAN to authorize a NF-e in tax authority. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Sold-to Party | 33100003 | Domestic UAE Customer 3 | Payment Card Data in Business Partner.One-time payment card customer. |
| Ship-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/d992d8dde0e31d3aee01285fa7085283)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Additionally, ensure that posting period is up to date. You need Buyer system to fetch the POs for sales order creation and to check whether the whole process flow is working. |

### Preliminary Steps

#### Maintain Customer-Material Info Record (Optional)

Purpose

This process shows you how to maintain the customer-material info record to run through this scope item.

|  |
| --- |
| Note If the customer-material info record already exist, or you want to maintain the customer material manually when creating the scheduling agreement, please skip the step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Materials (F2499). |  |  |
| 3 | Access the Creation of Customer Material | Choose Create. | The Customer Material screen displays. |  |
| 4 | Enter Basic Customer-Material Information Value Mappings | Make the following entries:Customer: 33100003Product: TG11Sales Organization: 3310Distribution Channel: 10Customer Material Description: RM129 | Basic customer-material information is maintained. |  |
| 5 | Save | Choose Save. | The Customer Material is successfully saved. |  |

#### Set Initial Stock for Material

Purpose

This process shows you how to enable materials in stock to run through this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays.Note It will be displayed this way only if it was your last transaction. So the action for the user should be to select the Reference Document for MIGO Transaction Other field. |  |
| 3 | Enter the Movement Type | Select the following options and then choose Enter.Goods Receipt - Executable Action in Transaction MIGOOther - Reference Document for MIGO Transaction |  |  |
| 4 | Make Entry in the Goods Receipt Other Screen: Material Tab | Under Goods Receipt Other Screen: Material tab, make the following entry and choose Enter.Material: <Material Number> |  |  |
| 5 | Make Entry in the Goods Receipt Other Screen: Quantity Tab | Under Goods Receipt Other Screen: Quantity tab, make the following entry and choose Enter.Qty in Unit of Entry: <Quantity in UOM>Unit of Entry: <PC> |  |  |
| 6 | Make Entry in the Goods Receipt Other Screen: Where Tab | Under Goods Receipt Other Screen: Where tab, make the following entry and choose Enter.Movement Type: 561- Receipt per initial en-try of stock balances into usePlant: <Plant>Storage Location: <Storage Location> |  |  |
| 7 | Make Entry in the Goods Receipt Other Screen: Batch Tab | Under Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter.Date of Manufacture: <Current Date or a past date> | Only relevant for batch-relevant materials. |  |
| 8 | Save | Choose Post. |  |  |

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

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Scheduling Agreement](#unique_12) [page ] 12 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Create scheduling agreement. |
| [Maintain Planning Delivery Schedule Instruction (Optional)](#unique_13) [page ] 13 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Maintain planning delivery schedule instruction. |
| [Check Incoming Delivery Schedules in AIF (Message Dashboard) - EDI relevant](#unique_14) [page ] 14 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | The message (Forecast Delivery Schedule and/or JIT Delivery Schedule) is checked in dashboard. |
| [Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional)](#unique_15) [page ] 15 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manually maintain the forecast delivery schedule. |
| [Update Scheduling Agreement for JIT Delivery Schedule Manually (Optional)](#unique_16) [page ] 16 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manually maintain the JIT delivery schedule. |
| [Generate Planning Delivery Schedule (Optional)](#unique_17) [page ] 17 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manully generate planning delivery schedule. |
| [Check Planning Delivery Schedule (Optional)](#unique_18) [page ] 18 | Internal Sales Representative | Display Sales Scheduling Agreements (VA33) | Check planning delivery schedule. |
| [Create Delivery](#unique_19) [page ] 19 | Shipping Specialist | My Sales Order Schedule Lines - Due for Delivery (VL10E) | Outbound delivery is created. |
| [Execute Picking](#unique_20) [page ] 20 | Shipping Specialist | Outbound Deliveries for Picking (VL06P) | The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. |
| [Post Goods Issue](#unique_21) [page ] 21 | Shipping Specialist | Outbound Deliveries for Goods Issue (VL06G) | An advanced shipping notification is sent to the Buyer system. |
| [Send Advance Shipping Notice- EDI Relevant (Optional)](#unique_22) [page ] 22 |  |  | ASN is automatically sent to the Buyer system. |
| [Check Advanced Shipping Notice in AIF (Message Dashboard) - EDI Relevant (Optional)](#unique_23) [page ] 23 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | The message (ASN) is checked in dashboard. |
| [Create Preliminary Billing Document (Optional)](#unique_24) [page ] 23 | Billing Clerk | Create Preliminary Billing Documents (F2876) | The system generates an invoice for sales document automatically. |
| [Send Invoice - EDI Relevant](#unique_25) [page ] 26 |  |  | Supplier Invoice is automatically sent to the buyer system. |
| [Check Invoice in AIF (Message Dashboard) - EDI relevant](#unique_26) [page ] 27 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | The message (Invoice) is checked in dashboard. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet:

1. Log on to the SAP Fiori launchpad as a respective user, for example, Internal Sales Representative.

2. Access theEnterprise Search Bar by choosing the magnifying glass button in the upper right corner.

3. The Enterprise Search bar displays two filter fields next to the search button: All dropdown menu and a search field. Enter your Search Criteria and choose the business object type, for example, from the dropdown menu select Sales Scheduling Agreements, and enter a Sales Scheduling Agreement order number in the search field and choose Search, the Sales Scheduling Agreement is listed.

4. Choose the Sales Scheduling Agreement number link. The system navigates to the factsheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data by choosing the corresponding links.

There are factsheets available for the following objects (visible depending on the assigned role):

• Sales order

• Quotation

• Sales Scheduling Agreement

• Billing document

• Credit Memo

• Debit Memo

• Customer 360 Fact sheet

### Create Sales Scheduling Agreement

Purpose

This process step shows you how to create a Scheduling Agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Scheduling Agreements (F3515). |  |  |
| 3 | Navigate to Create Scheduling Agreement Screen | On the Manage Sales Scheduling Agreements screen, choose Create Scheduling Agreements. |  |  |
| 4 | Enter Data | On the Create Scheduling Agreements screen, make the following entries and choose Continue:Sched. Agreemt Type: LZSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-To Party: 33100003Ship-To Party: 33100003Customer Reference: Purchase scheduling agreement number from customerMaterial Number: TG11Customer Material: RM129 |  |  |
| 6 | Save Document | Choose Save.Make a note of the scheduling agreement number: __________.If you have created a scheduling agreement with the same data in your system and you use material TG11 and customer 33100003, the following warning may appear: |  |  |

### Maintain Planning Delivery Schedule Instruction (Optional)

Purpose

This process step shows you how to maintain planning delivery schedule instruction.

|  |
| --- |
| Note The step is only relevant that if you want to create planning delivery schedule according to forecast delivery schedule. Planning delivery schedule only relevant to the forecast delivery schedule based on week or Month. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Overview screen, choose the Item line, and choose Display Item Details |  |  |
| 5 | Enter Planning Delivery Schedule Instruciton | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Item Data screen, choose Call Control Parameter and make the following entries:PlanDS instruction: SAP1 |  |  |
| 6 | Save Document | Choose Save. |  |  |

### Check Incoming Delivery Schedules in AIF (Message Dashboard) - EDI relevant

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
| 3 | Choose Date And Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search.Choose the line of /SDSAR, Inbound Scheduling Agreement Processing and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding scheduling agreement number in Buyer system.Double choose the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

### Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional)

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
| 4 | Choose Forecast Delivery Schedule | On the Change Sched.Agr.w/ Rel. XXXXXXXX: Overview screen, choose the line Item and choose Fore. DlSch. |  |  |
| 5 | Enter the Forecast Delivery Schedule | On the Change Sched.Agr.w/ Rel. XXXXXXXX: Item Data screen, make the following entries and choose Enter.Dlv. Schedule: 0 (Del.sched.no. must be different from the previous one, so in case of existings ones choose previous no. +1)Dlv. Sched. Date: <Today>Date Type: WDate: <Today>Order Quantity: <6>Create similar entries for next 3 weeks. |  |  |
| 6 | Save Document | Choose Save to save your changes. |  |  |

### Update Scheduling Agreement for JIT Delivery Schedule Manually (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to manually create the JIT delivery schedule in predefined scheduling agreement.

|  |
| --- |
| Note JIT delivery schedule is an optional step. How schedule lines are handled in MRP is depending on the predefined settings. In this scenario following settings are predefined: within the JIT delivery schedule horizon the JIT delivery schedule is relevant for MRP, and delivery-outside the JIT delivery horizon the forecast delivery schedule is relevant for MRP and delivery. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Choose JIT Delivery Schedule | On the Change Sched.Agr.w/ Rel. XXXXXXXX: Overview screen, choose the line Item and choose JIT DlSch. |  |  |
| 5 | Enter the Forecast Delivery Schedule | On the Change Sched.Agr.w/ Rel. XXXXXXXX: Item Data screen, make the following entries and choose Enter.DIv.schedule:99Dlv. sched.date: <Today>JIT hor.: <Today-1>Order Quantity: 2Add additional schedule lines and choose Enter.Order Quantity: 3Order Quantity: 4 |  |  |
| 6 | Save Document | Choose Save to save your changes. |  |  |

### Generate Planning Delivery Schedule (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate planning delivery schedule manually.

Prerequisite

Planning delivery schedule instruction has been set. Forecast delivery schedule has been created manually with date type week or month. For delivery schedule generated via EDI, planning delivery schedule will generate automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Overview screen, choose the Item line, and choose Display Item Details. |  |  |
| 5 | Enter Planning Delivery Schedule Instruction | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Item Data screen, choose Planning Delivery Schedule, and choose Generate plan. dlv.sched. |  |  |
| 6 | Save Document | Choose Save. |  |  |

### Check Planning Delivery Schedule (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to check plannig delivery schedule.

Prerequisite

Planning delivery schedule is generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Display Sales Scheduling Agreements (VA33). |  |  |
| 3 | Choose Scheduling Agreement | On the Display Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Display Sched.Agr.w/ Rel.XXXXXXXX: Overview screen, choose the item line, and choose Display Item Details. |  |  |
| 5 | Enter Planning Delivery Schedule Instruciton | On the Display Sched.Agr.w/ Rel.XXXXXXXX: Item Data screen, choose Planning Delivery Schedule. |  |  |

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to log on to the SAP S/4HANA system to create an outbound delivery for the previously received delivery schedule (scheduling agreement).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open My Sales Order Schedule Lines - Due for Delivery (VL10E). | The Sales Order Schedule Lines screen displays. |  |
| 3 | Search Scheduling Agreement | On the Sales Order Schedule Lines screen, make the following entries and choose Continue:Shipping Point/Receiving Pt: 3310Deliv. Creation Date: <Shipping date>CalcRuleDefltDlvCrDt: <Blank>On the Sales Orders tab:SD Document: <Scheduling Agreement number created previously>Choose Execute. |  |  |
| 4 | Create Delivery | On the Activities Due for Shipping “Sales Order Schedule Lines” screen, choose Sales Sched. Agr. No. created in previous step, and choose Dialog. |  |  |
| 5 | Save Delivery | Choose Save, make a note of the delivery number. | Creation of a delivery is triggered. |  |

### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries, if the items is not relevant for picking please exclude this step execution : Example Consignment

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Outbound Deliveries for Picking (VL06P) . |  |  |
| 3 | Enter Shipping Point | Make the following entries, and choose Execute.Shipping Point/Receiving Pt: 3310Select Only Picking Without WM optionPicking Date: <Current Date +1> |  |  |
| 4 | Choose Delivery | On the Day’s Workload for Picking screen, choose the Delivery document created in previous step, and choose Change Outbound Deliveries. |  |  |
| 5 | Enter Picked Quantity | On the Delivery XXXXXXX Change: Overview screen, go to the Picking tab and enter quantity equal to delivery Qty in Picked Qty field for picking related item(s). |  |  |
| 6 | Choose Enter | Choose Enter. |  |  |
| 7 | Save | Choose Save. | The delivery is picked now. |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery in the SAP S/4HANA system (supplier side).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Outbound Deliveries for Goods Issue (VL06G). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Deliveries for Goods Issue screen, make the following entries and choose Execute.Shipping Point/Receiving Pt: 3310Pland Gds Mvmnt Date: <Current Date + 1> |  |  |
| 4 | Choose Outbound Delivery | On the Goods issue for Outbound Deliveries to be Posted screen, choose the outbound delivery document created in previous step, and choose Change Outbound Deliveries. |  |  |
| 5 | Post Good Issue | On the Delivery XXXXXXXX Change: Overview screen, choose Post Goods Issue. | The goods issue is posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 5408300Consptn Trde Gds | 13600000Inventory TradingGd | none |

### Send Advance Shipping Notice- EDI Relevant (Optional)

Purpose

This process step shows you how ASN is sent to the Buyer system.

Prerequisites

Goods issue must have been posted in the SAP S/4HANA system (supplier side).

This step is only relevant to EDI relevant deliveries schedules.

Procedure

This step is automatically generated.

### Check Advanced Shipping Notice in AIF (Message Dashboard) - EDI Relevant (Optional)

Purpose

The advanced shipping notification is sent via EDI to the Customer. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The outbound delivery has been created and goods issue has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR). |  |  |
| 3 | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search. In the Result List, choose the line of /LEEDI and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding delivering number.Double choose the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

### Create Preliminary Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the billing clerk creates preliminary billing documents based on these billing due list items, adjusts view settings and filters to customize your experience.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Billing Documents (F2876). | The Create Preliminary Billing Documents screen displays. |  |
| 3 | Search for Billing Due List Items | To enable a filter, type in a value directly to trigger autosuggest and press Enter, or use the input help to choose a value. | The Sales Document is displayed in the result. |  |
| 4 | Define Preliminary Billing Settings | Choose Preliminary Billing Settings at the top and make the following settings:Set billing date and enter before creating Preliminary billing document - OFFCreate separate preliminary billing document for each item of billing due list - OFFDisplay preliminary billing document after creation - ON |  |  |
| 5 | Adjusting Settings | Choose Settings above the worklist to open the View Settings view.Each of the three tabs (Columns, Sort, Group) lets you perform a different function.The Columns tab allows you to add or remove columns from the worklist.You can search for the names of columns using the search field.You can choose Move Up or Move Down to change the order of the columns in the worklist.Choose Restore to restore the default. |  |  |
| 6 | Select An Item to Create Preliminary Billing Document | Select the document and choose Create | The Manage Preliminary Billing Documents screen displays. |  |
| 7 | In the Manage Preliminary Billing Documents App | The preliminary billing document with ID Pxxxxxxxx has been created. | The system generates a Preliminary Billing Document for billing. |  |
| 8 | Define Billing Settings | Choose Billing Settings at the bottom and make the following settings:Automatically Post Billing Documents - OFFDisplay Billing Document after creation - ON |  |  |
| 9 | Select the Preliminary Billing Document to be Invoiced | Select the Preliminary Billing Document you have created and choose Create Billing Document. | The system generates an invoice for sales document automatically. |  |

|  |
| --- |
| Note If you finished the above steps and created both the preliminary billing document and billing document, then please skip the next step Create billing Document. |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create invoices in SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar, you can make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Choose Individual Billing Document | Select row of delivery document created previously and choose Create Billing Documents. | The Create Billing Document screen displays |  |
| 5 | Maintain Billing Data | Choose billing type F2 Invoice and maintain billing date, for example current date, then choose OK and Save. | New billing document is created. |  |
| 6 | Display Billing Document | The billing document appears automatically. | The system generates an invoice for billing. |  |

Financial Postings

Example

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Goods (HAWA) | 33100003Domestic UAE Customer 3 | 41000000Rev Domestic Prod22001000Sales Tax Accrued21730000 (optional)Freight Clrg MM | none |

### Send Invoice - EDI Relevant

Purpose

This process step shows you how to send invoice to the Buyer system.

Prerequisites

Billing Document must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

### Check Invoice in AIF (Message Dashboard) - EDI relevant

Purpose

The customer invoice is sent via EDI to the Buyer. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The billing document has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). |  |  |
| 3 | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search. In the Result List, choose the line of /SDEDI, Outbound Invoice Processing and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding billing number created in previous step.Double click the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Preceding Processes

If you want to process the EDI relevant steps, you must have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| BMR- Scheduling Agreements in Procurement | Sections Creating Scheduling Agreement,Maintain Delivery Schedule,Create Supplier Invoice, etc. |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Account Receivable (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items.) |

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
- related-to :: [[08-sales-order-management/automotive-supply-to-customer-inventory-management-55f-ae-test-script]]
- related-to :: [[08-sales-order-management/test-script-just-in-time-supply-to-customer-with-delivery-confirmation]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 46,092 chars in the whole document
