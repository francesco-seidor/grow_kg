---
id: 08-sales-order-management/test-script-just-in-time-supply-to-customer-with-delivery-confirmation
title: "Test Script: Just-In-Time Supply to Customer with Delivery Confirmation (53X_AE) (53X_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 53X: sequenced JIT calls, JIT delivery confirmation, goods issue and invoicing, with master data and roles."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-scheduling-agreements-and-jit]
aliases: [53X_S4CLD2608_BPD_EN_AE]
keywords: [Sales Scheduling Agreements and JIT Supply to Customer, jit delivery confirmation, sequenced jit calls, jit master data, packing groups, jit teams and responsibilities, sales scheduling agreements, consignment stock, outbound delivery, post goods issue]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53X_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1063
topic: 08-sales-order-management/sales-scheduling-agreements-and-jit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Just-In-Time Supply to Customer with Delivery Confirmation (53X_AE) (53X_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53X_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Scheduling Agreements and JIT Supply to Customer** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Just-In-Time Supply to Customer with Delivery Confirmation (53X_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232855619)

[2 Prerequisites 5](#_Toc232855620)

[2.1 Additional Manual Configuration 5](#_Toc232855621)

[2.2 System Access 5](#_Toc232855622)

[2.3 Roles 5](#_Toc232855623)

[2.4 Master Data, Organizational Data, and Other Data 6](#_Toc232855624)

[2.5 Business Conditions 7](#_Toc232855625)

[2.6 Preliminary Steps 8](#_Toc232855626)

[2.6.1 Check Stock Overview 8](#_Toc232855627)

[2.6.2 Maintain Reason Code Configuration 9](#_Toc232855628)

[2.6.3 Assign Sold-To Party for EDI Processing 10](#_Toc232855629)

[2.6.4 Assign Customer or Supplier to Sales Organization Data 10](#_Toc232855630)

[2.6.5 Convert External to Internal Partner Number 11](#_Toc232855631)

[2.7 Necessary Steps for Sequenced JIT Calls 13](#_Toc232855632)

[2.7.1 Sequenced JIT Call (Supply from Stock) 13](#_Toc232855633)

[2.7.1.1 Create Just-In-Time Master Data 13](#_Toc232855634)

[2.7.1.1.1 Create Customer Supply Control Records 13](#_Toc232855635)

[2.7.1.1.2 Define Packing Group Specification 14](#_Toc232855636)

[2.7.1.1.3 Create Just-In-Time Delivery Sequence Groups 15](#_Toc232855637)

[2.7.1.1.4 Create Just-In-Time Teams and Define Responsibilities 16](#_Toc232855638)

[2.7.1.2 Create Sales Scheduling Agreement 18](#_Toc232855639)

[2.7.1.3 Copy and Replace Sales Scheduling Agreements (Optional) 20](#_Toc232855640)

[2.7.1.4 Create Customer Sequenced Just-In-Time Call Manually 21](#_Toc232855641)

[2.7.1.5 Change Customer Sequenced Just-In-Time Call Manually (Optional) 23](#_Toc232855642)

[2.7.1.6 Create JIT Delivery Schedule – Background Job (Optional) 24](#_Toc232855643)

[2.7.1.7 Create Packing Group – Background Job 25](#_Toc232855644)

[2.7.1.8 Release to Packing and Confirm Packing for Packing Groups 26](#_Toc232855645)

[2.7.1.8.1 Manage Customer JIT Calls – by Component Groups (Optional) 27](#_Toc232855646)

[2.7.1.8.2 Manage JIT Packing Groups 28](#_Toc232855647)

[2.7.1.8.3 Process Customer JIT Calls – by Scan/Data Entry (Optional) 30](#_Toc232855648)

[2.7.1.9 Create Handling Units from Packing Groups for Sequenced JIT Calls 31](#_Toc232855649)

[2.7.1.10 Create Outbound Delivery from Sequenced JIT Calls 32](#_Toc232855650)

[2.7.2 Sequenced JIT Call (Supply with Production) 34](#_Toc232855651)

[2.7.2.1 Create Just-In-Time Master Data 34](#_Toc232855652)

[2.7.2.1.1 Create Customer Supply Control Records 34](#_Toc232855653)

[2.7.2.1.2 Define Packing Group Specification 35](#_Toc232855654)

[2.7.2.1.3 Create Just-In-Time Delivery Sequence Groups 37](#_Toc232855655)

[2.7.2.1.4 Create Just-In-Time Teams and Define Responsibilities 38](#_Toc232855656)

[2.7.2.2 Create Sales Scheduling Agreement 40](#_Toc232855657)

[2.7.2.3 Create Customer Sequenced Just-In-Time Call Manually 42](#_Toc232855658)

[2.7.2.4 Create Packing Group – Background Job 44](#_Toc232855659)

[2.7.2.5 Release Sequenced JIT Call Component Groups to Production 45](#_Toc232855660)

[2.7.2.6 Production Confirmation of JIT Calls 46](#_Toc232855661)

[2.7.2.6.1 Confirm Production of Sequenced JIT Call Component Groups 46](#_Toc232855662)

[2.7.2.7 Release to Packing and Confirm Packing for Packing Groups 47](#_Toc232855663)

[2.7.2.7.1 Manage Customer JIT Calls – by Component Groups (Optional) 48](#_Toc232855664)

[2.7.2.7.2 Manage JIT Packing Groups 49](#_Toc232855665)

[2.7.2.7.3 Process Customer JIT Calls – by Scan/Data Entry (Optional) 51](#_Toc232855666)

[2.7.2.8 Create Handling Units from Packing Groups for Sequenced JIT Calls 52](#_Toc232855667)

[2.7.2.9 Create Outbound Delivery from Sequenced JIT Calls 53](#_Toc232855668)

[2.7.2.10 Process Packing Groups (Optional) 54](#_Toc232855669)

[2.7.2.11 Schedule Goods Movement from Production for Customer JIT Calls (Optional) 56](#_Toc232855670)

[2.7.2.12 Reprocessing of Failed Stock Posting After Confirmation of Production (Optional) 57](#_Toc232855671)

[3 Test Procedures 59](#_Toc232855672)

[3.1 Create JIT Delivery Confirmation 59](#_Toc232855673)

[3.2 Release JIT Delivery Confirmation 61](#_Toc232855674)

[3.3 Post Goods Issue 62](#_Toc232855675)

[3.4 Check Stock Overview 63](#_Toc232855676)

[3.5 Create Customer Invoice 64](#_Toc232855677)

[4 Appendix 66](#_Toc232855678)

[4.1 Process Integration 66](#_Toc232855679)

[4.1.1 Preceding Processes 66](#_Toc232855680)

[4.1.2 Succeeding Processes 66](#_Toc232855681)

## Purpose

Overview

The process starts with receiving a Just -In- time (JIT) call from customers (see the Just-In-Time Supply to Customer (2EM) scope item). During the processing of such JIT calls, the goods are posted as consignment stock. Consignment goods are stored at the customer location but owned by suppliers.

The customers are not obligated to pay for these goods until they remove it from consignment stock. As the goods are consumed, customers send JIT delivery confirmations via SOAP API with information about materials, quantity, and reference JIT calls.

The delivery confirmation is matched with the existing JIT calls within the supplier system. The material planner (JIT supply) has an option to release them manually.

Once the delivery confirmation is released, subsequent documents (such as customer consignment issue order and outbound delivery related to customer consignment issue order) are created and the goods issue is posted.

After the billing is done, the JIT call lifecycle status is updated.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

Scope item 2EM (Just-In-Time Supply to Customer) is a prerequisite for this scope item.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/)

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign these to your individual test users.

Alternatively, if available, you can use the following space templates that determine the SAP Fiori launchpad layout for a business role. With the space template, you create a space with pages containing predefined apps and assign it to the business role. You then assign this business role to your individual users. For more information, refer to How to Create a Business Role for a Key User in the product assistance for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |
| Master Data Specialist - Just-In-Time Supply | SAP_BR_MD_SPECIALIST_JIT | Master Data - Just-In-Time | SAP_BR_MD_SPECIALIST_JIT |
| Material Planner - Just-In-Time Supply | SAP_BR_MATL_PLNR_JIT_S_TO_C | Material Planning - Just-In-Time | SAP_BR_MATL_PLNR_JIT_S_TO_C |
| Shipping Specialist - Just-In-Time Supply | SAP_BR_SHIP_SPECIALIST_JIT | Shipping - Just-In-Time | SAP_BR_SHIP_SPECIALIST_JIT |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Configuration | SAP_BR_CONF_EXPERT_BUS_NET_INT |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA system in the implementation phase. This includes data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Additional Master Data (Default Values)

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Use the following master data in the process steps described in this document:

| Master / Org. Data | Value |
| --- | --- |
| Material (Supply from Stock) – Sequenced JIT Call | FGJIT02 |
| Material (Supply from Production) – Sequenced JIT Call | SGJIT02 |
| Material (Packaging Material for Sequenced JIT Calls) | PKGJITSEQ |
| Sold-To Party | 33154802 |
| Ship-To Party | 33154802 |
| Plant | 3310 |
| Storage Location for Material (Supply from Stock) – Sequenced JIT Call | 331Afor FGJIT02. |
| Storage Location for Material (Supply from Production) – Sequenced JIT Call | 331Bfor SGJIT02. |
| Shipping Point | 3310 |
| Shipping Point - Consignment | 331C |
| Sales Organization | 3310 |
| Distribution Channel | 10 |
| Division | 00 |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| 2EM – Just-In-Time Supply to Customer | To run through this scope item, you need to have materials in the consignment stock. To achieve the same, refer to test script of scope item 2EM and perform the below steps:Create Just-In-Time customer master data [ Manage JIT Customer data (F3011) application]:Customer: 33154802Material for Sequenced JIT Call - Supply from Stock: FGJIT02Material for Sequenced JIT Call - Supply from Production: SGJIT02Sold-To Party: 33154802Ship-To Party: 33154802Create a scheduling agreement of type LKJ for customer 33154802 and for materials FGJIT02 and SGJIT02. [ Manage Sales Scheduling Agreements (F3515)Create supply control records for materials FGJIT02 and SGJIT02 [ Manage JIT Customer Supply Controls (F3010) application]Under the Delivery Control facet, maintain the below value:Delivery Confirmation Control: Combined confirmation for original and reorder JIT callsCreate packing group specification for FGJIT02/SGJIT02 [ Manage Packing Group Specification for Sequenced JIT Calls (F3896)Create appropriate teams and assign responsibilities (for Production Confirmation, Release to Packing, Packing Confirmation, etc.) to user. [ Manage Teams and Responsibilities (F5787) application]Create a delivery sequence group for customer 33154802.Create sequenced JIT calls for materials FGJIT02 and SGJIT02 [ Manage Customer JIT Calls (F6078) application]Create a packing group using the background job. [ Schedule package unit creation for sequenced JIT call (F4960) application]For material FGJIT02, perform the step below:Set initial stock for materialFor material SGJIT02, perform the steps below:Release sequenced JIT call to production [ Release JIT Calls to Production (F4330) application for summarized JIT calls and Release JIT Calls to Production (F4331) application for sequenced JIT calls.]Confirm production [ Confirm Production for Customer JIT Calls (F4315) application]Perform goods movement using background job [ Schedule goods movement from production for customer JIT calls (F5168) application]Release to packing using Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) application.Confirm packing using Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) application.Create handling units using background job [ Schedule Handling Unit creation from JIT Package Group (F5260) application]Create outbound delivery [ Create Outbound Deliveries from Sequenced JIT Calls (F3897) application]Post goods issue [ Manage Outbound Deliveries - VL06O (VL06O_CLOUD) application] |

### Preliminary Steps

#### Check Stock Overview

Purpose

The goods are now in the customer's consignment stock. The stock overview reflects this transfer of products. This step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Stock (F1595). | The Stock - Multiple Materials screen is displayed. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: FGJIT02Customer: 33154802Special Stock Type: WThen choose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomer (You may need to adapt column settings.) |  |

#### Maintain Reason Code Configuration

You can configure reason codes that need to be assigned while releasing JIT delivery configurations.

1. Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:
    - Configure Your Solution:

Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution

On the Configure Your Solution: Realize Phase screen, filter the list using the following values:

-
    -
        - Application Area: Logistics
        - Sub Application Area: Just-In-Time Processing

In the Configuration Item area, click the following entry: General Settings.

In the Configure Your Solution: General Settings screen area, choose the Configuration Steps tab.

Search for Maintain Reason Code for JIT Delivery Confirmation and choose Configure.

Enter any allowed 2-character value as the reason code, and 104307 as the configuration ID for the reason code.

-
    - SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app and search for the following activity: Maintain Reason Code for JIT Delivery Confirmation.

Choose the line item in the search result to see more details about this configuration activity.

Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

1. Choose New Entries. You can create your own entries as required.
2. Choose Save.

#### Assign Sold-To Party for EDI Processing

In this SAP Fiori master data app, you can define supplier, plant, unloading point and sold-to party.

Procedure

1. Log on to the SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system.
2. The logged in user should have the business role SAP_BR_INTERNAL_SALES_REP.
3. Choose Sales Scheduling Agreement Master Data > Assign Sold-to Parties.
4. On the list page of the SAP Fiori app, you can see all the processing options that are saved in the database as well as the draft processing options.
5. On choosing Create icon, you can create a new sold-to party assignment with supplier, plant, unloading point and valid sold-to party.
6. Enter the following details:

| Fields | Example Values |
| --- | --- |
| Supplier | (Number generated from 2YX master data script) |
| Partner Description (Plant) | P001 |
| Unloading Point | UL01 |
| Sold-To Party | 33154802 |

1. Choose Save (Ensure that the supplier, plant and unloading point combination is unique).

#### Assign Customer or Supplier to Sales Organization Data

You can assign a customer or a supplier to sales organization data for the Electronic Data Interchange (EDI) process.

1. Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:
    - Configure Your Solution:

Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution

On the Configure Your Solution: Realize Phase screen, filter the list using the following values:

-
    -
        - Application Area: Sales
        - Sub Application Area: Integration

In the Configuration Item area, click the following entry: Integration with Buyers.

In the Configure Your Solution: Integration with Buyers screen area, choose the Configuration Steps tab.

Search for Assign Customer/Supplier to Sales Organization Data and choose Configure.

Enter any allowed 2-character value as the reason code, and 101337 as the configuration ID.

-
    - SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Customer/Supplier to Sales Organization Data.

Choose Open Documentation for the found line item to see more details about this configuration activity.

Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

1. Choose New Entries. You can create your own entries as shown in the following example:

| Fields | Example Values |
| --- | --- |
| Customer Number / Customer | 33154802 |
| Supplier Number | (Number generated from 2YX master data script) |
| Sales Organization | 3310 |
| Distribution Channel | 10 |
| Division | 00 |
| Sales Document Type | LKJ |

1. Choose Save.

#### Convert External to Internal Partner Number

You can convert the external number belonging to an EDI partner into an internal number.

Procedure

1. Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:
    - Configure Your Solution:

Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage Your Solution > Configure Your Solution

On the Configure Your Solution: Realize Phase screen, make the following entries:

-
    -
        - Application Area: Sales
        - Sub Application Area: Integration

In the Configuration Item area, click the entry that has these values and also the Name as Integration with Buyers.

In the Configure Your Solution: Integration with Buyers screen area, choose the Configuration Steps tab.

Choose Configure of the configuration step Convert External to Internal Partner Numbers.

Enter any allowed 2-character value as the reason code, and 101300 as the configuration ID.

-
    - SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Convert External to Internal Partner Numbers.

Choose Open Documentation for the found line item to see more details about this configuration activity.

Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

1. Choose New Entries. You can create your own entries as shown in the following example:

| Fields | Example Values |
| --- | --- |
| Customer Number | 33154802 |
| Partner Function | SH (Ship-To Party)SP (Sold-To Party) |
| External Partner Number | P001 |
| Internal Partner Number | 10154802 (DE); 17154802 (US) |

1. Choose Save.

### Necessary Steps for Sequenced JIT Calls

#### Sequenced JIT Call (Supply from Stock)

##### Create Just-In-Time Master Data

###### Create Customer Supply Control Records

Purpose

To create a customer supply control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Supply Controls (F3010) app. |  |  |
| 3 | Create Customer Supply Control | Choose Create to create a new customer supply control | Object screen is displayed to create a new customer supply control |  |
| 4 | Maintain Customer Supply Control | On the Supply Control Detail screen, make the following entries and choose Save and Activate:Supply ControlSupply Control DescriptionCustomer: 33154802Plant: 3310Customer Supply Area: PSA_03MaterialMaterial for Sequenced JIT Call - Supply from Stock: FGJIT02Component Group Material: FGJIT02Call ProcessingAction Control: S2C_SEQJCCall Type: Sequenced JIT CallRepetitive Manufacturing is Allowed: NoProduction Version: <Not required>Delivery ControlPartial Delivery Allowed: No |  | The below information is retrieved from JIT Customer Master and displayed:Unloading Point, Assembly Location |
| 5 | Save the Entries | Choose Save and Activate | The status of the supply control is set to Active. |  |

###### Define Packing Group Specification

Purpose

To create a packing group specification as per customer requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Packing Group Specification for Sequenced JIT Calls (F3896) app. |  |  |
| 3 | Create a New Packing Group Specification | Choose Create to create a new packing group specification | Object screen is displayed to create a new packing group specification. |  |
| 4 | Maintain Packing Group Specification | On the Packing Group Specification Detail screen, make the following entries and choose Save and Activate:Packing Group Specification Description: <Packing Group Specification for <Customer Name>Packaging Material: PKGJITSEQTotal Number of Slots: 2Reorder Package Specification: No |  |  |
| 5 | Maintain Slot Group Information | On the Packing Group Specification Detail screen, choose Create in the Slot Group section.Make the following entries and choose Save and Activate:Slot GroupFirst Slot ID: 1Last Slot ID: 2Increment: 1Content Type: Component Group MaterialComponent Group Material: FGJIT02Withdrawal Sort Sequence: AscendingPacking Sort Sequence: Ascending |  |  |
| 6 | Save the Entries | Choose Save and Activate | The status of the package specification is set to Active. |  |

###### Create Just-In-Time Delivery Sequence Groups

Purpose

In order to deliver products for individual manufacturing orders according to the production sequence, delivery sequence groups are created. JIT call component groups are packed together into handling units according to the production sequence at the customer. Delivery and processing at supplier and customer of those handling units must follow the production sequence as well.

For managing delivery and processing in sequence, the following conditions are necessary:

- Subsequent alternative handling unit IDs are used for each delivery sequence
- Component group materials could be grouped together to follow a common delivery sequence

The alternative handling unit number is the concatenation of prefix, the number between from-value and to-value, and suffix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage JIT Delivery Sequence Groups for Sequence JIT Calls (F4879) app. |  |  |
| 3 | Create JIT delivery sequence groups | Click on Create to create a new JIT delivery sequence group. | Object screen is displayed to create a new JIT delivery sequence group |  |
| 4 | Maintain JIT Delivery Sequence Group | On Just-In-Time Delivery Sequence Group screen, make the following entries and choose Save:HeaderDescription: <fill in the description without any spaces>Customer: 33154802Plant: 3310Customer Supply Area: PSA_03Number SettingsTo add number settings, choose Add Normal Setting.Prefix: <fill in the description without any spaces>From: 00001To: 99999Length of Short Number: 3Assign Supply ControlCustomer Supply Control: To add customer supply control assignments, choose Add. Assign the supply control created for material FGJIT02 in previous steps.Packing Group Specification AssignmentIn the Packing Group Specification Assignment facet, choose Create. Then assign the packing group specification created for material FGJIT02 in the previous step. You must also specify appropriate Valid From and Valid To dates for this assignment. |  |  |
| 5 | Save the Entries | Choose Save and Activate | The status of the delivery sequence group is set to Active. |  |

###### Create Just-In-Time Teams and Define Responsibilities

Purpose

To create different teams for processing JIT calls by component groups (JIT1CG) and packing groups (JIT1PG).

Multiple teams could be created based on different team types per standard team category of component group/packing group. Responsibility definitions can be maintained for each team as pre-filters. Users can be assigned as team members and various functions shall be assigned for each user.

The user can log on to different applications (as mentioned below) to perform business processes based on the team to which he/she is assigned.

Team definition is a prerequisite to be able to perform business processes via applications:

- Process Customer JIT Calls – by Scan/Data Entry
- Manage Customer JIT Calls – by Component Groups
- Manage JIT Packing Groups

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). You will also need the role Business Process Specialist (SAP_BR_BUSINESS_PROCESS_SPEC). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F5787). |  |  |
| Team for Release to Packing |  |  |  |  |
| 3 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 4 | Maintain JIT Team | On Team screen, make the following entries and choose Save:HeaderDescription: <fill in the description>Name: <fill in the name>Global ID: <fill in the ID / Use auto-populated ID>Type: Release Packing for JIT Packing Groups (JIT1PGRPK)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_03JIT Customer: 33154802Plant: 3310Packing Group Status: I (In Progress)Assign Team MemberCreate: <Assign a team member who would be performing Release to Packing>Choose function Release to Packing. |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 5 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Team for Packing Confirmation |  |  |  |  |
| 6 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team. |  |
| 7 | Maintain JIT Team | On Team screen, make the following entries and choose Save:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Confirm Packing for JIT Packing Groups (JIT1PGCPK)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_03JIT Customer: 33154802Plant: 3310Packing Group Status: H (Released for Packing)Assign Team MemberCreate: <Assign same team member as assigned in step 4 above>Choose function Confirm Packing. | The status of the team is set to Enabled. | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 8 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |

##### Create Sales Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Scheduling Agreements (F3515). |  |  |
| 3 | Navigate to Create Scheduling Agreement Screen | On the Manage Scheduling Agreements screen, choose Create Scheduling Agreement. |  |  |
| 4 | Enter Data | On the Create Scheduling Agreement screen, make the following entries and choose Continue:Sched. Agreemt Type: LKJSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-to Party: 33154802Ship-to Party: 33154802Customer Reference: Purchase scheduling agreement number from customerMaterial Number: FGJIT02Customer Material Number: CFGJIT02 |  |  |
| 6 | Maintain Pricing | Double-click the item, and on the Condition tab, maintain the following entries:Condition Type: PPROAmount: 2 AED |  |  |
| 7 | Maintain Schedule Lines | Select the material, double-click the item, and on choose Fore.DISch (forecast delivery schedule), maintain the following:Date TypeDateOrder Quantity (Enter a round quantity only.)Storage Location: 331A (On Shipping tab) |  |  |
| 9 | Save Document | Choose Save.Make a note of the scheduling agreement number. |  |  |

##### Copy and Replace Sales Scheduling Agreements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Analyze and Copy Scheduling Agreements. |  |  |
| 3 | Enter Data | On the Copying SD Scheduling Agreements screen, make the following entries:Organizational Data:Sales Organization: 3310Distribution Channel: 10Division: 00Document Data:Sales Document: <Enter sales scheduling agreement that needs to be copied and replaced>Business Data:Material: <Enter the internal material number of the scheduling agreement>Customer Material: <Enter the customer material number of the scheduling agreement>Processing Mode and Parameters:Test Mode (Bckgr. Proc. Only): <Deselect>Distribute Items to New SAs: <Select>Reason for Rejection (Canc. SA): <Enter a valid reason>Reason for Rejection (New SA): <Enter a valid reason> |  |  |
| 4 | Execute | Choose Execute. | Copies the sales scheduling agreement and creates a new scheduling agreement. | New scheduling agreement number can be found on the Application Log tab. |

##### Create Customer Sequenced Just-In-Time Call Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls (F6078) |  |  |
| 3 | Create JIT Call | Choose Create. |  |  |
| 4 |  | On Manage Customer JIT Calls screen, make the following entries:Header DetailsExternal Call Number: <Number to identify the JIT call uniquely from customer perspective>Call Type: Sequenced JIT CallMaterial Usage Indicator: S SeriesReorder: NoVehicle InformationVehicle Number: <Vehicle No.>Vehicle Model: <Vehicle Model>External Sequence Number: <Sequence No.> (Important for appropriate processing of sequenced JIT calls)Partner DataPartner Description of Ship-To Party: <P001>Partner Description of Supplier: 33154802 | The following attributes are derived and populated automatically:Ship-To PartySold-To PartySales OrganizationDistribution ChannelDivisionUnloading Point |  |
| 5 | Add Components | To add components into a JIT call, navigate to Components facet and choose Create. | Object page for maintaining data related to component material is displayed. |  |
| 6 |  | Make the following entries in the object page. Choose Apply after maintaining the below data:Customer Material Number: CFGJIT02External Component Group Number: <Number to group the component groups together> [Optional]Unloading Point: UL03Customer Supply Area: PSA_03Requested Quantity: <Enter the requested quantity>Requirement Date and Time: <Enter the requirement date>Transmitted External Status: SNEW | The following are derived and auto-filled, while the object page is closed automatically:Component Material NumberComponent Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemCustomer Supply Area Desc. |  |
| 7 |  | Choose Create. | The component groups are derived automatically, either based on the BADI implementation or on rules set in the SAP Business Rules service or default component group determination.The following entries are filled for component group:Component Group NumberComponent Group MaterialCustomer Supply ControlInternal Processing StatusRequirement DatePlanned Delivery Creation Date/TimePlanned Goods Issue Date/TimePlantCustomer Supply AreaOnce all the above information is derived successfully, the JIT call is saved and activated with life cycle status Active. |  |

##### Change Customer Sequenced Just-In-Time Call Manually (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls (F6078). |  |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Enter:Ship-To Party: 33154802 |  |  |
| 4 | View Details of a JIT Call | Choose Chevron to navigate to the details screen for Ship-To Party 33154802 | Object page of the chosen JIT call is displayed. |  |
| 5 | Edit JIT Call | To edit the chosen JIT call, choose Edit. |  |  |
| 6 | Edit (Add/Delete/Modify) Components | Navigate to Components facet. Then choose Chevron to navigate to the component object page for editing. | Component object page is displayed with fields that are allowed to be modified. |  |
| 7 |  | Make the following change to the component:Requirement Date and Time: <Change the Date/Time> |  |  |
| 8 |  | Choose Apply on the object page. | The following are derived and auto-filled, while the object page is closed automatically:Component Group NumberComponent Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemCustomer Supply Area Desc. |  |
| 9 | View Components of a Component Group | On Manage Customer JIT Calls screen, under section Component Group, choose Chevron for a component group. | An object page with component group details is opened with multiple facets including Components facet. |  |

##### Create JIT Delivery Schedule – Background Job (Optional)

Purpose

In this step, you schedule a background job to create JIT delivery schedules.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule JIT Delivery Schedule Creation - For Customer JIT Calls (F5001) app. |  |  |
| 3 | Create a New Job | Choose Create to create a new job. | Template section is displayed with appropriate job template by default. |  |
| 4 | Maintain Schedule Information | Choose Step 2.Make the following entries and choose Schedule:Scheduling Options - Choose Start Immediately or define the recurring pattern and maintain the scheduling information.Choose Step 3.Parameters:Ship-To Party: 33154802Plant: 3310Material: FGJIT02Note The job must be scheduled for a single material of a sales scheduling agreement at a time. If the sales scheduling agreement contains multiple materials, the job must be restricted to any one of those materials to avoid locking issues. For more information, refer to [3590322](https://me.sap.com/notes/3590322) | Delivery schedule background job is scheduled. |  |

##### Create Packing Group – Background Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job to create packing groups for sequenced JIT calls based on the package specification defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Packing Group Creation/Update (F4960) app. |  |  |
| 3 | Create a new job | Choose Create to create a new job. | Template section is displayed with appropriate job template by default. |  |
| 4 | Maintain Information and Schedule Job | Choose Step 2.Scheduling OptionsChoose Start Immediately or define the recurring pattern and maintain the scheduling information.Choose Step 3.ParametersShip-To Party: 33154802Component Group Material: FGJIT02Customer Supply Area: PSA_03 | Packing groups would be created for materials FGJIT02 . | For reorder JIT calls, a separate packing group is created, based on the package specification. |

##### Release to Packing and Confirm Packing for Packing Groups

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions, users and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for production operations, with the role Production Operator - Lean Manufacturing. See Create Just-In-Time Teams and Define Responsibilities chapter for more information. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Customer JIT Calls (F5138). | List of teams to which the user is assigned is displayed with the appropriate function that could be performed with selection of the team. |  |
| 3 | Choose an appropriate team for further processing | Select the appropriate team created with function Release to Packing. | Navigates to initial page from where Release to Packing can be executed via scanning or data entry. |  |
| 4 | Process Packing Group to be Released for Packing | Enter the alternative packing group ID that shall be released for packing. | The status of component group is set to Released for Packing. The status of the component group can be verified by navigating to Manage Customer JIT Calls - By Component Groups (F6077) application with the appropriate role (Material Planner - Just-In-Time Supply). |  |
| 5 | Navigate Back to List of Teams | Click the Back button to navigate back to the list page with teams and functions. | List page is displayed with appropriate functions for release to packing and confirmation of packing. |  |
| 6 | Choose an appropriate team for further processing | Select the appropriate team with function Confirm Packing. | Navigates to initial page from where Confirm Packing can be executed via scanning or data entry. |  |
| 7 | Process Component Group(s) to be Confirmed for Packing | Enter the external JIT call number of the component group that shall be confirmed for packing. | The internal processing status of scanned component group is set to Packing Confirmed. |  |
| 8 | Process all component groups belonging to the packing group for packing confirmation | Repeat previous step for all component groups/external JIT call numbers that need to be confirmed for packing/ belonging to the same packing group. | The internal processing status of all component groups is set to Packing Confirmed. The packing group status is set to In Packing. The status of component groups can be verified by navigating to Manage Customer JIT Calls (F6077)application. The status of a packing group can be verified by navigating to the object page of the respective component group from the same application. |  |

###### Manage Customer JIT Calls – by Component Groups (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This application is integrated with Teams. All business processes on sequenced JIT call component groups are allowed to be performed in this application, provided a team with administrative capabilities is created and the user is assigned to appropriate functions. By selecting the team, you can perform all authorized business processes within this application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) app. |  |  |
| 3 | Filter JIT Call Component Groups to be Released to Packing | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Release to Packing> | Component Groups are filtered based on Responsibility Definition values maintained in the team. Release to Packing button appears in the toolbar dynamically. |  |
| 4 | Execute Release to Packing | Choose component group FGJIT02 and choose Release to Packing. | The action is executed on the corresponding packing group. The JIT call component group status as well as packing group status is updated to Released to Packing. |  |
| 5 | Filter JIT Call Component Groups to be Confirmed for Packing | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Confirm Packing> | Component Groups are filtered based on Responsibility Definition values maintained in the team. Confirm Packing button appears in the toolbar dynamically. |  |
| 6 | Execute Confirm Packing | Choose component group FGJIT02 and choose Confirm Packing. | The action is executed on the corresponding packing group. The JIT call component group status as well as packing group status is updated to Packing Confirmed. |  |
| 7 | View Logs | Choose Application Log button to view log information that was captured during the action processing. | The standard application log screen is displayed with details. |  |

###### Manage JIT Packing Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the packing groups that are created via the background job.

Prerequisites

You have created packing groups based on the packing group specification defined. Proceed as described in Create Packing Group – Background Job chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for Release to Packing/Packing Confirmation created earlier and with the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) app. |  |  |
| 3 | Filter JIT Packing Groups to be processed via Teams for Release to Packing | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Release to Packing> | Packing groups are filtered based on Responsibility Definition values maintained in the Teams.Release to Packing button appears in the toolbar dynamically. |  |
| 4 | Select Packing Groups that need to be processed. [Optional] A number could be entered in field Select Packing Groups for automatic selection of packing groups. | Select one or more packing groups and choose Release to Packing. | The action is executed and the packing groups on which the action was applied successfully disappear from the list. |  |
| 5 | Filter JIT Packing Groups to be processed via Teams for Packing Confirmation | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Confirm Packing> | Packing groups are filtered based on Responsibility Definition values maintained in the Teams.Confirm Packing button appears in the toolbar dynamically. |  |
| 6 | Select Packing Groups that need to be processed. [Optional] A number could be entered in field Select Packing Groups for automatic selection of packing groups. | Select one or more packing groups and choose Confirm Packing. | The action is executed and the packing groups on which the action was applied successfully disappear from the list. |  |
| 7 | Filter JIT Packing Groups to be Viewed | Remove Team ID entered in previous steps from filter.Make the following entry in filters and choose Enter:Ship-To Party ID/Description: 33154802 | Packing groups created/processed are displayed with additional information. |  |
| 8 | View Contents | Select a packing group and click the chevron icon. | The packing group details are displayed. |  |

###### Process Customer JIT Calls – by Scan/Data Entry (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for production operations, with the role Production Operator - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Customer JIT Calls (F5138). | List of teams to which the user is assigned shall be displayed with appropriate function that could be performed with selection of the team. |  |
| 3 | Choose an appropriate team for further processing | Select the appropriate team created with function Release to Packing. | Navigates to initial page from where Release to Packing could be executed via scanning or data entry or selection from F4 options. |  |
| 4 | Select Packing Group to be Released for Packing | Choose F4 on the input field. | Displays list of packing groups filtered based on the Responsibility Definition attributes that are set in the Teams. |  |
| 5 | Execute Release to Packing | Select the packing group on which Release to Packing needs to be executed. | Action shall be executed and a dialog box indicates success or failure.Once the action is successfully executed, the record disappears from the list. |  |
| 6 | Navigate Back to List of Teams | Click the Back button to navigate back to the list page with teams and functions. | List page is displayed with appropriate functions for release to packing and confirm packing. |  |
| 7 | Choose an appropriate team for further processing | Select the appropriate team (created for production operations) with function Confirm Packing. | Navigates to initial page from where Confirm Packing could be executed via scanning or data entry or selection from F4 options. |  |
| 8 | Select Packing Groups for Packing Confirmation | Choose F4 on the input field. | Displays list of packing groups with additional data on which Confirm Packing could be performed. The value help is filtered based on the Responsibility Definition attributes that are set in the Teams. |  |
| 9 | Execute Confirm Packing | Select the packing group on which Confirm Packing needs to be executed. | Action shall be executed and a dialog box indicates success or failure.Once the action is successfully executed, the record disappears from the list. |  |

##### Create Handling Units from Packing Groups for Sequenced JIT Calls

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, handling units are created from packing groups; the information is cascaded to the delivery document.

|  |
| --- |
| Note Optionally, this could also be achieved with Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) app. |  |  |
| 3 | Filter JIT Calls to Create Handling Unit | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for creating Handling Unit for Sequenced JIT Call> | Based on the responsibility definitions filter, appropriate JIT call component groups are displayed that could be confirmed for production. |  |
| 4 | Create Handling Unit | Choose component group(s) and choose the function Create Handling Unit from Package Group. | Accordingly the JIT call component group status is updated to HU Created. |  |
| 5 | View Logs | Choose Application Log in the confirmation dialog box to view any errors or warnings that occurred during production confirmation. | The standard application log screen is displayed with details. |  |

##### Create Outbound Delivery from Sequenced JIT Calls

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries from Sequenced JIT Calls (F3897) app. |  |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Go:Ship-To Party ID/Description: 33154802 | Ship-to party33154802 is displayed with additional information. |  |
| 4 | View Contents | Choose packing group and select Chevron. | The package contents are displayed. | [Optional: Only if delivery sequence group is created] Packing group is displayed based on ascending Alternative Handling Unit ID generated, which is based on JIT delivery sequence group created in an earlier step. |
| 5 | Create Outbound Delivery | Choose Create Outbound Delivery | Accordingly the JIT call status is updated to Delivery Created. |  |
| 6 | View Logs | Choose View Logs to view any errors/warnings that occurred during delivery creation | The delivery view logs application screen is displayed with details. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Sequenced JIT Call (Supply with Production)

##### Create Just-In-Time Master Data

###### Create Customer Supply Control Records

Purpose

To create a customer supply control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Supply Controls (F3010) app. |  |  |
| 3 | Create Customer Supply Control | Choose Create to create a new customer supply control | Object screen is displayed to create a new customer supply control |  |
| 4 | Maintain Customer Supply Control | On the Supply Control Detail screen, make the following entries:Supply ControlSupply Control DescriptionCustomer: 33154802PlantPlant: 3310Supply AreaCustomer Supply Area: PSA_04MaterialMaterial for Sequenced JIT Call - Supply from Production: SGJIT02Component Group MaterialComponent Group Material: SGJIT02Call ProcessingAction Control: S2C_SEQJCCall Type: Sequenced JIT CallRepetitive Manufacturing is Allowed: Yes (In case of repetitive manufacturing scenarios only)Production Version: 0002Delivery ControlPartial Delivery Allowed: No |  |  |
| 5 | Save the Entries | Choose Save and Activate | The status of the supply control is set to Active. |  |

###### Define Packing Group Specification

Purpose

To create a packing group specification as per customer requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Packing Group Specification for Sequenced JIT Calls (F3896) app. |  |  |
| 3 | Create a New Packing Group Specification | Choose Create to create a new packing group specification | Object screen is displayed to create a new packing group specification. |  |
| 4 | Maintain Packing Group Specification | On the Packing Group Specification Detail screen, make the following entries and choose Save and Activate:Packing Group Specification Description: <Packing Group Specification for <Customer Name>Packaging Material: PKGJITSEQTotal Number of Slots: 2Reorder Packing Group Specification: No |  |  |
| 5 | Maintain Slot Group Information | On the Packing Group Specification Detail screen, choose Create in the Slot Group section.Make the following entries and choose Save and Activate:Slot GroupFirst Slot ID: 1Last Slot ID: 2Increment: 1Content Type: Component Group MaterialComponent Group Material: SGJIT02Withdrawal Sort Sequence: AscendingPacking Sort Sequence: Ascending |  |  |
| 6 | Save the Entries | Choose Save and Activate | The status of the package specification is set to Active. |  |
| 7 | Create a New Packing Group Specification for material SGJIT02 | Choose Create to create a new packing group specification. | Object screen is displayed to create a new packing group specification. |  |
| 8 | Maintain Packing Group Specification | On the Packing Group Specification Detail screen, make the following entries and choose Save and Activate:Packing Group Specification Description: <Packing Group Specification for <Customer Name>Packaging Material: PKGJITSEQTotal Number of Slots: 2Reorder Packing Group Specification (Optional): Yes |  | Setting reorder packing group specification to Yes would make the packing group specification exclusive to reorder JIT calls. |
| 9 | Maintain Slot Group Information | On the Packing Group Specification Detail screen, choose Create in the Slot Group section.Make the following entries and choose Save and Activate:Slot GroupFirst Slot ID: 1Last Slot ID: 2Increment: 1Content Type: Component Group MaterialComponent Group Material: SGJIT02Withdrawal Sort Sequence: AscendingPacking Sort Sequence: Ascending |  |  |
| 10 | Save the Entries | Choose Save and Activate | The status of the package specification is set to Active. |  |

###### Create Just-In-Time Delivery Sequence Groups

Purpose

In order to deliver products for individual manufacturing orders according to the production sequence, delivery sequence groups are created. JIT call component groups are packed together into handling units according to the production sequence at the customer. Delivery and processing at supplier and customer of those handling units must follow the production sequence as well.

For managing delivery and processing in sequence, the following conditions are necessary:

- Subsequent alternative handling unit IDs are used for each delivery sequence
- Component group materials could be grouped together to follow a common delivery sequence

The alternative handling unit number is the concatenation of prefix, the number between from-value and to-value, and suffix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage JIT Delivery Sequence Groups for Sequence JIT Calls (F4879) app. |  |  |
| 3 | Create JIT delivery sequence groups | Click on Create to create a new JIT delivery sequence group. | Object screen is displayed to create a new JIT delivery sequence group |  |
| 4 | Maintain JIT Delivery Sequence Group | On Just-In-Time Delivery Sequence Group screen, make the following entries and choose Save:HeaderDescription: <fill in the description>Customer: 33154802Plant: 3310Customer Supply Area: PSA_04Number SettingsTo add number settings, choose Add Normal Setting.Prefix: <fill in the description>From: 00001To: 99999Length of Short Number: 3Assign Supply ControlCustomer Supply Control: To add customer supply control assignments, choose Add. Assign the supply control created for material SGJIT02 in previous steps.Package Group Specification AssignmentIn the Package Group Specification Assignment facet, choose Create. Then assign the packing group specification created for material SGJIT02 in the previous step. You must also specify appropriate Valid From and Valid To dates for this assignment. |  |  |
| 5 | Save the Entries | Choose Save and Activate | The status of the delivery sequence group is set to Active. |  |

###### Create Just-In-Time Teams and Define Responsibilities

Purpose

To create different teams for processing JIT calls by component groups (JIT1CG) andpacking groups (JIT1PG).

Multiple teams could be created based on different team types per standard team categoryof component group/packing group. Responsibility definitions can be maintained for eachteam as pre-filters. Users can be assigned as team members and various functions shallbe assigned for each user.

The user can log on to different applications (as mentioned below) to perform businessprocesses based on the team to which he/she is assigned.

Team definition is a prerequisite to be able to perform business processes viaapplications:

- Process Customer JIT Calls – by Scan/Data Entry
- Manage JIT Packing Groups

Prerequisites

In the Maintain Business Roles app, go to SAP_BR_MATL_PLNR_JIT_S_TO_C > Assign Business User, and assign PRODN_OPTR_LEAN_MFG user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). You will also need the roleBusiness Process Specialist (SAP_BR_BUSINESS_PROCESS_SPEC). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F5787). |  |  |
| Production Confirmation Team |  |  |  |  |
| 3 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 4 | Maintain JIT Team | On Team screen, make the following entries and choose Save:HeaderName:<fill in the description>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Confirm Production for JIT Call Component Groups (JIT1CGCPR)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_04JIT Customer: 33154802Plant: 3310Packing Group Status: I (In Progress)Assign Team MemberCreate: <Assign a team member who would be performing Release to Packing via Manage JIT Packing Groups>Choose function Confirm Production. |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 5 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Administrative Team for Release to Packing, Confirm Packing, Handling Unit Creation, Outbound Delivery Creation |  |  |  |  |
| 6 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team. |  |
| 7 | Maintain JIT Teams | On Team screen, make the following entries and choose Save:HeaderName:<fill in the description>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Confirm Packing for JIT Packing Groups (JIT1PGCPK)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_04Internal Processing Status: <0135/ 0136/ 0140> or <Internal Status on which packing release could be executed>JIT Customer: 33154802Plant: 3310Assign Team MemberCreate: <Assign a team member who would be performing below business processes via Manage JIT Packing Groups:S1_PG_RPCK: Release to PackingS1_PG_PACK: Confirm PackingS1_PG_HUCR: Create Handling UnitsS1_PG_CDLV: Create Outbound Delivery for Sequenced JIT Calls | The status of the team is set to Enabled. | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 8 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |

##### Create Sales Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Scheduling Agreements (F3515). |  |  |
| 3 | Navigate to Create Scheduling Agreement Screen | On the Manage Scheduling Agreements screen, choose Create Scheduling Agreement. |  |  |
| 4 | Enter Data | On the Create Scheduling Agreement screen, make the following entries and choose Continue:Sched. Agreemt Type: LKJSales Organization: 3310Distribution Channel: 10Division: 00Storage Location: 331B |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-to Party: 33154802Ship-to Party: 33154802Customer Reference: Purchase scheduling agreement number from customerMaterial Number: SGJIT02Customer Material Number: CSGJIT02 |  |  |
| 6 | Maintain Pricing | Double-click the item, and on the Condition tab, maintain the following entries:Condition Type: PPROAmount: 2 AED |  |  |
| 7 | Maintain Schedule Lines | Select the material, double-click the item, choose Fore.DISch (forecast delivery schedule), and maintain the following:Date TypeDateOrder Quantity (Enter a round quantity only.) |  |  |
| 8 | Save Document | Choose Save.Make a note of the scheduling agreement number. |  |  |

##### Create Customer Sequenced Just-In-Time Call Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls (F6078) |  |  |
| 3 | Create JIT Call | Choose Create. |  |  |
| 4 |  | On Manage Customer JIT Calls screen, make the following entries:Header DetailsExternal Call Number: <Number to identify the JIT call uniquely from customer perspective>Call Type: Sequenced JIT CallMaterial Usage Indicator: S SeriesReorder: NoVehicle InformationVehicle Number: <Vehicle No.>Vehicle Model: <Vehicle Model>External Sequence Number: <Sequence No.> (Important for appropriate processing of sequenced JIT calls)Partner DataPartner Description of Ship-To Party: <P001>Partner Description of Supplier: 33154802 | The following attributes are derived and populated automatically:Ship-To PartySold-To PartySales OrganizationDistribution ChannelDivisionUnloading Point |  |
| 5 | Add Components | To add components into a JIT call, navigate to Components facet and choose Create. | Object page for maintaining data related to component material is displayed. |  |
| 6 |  | Make the following entries in the object page. Choose Apply after maintaining the below data:Customer Material Number: CSGJIT02External Component Group Number: <Number to group the component groups together> [Optional]Unloading Point: UL04Customer Assembly Location: <Body Shop>Customer Supply Area: PSA_04Requested Quantity: <Enter the requested quantity>Requirement Date and Time: <Enter the requirement date>Transmitted External Status: SNEW | The following are derived and auto-filled, while the object page is closed automatically:Component Material NumberComponent Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemCustomer Supply Area Desc. |  |
| 7 |  | Choose Create. | The component groups are derived automatically, either based on the BAdI implementation or on rules set in the SAP Business Rules service or default component group determination.The following entries are filled for component group:Component Group NumberComponent Group MaterialCustomer Supply ControlInternal Processing StatusRequirement DatePlanned Delivery Creation Date/TimePlanned Goods Issue Date/TimePlantCustomer Supply AreaOnce all the above information is derived successfully, the JIT call is saved and activated with lifecycle status Active. |  |

##### Create Packing Group – Background Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job to create packing groups based on the package specification defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Packing Group Creation/Update (F4960) app. |  |  |
| 3 | Create a new job | Choose Create to create a new job. | The Scheduling Information screen is displayed. |  |
| 4 | Maintain Schedule Information | Make the following entries and choose Schedule:Scheduling OptionsChoose Start Immediately or define the recurring pattern and maintain the scheduling information.ParametersShip-To Party: 33154802Component Group Material: SGJIT02Customer Supply Area: PSA_04 | Packing groups are created based on packing group specification maintained earlier; sequenced JIT calls are packed in appropriate slots. |  |

##### Release Sequenced JIT Call Component Groups to Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release a sequenced JIT call to production.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Planner - Lean Manufacturing or Material Planner - Just-In-Time Supply depending on user assigned to the respective team in Create Just-In-Time Teams and Define Responsibilities above. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) |  |  |
| 3 | Filter JIT Calls to be Released for Production | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for production activities for Sequenced JIT Call (Supply with Production)> | Based on the responsibility definitions filter, appropriate JIT call component groups are displayed that could be released to production. |  |
| 4 | Release to Production | Choose component group(s) and choose the function Release Sequenced JIT Call to Production. | Accordingly the JIT call component group status is updated to Released for Production. |  |
| 5 | View Logs | Choose Application Log in the confirmation dialog box to view any errors or warnings that occurred during release to production. | The standard application log screen is displayed with details. |  |

##### Production Confirmation of JIT Calls

Production confirmation of JIT calls is possible only with Process Customer JIT Calls (F5138)] application. Serial number assignment is not possible with any other application.

|  |
| --- |
| Note In Manage Product Master Data, you must maintain the JIT production confirmation profile as Execution of Custom Specific Logic. |

###### Confirm Production of Sequenced JIT Call Component Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Operator - Lean Manufacturing or Material Planner - Just-In-Time Supply depending on user assigned to the respective team in Create Just-In-Time Teams and Define Responsibilities chapter. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) . |  |  |
| 3 | Filter JIT Calls to Confirm Production)> | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for production activities for Sequenced JIT Call (Supply with Production)> | Based on the responsibility definitions filter, appropriate JIT call component groups are displayed that could be confirmed for production. |  |
| 4 | Confirm Production | Choose component group(s) and choose the function Confirm Production. | Accordingly the JIT call component group status is updated to Production Confirmed and the component groups disappear from the list based on the internal processing status. |  |
| 5 | View Logs | Choose Application Log in the confirmation dialog box to view any errors or warnings that occurred during production confirmation. | The standard application log screen is displayed with details. |  |

##### Release to Packing and Confirm Packing for Packing Groups

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions, users and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for production operations, with the role Production Operator - Lean Manufacturing. See Create Just-In-Time Teams and Define Responsibilities chapter for more information. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Customer JIT Calls (F5138). | List of teams to which the user is assigned is displayed with the appropriate function that could be performed with selection of the team. |  |
| 3 | Choose an appropriate team for further processing | Select the appropriate team created with function Release to Packing. | Navigates to initial page from where Release to Packing can be executed via scanning or data entry. |  |
| 4 | Process Packing Group to be Released for Packing | Enter the alternative packing group ID that shall be released for packing. | The status of component group is set to Released for Packing. The status of the component group can be verified by navigating to Manage Customer JIT Calls - By Component Groups (F6077) application with the appropriate role (Material Planner - Just-In-Time Supply). |  |
| 5 | Navigate Back to List of Teams | Click the Back button to navigate back to the list page with teams and functions. | List page is displayed with appropriate functions for release to packing and confirmation of packing. |  |
| 6 | Choose an appropriate team for further processing | Select the appropriate team with function Confirm Packing. | Navigates to initial page from where Confirm Packing can be executed via scanning or data entry. |  |
| 7 | Process Component Group(s) to be Confirmed for Packing | Enter the external JIT call number of the component group that shall be confirmed for packing. | The internal processing status of scanned component group is set to Packing Confirmed. |  |
| 8 | Process all component groups belonging to the packing group for packing confirmation | Repeat previous step for all component groups/external JIT call numbers that need to be confirmed for packing/ belonging to the same packing group. | The internal processing status of all component groups is set to Packing Confirmed. The packing group status is set to In Packing. The status of component groups can be verified by navigating to Manage Customer JIT Calls (F6077)application. The status of a packing group can be verified by navigating to the object page of the respective component group from the same application. |  |

###### Manage Customer JIT Calls – by Component Groups (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This application is integrated with Teams. All business processes on sequenced JIT call component groups are allowed to be performed in this application, provided a team with administrative capabilities is created and the user is assigned to appropriate functions. By selecting the team, you can perform all authorized business processes within this application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) app. |  |  |
| 3 | Filter JIT Call Component Groups to be Released to Packing | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Release to Packing> | Component Groups are filtered based on Responsibility Definition values maintained in the team. Release to Packing button appears in the toolbar dynamically. |  |
| 4 | Execute Release to Packing | Choose component group SGJIT02 and choose Release to Packing. | The action is executed on the corresponding packing group. The JIT call component group status as well as packing group status is updated to Released to Packing. |  |
| 5 | Filter JIT Call Component Groups to be Confirmed for Packing | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Confirm Packing> | Component Groups are filtered based on Responsibility Definition values maintained in the team. Confirm Packing button appears in the toolbar dynamically. |  |
| 6 | Execute Confirm Packing | Choose component group SGJIT02 and choose Confirm Packing. | The action is executed on the corresponding packing group. The JIT call component group status as well as packing group status is updated to Packing Confirmed. |  |
| 7 | View Logs | Choose Application Log button to view log information that was captured during the action processing. | The standard application log screen is displayed with details. |  |

###### Manage JIT Packing Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the packing groups that are created via the background job.

Prerequisites

You have created packing groups based on the packing group specification defined. Proceed as described in Create Packing Group – Background Job chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for Release to Packing/Packing Confirmation created earlier and with the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) app. |  |  |
| 3 | Filter JIT Packing Groups to be processed via Teams for Release to Packing | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Release to Packing> | Packing groups are filtered based on Responsibility Definition values maintained in the Teams.Release to Packing button appears in the toolbar dynamically. |  |
| 4 | Select Packing Groups that need to be processed. [Optional] A number could be entered in field Select Packing Groups for automatic selection of packing groups. | Select one or more packing groups and choose Release to Packing. | The action is executed and the packing groups on which the action was applied successfully disappear from the list. |  |
| 5 | Filter JIT Packing Groups to be processed via Teams for Packing Confirmation | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for Confirm Packing> | Packing groups are filtered based on Responsibility Definition values maintained in the Teams.Confirm Packing button appears in the toolbar dynamically. |  |
| 6 | Select Packing Groups that need to be processed. [Optional] A number could be entered in field Select Packing Groups for automatic selection of packing groups. | Select one or more packing groups and choose Confirm Packing. | The action is executed and the packing groups on which the action was applied successfully disappear from the list. |  |
| 7 | Filter JIT Packing Groups to be Viewed | Remove Team ID entered in previous steps from filter.Make the following entry in filters and choose Enter:Ship-To Party ID/Description: 33154802 | Packing groups created/processed are displayed with additional information. |  |
| 8 | View Contents | Select a packing group and click the chevron icon. | The packing group details are displayed. |  |

###### Process Customer JIT Calls – by Scan/Data Entry (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for production operations, with the role Production Operator - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Customer JIT Calls (F5138). | List of teams to which the user is assigned shall be displayed with appropriate function that could be performed with selection of the team. |  |
| 3 | Choose an appropriate team for further processing | Select the appropriate team (created for production operations earlier) with function Confirm Production. | Navigates to initial page from where Confirm Production could be executed via scanning or data entry or selection from F4 options. |  |
| 4 | Select JIT Call for Production Confirmation | Choose F4 on the input field. | Displays list of JIT calls with additional data on which production confirmation could be performed. The value help is filtered based on the Responsibility Definition attributes that are set in the Teams. |  |
| 5 | Execute Production Confirmation | Select the JIT call on which Confirm Production needs to be executed. | Action shall be executed and a dialog box indicates success or failure.Once the action is successfully executed, the record disappears from the list. |  |
| 6 | Navigate Back to List of Teams | Click the Back button to navigate back to the list page with teams and functions. | List page is displayed with appropriate functions for release to packing and confirm packing. |  |

##### Create Handling Units from Packing Groups for Sequenced JIT Calls

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, handling units are created from packing groups; the information is cascaded to the delivery document.

|  |
| --- |
| Note Optionally, this could also be achieved with Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) app. |  |  |
| 3 | Filter JIT Calls to Create Handling Unit | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for creating Handling Unit for Sequenced JIT Call> | Based on the responsibility definitions filter, appropriate JIT call component groups are displayed that could be confirmed for production. |  |
| 4 | Create Handling Unit | Choose component group(s) and choose the function Create Handling Unit from Package Group. | Accordingly the JIT call component group status is updated to HU Created. |  |
| 5 | View Logs | Choose Application Log in the confirmation dialog box to view any errors or warnings that occurred during production confirmation. | The standard application log screen is displayed with details. |  |

##### Create Outbound Delivery from Sequenced JIT Calls

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries from Sequenced JIT Calls (F3897) app. |  |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Go:Ship-To Party ID/Description: 33154802 | Ship-to party33154802 is displayed with additional information. |  |
| 4 | View Contents | Choose packing group and select Chevron. | The package contents are displayed. | [Optional: Only if delivery sequence group is created] Packing group is displayed based on ascending Alternative Handling Unit ID generated, which is based on JIT delivery sequence group created in an earlier step. |
| 5 | Create Outbound Delivery | Choose Create Outbound Delivery | Accordingly the JIT call status is updated to Delivery Created. |  |
| 6 | View Logs | Choose View Logs to view any errors/warnings that occurred during delivery creation | The delivery view logs application screen is displayed with details. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

##### Process Packing Groups (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Packing groups created need to be released for packing and confirmed for packing. Once physical packing confirmation happens, handling units are created and then outbound delivery is created with a link to handling unit. In this step, all of the above mentioned processing shall be performed via an application with administrative capabilities with integration to teams.

Prerequisites

You have created packing groups based on the packing group specification defined.

An appropriate (administrative) team is created and the user is assigned to the respective team.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the same user assigned earlier to administrative team and the role Material Planner - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) app. |  |  |
| 3 | Filter JIT Packing Groups to be processed via teams | Make the following entry in filters and choose Enter:Team ID: Create Packing Group – Background Job (Mandatory for <Team ID that was created in previous steps.> | Packing groups are filtered based on responsibility definition values maintained in the teams.Release to Packing, Confirm Packing, Create Handling Unit, and Create Outbound Delivery buttons appear in the toolbar dynamically. |  |
| 4 | Select packing groups that need to be processed.[Optional] A number could be entered in field Select Packing Groups for automatic selection of packing groups. | Select one or more packing groups and click Release to Packing. | The action is executed and the status of packing groups on which the action was applied is updated to the resultant status. |  |
| 5 | Execute Confirm Packing | Select one or more packing groups and click Confirm Packing. | The action is executed and the status of packing groups on which the action was applied is updated to the resultant status. |  |
| 6 | Execute Create Handling Unit | Select one or more packing groups and click Create Handling Unit. | The action is executed and the status of packing groups on which the action was applied is updated to the resultant status. |  |
| 7 | Execute Create Outbound Delivery – for Sequenced JIT Calls | Select one or more packing groups and click Create Outbound Delivery – for Sequenced JIT Calls. | The action is executed and the status of packing groups on which the action was applied is updated to the resultant status. |  |
| 8 | Filter JIT Packing Groups to be Viewed | Remove Team ID entered in previous steps from filter.Make the following entry in filters and choose Enter:Ship-To Party ID/Description:33154802 | Packing groups created/processed are displayed with additional information. |  |
| 9 | View Contents | Select a packing group and click the chevron icon. | The packing group details are displayed. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose More > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

##### Schedule Goods Movement from Production for Customer JIT Calls (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Based on settings in the supply control, goods movement can be scheduled using a background job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Operator - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule goods movement from production for customer JIT calls (F5168). |  |  |
| 3 | Create a New Job | Choose Create to create a new job. | The Scheduling Information screen is displayed. |  |
| 4 | Maintain Schedule Information | Make the following entries and choose Schedule:Component Group Material:SGJIT02Note Use component group material SGJIT02-SERIALIZED when executing Serial Number Integration scenario. | Goods movement gets scheduled. |  |

##### Reprocessing of Failed Stock Posting After Confirmation of Production (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If goods movement fails for components in the previous step, the failed entries appear in the app and goods movement can be re-triggered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Supervisor - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Reprocessing List - For Customer JIT Calls (F5092) . | List of component materials for which goods movement have failed gets displayed. |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Ship-To Party ID/Description: 33154802 | Ship-to party 33154802 is displayed with additional information. |  |
| 4 | Reprocess Goods Movement | Choose a material and execute reprocessing. | After resolving the issue based on message short text column, goods movement can be re-triggered. |  |

## Test Procedures

This section describes procedures for each process step that belongs to scope item 53X - Just-In-Time Supply to Customer with Delivery Confirmation.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as apps or factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data, or find related objects.

How to access and check a factsheet:

1. Log on to the SAP Fiori Launchpad using the respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search bar and choose the Search icon in the upper right corner.
3. The Enterprise Search bar is displayed, and two filter fields appear to the left of the Search icon. Enter your search criteria and choose the business object type in the menu, for example, Just-In-Time Calls. Enter JIT call number and choose Search.

The JIT call is listed.

1. Choose the JIT call number link. The system navigates to the factsheet screen and JIT call-related information is integrated and summarized on one SAP Fiori screen. You can get detailed data by choosing the corresponding links.

There are factsheets available for the following objects: (Visible depending on the assigned role)

- Just-In-Time Calls
- Just-In-Time Customer Master Data
- Just-In-Time Package Specifications
- Just-In-Time Supply Controls

### Create JIT Delivery Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To test this scope item, JIT delivery confirmation should be created based on the consumption of materials at the customer or OEM. In a real-world scenario, the customer/OEM system would be integrated with a supplier system to send JIT delivery confirmation. For the purpose of testing, it can be simulated by using a third-party tool (SOAP UI) to trigger JIT delivery confirmation.

For more information on SOAP UI projects, refer to the publicly available document mentioned in the Related Links section below.

Procedure

|  |
| --- |
| Note The procedure below is only to simulate the actual scenario; this should not be considered a standard. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. | The SAP Fiori launchpad displays. |  |
| 2 | Choose appCommunication Arrangements (F1763) | Open Communication Arrangements (F1763) and search for Scenario ID SAP_COM_0728. Download WSDL and make note of Service URL/Service Interface. |  | A communication arrangement would already exist, based on the 53X master setup guide. |
| 3 | Choose appMaintain Communication Users (F1338) | In the Maintain Communication Users (F1338) app, make note of the user and password used in the communication arrangement. |  | A communication system and user would already exist, based on the 53X master setup guide. |
| 4 | Setup SOAP UI | After downloading SOAP UI, create a new project and add WSDL downloaded in above step. |  |  |
| 5 | Maintain SOAP UI Settings | Maintain communication username and password under Properties tab and enter Service URL/Service Interface URL in SOAP UI URL field. |  |  |
| 6 | Send JIT Delivery Confirmation | Based on the WSDL, fill in the value in the payload to send JIT delivery confirmation.Note Quantity unit code should always be an ISO code - and not an internal unit of measure. | JIT delivery confirmation gets created in supplier system. | For reference, the below payload can be used to create JIT delivery confirmation:Sample Code<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:njit="http://sap.com/xi/NJIT"> <soapenv:Header/> <soapenv:Body> <njit:JITDeliveryConfirmation> <MessageHeader> <CreationDateTime>2006-03-28T12:00:00.1234567Z</CreationDateTime> </MessageHeader> <DeliveryConfirmationHeader> <DeliveryConfirmationNumber></DeliveryConfirmationNumber> <ConfirmationDate></ConfirmationDate> <InvoiceDocumentNumber></InvoiceDocumentNumber> <InvoiceDocumentDate></InvoiceDocumentDate> <ReorderIndicator/> <Party> <PartyType></PartyType> <BuyerPartyID></BuyerPartyID> </Party> <Party> <PartyType></PartyType> <BuyerPartyID></BuyerPartyID> </Party> <DeliveryConfirmationItem> <ComponentMaterial> <GlobalTradeItemNumber/> <BuyerProductID></BuyerProductID> <SupplierProductID></SupplierProductID> </ComponentMaterial> <Quantity unitCode="EA"></Quantity> <BuyerCallItemID></BuyerCallItemID> <ReferenceJITCall> <BuyerJITCallID></BuyerJITCallID> </ReferenceJITCall> </DeliveryConfirmationItem> </DeliveryConfirmationHeader> </njit:JITDeliveryConfirmation> </soapenv:Body> </soapenv:Envelope> |

Further Links

For example, SoapUI, https://www.soapui.org/docs/soapui-projects/

### Release JIT Delivery Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manage JIT Delivery Confirmation app is primarily for Material Planner - Just-In-Time Supply to monitor and manage incoming JIT delivery confirmations. The material planner can launch the app and check the matching and release status. If a JIT delivery confirmation is matched or over-confirmed, it gets released automatically; subsequent documents and actions get triggered, for example, customer consignment issue order, delivery based on customer consignment issue order, and post goods issue.

If the JIT delivery confirmation is not matched, the material planners can monitor the details on the object screen of the JIT delivery confirmation. They can also refer to reference JIT calls along with process flows and related JIT delivery confirmation by navigating to delivery confirmation items.

Prerequisites

Ensure that confirmation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Delivery Confirmations (F5268). |  |  |
| 3 | View Delivery Confirmation Items | Choose the chevron icon of a JIT delivery confirmation to navigate to the object page. | The JIT delivery confirmation item details are displayed. Matching status and release status for each item can be viewed. |  |
| 4 | Manually Release Partially Confirmed JIT Delivery Confirmations | Choose one or multiple delivery confirmation items and choose Release button. Select a reason code from the menu options and choose OK. | The processing status of the chosen delivery confirmation items changes to Released/ Consignment Issue Order Created.If all items of a delivery confirmation are released, the release status of the delivery confirmations changes to Released. If a few items of the selected delivery confirmations are released, the release status of the delivery confirmations changes to Partially Released.The process flow in the third section of FCL (Go to delivery confirmation and choose Delivery Confirmation Items) gets updated with subsequent documents such as customer consignment issue order and delivery based on customer consignment issue order. | Delivery confirmations that are matched or over-confirmed are automatically released. |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

OPTION 1: Without Scheduling

Purpose

In this activity, you post the goods issue for this delivery to reduce the consignment stock on record and increase the cumulative quantity issued by the external agent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist - Just-In-Time Supply. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Pick Outbound Delivery (F0868) app. | The Pick Outbound Delivery screen is displayed. |  |
| 3 | Maintain Delivery Document Number | Enter the delivery number. |  |  |
| 4 | Post Goods Issue | Choose Post GI to post the goods issue. | The goods issue is posted. |  |

OPTION 2: With Scheduling

Purpose

In this activity, you schedule the posting of goods issue for deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist - Just-In-Time Supply. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Goods Issue For Deliveries app. | The Application Jobs screen displays. |  |
| 3 | Create Scheduling Job | Choose New and make at least the following entries:Start DateShipping Point: 331CYou can also choose Add More Scheduling Options.Choose Schedule. | The New Job screen displays.Depending on the scheduling options, the goods issue posting is started immediately or at a specific time, for one or more consignment deliveries.The Application Jobs screen displays. |  |
| 4 | View Job Log | On the Application Jobs screen, choose Go to refresh the status. If you scheduled the job for immediate start, the job should start and finish immediately. Once the job status is updated, navigate to the job log from the column Log. | The goods issue is posted. |  |

### Check Stock Overview

Purpose

The goods are transferred from the customer's consignment stock and are no longer owned by the company. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Stock (F1595). | The Stock - Multiple Materials screen is displayed. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: <Enter material numbers used in the scheduling agreement consignment fill-up.>Customer: <Enter the customer used in scheduling agreement.>Special Stock Type: WThen choose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomer (You may need to adapt column settings.) |  |

### Create Customer Invoice

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

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk (SAP_BR_BILLING_CLERK for Brazil). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | OpenCreate Billing Documents (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Search for Billing Due Items | Enter the relevant search criteria, such as sold-to party, sales document ID, or sales document category.In the SD Document field, enter the consignment delivery number that was generated in [Release JIT Delivery Confirmation](#unique_55) [page ] 61.In the SD Document Category filter, choose Delivery. | A list of delivery-related billing due list items is displayed. |  |
| 4 | Make Billing Settings | Choose the cog symbol on the bottom right-hand corner of the screen.Ensure that Display Billing Documents After Creation is switched on. If not, switch it on.Ensure that Automatically Post Billing Documents is switched on. If not, switch it on.Choose OK. | The Billing Settings dialog is displayed and you make your settings. |  |
| 5 | Select Billing Due List Item | Select a row and set a check mark next to the billing due list item for which you want to create a billing document. | The appropriate billing due list item is selected. |  |
| 6 | Create and Display Invoice | Choose the Create button at the bottom of the screen.In the Create Billing Documents dialog box, enter the following data and choose OK:Billing Type: Invoice (F2)Billing Date: Today | The system generates a draft customer invoice with ID TMPxxxxxxx and displays the invoice details in the Manage Billing Documents app. |  |
| 7 | Save Billing Document | On the Billing Document screen, click Save. The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxxxx. Make a note of the billing document number. | The system generates an invoice for billing. |  |
| 8 | Display Print Preview | Choose Preview at the bottom of the screen. | A preview of the invoice document in PDF form is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

Before starting the activities in this test script, you can set up using the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 4LZ - Sales Scheduling Agreement with Consignment | Create a sales scheduling agreement of type LKJ , etc.Using the master data from this document, complete the following activities described in the test script:Creation of sales scheduling agreement |
| 2EM – Just-In-Time Supply to Customer | Create a JIT call based on sales scheduling agreement of type LKJ and complete the creation, production, delivery, and PGI of components. |

#### Succeeding Processes

| Scope Item | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable (Sections: Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items) |

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
- related-to :: [[08-sales-order-management/test-script-sales-scheduling-agreements-3nr-ae-sap-s-4hana-cloud-publi]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53X_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 118,453 chars in the whole document
