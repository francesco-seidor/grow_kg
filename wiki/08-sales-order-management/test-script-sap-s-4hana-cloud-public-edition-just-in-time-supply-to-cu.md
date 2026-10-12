---
id: 08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu
title: Test Script SAP S/4HANA Cloud Public Edition - Just-In-Time Supply to Customer (2EM_AE) (2EM_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 2EM (AE, release 2608): JIT supply to customer, summarized and sequenced JIT calls, from stock or production, through delivery and billing."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-scheduling-agreements-and-jit]
aliases: [2EM_S4CLD2608_BPD_EN_AE]
keywords: [Sales Scheduling Agreements and JIT Supply to Customer, just-in-time supply, summarized jit calls, sequenced jit calls, jit teams and responsibilities, customer supply control, packing groups, sales scheduling agreements, delivery sequence groups, serialized materials]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EM_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-816
topic: 08-sales-order-management/sales-scheduling-agreements-and-jit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Just-In-Time Supply to Customer (2EM_AE) (2EM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Scheduling Agreements and JIT Supply to Customer** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Just-In-Time Supply to Customer (2EM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232849175)

[2 Prerequisites 5](#_Toc232849176)

[2.1 Additional Manual Configuration 5](#_Toc232849177)

[2.2 Roles 5](#_Toc232849178)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232849179)

[2.3.1 System Access 8](#_Toc232849180)

[2.3.2 Master Data Creation in SAP On-Premise System [Customer or OEM System] 9](#_Toc232849181)

[2.3.2.1 Create Material 9](#_Toc232849182)

[2.3.2.2 Create Vendor 10](#_Toc232849183)

[2.3.2.3 Create Purchasing Scheduling Agreement 10](#_Toc232849184)

[2.3.2.4 Create Supply Area 11](#_Toc232849185)

[2.3.2.5 Create Control Cycle 11](#_Toc232849186)

[2.3.2.6 Create Control Records 12](#_Toc232849187)

[2.3.3 Business Conditions 12](#_Toc232849188)

[2.4 Preliminary Steps 13](#_Toc232849189)

[2.4.1 Set Initial Stock for Material 13](#_Toc232849190)

[2.4.2 Create Serial Numbers in Stock 14](#_Toc232849191)

[2.4.3 Assign Sold-To Party for EDI Processing 15](#_Toc232849192)

[2.4.4 Assign Customer or Supplier to Sales Organization Data 16](#_Toc232849193)

[2.4.5 Convert External to Internal Partner Number 17](#_Toc232849194)

[2.4.6 Master Data for Repetitive Manufacturing Scenarios 18](#_Toc232849195)

[2.4.6.1 Create Product Cost Collectors 18](#_Toc232849196)

[2.4.6.2 Create Preliminary Cost for the Product Cost Collector 19](#_Toc232849197)

[2.4.6.3 Maintain JIT Production Confirmation Profile 19](#_Toc232849198)

[2.4.7 Preliminary Steps for Electronic Invoicing (Optional) 20](#_Toc232849199)

[2.4.7.1 Assign Party ID Types to Business Partner (EDOEUBUPAV) 21](#_Toc232849200)

[2.4.7.2 Assign Party ID Types to Companies (EDOEUCOMPV) 22](#_Toc232849201)

[3 Overview Table 24](#_Toc232849202)

[4 Test Procedures 26](#_Toc232849203)

[4.1 Create Just-In-Time Customer Master Data 26](#_Toc232849204)

[4.2 Create Just-In-Time Teams and Define Responsibilities 28](#_Toc232849205)

[4.3 Summarized JIT Calls (Supply from Stock) 35](#_Toc232849206)

[4.3.1 Create Just-In-Time Master Data 35](#_Toc232849207)

[4.3.1.1 Create Customer Supply Control Records 35](#_Toc232849208)

[4.3.2 Create Sales Scheduling Agreement 36](#_Toc232849209)

[4.3.3 Copy and Replace Sales Scheduling Agreements (Optional) 38](#_Toc232849210)

[4.3.4 Create Customer Summarized Just-In-Time Call 39](#_Toc232849211)

[4.3.4.1 Create Customer Summarized Just-In-Time Call Using Integration 39](#_Toc232849212)

[4.3.4.2 Create Customer Summarized Just-In-Time Call Manually (Optional) 40](#_Toc232849213)

[4.3.5 Cancel Customer Summarized Just-In-Time Call (Optional) 42](#_Toc232849214)

[4.3.6 Create Outbound Delivery from Summarized JIT Calls 43](#_Toc232849215)

[4.3.7 Assign Handling Units to Outbound Delivery 45](#_Toc232849216)

[4.4 Summarized JIT Calls (Supply with Production) 46](#_Toc232849217)

[4.4.1 Create Just-In-Time Master Data 46](#_Toc232849218)

[4.4.1.1 Create Customer Supply Control Records 46](#_Toc232849219)

[4.4.2 Create Sales Scheduling Agreement 47](#_Toc232849220)

[4.4.3 Create Customer Summarized Just-In-Time Call 48](#_Toc232849221)

[4.4.3.1 Create Customer Summarized Just-In-Time Call Using Integration 49](#_Toc232849222)

[4.4.3.2 Create Customer Summarized Just-In-Time Call Manually (Optional) 50](#_Toc232849223)

[4.4.4 Release Summarized JIT Call Component Groups to Production 51](#_Toc232849224)

[4.4.5 Confirm Production of Summarized JIT Call Component Groups 52](#_Toc232849225)

[4.4.6 Create Outbound Delivery from Summarized JIT Calls 53](#_Toc232849226)

[4.4.7 Assign Handling Units to Outbound Delivery 55](#_Toc232849227)

[4.5 Sequenced JIT Call (Supply from Stock) 56](#_Toc232849228)

[4.5.1 Create Just-In-Time Master Data 56](#_Toc232849229)

[4.5.1.1 Create Customer Supply Control Records 56](#_Toc232849230)

[4.5.1.2 Define Packing Group Specification 57](#_Toc232849231)

[4.5.1.3 Create Just-In-Time Delivery Sequence Groups 58](#_Toc232849232)

[4.5.2 Create Sales Scheduling Agreement 59](#_Toc232849233)

[4.5.3 Copy and Replace Sales Scheduling Agreements (Optional) 61](#_Toc232849234)

[4.5.4 Create Customer Sequenced Just-In-Time Call Manually 62](#_Toc232849235)

[4.5.5 Change Customer Sequenced Just-In-Time Call Manually (Optional) 64](#_Toc232849236)

[4.5.6 Create JIT Delivery Schedule – Background Job (Optional) 65](#_Toc232849237)

[4.5.7 Create Packing Group – Background Job 66](#_Toc232849238)

[4.5.8 Release to Packing and Confirm Packing for Packing Groups 67](#_Toc232849239)

[4.5.9 Create Handling Units from Packing Groups for Sequenced JIT Calls 68](#_Toc232849240)

[4.5.10 Create Outbound Delivery from Sequenced JIT Calls 69](#_Toc232849241)

[4.6 Sequenced JIT Call (Supply with Production) 71](#_Toc232849242)

[4.6.1 Create Just-In-Time Master Data 71](#_Toc232849243)

[4.6.1.1 Create Customer Supply Control Records 71](#_Toc232849244)

[4.6.1.2 Define Packing Group Specification 72](#_Toc232849245)

[4.6.1.3 Create Just-In-Time Delivery Sequence Groups 74](#_Toc232849246)

[4.6.2 Create Sales Scheduling Agreement 75](#_Toc232849247)

[4.6.3 Create Customer Sequenced Just-In-Time Call Manually 77](#_Toc232849248)

[4.6.4 Release Sequenced JIT Call Component Groups to Production 79](#_Toc232849249)

[4.6.5 Confirm Production of Sequenced JIT Call Component Groups 79](#_Toc232849250)

[4.6.6 Create Packing Group – Background Job 81](#_Toc232849251)

[4.6.7 Release to Packing and Confirm Packing for Packing Groups 82](#_Toc232849252)

[4.6.8 Create Handling Units from Packing Groups for Sequenced JIT Calls 83](#_Toc232849253)

[4.6.9 Create Outbound Delivery from Sequenced JIT Calls 84](#_Toc232849254)

[4.6.10 Schedule Goods Movement from Production for Customer JIT Calls (Optional) 85](#_Toc232849255)

[4.6.11 Reprocessing of Failed Stock Posting After Confirmation of Production (Optional) 86](#_Toc232849256)

[4.7 Sequenced JIT Call (Supply from Production of Serialized Materials) 87](#_Toc232849257)

[4.7.1 Create Just-In-Time Master Data 87](#_Toc232849258)

[4.7.1.1 Create Customer Supply Control Records 87](#_Toc232849259)

[4.7.1.2 Define Packing Group Specification 88](#_Toc232849260)

[4.7.1.3 Create Just-In-time Delivery Sequence Groups 90](#_Toc232849261)

[4.7.2 Create Sales Scheduling Agreement 92](#_Toc232849262)

[4.7.3 Create Customer Sequenced Just-In-Time Call Manually 93](#_Toc232849263)

[4.7.4 Release Sequenced JIT Call Component Groups to Production 95](#_Toc232849264)

[4.7.5 Confirm Production of Sequenced JIT Call Component Groups 96](#_Toc232849265)

[4.7.6 Create Packing Group – Background Job 97](#_Toc232849266)

[4.7.7 Release to Packing and Confirm Packing for Packing Groups 98](#_Toc232849267)

[4.7.8 Create Handling Units from Packing Groups for Sequenced JIT Calls 99](#_Toc232849268)

[4.7.9 Create Outbound Delivery from Sequenced JIT Calls 100](#_Toc232849269)

[4.7.10 Process Packing Groups (Optional) 102](#_Toc232849270)

[4.8 Execute Picking and Post Goods Issue 104](#_Toc232849271)

[4.9 Create Billing Document 105](#_Toc232849272)

[4.10 eDocument Cockpit (Optional) 107](#_Toc232849273)

[5 Appendix 110](#_Toc232849274)

[5.1 Process Integration 110](#_Toc232849275)

[5.1.1 Preceding Processes 110](#_Toc232849276)

[5.1.2 Succeeding Processes 110](#_Toc232849277)

## Purpose

Overview

The process starts with receiving Just-In-Time (JIT) calls from customers.

JIT calls are sent via an EDI integration and contain the component details with the requirements date and time. The material planner (JIT supply) monitors and manages the JIT calls. The production planner releases production-relevant component group materials or package units for production for summarized and sequenced JIT calls respectively.

The production operator then confirms the production of the components. The production supervisor reprocesses failed stocks.

The shipping specialist (JIT supply) creates deliveries that reflect the status accordingly. Advanced shipping notifications are sent via EDI to the OEM. The shipping specialist and material planner can create handling units as well.

After picking and posting of goods issue, the JIT call status is updated. Optionally, for summarized JIT calls, picking and post goods issue can be done in Extended Warehouse Management.

After the billing is created, the JIT call is updated to completed status.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2EM_S4CLD2602_BPD_EN_AE.docx) ). |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e1c9c582bf8ee8a87445e77b0913447e)

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |
| Master Data Specialist - Just-In-Time Supply | SAP_BR_MD_SPECIALIST_JIT | Master Data - Just-In-Time | SAP_BR_MD_SPECIALIST_JIT |
| Material Planner - Just-In-Time Supply | SAP_BR_MATL_PLNR_JIT_S_TO_C | Material Planning - Just-In-Time | SAP_BR_MATL_PLNR_JIT_S_TO_C |
| Shipping Specialist - Just-In-Time Supply | SAP_BR_SHIP_SPECIALIST_JIT | Shipping - Just-In-Time | SAP_BR_SHIP_SPECIALIST_JIT |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |
| Production Operator - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG | Production Execution - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG |
| Production Planner - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Production Planning - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |
| Production Supervisor - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG | Production Supervisor - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |

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
| Material (Supply from Stock) – Summarized JIT Call | FGJIT01 |
| Material (Supply from Production) – Summarized JIT Call | SGJIT01 |
| Material (Supply from Stock) – Sequenced JIT Call | FGJIT02 |
| Material (Supply from Production) – Sequenced JIT Call | SGJIT02 |
| Raw Material (Supply from Production) | RMJIT01 |
| Raw Material (Supply from Production) | RMJIT02 |
| Material (EWM Integration) | FGJIT03 |
| Material (Packaging Material for Sequenced JIT Calls) | PKGJITSEQ |
| Material (Packaging Material for Handling Unit) | PKGJITHU |
| Serialized Material (Supply from Production) – Sequenced JIT Call | SGJIT02-SERIALIZED |
| Sold-To Party | 33154801 |
| Ship-To Party | 33154801 |
| Plant | 3310 |
| Storage Location | 331Afor materials FGJIT01, FGJIT02, and FGJIT03.331Bfor materials SGJIT01, SGJIT02, SGJIT02-SERIALIZED, RMJIT01 and RMJIT02. |
| Shipping Point | 3310 |
| Sales Organization | 3310 |
| Distribution Channel | 10 |
| Division | 00 |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |
| BND | Create Customer Master |
| 2YX | Create Supplier Master |

#### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Master Data Creation in SAP On-Premise System [Customer or OEM System]

Examples to create master data in SAP On-Premise system [Customer or OEM System].

##### Create Material

Material can be created with the following entries, for example:

- Material Name: RP001JIT01
- Material Type: Finished Product
- Maintain the following views:
    - Basic Data 1
        - Plant: 3310
        - Sales Organization: 3310
        - Distribution Channel: 01
        - Description: <Material Description>
        - Base Unit of Measure: EA
        - Material Group: <L004>
        - GenItemCatGroup: NORM
        - Gross Weight: <2> KG
        - Net Weight: <2> KG
    - Basic Data 2
    - Sales: Sales Org. Data 1
    - Sales: Sales Org. Data 2
    - Sales: General/Plant Data
        - Loading Group: 0001
    - Purchasing
    - General Plant Data / Storage 1
        - Plant: 3310
        - Storage Location:

331A for materials FGJIT01, FGJIT02, and FGJIT03.

331B for materials SGJIT01 and SGJIT02.

-
    - Accounting 1
        - Standard Price: <10>
        - Valuation Class: 7920 (Finished product)
    - Accounting 2

|  |
| --- |
| Note Material name should be the same as mentioned above; the details of the material can change. Follow similar steps to create materials RP001JIT02, RP001JIT03, and RP001JIT04. |

##### Create Vendor

Vendor can be created with the following steps, for example:

1. Go to transaction BP.
2. Create a vendor with the following information:
    - Address information
    - Purchasing information
        - Purchase Organization: <E001>
        - Currency: <INR>
3. Under Partner Function tab, maintain an entry for supplier, that is to say, vendor number, and assign the BP number.

|  |
| --- |
| Note The vendor number can be found in the Vendor: General Data tab of BP. |

##### Create Purchasing Scheduling Agreement

Purchasing Scheduling Agreement can be created with the following steps, for example:

1. Go to transaction ME31L.
2. Create a Purchasing Scheduling Agreement with the following information:
    - Vendor: <Specify the vendor number created in the above step>
    - Agreement Type: LPA
    - Purchasing Organization and Group: <for example, E001 / 000>
    - Validity Date: <>
    - Incoterm: CFR
    - Material: RP001JIT01
    - Target Quantity: <for example, 10 >
    - Net Price: <for example, 10>
    - Plant: 3310
    - Confirmation Control Key: 0001
3. Save the entries; the scheduling agreement is created.
4. Follow similar steps to create purchasing scheduling agreements for RP001JIT02, RP001JIT03, and RP001JIT04.

|  |
| --- |
| Note Make sure the Kanban indicator Z is maintained for scheduling agreement. |

##### Create Supply Area

A new supply area can be created with the following steps, for example: (An existing entry can also be used)

1. Go to transaction PK05S.
2. Maintain the following information and choose Save:
    - Plant: 3310
    - Supply Area: PSA_01
    - Description: <Description>
    - Supply Area Responsible

|  |
| --- |
| Note Create additional supply areas PSA_02, PSA_03, and PSA_04 for plant 3310, as mentioned above, which would be used for different scenarios. |

##### Create Control Cycle

A new control cycle can be created with the following steps, for example:

1. Go to transaction PKMC.
2. Maintain the plant and execute.
3. In change mode, choose Create Action.
4. Select Manual Summarized JIT Call
5. Maintain the following and choose OK:
    - Material: RP001JIT01
    - Plant: 3310
    - Production Supply Area: PSA_01
    - Life Cycle Status: Released
6. Maintain the following and choose Save:
    - Call
        - Call Item Qty: <50> EA
    - External Procurement
        - Ext. Procurement: <AUE1>
        - Agreement: <Scheduling agreement number>
    - Flow Control
        - JIT Call Prof.: <AU01>
    - Plng
        - Schedule Profile: <AU01>
        - RLT[h:mm]: <:25>

|  |
| --- |
| Note Create additional control cycle with PSA_02 as production supply area, to be used for scenario Summarized JIT Calls [Supply from Production]. |

##### Create Control Records

A new control record can be created with the following steps, for example:

1. Go to transaction PJNK1.
2. Select output type OJIT and choose Enter.
3. Maintain the following entries and choose Save:
    - Plant: 3310
    - JC Profile: AU01
    - Vendor: <Vendor No.>
    - Function: VN
    - Medium: 6 (EDI)
    - Date / Time: 4 (Send Immediately)
    - Language: EN

#### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Set Initial Stock for Material

To run through this scope item, the materials must be available in stock.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Warehouse Clerk (SAP_BR_WAREHOUSE_CLERK) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Post Goods Movement (MIGO) app. | The Goods Receipt Other screen is displayed. | It will be displayed this way only if it was your last transaction. So the action for you should be to select the Reference Document for MIGO Transaction Other field. |
| 3 | Enter the Movement Type | Select the following options and then choose Enter. Select the following:Trans./Event: Goods ReceiptReference Document: Other |  |  |
| 4 | Make Entry in the Goods Receipt Other Screen: Material tab | In the Goods Receipt Other screen: Material tab, make the following entry and choose Enter. Enter values for the following:Material: FGJIT01 |  |  |
| 5 | Make Entry in the Goods Receipt Other Screen: Quantity tab | In the Goods Receipt Other screen: Quantity tab, make the following entries and choose Enter. Enter values for the following:Qty in Unit of Entry: 100, for exampleUnit of Entry: Pc, for example |  |  |
| 6 | Make Entry in the Goods Receipt Other Screen: Where tab | In the Goods Receipt Other screen: Where tab, make the following entries and choose Enter.Movement Type: 561- Receipt per initial entry of stock balances into unr.-usePlant: 3310Storage Location: 331A |  |  |
| 7 | Make Entry in the Goods Receipt Other Screen: Batch tab | In the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of manufacture: <Current date or a past date> |  | Only relevant for batch-relevant materials |
| 8 | Save your Entries | Choose Post. |  |  |
| 9 | Set Stock for FGJIT02 | Follow the above steps and set stock for material FGJIT02.In the Goods Receipt Other screen, Material tab, make the following entry and choose Enter. Enter values for the following:Material: FGJIT02Plant: 3310Storage Location: 331A |  |  |
| 10 | Set Stock for RMJIT01 and RMJIT02 | Follow the above steps and set stock for materials RMJIT01 and RMJIT02In the Goods Receipt Other screen, on the Material tab, make the following entry and choose Enter. Enter values for the following:Material: RMJIT01 and RMJIT02Plant: 3310Storage Location: 331B |  |  |

#### Create Serial Numbers in Stock

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Warehouse Clerk (SAP_BR_WAREHOUSE_CLERK) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Post Goods Receipt without Reference (F3244) app. | The Post Goods Movement without Reference screen is displayed. | Create serial numbers in stock by posting goods receipt without purchase documents or production orders. |
| 3 | Make Entry in the Items tab | Enter values as follows:Material: SGJIT02-SERIALIZEDQuantity: <10, for example>Unit of Entry: <EA, for example>Auto-Create Serial Numbers: XPlant: 3310Storage Location: 331BStock Type: Unrestricted-Use |  |  |
| 4 | Save your Entries | Choose Post. |  |  |
| Display Material Serial Number |  |  |  |  |
| 5 | Log On | Log on to the SAP Fiori Launchpad using the Maintenance Planner (SAP_BR_MAINTENANCE_PLANNER) role. | The SAP Fiori launchpad displays. |  |
| 6 | Access App | Open the Display Material Serial Number app. Alternatively, you can run IQ09 or IQ03 transactions. | The Display Material Serial Number: Initial screen is displayed. |  |
| 7 | Display the serial numbers created in steps above | Enter the below information:Material: SGJIT02-SERIALIZEDChoose Existing SerialNos list. | The Display Material Serial Number: Serial Number list is displayed with serial number and plant/storage location information. |  |

#### Assign Sold-To Party for EDI Processing

In this SAP Fiori master data app, you can define supplier, plant, unloading point and sold-to party.

Procedure

1. Log on to the SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system.
2. The logged in user should have the business role SAP_BR_INTERNAL_SALES_REP.
3. Open the SAP Fiori app Sales Scheduling Agreement Master Data > Assign Sold-to Parties.
4. On the list page of the SAP Fiori app, you can see all the processing options that are saved in the database as well as the draft processing options.
5. On choosing Create icon, you can create a new sold-to party assignment with supplier, plant, unloading point and valid sold-to party.
6. Enter the following details:

| Fields | Example Values |
| --- | --- |
| Supplier | Number generated from 2YX master data script |
| Partner Description (Plant) | P001 |
| Unloading Point | UL01 |
| Sold-To Party | 33154801 |

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
| Sales Document Type | LZJ |

1. Choose Save.

#### Convert External to Internal Partner Number

The external partner number is the number used by customers to identify themselves in their message to the SAP system, including the SAP partner function. You can convert the external number belonging to an EDI partner into an internal number.

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

-
    - SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Convert External to Internal Partner Numbers.

Choose Open Documentation for the found line item to see more details about this configuration activity.

Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

1. Choose New Entries. You can create your own entries as shown in the following example:

| Fields | Example Values |
| --- | --- |
| Customer Number / Customer | 33154801 |
| Partner Function / Ext. Function | SH (Ship-To Party), SP (Sold-To Party) |
| External Partner Number | P001 |
| Internal Partner Number | 33154801 |

1. Choose Save.

#### Master Data for Repetitive Manufacturing Scenarios

##### Create Product Cost Collectors

This step can only be executed if product cost planning is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Cost Accountant - Production SAP_BR_PRODN_ACCOUNTANT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Create Product Cost Collectors - Production Versions - Collective (KKF6M). | The Create Multiple Product Cost Collector for Production Versions screen opens. |  |
| 5 | Enter Relevant Values | Make the following entries and choose Run:Plant: 3310Material: SGJIT01Order Type: YBMROnly Repetitive Mfg Mat: select |  |  |
| 6 | Exit | Choose Exit. |  |  |
| 7 | Create Product Cost Collector for Material SGJIT02 | Follow steps 1 to 6 to create product cost collectors for material SGJIT02. |  |  |

##### Create Preliminary Cost for the Product Cost Collector

This step can only be executed if product cost planning is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Cost Accountant - Production SAP_BR_PRODN_ACCOUNTANT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Create Preliminary Cost Estimate - Product Cost Collectors (MF30). | The Creation of Preliminary Cost Estimates for Product Cost Collectors screen opens. |  |
| 5 | Enter Relevant Values | Make the following entries and choose Run:Costing Date: <Current Date>Plant: 3310 |  |  |

##### Maintain JIT Production Confirmation Profile

This step needs to be executed in order to maintain appropriate profiles for execution of backflush/goods movement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Planner SAP_BR_PRODN_PLNR). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Manage Product Master Data (F1602). | The Manage Product Master Data screen opens. |  |
| 3 | Search Material | For the Summarized JIT Call (Suppy from Production) scenario, enter SGJIT01 in Product filter and choose Go.Note If you are running the Sequenced JIT Call (Suppy from Production) scenario, enter SGJIT02 instead.For the Sequenced JIT Call - Serialized Material (Supply from Production) scenario, enter SGJIT02-SERIALIZED instead. | Product SGJIT01 is filtered. |  |
| 4 | Navigate to Object Page | Click on the chevron to navigate to the object page. | Object page of chosen material is displayed. |  |
| 5 | Navigate to Plant 3310 | Choose Plants and click on chevron against plant 3310. | Object page of chosen plant is displayed. |  |
| 6 | Navigate to Repetitive Manufacturing section | Choose MRP Data and select Repetitive Manufacturing. | Repetitive Manufacturing section is displayed. |  |
| 7 | Maintain JIT Production Confirmation Profile | Choose Edit. Choose the menu option for JIT Production Confirmation Profile. Select value Asynchronous execution of Backflush. Choose Apply. | The chosen entry is saved as draft entry. |  |
| 8 | Save the changes | Choose Save. | Appropriate JIT Production Confirmation Profile is saved for material SGJIT01 |  |

#### Preliminary Steps for Electronic Invoicing (Optional)

These settings are optional, but necessary if you want to test eDocument Cockpit.

Purpose

To be able to run the optional step for eDocument Cockpit, the following prerequisites should be met:

- Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301)
- Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304)
- Assign Business Partner Identification Types to Party ID types (EDOEUBPIDTYPEV) (SSCUI 103302)

##### Assign Party ID Types to Business Partner (EDOEUBUPAV)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution.In the Set Country Version dialog box, select the country from the dropdown menu and choose Set Country Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Settings for Peppol item name and choose arrow at the item end. | The Configure Your Solution - Settings for Peppol screen displays. |  |
| 6 | Navigate to Assign Party ID Types to Business Partner | For the Assign Party ID Types to Business Partner row, choose Configure. | The Assign Party ID Types to Business Partner screen displays. |  |
| 7 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Partner ID: <business partner ID>Type: C Customer / V VendorParty ID type: SG: UENE-mail: <select this only if the customer cannot receive electronic invoices> |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app.Search for the Assign Party ID Types to Business Partner activity and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Party ID Types to Business Partner screen displays. |  |
| 3 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Partner ID: <business partner ID>Party ID type: SG: UENType: C Customer / V VendorE-mail: <select this only if the customer cannot receive electronic invoices> |  |  |

##### Assign Party ID Types to Companies (EDOEUCOMPV)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution.In the Set Country Version dialog box, select the country from the dropdown menu and choose Set Country Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Settings for Peppol item name and choose arrow at the item end. | The Configure Your Solution - Settings for Peppol screen displays. |  |
| 6 | Navigate to Assign Party ID Types to Companies | For the Assign Party ID Types to Companies row, choose Configure. | The Assign Party ID Types to Companies screen displays. |  |
| 7 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Company code: 6110Party ID type: SG: UEN |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app.Search for the Assign Party ID Types to Companies activity and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Party ID Types to Companies screen displays. |  |
| 3 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Company code: 6110Party ID type: SG: UEN |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | System | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- | --- |
| Create/Change JIT Customer Data | SAP S/4HANA Cloud Public Edition | Master Data Specialist - Just-In-Time Supply | Manage JIT Customer data (F3011) | Just-In-Time customer master data created |
| Create/Change JIT Customer Supply Controls | SAP S/4HANA Cloud Public Edition | Master Data Specialist - Just-In-Time Supply | Manage JIT Customer Supply Controls (F3010) | Just-In-Time customer supply controls created |
| Create/Change Packing Group Specification for Sequenced JIT Calls | SAP S/4HANA Cloud Public Edition | Master Data Specialist - Just-In-Time Supply | Manage Packing Group Specification for Sequenced JIT Calls (F3896) | Just-In-Time packing group specification created |
| Create/Change JIT Delivery Sequence Groups | SAP S/4HANA Cloud Public Edition | Master Data Specialist - Just-In-Time Supply | Manage JIT Delivery Sequence Groups for Sequence JIT Calls (F4879) | Just-In-Time delivery sequence groups created |
| Create/Change Teams and Responsibilities: Just-In-Time | SAP S/4HANA Cloud Public Edition | Master Data Specialist - Just-In-Time Supply | Manage Teams and Responsibilities (F5787) | Just-In-Time teams created |
| [Create Sales Scheduling Agreement](#unique_29) [page ] 36 | SAP S/4HANA Cloud Public Edition | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Sales Scheduling Agreement is created |
| [Create Customer Summarized Just-In-Time Call Using Integration](#unique_30) [page ] 39(Corresponding JIT call will be created in Supplier Cloud system) | [Customer System] SAP S/4HANA Cloud Public Edition / SAP ERP On-Premise |  | PK23 | Summarized JIT Call is created |
| [Create Customer Sequenced Just-In-Time Call Manually](#unique_31) [page ] 62 | SAP S/4HANA Cloud Public Edition | Material Planner - Just-In-Time Supply | Manage Customer JIT Calls (F6078) | Sequenced JIT Call is created |
| Monitor Just-In-Time Calls (Optional) | SAP S/4HANA Cloud Public Edition | Material Planner - Just-In-Time Supply | Manage Customer JIT Calls (F6078) | View Just-In-Time Calls from OEMs |
| [Change Customer Sequenced Just-In-Time Call Manually (Optional)](#unique_32) [page ] 64 | SAP S/4HANA Cloud Public Edition | Material Planner - Just-In-Time Supply | Manage Customer JIT Calls (F6078) | Customer Just-In-Time Call is changed |
| Manage Customer JIT Calls – ByComponent Groups (Optional) |  | Material Planner - Just-In-Time Supply | Manage Customer JIT Calls (F6077) | Monitor/Manage Customer JIT Calls – by Component Groups |
| Manage JIT Packing Groups (Optional) | SAP S/4HANA Cloud Public Edition | Material Planner - Just-In-Time Supply | Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) | Monitor/Manage Packing Groups |
| Release Summarized JIT Calls to Production | SAP S/4HANA Cloud Public Edition | Production Planner - Lean Manufacturing | Release JIT Calls to Production (F4330) | Summarized JIT Call released to production |
| Release Sequenced JIT Calls to Production | SAP S/4HANA Cloud Public Edition | Production Planner - Lean Manufacturing | Release JIT Calls to Production (F4331) | Sequenced JIT Call released to production |
| Confirm JIT Calls for Production | SAP S/4HANA Cloud Public Edition | Production Operator - Lean Manufacturing | Confirm Production for Customer JIT Calls (F4315) | Confirm JIT Call for production |
| Process Customer JIT Calls – by Scan/ Data Entry | SAP S/4HANA Cloud Public Edition | Production Operator - Lean Manufacturing | Process Customer JIT Calls (F5138) | Process Customer JIT Calls by Component Groups/Packing Groups |
| [Create Outbound Delivery from Summarized JIT Calls](#unique_33) [page ] 43 | SAP S/4HANA Cloud Public Edition | Shipping Specialist - Just-In-Time Supply | Create Outbound Deliveries (F3012) | Outbound delivery is created |
| Assign Handling Units to Outbound Delivery (Only for Summarized JIT Calls) | SAP S/4HANA Cloud Public Edition | Shipping Specialist - Just-In-Time Supply | Change Outbound Delivery (VL02N) | Handling unit is created. |
| Create Handling Units from Packing Groups for Sequenced JIT Calls | SAP S/4HANA Cloud Public Edition | Material Planner - Just-In-Time Supply | Schedule Handling Unit creation from JIT Package Group (F5260) | Handling unit is created for packing groups. |
| [Create Outbound Delivery from Sequenced JIT Calls](#unique_34) [page ] 69 | SAP S/4HANA Cloud Public Edition | Shipping Specialist - Just-In-Time Supply | Create Outbound Deliveries from Sequenced JIT Calls (F3897) | Outbound delivery is created |
| [Execute Picking and Post Goods Issue](#unique_35) [page ] 104 | SAP S/4HANA Cloud Public Edition | Shipping Specialist - Just-In-Time Supply | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking for the delivery is executed.The goods issue is posted. |
| [Create Billing Document](#unique_36) [page ] 105 | SAP S/4HANA Cloud Public Edition | Billing Clerk | Create Billing Documents (F0798) | Billing document is created |

## Test Procedures

This section describes procedures for each process step that belongs to scope item 2EM - Just-In-Time Supply to Customer.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, You can search for objects such as apps or factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data, or find related objects.

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

### Create Just-In-Time Customer Master Data

Purpose

To maintain JIT-specific information for a JIT customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Data app | Customer information is displayed. | By default, all the customers for whom the JIT-relevant information is maintained are displayed. You can filter to narrow down the customers list. |
| 3 | Create JIT-Relevant Customer | Choose Create to create a JIT-relevant customer. | Object screen is displayed. |  |
| 4 | Maintain Customer ID | Choose Enter Customer: 33154801 |  | By default, the following information is displayed on the screen:Sales Area, Country, City, Status |
| 5 | Maintain Different Destinations for a Customer for Different Processes | On the Customer Detail screen, make the following entries:DestinationCustomer Supply Area: PSA_01Unloading Point: UL02Customer Assembly Location: <Body Shop>DestinationCustomer Supply Area: PSA_02Unloading Point: UL03Customer Assembly Location: <Body Shop>DestinationCustomer Supply Area: PSA_03Unloading Point: UL04Customer Assembly Location: <Body Shop>DestinationCustomer Supply Area: PSA_04Unloading Point: UL01Customer Assembly Location: <Body Shop> |  |  |
| 6 | Maintain Additional JIT-specific Information for a Customer | On the Customer Detail screen, additionally make the following entries and choose Save and Activate:External Status MappingTransmitted Status: <Blank>External Status: SNEWExternal Status MappingTransmitted Status: SNEWExternal Status: SMODCall ProcessingExt. JIT Call No. Unique for (Days): 9999Sequence Number Profile: <Blank>[Optional] Split criteria for summarized JIT calls: No split[Optional] Split criteria for sequenced JIT calls: No split |  | For Delivery Split Criteria, there is no default option selected.For Split criteria for summarized JIT calls, the following options can be selected from the menu:External Component Group Number: Selecting this option splits the delivery document based on external component group number.External JIT Call Number: Selecting this option splits the delivery document based on external JIT call number.For Split criteria for sequenced JIT calls, the following options can be selected from the menu:Customer Supply Area: Selecting this option splits the delivery document based on customer supply area.Delivery Sequence Group: Selecting this option splits the delivery document based on delivery sequence group.Planned Handling Units: Selecting this option splits the delivery document based on planned handling units. |
| 7 | Save the Entries | Choose Save and Activate | The status of the customer is set to Active. |  |

### Create Just-In-Time Teams and Define Responsibilities

Purpose

To create different teams for processing JIT calls by component groups (JIT1CG) and packing groups (JIT1PG).

Multiple teams could be created based on different team types per standard team category of component group/packing group. Responsibility definitions can be maintained for each team as pre-filters. Users can be assigned as team members and various functions shall be assigned to each user.

The user can log on to different applications (as mentioned below) to perform business processes based on the team to which he/she is assigned.

Team definition is a prerequisite to be able to perform business processes via applications:

- Process Customer JIT Calls – by Scan/Data Entry
- Manage JIT Customer JIT Call – by Component Groups
- Manage JIT Packing Groups

Prerequisites

- If you are using a standard business user as Team Member to perform business operations (using the above mentioned applications), you must assign the appropriate business roles authorized to perform the business operations (Refer to Overview table above) to the respective business user.

For example, if you are using the business user Material Planner Just-In-Time Supply (MATL_PLNR_JIT_S_TO_C) as a team member and would like to perform outbound delivery creation, then you need to assign role SAP_BR_SHIP_SPECIALIST_JIT to that business user.

.

- If you are creating your own business user and assign this newly created business user as team member to perform various business operations using the above mentioned applications, you need to assign the appropriate business roles authorized to perform the business operations (Refer to Overview table above) to the business user created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). You will also need the role Business Process Specialist (SAP_BR_BUSINESS_PROCESS_SPEC). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F5787). |  |  |
| Create a Team for Production Activities - [Scenario: Summarized JIT Calls (Supply with Production)] |  |  |  |  |
| 3 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 4 | Maintain JIT Teams | On Team screen, make the following entries:HeaderDescription: <fill in the description>Name: <fill in the name>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Call Component Groups Generally (JIT1CGGEN)Status: EnabledResponsibility Definitions:Component Group Material: SGJIT01Customer Supply Area: PSA_02Internal Processing Status: <Internal status on which component groups could be released for production and production confirmation>JIT Customer: 33154801Plant: 3310Assign Team MemberCreate: <Assign a team member (see prerequisites) who would be performing the below business processes>S1_JC_R2P: Release JIT Call to ProductionS1_JC_CP: Confirm Production |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 5 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Create a Team for Release to Packing - [Scenario: Sequenced JIT Calls (Supply from Stock)] - OPTIONAL |  |  |  |  |
| 6 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 7 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Packing Groups Generally (JIT1PGGEN)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_03JIT Customer: 33154801Plant: 3310Packing Group Status: I - In ProcessVerification Profile: S1_PG_AUTO_PROC_02 (Scan Alternate Packing Group ID for automatic processing)Assign Team MemberCreate: <Assign a team member (see prerequisites) who would be performing the below business process>S1_PG_RPCK: Release to Packing |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 8 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Create a Team for Confirm Packing [Scenario: Sequenced JIT Call (Supply from Stock)] |  |  |  |  |
| 9 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 10 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Call Component Groups Generally (JIT1CGGEN)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_03Internal Processing Status: <0130/ 0135/ 0140> or <Internal status on which component groups could be confirmed for packing>JIT Customer: 33154801Plant: 3310Verification Profile: S1_CG_AUTO_PROC_01 (Scan External JIT Call No. for automatic processing)Assign Team MemberCreate: <Assign a team member (see prerequisites) who would be performing the below business process>S1_JC_PACK: Confirm Packing |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 11 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Create a Team for Production Activities [Scenario: Sequenced JIT Calls (Supply with Production)] |  |  |  |  |
| 12 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 13 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Call Component Groups Generally (JIT1CGGEN)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_04Internal Processing Status: <Internal status on which component groups could be released for production and confirmation of production>JIT Customer: 33154801Plant: 3310Assign Team MemberCreate: <Assign a team member (see prerequisites) who would be performing the below business processes>S1_JC_R2P: Release JIT Call to ProductionS1_JC_CP: Confirm Production |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 14 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Create a Team for Release to Packing [Scenario: Sequenced JIT Call (Supply with production) including serialized materials] - Optional |  |  |  |  |
| 15 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 16 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Packing Groups Generally (JIT1PGGEN)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_04JIT Customer: 33154801Plant: 3310Packing Group Status: <I – In Process>Verification Profile: S1_PG_AUTO_PROC_02 (Scan Alternate Packing Group ID for automatic processing)Assign Team MemberCreate: <Assign a team member (see prerequisites) who would be performing the below business process>S1_PG_RPCK: Release to Packing |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 17 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Create a Team for Confirm Packing [Scenario: Sequenced JIT Call (Supply with Production) including serialized materials] |  |  |  |  |
| 18 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 19 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Call Component Groups Generally (JIT1CGGEN)Status: EnabledResponsibility Definitions:Customer Supply Area: PSA_04Internal Processing Status: <0130/ 0135/ 0140> or <Internal status on which component groups could be confirmed for packing>JIT Customer: 33154801Plant: 3310Verification Profile: S1_CG_AUTO_PROC_01 (Scan External JIT Call No. for automatic processing)Assign Team MemberCreate: <Assign a team member (see prerequisites) who would be performing the below business process>S1_JC_PACK: Confirm Packing |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 20 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |
| Create a Team for Production Confirmation [Scenario: Sequenced JIT Call (Supply with Production) of Serialized Material] |  |  |  |  |
| 21 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 22 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Confirm Production for JIT Call Component Groups (JIT1CGCPR)Status: EnabledResponsibility Definitions:Component Group Material: SGJIT02-SERIALIZEDCustomer Supply Area: PSA_04JIT Customer: 33154801Plant: 3310Verification Profile: S1_CG_AUTO_PROC_SN01 (Scan External JIT Call No. for automatic processing)Assign Team MemberCreate: <Assign a team member (see prerequisites) who would be performing the below business process>S1_JC_CP: Confirm Production |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 23 | Save the Entries | Choose Save | The status of the team is set to Enabled. |  |

### Summarized JIT Calls (Supply from Stock)

#### Create Just-In-Time Master Data

##### Create Customer Supply Control Records

Purpose

To create a customer supply control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Supply Controls (F3010) app. |  |  |
| 3 | Create Customer Supply Control | Choose Create to create a new customer supply control | Object screen is displayed to create a new customer supply control |  |
| 4 | Maintain Customer Supply Control | On the Supply Control Detail screen, make the following entries and choose Save and Activate:Supply ControlSupply Control DescriptionCustomer: 33154801PlantPlant: 3310Supply AreaCustomer Supply Area: PSA_01Component Group MaterialComponent Group Material: FGJIT01Call ProcessingAction Control: S2C_SUMJCCall Type: Summarized JIT CallRepetitive Manufacturing is Allowed: Yes (In case of repetitive manufacturing scenarios only)Production Version: 0001Delivery ControlDelivery Confirmation Control: No delivery confirmationPartial Delivery Allowed: YesUnderdelivery Tolerance (%): 99Overdelivery Tolerance (%): 0.00Unlimited Overdelivery Allowed: No |  | The below information is retrieved from JIT Customer Master and displayed:Unloading Point, Assembly Location |
| 5 | Save the Entries | Choose Save and Activate | The status of the supply control is set to Active. |  |

#### Create Sales Scheduling Agreement

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

#### Copy and Replace Sales Scheduling Agreements (Optional)

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

#### Create Customer Summarized Just-In-Time Call

Purpose

In this step, a summarized JIT call is created from a customer (simulated) system.

Prerequisites

- Make sure the material for which the JIT call is triggered from SAP ERP system is assigned with the same vendor material number as maintained in the sales scheduling agreement.
- Supply area maintained for the material in control cycle should match with the supply area maintained for OEM in Manage Customer Master Data app.
- Purchase schedule agreement document should be created with type LPA and the Kanban indicator should be set.

Example to setup a master data in SAP On-Premise system is mentioned in Master Data Creation in SAP On-Premise System documentation.

##### Create Customer Summarized Just-In-Time Call Using Integration

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
| 1 | Log On | Log on to the SAP S/4HANA On-Premise or SAP ERP On-Premise System | The SAP Fiori launchpad displays. |  |
| 2 | Create Summarized JIT Call | Go to transaction PK23 |  |  |
| 3 | Choose control cycle | Make the following entries and choose Save:Control Cycle Radio Button: SelectedControl Cycle No.:<Control Cycle No., for example, 228> |  |  |
| 4 | Save the Entries | Choose Save. | Summarized JIT call is created and transmitted to vendor via IDoc. |  |
| 5 | View IDoc Details | To view more information on the JIT call details sent to vendor, go to transaction JITOM. |  |  |
|  |  | Expand the IDoc generated. |  |  |
|  |  | Choose the header information record and right-click |  |  |
|  |  | Select IDoc. | Details of the IDoc sent to vendor are displayed. |  |

##### Create Customer Summarized Just-In-Time Call Manually (Optional)

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
| 4 |  | On Manage Customer JIT Calls screen, make the following entries:Header DetailsExternal Call Number: <Number to identify the JIT call uniqely from customer perspective>Call Type: Summarized JIT CallMaterial Usage Indicator: S SeriesReorder: NoPartner DataPartner Description of Ship-To Party: <P001>Partner Description of Supplier: 33154801 | The following attributes are derived and populated automatically:Ship-To PartySold-To PartySales OrganizationDistribution ChannelDivisionUnloading Point |  |
| 5 | Add/Create Components | To add components into a JIT call, navigate to Components facet and choose Create. | Object page for maintaining data related to component material is displayed. |  |
| 6 |  | Make the following entries in the object page by choosing Add. Choose Apply after maintaining the below data:Customer Material Number: CFGJIT01External Component Group Number: <Number to group the component groups together> [Optional]Unloading Point: UL01Customer Assembly Location: <Body Shop>Customer Supply Area: PSA_01Requested Quantity: <Enter the requested quantity>Requirement Date and Time: <Enter the requirement date>Transmitted External Status: SNEW | The following are derived and auto-filled, while the object page is closed automatically:Component Material NumberComponent Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemCustomer Supply Area Desc. |  |
| 7 |  | Choose Create. | The component groups are derived automatically, either based on the BAdI implementation or on rules set in the SAP Business Rules service or default component group determination.The following entries are filled for component group:Component Group NumberComponent Group MaterialCustomer Supply ControlInternal Processing StatusRequirement DatePlanned Delivery Creation Date/TimePlanned Goods Issue Date/TimePlantCustomer Supply AreaOnce all the above information is derived successfully, the JIT call is saved and activated with lifecycle status Active. |  |

#### Cancel Customer Summarized Just-In-Time Call (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

- A new JIT call has been created. Refer to section Create Customer Summarised Just-In-Time Call - Integration.
- Make sure the material for which the JIT call is triggered from SAP ERP system is assigned with the same vendor material number as maintained in the sales scheduling agreement.
- Supply area maintained for the material in control cycle should match with the supply area maintained for OEM in Manage Customer Master Data app.
- Purchase schedule agreement document should be created with type LPA and the Kanban indicator should be set.

Example to setup a master data in SAP On-Premise system is mentioned in Master Data Creation in SAP On-Premise System section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA On-Premise or SAP ERP On-Premise System. | The SAP Fiori launchpad displays. |  |
| 2 | Create Summarized JIT Call | Go to Transaction JITOM |  |  |
| 3 | Cancel JIT Call | Select the JIT call to be cancelled and choose Execute Action. |  |  |
| 4 |  | Choose the cancel action ZCAN | IDOC is triggered with cancellation status |  |
| 5 | Logon | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply (SAP_BR_MATL_PLNR_JIT_S_TO_C) |  |  |
|  | Access the App | Open Manage Just-In-Time Customer Data app. | The selected JIT call should have a status Cancelled. |  |

#### Create Outbound Delivery from Summarized JIT Calls

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Summarized JIT Calls (F3922). |  |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Go:Ship-to Party: 33154801 | Ship-to party 33154801 is displayed with additional information. |  |
| 4 | Create Outbound Delivery | Choose Component Group FGJIT01 and choose Create Outbound DeliveryNote Ensure that both the overdelivery and underdelivery tolerance values set in customer supply controls are less than 100%. | Accordingly the JIT call status is updated to Delivery Created. | Note Outbound delivery is created based on the selected split criteria; refer to section Create Just-In-Time Customer Master Data. |
| 5 | View Logs | Choose View Logs to view any errors/warnings that occured during delivery creation | The delivery view logs application screen is displayed with details. |  |
| 6 | Integration with EWM – Optional | To execute picking in EWM, go to succeeding processes under Appendix section of this document and execute scope item 3BS - Warehouse Outbound Processing. | Picking of material can be done in EWM, subsequently updating the JIT call. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the Shipping Specialist role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Assign Handling Units to Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign a handling unit to outbound delivery. This step is valid only for summarized JIT calls and is a part of scope item 4MM – Handling Unit Management. (Refer to Succeeding Processes section.)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) and enter the delivery document number created in the previous step. |  |  |
| 3 | Maintain the Outbound Delivery | Choose the item and click on Pack. |  |  |
| 4 | Assign the Handling Unit | Enter the packaging material PKGJITHU and press Enter. Choose the material to be packed and the handling unit, then click on Pack button. | Handling unit is created. |  |
| 5 | View the Assigned Handling Unit | Go to Manage Customer JIT Calls app and view the assigned handling unit under Component Group section. | Clicking on handling unit number shows further information. | [Optional] Repeat these steps to create multiple handling units, which can be then split based on the steps in the following chapter. |

### Summarized JIT Calls (Supply with Production)

#### Create Just-In-Time Master Data

##### Create Customer Supply Control Records

Purpose

To create a customer supply control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Supply Controls (F3010) app. |  |  |
| 3 | Create Customer Supply Control | Choose Create to create a new customer supply control | Object screen is displayed to create a new customer supply control |  |
| 4 | Maintain Customer Supply Control | On the Supply Control Detail screen, make the following entries and choose Save and Activate:Supply ControlSupply Control DescriptionCustomer: 33154801Plant: 3310Customer Supply Area: PSA_02Component Group Material: SGJIT01Call ProcessingAction Control: S2C_SUMJCCall Type: Summarized JIT CallRepetitive Manufacturing is Allowed: Yes (In case of repetitive manufacturing scenarios only)Production Version: 0001Delivery ControlPartial Delivery Allowed: YesUnderdelivery Tolerance (%): 99Overdelivery Tolerance (%): 0.00Unlimited Overdelivery Allowed: No |  | The below information is retrieved from JIT Customer Master and displayed:Unloading Point, Assembly Location |
| 5 | Save the Entries | Choose Save and Activate | The status of the supply control is set to Active. |  |

#### Create Sales Scheduling Agreement

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
| 4 | Enter Data | On the Create Scheduling Agreement screen, make the following entries and choose Continue:Sched. Agreemt Type: LZJSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-to Party: 33154801Ship-to Party: 33154801Customer Reference: Purchase scheduling agreement number from customerMaterial Number: SGJIT01Customer Material Number: CSGJIT01 |  |  |
| 6 | Maintain Pricing | Double-click the item, and on the Condition tab, maintain the following entries:Condition Type: PPROAmount: 2 AED |  |  |
| 7 | Maintain Schedule Lines | Select the material, double-click the item, and on choose Fore.DISch (forecast delivery schedule), maintain the following:Date TypeDateOrder Quantity (Enter a round quantity only.)Storage Location: 331B (On Shipping tab) |  |  |
| 8 | Save Document | Choose Save.Make a note of the scheduling agreement number. |  |  |

#### Create Customer Summarized Just-In-Time Call

Purpose

In this step, a summarized JIT call is created from a customer (simulated) system.

Prerequisites

- Make sure the material for which the JIT call is triggered from SAP ERP system is assigned with the same vendor material number as maintained in the sales scheduling agreement.
- Supply area maintained for the material in control cycle should match with the supply area maintained for OEM in Manage Customer Master Data app.
- Purchase schedule agreement document should be created with type LPA and the Kanban indicator should be set.

Example to setup a master data in SAP On-Premise system is mentioned in Master Data Creation in SAP On-Premise System documentation.

##### Create Customer Summarized Just-In-Time Call Using Integration

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
| 1 | Log On | Log on to the SAP S/4HANA On-Premise or SAP ERP On-Premise System | The SAP Fiori launchpad displays. |  |
| 2 | Create Summarized JIT Call | Go to transaction PK23 |  |  |
| 3 | Choose control cycle | Make the following entries and choose Save:Control Cycle Radio Button: SelectedControl Cycle No.:<Control Cycle No., for example, 229> |  |  |
| 4 | Save the Entries | Choose Save. | Summarized JIT Call is created and transmitted to vendor via IDoc. |  |
| 5 | View IDoc Details | To view more information on the JIT call details sent to vendor, go to transaction JITOM. |  |  |
|  |  | Expand the IDoc generated. |  |  |
|  |  | Choose the header information record and right-click |  |  |
|  |  | Select IDoc. | Details of the IDoc sent to vendor are displayed. |  |

##### Create Customer Summarized Just-In-Time Call Manually (Optional)

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
| 4 |  | On Manage Customer JIT Calls screen, make the following entries:Header DetailsExternal Call Number: <Number to identify the JIT call uniqely from customer perspective>Call Type: Summarized JIT CallMaterial Usage Indicator: S SeriesReorder: NoPartner DataPartner Description of Ship-To Party: <P001>Partner Description of Supplier: 33154801 | The following attributes are derived and populated automatically:Ship-To PartySold-To PartySales OrganizationDistribution ChannelDivisionUnloading Point |  |
| 5 | Add Components | To add components into a JIT call, navigate to Components facet and choose Create. | Object page for maintaining data related to component material is displayed. |  |
| 6 |  | Make the following entries in the object page. Choose Apply after maintaining the below data:Customer Material Number: CSGJIT01External Component Group Number: <Number to group the component groups together> [Optional]Unloading Point: UL02Customer Assembly Location: <Body Shop>Customer Supply Area: PSA_02Requested Quantity: <Enter the requested quantity>Requirement Date and Time: <Enter the requirement date>Transmitted External Status: SNEW | The following are derived and auto-filled, while the object page is closed automatically:Component Material NumberComponent Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemCustomer Supply Area Desc. |  |
| 7 |  | Choose Create. | The component groups are derived automatically, either based on the BAdI implementation or on rules set in the SAP Business Rules service or default component group determination.The following entries are filled for component group:Component Group NumberComponent Group MaterialCustomer Supply ControlInternal Processing StatusRequirement DatePlanned Delivery Creation Date/TimePlanned Goods Issue Date/TimePlantCustomer Supply AreaOnce all the above information is derived successfully, the JIT call is saved and activated with lifecycle status Active. |  |

#### Release Summarized JIT Call Component Groups to Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release a summarized JIT call to production.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Planner - Lean Manufacturing or Material Planner - Just-In-Time Supply, depending on the user assigned to the respective team in Create Just-In-Time Teams and Define Responsibilities above. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) App. |  |  |
| 3 | Filter JIT Calls to be Released for Production | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for production activities> | Based on the responsibility definitions filter, the appropriate JIT call component groups are displayed that could be released to production. |  |
| 4 | Release to Production | Choose component group SGJIT01 and choose the function Release Summarized JIT to Production. | Accordingly the JIT call status is updated to Released for Production. |  |
| 5 | View Logs | Choose Application Log button to view successes, errors, or warnings that occurred during release to production. | The standard application log screen is displayed with details. |  |

#### Confirm Production of Summarized JIT Call Component Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note In Manage Product Master Data, you must maintain the JIT production confirmation profile as Execution of Custom Specific Logic. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Planner - Lean Manufacturing or Material Planner - Just-In-Time Supply, depending on the user assigned to the respective team in[Create Just-In-Time Teams and Define Responsibilities](#unique_39) [page ] 28 above. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) App. |  |  |
| 3 | Filter JIT Calls to Confirm Production | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for production activities> | Based on the responsibility definitions filter, the appropriate JIT call component groups are displayed that could be released to production. |  |
| 4 | Confirm Production | Select component group SGJIT01 and choose the function Confirm Production. | Accordingly the JIT call status is updated to Production Confirmed and the component groups disappear from the list based on the Internal Pro-cessing Status |  |
| 5 | View Logs | Choose Application Log button to view successes, errors, or warnings that occurred during production confirmation. | The standard application log screen is displayed with details. |  |

#### Create Outbound Delivery from Summarized JIT Calls

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries (F3012). |  |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Enter:Ship-To Party ID/Description: 33154801 | Ship-to party 33154801 is displayed with additional information. |  |
| 4 | Create Outbound Delivery | Choose Component Group SGJIT01 and choose Create Outbound Delivery | Accordingly the JIT call status is updated to Delivery Created. | Note Outbound delivery is created based on the selected split criteria; refer to section Create Just-In-Time Customer Master Data. |
| 5 | View Logs | Choose View Logs to view any errors/warnings that occured during delivery creation | The delivery view logs application screen is displayed with details. |  |
| 6 | Integration with EWM – Optional | To execute picking in EWM, go to succeeding processes under Appendix section of this document and execute scope item 3BS - Warehouse Outbound Processing. | Picking of material can be done in EWM, subsequently updating the JIT call. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the Shipping Specialist role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose More > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Assign Handling Units to Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign a handling unit to outbound delivery. This step is valid only for summarized JIT calls and is a part of scope item 4MM – Handling Unit Management. (Refer to Succeeding Processes section.)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) and enter the delivery document number created in the previous step. |  |  |
| 3 | Maintain the Outbound Delivery | Choose the item and click on Pack. |  |  |
| 4 | Assign the Handling Unit | Enter the packaging material PKGJITHU and press Enter. Choose the material to be packed and the handling unit, then click on Pack button. | Handling unit is created. |  |
| 5 | View the Assigned Handling Unit | Go to Manage Customer JIT Calls app and view the assigned handling unit under Component Group section. | Clicking on handling unit number shows further information. | [Optional] Repeat these steps to create multiple handling units, which can be then split based on the steps in the following chapter. |

### Sequenced JIT Call (Supply from Stock)

#### Create Just-In-Time Master Data

##### Create Customer Supply Control Records

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

##### Define Packing Group Specification

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

##### Create Just-In-Time Delivery Sequence Groups

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

#### Create Sales Scheduling Agreement

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
| 4 | Enter Data | On the Create Scheduling Agreement screen, make the following entries and choose Continue:Sched. Agreemt Type: LZJSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-to Party: 33154801Ship-to Party: 33154801Customer Reference: Purchase scheduling agreement number from customerMaterial Number: FGJIT02Customer Material Number: CFGJIT01 |  |  |
| 6 | Maintain Pricing | Double-click the item, and on the Condition tab, maintain the following entries:Condition Type: PPROAmount: 2 AED |  |  |
| 7 | Maintain Schedule Lines | Select the material, double-click the item, and on choose Fore.DISch (forecast delivery schedule), maintain the following:Date TypeDateOrder Quantity (Enter a round quantity only.)Storage Location: 331A (On Shipping tab) |  |  |
| 9 | Save Document | Choose Save.Make a note of the scheduling agreement number. |  |  |

#### Copy and Replace Sales Scheduling Agreements (Optional)

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

#### Create Customer Sequenced Just-In-Time Call Manually

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

#### Change Customer Sequenced Just-In-Time Call Manually (Optional)

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

#### Create JIT Delivery Schedule – Background Job (Optional)

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

#### Create Packing Group – Background Job

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

#### Release to Packing and Confirm Packing for Packing Groups

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

#### Create Handling Units from Packing Groups for Sequenced JIT Calls

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

#### Create Outbound Delivery from Sequenced JIT Calls

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

### Sequenced JIT Call (Supply with Production)

#### Create Just-In-Time Master Data

##### Create Customer Supply Control Records

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

##### Define Packing Group Specification

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

##### Create Just-In-Time Delivery Sequence Groups

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

#### Create Sales Scheduling Agreement

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

#### Create Customer Sequenced Just-In-Time Call Manually

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

#### Release Sequenced JIT Call Component Groups to Production

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

#### Confirm Production of Sequenced JIT Call Component Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Production confirmation of JIT calls for serialized materials is possible only with Process Customer JIT Calls - By Scan/Data Entry (F5138) application. Serial number assignment is not possible with any other application.

|  |
| --- |
| Note In Manage Product Master Data, you must maintain the JIT production confirmation profile as Execution of Custom Specific Logic. |

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for production confirmation of serialized materials, with the role Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Customer JIT Calls - By Scan/Data Entry (F5138) . | List of teams to which the user is assigned shall be displayed with appropriate function that could be performed with selection of the team. |  |
| 3 | Choose an appropriate team for further processing | Select the appropriate team (Created for production confirmation of serialized materials earlier) with function Confirm Production. | Displays list of JIT calls on which production confirmation could be performed. The list is filtered based on the responsibility definition attributes that are set in the teams. |  |
| 4 | Process JIT call component group for production confirmation | Enter the external JIT call number of the component group that shall be confirmed for production. | An object page is displayed based on the verification profile maintained, with below mentioned attributes available for confirmation scan:Component Group MaterialComponent MaterialSerial NumberScan each of the above attributes one by one. Once serial number is scanned, the action shall be executed and a dialog box displays success or failure message. Control navigates back to initial page for processing of next object. |  |

#### Create Packing Group – Background Job

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

#### Release to Packing and Confirm Packing for Packing Groups

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

#### Create Handling Units from Packing Groups for Sequenced JIT Calls

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

#### Create Outbound Delivery from Sequenced JIT Calls

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

#### Schedule Goods Movement from Production for Customer JIT Calls (Optional)

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

#### Reprocessing of Failed Stock Posting After Confirmation of Production (Optional)

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

### Sequenced JIT Call (Supply from Production of Serialized Materials)

#### Create Just-In-Time Master Data

##### Create Customer Supply Control Records

Purpose

To create a customer supply control for serialized material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Supply Controls (F3010) app. |  |  |
| 3 | Create Customer Supply Control | Choose Create to create a new customer supply control | Object screen is displayed to create a new customer supply control |  |
| 4 | Maintain Customer Supply Control | On the Supply Control Detail screen, make the following entries:Supply ControlSupply Control DescriptionCustomer: 33154801PlantPlant: 3310Supply AreaCustomer Supply Area: PSA_04Component Group MaterialComponent Group Material: SGJIT02-SERIALIZEDCall ProcessingAction Control: S2C_SEQJCCall Type: Sequenced JIT CallRepetitive Manufacturing is Allowed: Yes (In case of repetitive manufacturing scenarios only)Production Version: 0002Delivery ControlPartial Delivery Allowed: No |  |  |
| 5 | Save the Entries | Choose Save and Activate | The status of the supply control is set to Active. |  |

##### Define Packing Group Specification

Purpose

To create a packing group specification for serialized material as per customer requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Packing Group Specification for Sequenced JIT Calls (F3896) app. |  |  |
| 3 | Create a New Packing Group Specification | Choose Create to create a new packing group specification | Object screen is displayed to create a new packing group specification. |  |
| 4 | Maintain Packing Group Specification | On the Packing Group Specification Detail screen, make the following entries and choose Save and Activate:Packing Group Specification Description: <Packing Group Specification for Customer Name>Packaging Material: PKGJITSEQTotal Number of Slots: 2Reorder Packing Group Specification: No |  |  |
| 5 | Maintain Slot Group Information | On the Packing Group Specification Detail screen, choose Create in the Slot Group section.Make the following entries and choose Save and Activate:Slot GroupFirst Slot ID: 1Last Slot ID: 2Increment: 1Content Type: Component Group MaterialComponent Group Material: SGJIT02-SERIALIZEDWithdrawal Sort Sequence: AscendingPacking Sort Sequence: Ascending |  |  |
| 6 | Save the Entries | Choose Save and Activate | The status of the package specification is set to Active. |  |
| 7 | Create a New Reorder Packing Group Specification for material SGJIT02-SERIALIZED | Choose Create to create a new packing group specification. | Object screen is displayed to create a new packing group specification. |  |
| 8 | Maintain Packing Group Specification | On the Packing Group Specification Detail screen, make the following entries and choose Save and Activate:Packing Group Specification Description: <Packing Group Specification for Customer Name>Packaging Material: PKGJITSEQTotal Number of Slots: 2Reorder Packing Group Specification (Optional): Yes |  | Setting reorder packing group specification to Yes would make the packing group specification exclusive to reorder JIT calls. |
| 9 | Maintain Slot Group Information | On the Packing Group Specification Detail screen, choose Create in the Slot Group section.Make the following entries and choose Save and Activate:Slot GroupFirst Slot ID: 1Last Slot ID: 2Increment: 1Content Type: Component Group MaterialComponent Group Material: SGJIT02-SERIALIZEDWithdrawal Sort Sequence: AscendingPacking Sort Sequence: Ascending |  |  |
| 10 | Save the Entries | Choose Save and Activate | The status of the package specification is set to Active. |  |

##### Create Just-In-time Delivery Sequence Groups

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
| 4 | Maintain JIT Delivery Sequence Group | On Just-In-Time Delivery Sequence Group screen, make the following entries and choose Save:HeaderDescription: <fill in the description>Customer: 33154801Plant: 3310Customer Supply Area: PSA_04Number SettingsTo add number settings, choose Add Normal Setting.Prefix: <fill in the description>From: 00001To: 99999Length of Short Number: 3Assign Supply ControlCustomer Supply Control: To add customer supply control assignments, choose Add. Assign the supply control created for material SGJIT02-SERIALIZED in previous steps.Package Group Specification AssignmentIn the Package Group Specification Assignment facet, choose Create. Then assign the packing group specification created for material SGJIT02-SERIALIZED in the previous step. You must also specify appropriate Valid From and Valid To dates for this assignment.Note The Valid To date must be a future date. |  |  |
| 5 | Save the Entries | Choose Save and Activate | The status of the delivery sequence group is set to Active. |  |

#### Create Sales Scheduling Agreement

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
| 4 | Enter Data | On the Create Scheduling Agreement screen, make the following entries and choose Continue:Sched. Agreemt Type: LZJSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-to Party: 33154801Ship-to Party: 33154801Customer Reference: Purchase scheduling agreement number from customerMaterial Number: SGJIT02-SERIALIZEDCustomer Material Number: CSGJIT02-SERIALIZED |  |  |
| 6 | Maintain Pricing | Double-click the item, and on the Condition tab, maintain the following entries:Condition Type: PPROAmount: 2 AED |  |  |
| 7 | Maintain Schedule Lines | Select the material, double-click the item, and on choose Fore.DISch (forecast delivery schedule), maintain the following:Date TypeDateOrder Quantity (Enter a round quantity only.)Storage Location: 331B (On Shipping tab) |  |  |
| 8 | Save Document | Choose Save.Make a note of the scheduling agreement number. |  |  |

#### Create Customer Sequenced Just-In-Time Call Manually

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
| 4 |  | On Manage Customer JIT Calls screen, make the following entries:Header DetailsExternal Call Number: <Number to identify the JIT call uniquely from customer perspective>Call Type: Sequenced JIT CallMaterial Usage Indicator: S SeriesReorder: NoVehicle InformationVehicle Number: <Vehicle No.>Vehicle Model: <Vehicle Model>External Sequence Number: <Sequence No.> (Important for appropriate processing of sequenced JIT calls)Partner DataPartner Description of Ship-To Party: <P001>Partner Description of Supplier: 33154801 | The following attributes are derived and populated automatically:Ship-To PartySold-To PartySales OrganizationDistribution ChannelDivisionUnloading Point |  |
| 5 | Add Components | To add components into a JIT call, navigate to Components facet and choose Create. | Object page for maintaining data related to component material is displayed. |  |
| 6 |  | Make the following entries in the object page. Choose Apply after maintaining the below data:Customer Material Number: CSGJIT02-SERIALIZEDExternal Component Group Number: <Number to group the component groups together> [Optional]Unloading Point: UL04Customer Assembly Location: <Body Shop>Customer Supply Area: PSA_04Requested Quantity: <Enter the requested quantity>Requirement Date and Time: <Enter the requirement date>Transmitted External Status: SNEW | The following are derived and auto-filled, while the object page is closed automatically:Component Material NumberComponent Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemCustomer Supply Area Desc. |  |
| 7 |  | Choose Create. | The component groups are derived automatically, either based on the BAdI implementation or on rules set in the SAP Business Rules service or default component group determination.The following entries are filled for component group:Component Group NumberComponent Group MaterialCustomer Supply ControlInternal Processing StatusRequirement DatePlanned Delivery Creation Date/TimePlanned Goods Issue Date/TimePlantCustomer Supply AreaOnce all the above information is derived successfully, the JIT call is saved and activated with lifecycle status Active. |  |
| 8 | View Components of a Component Group | Under section Component Group, choose Chevron for the component group. | An object page with component details is opened with list of components for a selected component group. |  |

#### Release Sequenced JIT Call Component Groups to Production

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

#### Confirm Production of Sequenced JIT Call Component Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Production confirmation of JIT calls for serialized materials is possible only with Process Customer JIT Calls - By Scan/Data Entry (F5138) application. Serial number assignment is not possible with any other application.

|  |
| --- |
| Note In Manage Product Master Data, you must maintain the JIT production confirmation profile as Execution of Custom Specific Logic. |

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for production confirmation of serialized materials, with the role Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Customer JIT Calls - By Scan/Data Entry (F5138) . | List of teams to which the user is assigned shall be displayed with appropriate function that could be performed with selection of the team. |  |
| 3 | Choose an appropriate team for further processing | Select the appropriate team (Created for production confirmation of serialized materials earlier) with function Confirm Production. | Displays list of JIT calls on which production confirmation could be performed. The list is filtered based on the responsibility definition attributes that are set in the teams. |  |
| 4 | Process JIT call component group for production confirmation | Enter the external JIT call number of the component group that shall be confirmed for production. | An object page is displayed based on the verification profile maintained, with below mentioned attributes available for confirmation scan:Component Group MaterialComponent MaterialSerial NumberScan each of the above attributes one by one. Once serial number is scanned, the action shall be executed and a dialog box displays success or failure message. Control navigates back to initial page for processing of next object. |  |

#### Create Packing Group – Background Job

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
| 4 | Maintain Schedule Information | Make the following entries and choose Schedule:Scheduling OptionsChoose Start Immediately or define the recurring pattern and maintain the scheduling information.ParametersShip-To Party: 33154801Component Group Material: SGJIT02-SERIALIZEDCustomer Supply Area: PSA_04 | Packing groups are created based on packing group specification maintained earlier; sequenced JIT calls are packed in appropriate slots. |  |

#### Release to Packing and Confirm Packing for Packing Groups

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

#### Create Handling Units from Packing Groups for Sequenced JIT Calls

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
| 3 | Create a New Job | Choose Create to create a new job. | The Scheduling Information screen is displayed. |  |
| 4 | Maintain Schedule Information | Make the following entries and choose Schedule:Ship-to Party: 33154801Customer Supply Area: PSA_04Internal Processing Status: Packing Confirmed (0148) | Handling units are created for material FGJIT02 based on the packing groups created earlier. |  |

#### Create Outbound Delivery from Sequenced JIT Calls

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
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Go:Ship-To Party ID/Description: 33154801 | Ship-to party 33154801 is displayed with additional information. |  |
| 4 | View Contents | Choose packing group and select Chevron. | The package contents are displayed. | [Optional: Only if delivery sequence group is created] Packing group is displayed based on ascending Alternative Handling Unit ID generated, which is based on Just-In-Time delivery sequence group created in an earlier step. |
| 5 | Create Outbound Delivery | Choose Create Outbound Delivery | Accordingly the JIT call status is updated to Delivery Created. |  |
| 6 | View Logs | Choose View Logs to view any errors/warnings that occurred during delivery creation | The delivery view logs application screen is displayed with details. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Process Packing Groups (Optional)

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

### Execute Picking and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. The shipping specialist picks the goods based on the pick list and does the Post Goods Issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori Launchpad screen is displayed. | Picking is only relevant for summarized JIT calls. |
| 2 | Access the SAP Fiori App | Open Pick Outbound Delivery (F0868) app. | The Pick Outbound Delivery screen is displayed. |  |
| 3 | Maintain Delivery Document Number | Enter the summarized JIT call delivery number. |  |  |
| 4 | Enter Picking Quantity | Enter the picking quantity, for example, 1. |  |  |
| 5 | Choose Enter | Choose Enter. |  |  |
| 6 | Save | Choose Save. | The delivery is picked. |  |
| 7 | Post Goods Issue | Choose Post GI to post the goods issue. (This step is repeated for delivery numbers created for both summarized and sequenced JIT calls.) | The goods issue is posted. |  |
| 8 | Optional – Deviation in picking quantity | Choose the picking quantity different from delivered quantity in step 4 above (Enter Picking Quantity) | Open Manage Customer JIT Calls (F6078) app and go to the components section under Component Group facet. Check the delivered quantity; it should be the same as picked quantity. | Deviation in picking quantity is only relevant for summarized JIT calls. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose More > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview Delivery Note | On the Delivery: Output screen, select the line with the Output Type DELIVERY_NOTE and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Billing Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798) app. | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the footer bar, then make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) are displayed. |  |
| 5 | Select Items for Billing | Select rows of sales documents created previously and choose Create. | Create Billing Documents window is displayed. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example, current date. Then choose OK. | The draft billing document with ID is displayed. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number. | The system generates an invoice for billing.The JIT call status is set to Completed. |  |

Manage Billing Documents (Optional)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Manage Billing Documents (F0797) app and go to Sales > Billing Document . | The Manage Billing Document screen is displayed. |  |
| 2 | Search the Billing Document Created in Previous Step | Input the billing document number recorded in previous step. Choose Enter. | The billing document created in previous step is displayed. |  |
| 3 | Display the Billing Document | Select the billing document item, and choose Display. | The billing document is displayed. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block – Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document is displayed. |  |
| 6 | Cancel Billing Document (Optional) | Select an appropriate billing document and choose Cancel Billing Docs | You see a log display – Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the edit mode, add, delete or update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (optional) | In the edit mode, you can add, delete or update these texts. Save your changes by choosing Save in the footer bar. |  |  |

If you have both the preliminary billing document and billing document, then skip the next step Create Billing Document.

### eDocument Cockpit (Optional)

In order to proceed with this chapter, it is necessary that the optional step in the prerequisite section Preliminary Steps for Electronic Invoicing (Optional) is performed correctly.

| Test Step # | Test Step Name | Instruction | Expected Results |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open eDocument Cockpit (EDOC_COCKPIT). |  |
| 3 | Select eInvoice Document | Make the following entries:Source Document: <Invoice number from prior steps>You can also search for your invoice. In the Results Overview section, expand Your Country to display your country's EU eInvoice. | Your country's EU eInvoice screen displays. |
| 4 | Submit eInvoice | Select the row and choose Submit. | The eDocument status updates with a message text: Action successfully executed: SUBMIT. |
| 5 | Review Status | Review the eDocument status. The possible status of submitted eDocument can be either of the following:Accepted by Receiving Access PointReceived by Access PointError at Sending Access PointSending RequestedReceived by Access PointError at Receiving Access Point |  |
| 6 | Display eDocument | Select the row for an eDocument with Accepted by Receiving Access Point status.From menu for Display, select Display/Preview XML. | The eDocument in XML format is shown. |
| 7 | Display Source Document | Select the row of an eDocument and from the Go to menu, select Source Document. | A view displays the original transaction that generated the eDocument (source document). |
| 8 | Back | Choose < (Back) to return to the previous view. |  |
| 9 | Review History of eDocument | From the Go to menu, select History to review the eDocument history. | The view displays the last process steps and statuses from selected eDocument. |
| 10 | Back | When completing your review, choose the Back button at the bottom of the view to return to the previous view. |  |
| 11 | Review Application Log | From the Go to menu, select Application Log.When there are no errors, a No Application Log found for the selected eDocument notification is displayed at the bottom of the view.If there are errors, an Application Log dialog box displays information about the error. Review the message and choose Continue to close the dialog box. |  |
| 12 | Review Interface Log | From the Go to menu, select Interface Log.An Interface Connector Log dialog box displays. Review the information and choose Continue to close. |  |
| 13 | Cancel eDocument | To cancel an eDocument, choose the row of an eDocument with Created status.From the buttons above the list, from the More menu, select Cancel eDocument. | The status of eDocument changes to eDocument Cancelled and the status icon turns green. |
| 14 | Delete eDocument | To delete an eDocument, choose a row from the list with a Created status.Mark the eDocument in status CreatedFrom the buttons above the list, from the More menu, select Delete eDocument. | At the bottom of the view, Number of eDocuments that have been deleted: 1 notification gets displayed. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 3NR – Sales Scheduling Agreements | Create a Sales Scheduling Agreement of type LZJ, etc.Using the master data from this document, complete the following activities described in the test script:Creation of Sales Scheduling Agreement |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable (Sections: Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items) |
| 3BS - Warehouse Outbound Processing | Picking of material in EWM – only for summarized JIT callUsing the master data from this document, complete the following activities described in the test script:Picking of material can be done in EWM, subsequently updating the JIT call. |
| 4MM – Handling Unit Management | Assignment of handling unit – Only for summarized JIT callUsing the master data from this document, complete the following activities described in the test script:Assign handling unit to the outbound delivery, subsequently updating the JIT call. |
| 53X – Just-In-Time Supply to Customer with Delivery Confirmation | Using the master data from this document, complete the following activities described in the test script:Releasing of JIT delivery confirmationCreation of customer consignment issue order and subsequent documents |

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
> Flagged while digesting this document, not verified: Summarized JIT (supply from stock) scheduling agreement uses sold-to/ship-to 33154802, material FGJIT02, customer material CFGJIT02 and type LKJ, while the supply control and JIT call for this scenario use customer 33154801, material FGJIT01 and CFGJIT01 (type LZJ elsewhere).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sequenced supply-from-stock scheduling agreement uses sold-to 33154801 and customer material CFGJIT01, while its supply control, delivery sequence group and JIT call use customer 33154802 and CFGJIT02; its packing group job uses SGJIT02/PSA_04 instead of FGJIT02/PSA_03.

> [!warning] Conflict
> Flagged while digesting this document, not verified: JIT production confirmation profile for summarized production is set to 'Asynchronous execution of Backflush' in preliminary steps, but a Note in Confirm Production says it must be 'Execution of Custom Specific Logic'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/automotive-supply-to-customer-inventory-management-55f-ae-test-script]]
- related-to :: [[08-sales-order-management/test-script-just-in-time-supply-to-customer-with-delivery-confirmation]]
- related-to :: [[08-sales-order-management/test-script-sales-scheduling-agreements-3nr-ae-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 188,895 chars in the whole document
