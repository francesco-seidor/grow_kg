---
id: 08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-advanced-available-to-pro
title: "Test Script: SAP S/4HANA Cloud Public Edition - Advanced Available-to-Promise Processing (1JW_AE) (1JW_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 1JW_AE (AE): Release for Delivery, Product Allocation, Alternative-Based Confirmation, Supply Protection, BPS."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/availability-check-atp]
aliases: [1JW_S4CLD2608_BPD_EN_AE]
keywords: [Available-to-Promise and Backorder Processing, advanced available-to-promise, release for delivery, order fulfillment responsibilities, product allocation, alternative-based confirmation, substitution strategy, supply protection, business process scheduling, sales order availability check]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1JW_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-730
topic: 08-sales-order-management/availability-check-atp
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP S/4HANA Cloud Public Edition - Advanced Available-to-Promise Processing (1JW_AE) (1JW_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1JW_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Available-to-Promise and Backorder Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Available-to-Promise Processing (1JW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847274)

[2 Prerequisites 4](#_Toc232847275)

[2.1 System Access 4](#_Toc232847276)

[2.2 Roles 4](#_Toc232847277)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847278)

[2.4 Additional Manual Configuration 7](#_Toc232847279)

[2.5 Business Conditions 7](#_Toc232847280)

[2.6 Preliminary Steps 7](#_Toc232847281)

[2.6.1 Set Initial Stock for Material 8](#_Toc232847282)

[2.6.2 Self-Service Configuration to Activate Product Allocation (PAL) 9](#_Toc232847283)

[2.6.3 Self-Service Configuration to Activate Alternative-Based Confirmation (ABC) 11](#_Toc232847284)

[2.6.4 Self-Service Configuration to Activate Supply Protection (SUP) 12](#_Toc232847285)

[2.6.5 Self-Service Configuration to Activate Business Process Scheduling (BPS) 15](#_Toc232847286)

[3 Overview Table 18](#_Toc232847287)

[4 Test Procedures 20](#_Toc232847288)

[4.1 Release for Delivery 20](#_Toc232847289)

[4.1.1 Preparation Activities for Release for Delivery 20](#_Toc232847290)

[4.1.1.1 Configure Order Fulfillment Responsibilities 20](#_Toc232847291)

[4.1.2 Release for Delivery 21](#_Toc232847292)

[4.1.2.1 Prepare/Release Sales Orders for Materials Without Availability Issues for Delivery 22](#_Toc232847293)

[4.1.2.2 Identify Most Important Sales Orders for Materials with Availability Issues 23](#_Toc232847294)

[4.1.2.3 Solve Issues by Redistributing Quantities 24](#_Toc232847295)

[4.1.2.4 Release Processed Sales Orders 26](#_Toc232847296)

[4.2 Product Allocation (PAL) 27](#_Toc232847297)

[4.2.1 Preparation Activities for Product Allocation (PAL) 27](#_Toc232847298)

[4.2.1.1 Configure Product Allocation 27](#_Toc232847299)

[4.2.1.2 Manage Product Allocation Planning Data 29](#_Toc232847300)

[4.2.1.3 Manage Product Allocation Sequences 31](#_Toc232847301)

[4.2.1.4 Assign Product to Product Allocation 33](#_Toc232847302)

[4.2.2 Check Availability with Product Allocation (PAL) 34](#_Toc232847303)

[4.3 Alternative-Based Confirmation (ABC) 36](#_Toc232847304)

[4.3.1 Preparation Activities for Alternative-Based Confirmation (ABC) 36](#_Toc232847305)

[4.3.1.1 Configure Alternative Determination (Optional) 36](#_Toc232847306)

[4.3.1.2 Configure Sourcing Profile (Optional) 37](#_Toc232847307)

[4.3.1.3 Configure Substitution Strategy 37](#_Toc232847308)

[4.3.1.4 Manage Characteristic Combinations 39](#_Toc232847309)

[4.3.1.5 Configure Alternative Control 40](#_Toc232847310)

[4.3.2 Check Availability with Alternative-Based Confirmation (ABC) 41](#_Toc232847311)

[4.3.3 Check Availability with Third-Party (Optional) 43](#_Toc232847312)

[4.4 Supply Protection (SUP) 45](#_Toc232847313)

[4.4.1 Preparation Activities for Supply Protection (SUP) 45](#_Toc232847314)

[4.4.1.1 Create Master Data for Supply Protection (SUP) 45](#_Toc232847315)

[4.4.2 Check Availability with Supply Protection (SUP) 46](#_Toc232847316)

[4.5 Business Process Scheduling (BPS) 48](#_Toc232847317)

[4.5.1 Preparation Activities for Business Process Scheduling (BPS) 48](#_Toc232847318)

[4.5.1.1 Manage Characteristic Combinations 48](#_Toc232847319)

[4.5.1.2 Configure Activity Attributes 49](#_Toc232847320)

[4.5.2 Scheduling with Days Granularity 51](#_Toc232847321)

[5 Appendix 54](#_Toc232847322)

[5.1 Delete Availability Check Data 54](#_Toc232847323)

## Purpose

Overview

This scope item details the process for configuring and checking availability against defined quantities during specific time periods. Furthermore, this scope item enables you to manually prioritize requirements in order documents for materials in limited supply and release them for subsequent delivery.

You can also use this scope item to perform substitution of an originally requested delivery plant or storage location (with an alternative plant or storage location) or material when a requested requirement can't be confirmed in terms of material, requested quantity, or date. Additionally, you can pass the order along to a third-party supplier who then ships the goods directly to the customer.

This scope item enables you to define protected quantities for prioritized supply protection groups so that even in shortage situations some minimum quantities are left for these groups.

The SAP Fiori app Configure Activity Attributes can be used to flexibly determine duration and working times of scheduling activities based on document characteristics to address your business needs.

This scope item builds on the features from the Basic Available-to-Promise Processing (2LN) scope item.

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
| Order Fulfillment Specialist | SAP_BR_ORDER_FULFILLMNT_SPCLST | Order Fulfillment Execution | SAP_BR_ORDER_FULFILLMNT_SPCLST |  |
| Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR | Order Fulfillment Management | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Order Fulfillment Manager - Scheduling | SAP_BR_ORD_FLFMT_MNGR_SCHDG | Business Process Scheduling | SAP_SCM_SPT_BUS_PROC_SCHDG_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Data Privacy Specialist | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

To run through this scope item, the required materials must be available in stock and sales orders must be available. You can achieve this by following the Sell from Stock (BD9) process.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Additionally, you can use your own master data or the following sample data to go through the test.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch |  |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No serial number, no batch |  |
| Sold-to Party | 3310000433100003 | Domestic UAE Customer 4Domestic UAE Customer 3 |  |
| Ship-to Party | 3310000433100003 | Domestic UAE Customer 4Domestic UAE Customer 3 |  |
| Payer | 33100004 | Customer domestic 04 |  |
| Plant | 33103320 | Plant 1 AEPlant 2 AE | Note The second set of organization entity IDs here is an example. In an evaluation project of the SAP Central Business Configuration environment, the ID follows the naming rule described in [Using the Set Up Organizational Structure App](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/d020ff461d504421bcc55d87cbc0ae57.html). |
| Storage Location | 331A332A | Std. storage 1Std. storage 1 |  |
| Shipping Point | 33103320 | Shipping Point 3310Shipping Point 3320 | Note The second set of organization entity IDs here is an example. In an evaluation project of the SAP Central Business Configuration environment, the ID follows the naming rule described in [Using the Set Up Organizational Structure App](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/d020ff461d504421bcc55d87cbc0ae57.html). |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/6f16219a7bb12c7d41e243a0c22d2898)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | To run through this scope item, the required materials must be available in stock and sales orders must be available.Sell from Stock (BD9) - Create Sales Order |
| 2LN - Basic Available-to-Promise Processing | Run through below steps of Basic Available-to-Promise Processing (2LN) processMonitor Product AvailabilitySchedule BOP RunMonitor BOP RunDelete Availability Check Data |

### Preliminary Steps

Materials created in the Sell from Stock (BD9) process use checking group SR (Stock and Reliable Receipts).

#### Set Initial Stock for Material

Purpose

To run through this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Input Movement Type | Choose Goods Receipt and Other at the top of the screen. |  |  |
| 4 | Input on the Goods Receipt Other Screen: Material Tab | On the Goods Receipt Other screen - Material tab, make the following entry and press Enter:Material : <Material>, for example, TG11 |  |  |
| 5 | Input on the Goods Receipt Other Screen: Quantity Tab | On the Goods Receipt Other screen - Quantity tab, make the following entry and press Enter:Qty in Unit of Entry: Qty in UOMUnit of Entry: PC |  |  |
| 6 | Input on the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other screen - Where tab, make the following entries and press Enter:Movement Type: 561 - Receipt per initial entry of stock balances into usePlant: <Plant>, for example, 3320Storage Location: <storage location>, for example, 332A |  | PlantStock33100332020NoteThe material must have been extended to plant 3320 before you can test this step.Must ensure stock in plant 3320 exceeds stock in plant 3310 |
| 7 | Input on the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other screen - Batch tab, make the following entry and press Enter:Date of Manufacture: <Enter the current date or a date in the past> |  | Only relevant for batch relevant materials. |
| 8 | Save Your Entries | Choose Post. |  |  |

#### Self-Service Configuration to Activate Product Allocation (PAL)

Purpose

This process step shows you how to turn on product allocation check in your system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution：

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The various configuration sections display. |  |
| 3 | Search for a Solution Configuration | Open the Configure Your Solution configuration section, and in the Search field, enter ATP. | Various configuration activities for ATP are displayed. |  |
| 4 | Select a Solution Configuration | Choose application ATP: Product Allocation Check. | The Configure Your Solution – ATP: Product Allocation Check screen displays. |  |
| 5 | Start the Configuration Activity | Choose Configure > Advanced ATP > Activate Product Allocation. | The configuration activity is started and displays a single field, Activate.Note If the Activate field displays the value 1, you do not need to proceed with the next steps. |  |
| 6 | Edit the Activation of the Product Allocation Check in aATP | Choose Edit. | The Activate field changes to edit mode. |  |
| 7 | Activate the Product Allocation Check in aATP | Select Yes, by Requested Delivery Date from the search help of the Activate field. Alternatively, you can also select Yes, by Material Availability Date depending on which order date you would like the Product Allocation Sequence to be found with.Choose Save. | The corresponding value displays in the Activate field:Yes, by Requested Delivery DateYes, by Material Availability Date |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Product Allocation.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Edit the Activation of the Product Allocation Check in aATP | Choose Edit. | The Activate field changes to edit mode. |  |
| 4 | Activate the Product Allocation Check in aATP | Select Yes, by Requested Delivery Date from the search help of the Activate field. Alternatively, you can also select Yes, by Material Availability Date depending on which order date you would like the Product Allocation Sequence to be found with.Choose Save. | The corresponding value displays in the Activate field:Yes, by Requested Delivery DateYes, by Material Availability Date |  |

#### Self-Service Configuration to Activate Alternative-Based Confirmation (ABC)

Purpose

This process step shows you how to turn on alternative-based confirmation in system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The various configuration sections display. |  |
| 3 | Search for a Solution Configuration | Open the Configure Your Solution configuration section, and in the Search field, enter ATP. | Various configuration activities for ATP are displayed. |  |
| 4 | Select a Solution Configuration | Choose ATP: Enhanced Check Methods app. | The Configure Your Solution – ATP: Enhanced Check Methods screen displays. |  |
| 5 | Start the Configuration Activity | In the Configuration Steps section, choose Configure action. | The Configure Enhanced Check Methods by Document Purpose screen displays. |  |
| 6 | Activate the Activate Alternative-Based Confirmation in aATP | Choose New Entries and create the following:Document Purpose: SLSAvailability Checking Group: <Leave blank so that all check groups are activated with ABC, or entering the check group (search via F4) you want to activate ABC for>Description: Stock and Rel. Rec.ABC is Active: XChoose Save. | Data saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app and search for the following activity: Configure Enhanced Check Methods by Document Purpose.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Activate the Configuration Activity | Create the following entries:Document Purpose: SLSAvailability Checking Group: <Leave blank so that all check groups are activated with ABC, or entering the check group (search via F4) you want to activate ABC for>Description: Stock and Rel. Rec.ABC is Active: X | The data was saved. |  |

#### Self-Service Configuration to Activate Supply Protection (SUP)

Purpose

This process step shows you how to turn on supply protection in your system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The various configuration sections display. |  |
| 3 | Search for a Solution Configuration | Open Configure Your Solution configuration section, and in the Search field, enter ATP. | Various configuration activities for ATP are displayed. |  |
| 4 | Select a Solution Configuration | Choose ATP: Basic Settings application. | The Configure Your Solution - ATP: Basic Settings screen displays. |  |
| 5 | Start the Configuration Activity | Choose Configure of step Configure Scope of Availability Check and choose the following item:Avail: <check group of your material>, for example, <SR>Description: Stock and Rel. Rec.CRl: AChecking Rule: Sales Order | The Configure Scope of Availability Check: Change screen displays. | Note If you use Supply Protection for Sales Documents you should also activate supply protection for the relevant checking rule for stock transport orders. This is important to avoid bypassing the protection for Sales Documents. Refer to [https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/550ab9d10dd349d999aad9a287fa64ac.html?version=latest](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/550ab9d10dd349d999aad9a287fa64ac.html?version=latest) for more details. |
| 6 | Activate the Supply Protection | In the Special Scenarios area, select the checkbox of With Supply Protection for Specific Document Types. Click on Save. | The data was saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Scope of Availability Check.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Start the Configuration Activity | On the Configure Scope of Availability Check: Change screen, choose the following item:Avail: <check group of your material>, for example, <SR>Description: Stock and Rel. Rec.CRl: AChecking Rule: Sales Order | The Configure Scope of Availability Check: Change screen displays. | Note If you use Supply Protection for Sales Documents you should also activate supply protection for the relevant checking rule for stock transport orders. This is important to avoid bypassing the protection for Sales Documents. Refer to [https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/550ab9d10dd349d999aad9a287fa64ac.html?version=latest](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/550ab9d10dd349d999aad9a287fa64ac.html?version=latest) for more details. |
| 4 | Activate the Supply Protection | In the Special Scenarios area, select the checkbox of With Supply Protection for Specific Document Types. Click on Save. | The data was saved. |  |

#### Self-Service Configuration to Activate Business Process Scheduling (BPS)

Purpose

This process step shows you how to enable scheduling with Business Process Scheduling for sales orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Configure Your Solution and search for Business Process Scheduling. Go to configuration step Activate BPS for Sales Documents. | The Activate BPS for Sales Documents screen displays. |  |
| 3 | Check Data | On the Activate BPS for Sales Documents screen, make the following entries if not available and choose Save:Sales Document Type: ORItem Category: TANShipping Point: 3310Schema: SALES_DAYS |  |  |
| 4 | Access the App | Open Configure Your Solution and search for Delivery and Transportation Scheduling. Go to configuration step Define Scheduling By Sales Document Type. | The Define Scheduling By Sales Document Type screen displays |  |
| 5 | Check Data | Check if the following entries are made. If not, make the following entries and choose Save:Sales Document Type: ORDelivery Scheduling: X (selected)Transportation Scheduling: X (selected) |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the BPS Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate BPS for Sales Documents.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Check Data | On the Activate BPS for Sales Documents screen, make the following entries if not available and choose Save:Sales Document Type: ORItem Category: TANShipping Point: 3310Schema: SALES_DAYS |  |  |
| 4 | Access the Scheduling Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Scheduling By Sales Document Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 5 | Check Data | Check if the following entries are made. If not, make the following entries and choose Save:Sales Document Type: ORDelivery Scheduling: X (selected)Transportation Scheduling: X (selected) |  |  |

## Overview Table

This scope item consists of the process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| Release for Delivery |  |  |  |
| [Configure Order Fulfillment Responsibilities](#unique_15) [page ] 20 | Order Fulfillment Manager | Configure Order Fulfillment Responsibilities (F2246) |  |
| [Release for Delivery](#unique_16) [page ] 21 |  |  |  |
| [Prepare/Release Sales Orders for Materials Without Availability Issues for Delivery](#unique_17) [page ] 22 | Order Fulfillment Specialist | Release for Delivery (F1786) |  |
| [Identify Most Important Sales Orders for Materials with Availability Issues](#unique_18) [page ] 23 | Order Fulfillment Specialist | Release for Delivery (F1786) |  |
| [Solve Issues by Redistributing Quantities](#unique_19) [page ] 24 | Order Fulfillment Specialist | Release for Delivery (F1786) |  |
| [Release Processed Sales Orders](#unique_20) [page ] 26 | Order Fulfillment Specialist | Release for Delivery (F1786) |  |
| Product Allocation (PAL) |  |  |  |
| [Configure Product Allocation](#unique_21) [page ] 27 | Order Fulfillment Manager | Configure Product Allocation (F2119) |  |
| [Manage Product Allocation Planning Data](#unique_22) [page ] 29 | Order Fulfillment Manager | Manage Product Allocation Planning Data (F2121) |  |
| [Manage Product Allocation Sequences](#unique_23) [page ] 31 | Order Fulfillment Manager | Manage Product Allocation Sequences (F2474) |  |
| [Assign Product to Product Allocation](#unique_24) [page ] 33 | Order Fulfillment Manager | Assign Product to Product Allocation (F2120) |  |
| [Check Availability with Product Allocation (PAL)](#unique_25) [page ] 34 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| Alternative-Based Confirmation (ABC) |  |  |  |
| [Configure Substitution Strategy](#unique_26) [page ] 37 | Order Fulfillment Manager | Configure Substitution Strategy (F2699) |  |
| [Manage Characteristic Combinations](#unique_27) [page ] 39 | Order Fulfillment Manager | Manage Characteristic Combinations (F5303) |  |
| [Configure Alternative Control](#unique_28) [page ] 40 | Order Fulfillment Manager | Configure Alternative Control (F2698) |  |
| [Check Availability with Alternative-Based Confirmation (ABC)](#unique_29) [page ] 41 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| Supply Protection (SUP) |  |  |  |
| [Create Master Data for Supply Protection (SUP)](#unique_30) [page ] 45 | Order Fulfillment Manager | Manage Supply Protection (F4569) |  |
| [Check Availability with Supply Protection (SUP)](#unique_31) [page ] 46 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| Business Process Scheduling (BPS) |  |  |  |
| [Manage Characteristic Combinations](#unique_32) [page ] 48 | Configuration Expert - Business Process Configuration | Manage Characteristic Combinations (F5303) |  |
| [Configure Activity Attributes](#unique_33) [page ] 49 | Configuration Expert - Business Process Configuration | Configure Activity Attributes (F6439) |  |
| [Scheduling with Days Granularity](#unique_34) [page ] 51 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Release for Delivery

#### Preparation Activities for Release for Delivery

##### Configure Order Fulfillment Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to configure order fulfillment responsibilities to enable your order fulfillment specialists to process all the materials for which they are responsible in the Release for Delivery app. This enables you to scope and personalize the work of your order fulfillment specialists and ensures that they only see sales documents and materials for which they are responsible within a specific time period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Order Fulfillment Responsibilities (F2246). | The List Report screen displays. |  |
| 3 | Check Existing Responsibilities | On the List Report screen, in Editing Status field, choose All, and then choose Go. | A list of existing responsibilities displays. |  |
| 4 | Create Responsibilities for Each Plant | Choose Mass Create. In the Create Multiple Order Fulfillment Responsibilities dialog screen, enter the following values and choose Create Responsibilities:Split Criterion: PlantDefault Horizon: 3 | A responsibility has been created for each plant. |  |
| 5 | Create A Single Responsibility | Choose Create (Create Object). On the General Information tab, enter the following values:Responsibility Name: for example, TEST_1JWResponsibility Description: for example, Test Responsibility 1JWDefault Horizon: 3On the Legacy Responsibility Definition tab, enter following selection condition:Selection Attribute: Product NumberOperator: isValue: TG11 | A single responsibility has been created for the material. |  |
| 6 | Add User Assignment | Choose Create. On the General Information screen that appears, enter the following values (leaving other fields with their default values) and choose Add:Assigned User: <Tester ID of Order Fulfillment Specialist in the system>Choose Apply. |  |  |
| 7 | Save Responsibility | Choose Create. | The responsibility you just created displays with the entries you chose.To make more changes, select Edit. |  |

#### Release for Delivery

Purpose

The Release for Delivery app is used to prioritize due sales orders containing materials with limited availability. The app allows you to view the material availability situation of materials for which they are responsible as well as assess the potential financial impact of being unable to fulfill sales orders. This, in combination with other factors, helps you decide how to distribute material quantities between sales orders, before releasing the sales orders for subsequent logistics processes (for example, picking or packing). This manual processing step prevents expensive cancellation and rollback activities that may occur if last minute, high priority sales orders come in, causing conflicts for materials for which quantities are limited.

##### Prepare/Release Sales Orders for Materials Without Availability Issues for Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to prepare sales order line items for delivery. The line items for the material-plant combinations do not have availability issues, meaning all requirements can be fulfilled and can be released directly without additional processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Release for Delivery (F1786). | The Release for Delivery screen displays. |  |
| 3 | Check Prepared Materials | The process status is displayed on the entry screen of the Release for Delivery app.You see three process statuses: Unprepared, Prepared, Released. Navigate to the list of prepared materials. | Several materials have Prepared status.All materials in the list should be fully confirmed. |  |
| 4 | Release Prepared Materials | All material-plant combinations for which you are responsible for as well as those for which have no availability issues should be displayed in the Prepared material list.Mark all the combinations and press the Release for Delivery button. | The released materials vanish from the Prepared list.The corresponding counter displays 0.Note To select all materials simultaneously, use the checkbox in the header line of the table. |  |
| 5 | Check Released Materials | Navigate to the list of Released materials. | The released materials appear in the Released list. |  |
| 6 | Navigate Back | Navigate back to the list of Unprepared materials. | The overview screen lists all unprepared items which still have availability issues.Note This step is preparation for the next process step. |  |

##### Identify Most Important Sales Orders for Materials with Availability Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to identify material-plant combinations with availability issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Release for Delivery (F1786). | The Release for Delivery screen displays. |  |
| 3 | Check Unprepared Materials | The process status is displayed on the entry screen of the Release for Delivery (F1786) app.You see three process statuses: Unprepared, Prepared, Released.Navigate to the list of unprepared items. | Several materials have the status Unprepared.All unprepared materials in the list contain at least one sales order requirement with availability issues. Thus, they are not fully confirmed. |  |
| 4 | Navigate to Detail Screen | All material-plant combinations in the list of Unprepared materials have an Impact bar.The Unprepared material list is sorted according to the Impact bar.Navigate to the first material-plant combination as it has the greatest impact. | All sales order items for this material-plant combination display.Note The impact is, by default, based on the relative net value of the material, multiplied by the unconfirmed quantity. |  |
| 5 | Filter Sales Order Items | The header of the sales order item table has both search and sort functions. Use the functions to identify the sales orders with, for example, the highest Delivery Priority. | A list of sales order line items displays, filtered by the selected search criteria. The sorting changes the sequence of the sales order line items according to the chosen sort attribute.Note Undo the filtering by deleting the search criteria. |  |

##### Solve Issues by Redistributing Quantities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to redistribute confirmed quantities according to, for example, delivery priority, order type, or sold-to party. This procedure builds on the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Release for Delivery (F1786). | The Release for Delivery screen displays. |  |
| 3 | Unconfirm A Single Sales Order Line Item | Each row of the sales order line item table contains multiple buttons. You can unconfirm a single sales order line item by choosing Unconfirm in the appropriate line. Choose Unconfirm for a line item with a low Delivery Priority. | The confirmed quantity changes to 0. The bar chart in the page header displays the same quantity as the Available Quantity. |  |
| 4 | Unconfirm Multiple Sales Order Line Items | Choose Unconfirm in the table header line. | The confirmed quantity is 0 for all sales order line items. |  |
| 5 | Fully Confirm a Single Sales Order Item | Confirm a single sales order line item by choosing Confirm in the appropriate line. Choose Confirm for a line item with a high Delivery Priority. | If there is sufficient Available Quantity, the line item shows a full confirmation.Note The Confirm button is inactive if there is insufficient quantity to fully confirm a line item. |  |
| 6 | Confirm A Constrained Single Sales Order Item | The maximum possible confirmation of sales order line items can be constrained by the availability at storage location or batch. The constraining elements are displayed in the Dependencies column. Identify a sales order line item with constraints and increase/decrease the confirmation. | The confirmation of sales order line item is changed and the color of the constraining elements in the Dependencies column changes accordingly:Gray indicates that the item can be confirmed fully.Blue indicates that, although additional quantity is available and can be distributed, the item cannot be confirmed fully.Yellow indicates that the maximum quantity for the constraining element has been distributed.Red indicates that more quantity has been used than is available.Note The Confirm button is inactive if there is insufficient quantity to fully confirm a line item. The Publish and Back button is inactive when there is more quantity used for a constraining element than available. |  |
| 7 | Protect a Single Sales Order Line Item | Protect a single sales order line item from mass changes by pressing the Protect button in the appropriate line. Press the Protect button for a line item with the highest Delivery Priority. | The Protect button is active.Note Leave the protected line item in this status for the next step. |  |
| 8 | Fully Confirm Multiple Sales Order Items | Filter the sales order line item table to display all items with the highest Delivery Priority. Press the Confirm button in the table header line. | The confirmed quantity is set, starting at the top to bottom of the list. If the Available Quantity is insufficient to fully confirm all filtered line items, the line items near the end of the list will not have full confirmations.Note The protected line item does not change. |  |
| 9 | Repeat | Repeat the previous steps until you are satisfied with the confirmation situation. |  |  |
| 10 | Publish Changes | If you are satisfied with the current confirmation situation of all sales order line items for the current material-plant combination, you can update the underlying sales order documents and proceed with the next material-plant combination. To do this, choose Publish and Back. | The sales order line item list displays the next material-plant combination from the Unprepared list.Repeat this test step.Note When the last material-plant-combination is reached, press Publish and Back. |  |

##### Release Processed Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to trigger the creation of delivery documents. This is the final procedure step in the Release for Delivery (F1786) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Assess the App | Open Release for Delivery (F1786). | The Release for Delivery screen displays. |  |
| 3 | Check Prepared Materials | The processing status is displayed on the entry screen of the Release for Delivery (F1786) app. There are three statuses: Unprepared, Prepared, Released. | The Prepared list displays published materials. |  |
| 4 | Release Prepared Materials | Navigate to the Prepared material list. Choose all materials and choose Release for Delivery. | The released materials vanish from the Prepared list. The corresponding counter displays 0.Note To select all items simultaneously, use the checkbox in the header line of the table. |  |
| 5 | Check Released Materials | Navigate to the list of Released materials. | The Released list displays released materials. |  |

### Product Allocation (PAL)

#### Preparation Activities for Product Allocation (PAL)

##### Configure Product Allocation

Purpose

In this optional procedure, you define a schema for a product allocation object. The schema of a product allocation object comprises, among others, the ID, and description of the product allocation object, its periodicity, characteristics structure and their hierarchy, the unit of measure for the planned allocation quantity, and the date/time type (material availability date, good issue date, or requested delivery date) used for the check against product allocation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Product Allocation (F2119). | The list report for product allocation objects in the Configure Product Allocation app displays. |  |
| 3 | Create a New Product Allocation Object | Choose Create. | The object page displays and contains some default values. |  |
| 4 | Enter Product Allocation Object Data | On the New Object screen, make the following entries (leave other fields with their default values):Allocation Object: Product allocation object nameDescription: Product allocation object descriptionQuantity Unit: for example, PCPeriod Type: Week |  |  |
| 5 | Add Characteristics | Choose Add above the Characteristics table. Select the characteristics you would like to use and select OK. For example:Sales Document > Sales Organization > Sales OrganizationSales Document > Distribution ChannelSales Document > Sales Document Item > Business partners > Ship-To Party > Customer NumberSales Document > Sales Document Item > Material Number | The selected characteristics appear in the Characteristics table. |  |
| 6 | Place Characteristics into a Hierarchical Order that Suits the Business Requirement | Use the Move Up and Move Down buttons to place the characteristics you chose into the required order. For example:Material NumberSales OrganizationDistribution ChannelShip-To Party – Customer Number | The selected characteristics are in the required order. |  |
| 7 | Save Product Allocation Object | Choose Create. | The product allocation object you just created is now in display mode and contains the characteristics you chose. To make more changes, select Edit. |  |

Monitor Allocation Object Changes

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Product Allocation (F2119). | The list report for product allocation objects in the Configure Product Allocation app displays. |  |
| 3 | Access the List of Allocation Objects | Choose Display Change Logs on the top right corner. | The Display Change Logs for Allocation Objects app displays. |  |
| 4 | Access the Change Logs | Choose the specific allocation object, on the detailed screen, you can access the change logs for this allocation object:In the Changes of Product Allocation Objects subscreen, you can see the changes made in the fields of the allocation object.In the Characteristic Value Combination Changes subscreen, you can see changes made to CVC of the allocation object.In the Changes of Periods subscreen, you can see changes made to the periods of a characteristic value combination. | The change logs details display. |  |

##### Manage Product Allocation Planning Data

Purpose

In this optional procedure, you can maintain characteristic value combinations and planned allocation quantities for the time periods of the characteristic value combinations. Characteristic value combinations and the corresponding time series can be maintained by uploading CSV files. The Manage Product Allocation Planning Data app also enables you to change the activation status and the constraint status of the characteristic value combinations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Product Allocation Planning Data (F2121). | The list report for product allocation objects in the Manage Product Allocation Planning Data app displays. |  |
| 3 | Search Product Allocation Object | Enter the name of the product allocation object you created in the previous step in the Allocation Object search field and select Go. | The product allocation object appears in the table of the list report. |  |
| 4 | Select Product Allocation Object | Select the entry of the product allocation object created in the previous step. | The Product Allocation Object object page appears in display mode. The Product Allocation Planning Data table is empty. |  |
| 5 | Edit Product Allocation Object Planning Data | Choose Edit. | The Add, Change StatusChange Constraint Status, DeleteDownload and Upload buttons appear above the Product Allocation Planning Data table. |  |
| 6 | Maintain Characteristic Values and Allocation Quantities | Characteristic values can be maintained manually by choosing Add or by first downloading the product allocation planning data schema, and maintaining the planning data in the spreadsheets (in .xlsx format) or comma separated values files (in .csv format) and uploading the files again.Ensure that you maintain at least one characteristic value combination for the characteristics you have chosen. For example,Material Number: TG11Sales Organization: 3310Distribution Channel: 10Ship-To Party - Customer Number: 33100003Enter allocation quantity for each period: 100Note Ensure that the allocation quantity you maintain per period is not too large. Otherwise, the restricting effect of product allocation on the overall ATP result is not visible. |  |  |
| 7 | Save Product Allocation Object | Choose Save. | The planning data you just created appears in display mode. To make more changes, select Edit. |  |
| 8 | Display Product Allocation Consumption Situation | Select one of the product allocation data records you created and choose Show Consumption. | A bar chart appears: the displayed periods show Planned and Available Quantity entries which are equal to the quantities you maintained previously. There are no quantity entries for Consumed Quantity. |  |

Remark

After you have performed process steps Manage Product Allocation Sequences and Assign Product to Product Allocation, as well as executed an availability check against product allocation for, for example, a sales order as described in the Sell from Stock (BD9) process, you can return to the Manage Product Allocation Planning Data app for the product allocation object you created in the previous step and choose Show Consumption again (as described previously).

The Consumption bar chart now displays the Consumed Quantity for the periods which were consumed during the availability check against product allocation because:

- The sales order was created for the characteristics chosen in step 6.
- The sales order item was created for the material and plant you assigned as Material and Plant in process step Assign Product to Product Allocation to the product allocation object from the previous step.
- The requested delivery date or material availability date for the sales order items falls within the Validity Start and Validity End you maintained in process step Assign Product to Product Allocation.

If you just created a product allocation for the standard customer and standard material used in many processes, and most likely used up all allocated quantities, you can change the product allocation planning data to Inactive status in the Manage Product Allocation Planning Data (F2121) app.

Monitor Allocation Object Changes

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Product Allocation Planning Data (F2121). | The list report for product allocation objects in the Manage Product Allocation Planning Data app displays. |  |
| 3 | Access the List of Allocation Objects | Choose a specific planning data, on the detailed screen, choose Display Change Logs on the top right corner. | The Display Change Logs for Allocation Objects app displays. |  |
| 4 | Access the Change Logs | You can access the change logs for this allocation object:In the Changes of Product Allocation Objects subscreen, you can see the changes made in the fields of the allocation object.In the Characteristic Value Combination Changes subscreen, you can see changes made to CVC of the allocation object.In the Changes of Periods subscreen, you can see changes made to the periods of a characteristic value combination. | The change logs details display. |  |

##### Manage Product Allocation Sequences

Purpose

In this optional procedure, you can define product allocation sequences for organizing the consumption strategy of product allocations. The product allocation sequence comprises, among others, the ID and description of the product allocation sequence, the settings for backward and forward consumption, sequence groups which allow you to efficiently combine product allocation objects as constraints or alternative allocations. For each single constraint validities and a consumption strategy can be defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Product Allocation Sequences (F2474). | The list report for product allocation sequences in the Manage Product Allocation Sequences app displays. |  |
| 3 | Create a New Product Allocation Sequence | Choose Create. | The object page displays an entry for a sales sequence group as a default. |  |
| 4 | Maintain Header Data for a Product Allocation Sequence | On the New Object screen, make the following entries:Allocation Sequence: <Product allocation sequence name>Description: <Product allocation sequence description>Backward Consumption and Forward Consumption: at least 1 for both fields: otherwise only the allocation quantity of the period within which the requested delivery date falls is considered for the availability check again product allocation.Consumption Unit: the base unit of measure of the material you chose or any other unit of measure that is convertible into the base unit of measure of that material. |  |  |
| 5 | Select Product Allocation Sequence Group | Press the entry for Sequence Group <10> in the Sales Sequence Groups section. | The details of the sales sequence group are displayed, an entry for a constraint is defaulted. |  |
| 6 | Maintain Product Allocation Sequence Group | On the General Information for Group screen, make the following entryDescription: <Product allocation sequence group description> |  |  |
| 7 | Select Product Allocation Sequence Group Constraint | Press the entry in the Constraints table. | The details of the sales sequence group constraint are displayed. Some fields from the product allocation sequence group are displayed. |  |
| 8 | Maintain Product Allocation Sequence Group Constraint | On the General Information for Constraint screen, make the following entries:Description: <Product allocation sequence group constraint description>Allocation Object: Select the allocation object you created in step Configure Product Allocation from the dropdown list. | The value for Check Data Time Type is taken over from the allocation object.Values for Past Period Allowed, Consumption Direction and the Validities are defaulted and can be kept. |  |
| 9 | Save Product Allocation Sequence | Choose Apply for the product allocation sequence group constraint.Choose Create for the product allocation sequence. | The product allocation sequence data you just created appears in display mode. To make further changes, choose Edit. |  |

Monitor Allocation Object Changes

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Product Allocation Sequences (F2474). | The list report for product allocation objects in the Manage Product Allocation Sequences app displays. |  |
| 3 | Access the List of Allocation Objects | Choose Display Change Logs on the top right corner. | The Display Change Logs for Allocation Objects app displays. |  |
| 4 | Access the Change Logs | Choose the specific allocation sequence, on the detailed screen, you can access the change logs for this product allocation sequence:The Changes of Product Allocation SequencesThe Changes of AssignmentsThe Changes of Sequence GroupsThe Changes of Constraints | The change logs details display. |  |

##### Assign Product to Product Allocation

Purpose

In this optional procedure, you can assign materials and material-plant combinations to the product allocation sequence you created in process step Manage Product Allocation Sequences. The assignment activates availability checks against product allocation for order requirements for the assigned materials and material-plant combinations. The assignment of materials and material-plant combinations is time-dependent and enables you, for example, to react easily to temporary or seasonal fluctuations of supply and demand.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Assign Product to Product Allocation (F2120). | The list report for product allocation objects in the Assign Product to Product Allocation app displays. |  |
| 3 | Search for a Product Allocation Sequence | Enter the name of the product allocation sequence you created in process step Manage Product Allocation Sequences in the Allocation Sequence search field and select Go. | The product allocation sequences appear in the table of the list report. |  |
| 4 | Select a Product Allocation Object | Select the entry for the product allocation sequence you created in process step Manage Product Allocation Sequence. | The Product Allocation Sequence object page appears in display mode. The Material-Plant Assignments table is empty. |  |
| 5 | Edit Material-Plant Assignment Data for a Product Allocation Sequence | Choose Edit. | The Add and Delete buttons appear above the Material-Plant Assignments table. |  |
| 6 | Maintain Material-Plant Assignments for the Product Allocation Sequence | Choose Add and create an assignment by maintaining the following entries:Material: <TG11> or a material you chose for the sales orderPlant: <3310> or a plant you chose for the sales orderValidity Start and Validity End: Values that ensure the item requested delivery date or material availability date of a sales order falls within the validity period | The date category (item requested delivery date or material availability date) depends on the setting in self-service configuration to activate product allocation. |  |
| 7 | Save the Material-Plant Assignment for the Product Allocation Sequence | Choose Save. | The material-plant assignment you just created is now in display mode. To make more changes, select Edit. |  |

Product Allocation Overview (F3474) app offers insights on how product allocation is used such as which and how order items are affected by product allocation.

#### Check Availability with Product Allocation (PAL)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for which product allocation is used to check availability.

This is a generic process step. In all scope items where a sales order is created with certain conditions and product allocation is active, the behavior is the same as below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Maintain Order Data | On the Create Sales Documents screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries and choose Save:Sold-to Party: 33100003Ship-to Party: 33100003Cust.Reference: <Test>Order Reason: <Excellent Price>Material: TG11Order Quantity: <200>First Date: <Date at least two weeks into the future>Enter the order quantity which is greater than that entered for the characteristic value combination defined in Manage Product Allocation Planning Data (F2121) app (step 4.2.1.2 [Manage Product Allocation Planning Data](#unique_22) [page ] 29).The first date should be in the future, to ensure that it lies within the defined validity of the sequence assignment in Assign Product to Product Allocation (F2120) app (step 4.2.1.4 [Assign Product to Product Allocation](#unique_24) [page ] 33). |  |  |
| 6 | Check with Product Allocation | On the Review Availability Check Result screen, only restricted quantity can be confirmed for the item.Choose the requirement item and choose Intermediate Results tab, hover over and choose the Sales Product Allocation Check or the Capacity Product Allocation icon. In the dialog box, choose Show Details, you can display the confirmations and consumptions details as requested.Go back to the Review Availability Check Result screen, you can choose Apply to directly confirm the delivery proposal. | This screen displays a header and a table with the confirmation and consumption result per product allocation sequence constraint and request. |  |
| 7 | Save Document | Choose Save. | The order is saved and the order confirmation is printed out. |  |

### Alternative-Based Confirmation (ABC)

#### Preparation Activities for Alternative-Based Confirmation (ABC)

##### Configure Alternative Determination (Optional)

Purpose

This process step shows you how to decide which substitutes are to be used to confirm requests in the Configure Alternative Determination (F5354) app. Then you can execute them in the Configure Substitution Strategy (F2699) app where the Alternative Determination field states how available alternatives are to be prioritized.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Alternative Determination (F5354). | The Configure Alternative De-termination screen displays. |  |
| 3 | Create a New Determination | Choose Create from Template, select from the following pre-configured determinations and choose Continue:Alternative Determination: <Full Confirmation>, or <Maximum Confirmation Earlier>, or <On-Time Confirmation>On the New Determination screen, make the following entries and choose Save:Determination Name: <your determination name>Determination Description: <your determination description>You can define custom determinations on the basis of rating attributes and hard constraints from the dropdown list.You can also create custom determination via Create with Attribute and Constraint or Create with Business Add-in buttons. | The determination is saved. |  |

##### Configure Sourcing Profile (Optional)

Purpose

This process step shows you how to define sourcing profiles in third-party order processing with aATP. You can create and assign a sourcing profile to a substitution strategy which ABC uses for finding substitutes in sales order items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Sourcing Profile (F7754). | The Configure Sourcing Profile screen displays. |  |
| 3 | Configure Sourcing Profile | On the Configure Sourcing Profile screen, choose Create. Enter the following entries and choose Create:Sourcing Profile: <Enter Profile Name>Description: <Enter Profile Description>Third-Party Shipment Type: <Third-Party Direct Shipment>Two Third-Party Shipment Type can be selected:Third-Party Direct Shipment: third-party supplier ships to customer directlyBought-In Item: third-party supplier ships to a plant or subsidiaryInfo Records: <Yes> | The Sourcing Profile is created. |  |
| 4 | Assign Sourcing Profile | Go through with next process step to assign the sourcing profile to a substitution strategy. |  |  |

##### Configure Substitution Strategy

Purpose

This process step shows you how to configure a substitution strategy in which you define a substitution and how alternatives are determined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Substitution Strategy (F2699). | The Configure Substitution Strategy screen displays. |  |
| 3 | Create a New Strategy | To create a new strategy, choose Create and make the following entries:Strategy Name: <your strategy name>Strategy Description: <your strategy description>Substitution Item Type: (Recommended value) Allow both Inline Substitution and Subitem GenerationThree item types can be selected:Force Inline Substitution: The sales order contains a single requirement item and the originally requested delivering plant is replaced by the alternative delivering plant.Force Subitem Generation: The requested data for the original requested item is always stored as a main item. Subitems are always generated for the confirmed data. If requirements are substituted, several subitems may be created for one main item. For each confirmation of a plant, product, and storage location, at least one corresponding subitem is generated. A subitem is also generated when the original request is confirmed fully without using substitutes. Use this type for third-party order processing check.Allow Inline Substitution and Subitem Generation: The system chooses the optimal solution based on stock availability in the potentially relevant delivering plants: if a single delivering plant can confirm the requested product, inline substitution is possible and is used; Otherwise, subitems are generated, which states the new plant or storage location and the product or substitute product used to confirm the requirement, as well as the confirmed delivery date and quantity.Consider Alternatives: AlwaysSubstitution Method: <Plant Substitution> or <Product Substitution> You can also add another method.Note To define master data for product substitution, you can refer to master data script 4VO - Create Product Substitution - MDS.Choose item Plant Substitution and go to detail screen for substitution method. Choose Substitution Method Source from dropdown list:Substitution Method Source: <All Possible Plants> System considers all plants where the material of the sales order requirement is defined, as possible alternatives. Or <Substitution Master Data> The substitution master data defines a directed graph of substituted plants. Alternative plants are determined by traversing through that graph and applying filter conditions, like the used sales organization and distribution channel. You can define the list of alternative plants, the sequence/priority, and time dependency.Note To define master data for location substitution, you can refer to master data script 5NG-Create Location Substitution and Exclusion - MDS.Choose Apply to return to Strategy screen.Alternative Determination: <MAX_EARLIER_CONFIRMATION> Maximum Confirmation Earlier. And you can add multiple methods, for example <FULL_CONFIRMATION> Full Confirmation, or <ON_TIME_CONFIRMATION> On-Time Confirmation, or the determination you created in last process step. | The Strategy Definition screen displays. |  |
| 4 | Save Your Strategy | Choose Create. | The strategy is saved. |  |

##### Manage Characteristic Combinations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Characteristic Combination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Characteristic Combinations (F5303). | The Manage Characteristic Combination screen is displayed. |  |
| 3 | Choose Create | In the Manage Characteristic Combination view, choose Create. | The Manage Characteristic Combination create Screen is displayed. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Combination: <Enter the Combination Name>Combination Description : <Enter the Description of the Combination>Usage: <Alternative-Based Confirmation>Catalog Type: <Base (Sales Order)>Combination, Usage and Catalog Type are mandatory to create a substitution. |  |  |
| 5 | Assign Characteristics | In the Characteristics section, the Characteristic can be assigned by clicking on Assign:On the Add Characteristics dialog box that displays, choose Expand All, select Sales Organization and Customer Number (under Business Partners > Sold-to Party > Customer Number ) and Material Number.Choose Assign.The Navigation Up arrow and Down arrow button can be used to set the order of the Characteristics. |  |  |
| 6 | Save Your Data | Choose Create. | System message shows that Combination is Created. |  |

##### Configure Alternative Control

Purpose

This process step shows you how to create an alternative control in which you can activate substitution strategy for a specific sales organization and customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Alternative Control (F2698). | The Configure Alternative Control screen displays. |  |
| 3 | Create Access | Choose Create.Combination: choose the Combination displayed in the F4 help for combination (Combination created in the previous step can be used).Status: ActiveChoose Create on the pop up. | The user is navigated to the details screen of the Access. |  |
| 4 | Add Characteristic Value Combinations | Choose Add, a new row is added and defaulted with *.Change the characteristic values with the following entries:Sales Organization: 3310Customer Number: 33100004Material Number: TG11Substitution Strategy: <Your Previously Created Strategy> Enter a strategy in the Strategy field using F4 (Strategy created in the previous step can be used)Execute ABC: Yes | The Alternative Control / Access is Saved. | Note The Characteristics displayed depends on the Combination selected during Access creation. |
| 5 | Create the Access | Choose Create. | The Access is created. |  |

#### Check Availability with Alternative-Based Confirmation (ABC)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for which Alternative-Based Confirmation (ABC) is used to check availability. This is a generic process step. In all scope items where a sales order is created with certain conditions and advanced ATP is active, the behavior is the same as the above.

In this test script, sales organization 3310 and customer 33100004 have been defined as conditions in the Configure Alternative Control (F2698) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order - VA01 . | The Create Sales Documents screen displays. |  |
| 4 | Maintain Order Data | On the Create Sales Documents screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries and choose Save:Sold-to Party: 33100004Ship-to Party: 33100004Cust. Reference: <Test>Order Reason: <Excellent Price>Material: TG11Order Quantity: <Quantity>Note Enter the order quantity which is greater than stock in plant 3310, less than or equal to stock in plant 3320.To get the stock information, you need log on to the SAP Fiori launchpad as a Warehouse Clerk and open the Display Stock Overview (MMBE) app. | An ATP check is carried out and will include ABC.In general, ABC is executed based on the originally requested material/plant combination. Based on the substitution strategy, the plant is substituted to 3320. |  |
| 6 | Choose Delivery Proposal | On the Review Availability Check Result screen, it displays the detailed results for requirements for which the delivering plant, storage location, or product has been substituted. Choose Apply to accept the result.You can choose the item to graphically display how the confirmation has been calculated on the Intermediate Results subscreen.On the Review Availability Check Result screen, you can also display alternative confirmation proposal defined in the corresponding substitution strategy. Choose to accept one of the proposals and apply to transfer your decision to the sales document. | In general, ABC is executed based on the originally requested material/plant combination. |  |
| 7 | Plant Substitution | If plant substitution is configured in substitution strategy in the prerequisite step, plant substitution is executed. And based on the substitution item type in substitution strategy, there could be different behavior in sales order.Substitution item type: Force Inline Substitution (I)Plant has been changed to 3320 within item line 10 .Substitution item type: Force Subitem Generation (S)Item category is changed to TAPA for main item 10.A new line item with item category TAN is created, and plant is substituted to 3320.Note More substitution items could be created according to required quantity and stock situation in alternative plants.Substitution item type: Allow both Inline Substitution and Subitem Generation (B)Depends on the stock situation:If single alternative plant stock meets sales order required quantity, inline substitution executes.If required quantity exceeds stock in single alternative plant, multiple subitems are generated for multiple alternative plants. | The order is saved and the order confirmation is printed out. |  |
| 8 | Product Substitution | If product substitution is configured, product substitution is executed according to the substitution master data you maintained in Create Product Substitution - MDS (4VO) Master Data Script.If both plant and product substitution methods are configured, substitution is executed according to the maintained method sequence. |  |  |
| 9 | Save Document | Choose Save.Make a note of the sales order number: __________. | The order is saved and the order confirmation is printed out. |  |

#### Check Availability with Third-Party (Optional)

Purpose

This process step shows you how to create a sales order for which third-party subitems are automatically created as substitutions during availability check. You should go through prerequisite step Create Purchasing Info Record in BD3 - Sales Processing using Third-Party with Shipping Notification / BDN - Sales of Non-Stock Item with Order-Specific Procurement with Material TG11 and step 4.3.1.5 [Configure Sourcing Profile (Optional)](#unique_37) [page ] 37 in this test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order - VA01 . | The Create Sales Documents screen displays. |  |
| 4 | Maintain Order Data | On the Create Sales Documents screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries and press Enter:Sold-to Party: 33100004Ship-to Party: 33100004Cust. Reference: <Test>Order Reason: <Excellent Price>Material: TG11Order Quantity: <Quantity> | The aATP check initiates the automatic creation of third-party subitems, with item category CB1 for third-party direct shipment or CBAB for bought-in item. |  |
| 6 | Check Third-Party Order Processing with aATP | Select the created subitem with item category CB1 or CBAB, choose Schedule Lines for Item, and choose Purchase Requisition. Check that on the Create Purchase Requisition screen data is automatically filled based on the info records.Substitutions can be varied based on the previous strategy configuration:If material and plant combinations are relevant, the substitution is straight forward;If substitution method <Plant Substitution> is combined with the source <All Possible Plants>, the substitution plant is with multiple valid sources of supply;If substitution method <Plant Substitution> is combined with the source <All Possible Plants>, substitution methods <Product Substitution> and <Storage Location Substitution> are combined with the source <Substitution Master Data>, the set of substitution plant and product is with multiple valid sources of supply. |  |  |
| 7 | Save Document | Choose Save.Make a note of the sales order number: __________.For CB1 order, follow the process step Convert Assigned Requisitions into Purchase Orders and the subsequent steps of BD3 - Sales Processing using Third-Party with Shipping Notification if necessary.For CBAB order, follow the process step Create Purchase Order and the subsequent steps of BDN - Sales of Non-Stock Item with Order-Specific Procurement if necessary. | The order is saved. |  |

### Supply Protection (SUP)

#### Preparation Activities for Supply Protection (SUP)

##### Create Master Data for Supply Protection (SUP)

Purpose

This process step shows you how to create master data for supply protection in which you can protect quantities of a material of a specific plant for other demands.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Supply Protection (F4569). | The Manage Supply Protection screen displays. |  |
| 3 | Define General Information | On the Manage Supply Protection screen, choose Create for a new supply protection object.On the General Information tab, enter the following:Name: <Protection Object for TG11>Material: TG11Plant: 3310Select the checkbox of Sales Document and Stock Transport Order for Planning Context. |  |  |
| 4 | Define Core Protection | On the Planning Horizon tab, enter the following:Planning Period Type: WeeklyPlanning Start Date: <Current date>Planning End Date: <Current date + 2 months>On the Core Protection tab, in the Core Characteristic area, enter the following:Characteristic 1: Distribution ChannelValue 1: 10 | The supply protection object is created. Other entries are available for further definition. |  |
| 5 | Specify Prioritized Protection | On the Prioritized Characteristics tab, choose Create.Enter Customer Group in the Characteristic field. | The protection group is saved. |  |
| 6 | Define Protection Group | On the Protection Groups tab, choose Create. A new row is displayed:Enter Priority: 1Maintain the characteristic Customer Group: 01Enter specific quantity for time buckets, for example, 100. | The protection group with time buckets is saved. |  |
| 7 | Define 2nd Protection Group | On the Protection Groups tab, choose Create. A new row is displayed:Enter Priority: 2Maintain the characteristic Customer Group: 02Enter specific quantity for time buckets, for example, 100, then choose Create. | The protection group with time buckets is saved.If the protection is executed in sales order, you can see the quantity consumed. Also relevant document details can display via choosing Protection Groups Details. |  |
| 8 | Activate Supply Protection | On the Supply Protection screen, choose Activate. | The supply protection object is activated now. |  |

#### Check Availability with Supply Protection (SUP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for which Supply Protection (SUP) is used to protect the demand of customers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order - VA01 . | The Create Sales Documents screen displays. |  |
| 4 | Maintain Order Data | On the Create Sales Documents screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Sales Orders: Overview screen, make the following entries and choose Save:Sold-to Party: 33100004Ship-to Party: 33100004Cust.Reference: <Test>Order Reason: <Excellent Price>Material: TG11Order Quantity: <quantity>, for example, <200>Enter the order quantity which is greater than that defined in protection group in prerequisite step. | An ATP check including supply protection is carried out.Only stock which is not restricted can be confirmed. |  |
| 6 | Save Document | Choose Save.Make a note of the sales order number: __________. | The order is saved and the order confirmation is printed out. |  |

### Business Process Scheduling (BPS)

Purpose

You can use BPS to schedule several business processes according to your own rules. BPS allows an increased scheduling precision through flexible configuration options. With the Configure Activity Attributes (F6439) app, you can granularly maintain durations and working times for logistical activities for certain characteristic combinations. This is an addition to Basic Business Process Scheduling (6JM).

#### Preparation Activities for Business Process Scheduling (BPS)

##### Manage Characteristic Combinations

Purpose

This process step shows you how to create a Characteristic Combination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager - Scheduling. | The SAP Fiori launchpad appears. |  |
| 2 | Access the App | Open Manage Characteristic Combinations (F5303).Note: In case the app is not available per default, add it using the App Finder. | The Manage Characteristic Combination screen is displayed. |  |
| 3 | Choose Create | In the Manage Characteristic Combination view, choose Create. | The Manage Characteristic Combination Create Screen is displayed. |  |
| 4 | Create Combination of Durations Usage | In the Header section, make the following entries:Combination: <Enter the Combination Name>Combination Description : <Enter the Description of the Combination>Usage: <Durations for Scheduling>Catalog Type: <Base (Sales Document)>Combination, Usage and Catalog Type are mandatory to create a combination. |  |  |
| 5 | Assign Characteristics | In the Characteristics section, the characteristic can be assigned by choosing Assign:On the Add Characteristics dialog box that displays, choose Expand All, select Sales Organization, Distribution Channel and Division.Choose Assign.The navigation Up arrow and Down arrow button can be used to set the order of the Characteristics. |  |  |
| 6 | Save Your Data | Choose Create. | System message shows that Combination is Created. |  |
| 7 | Create Combination of Working Times Usage | Repeat steps 4-6. In the Header section, make the following entries:Combination: <Enter the Combination Name>Combination Description : <Enter the Description of the Combination>Usage: <Working Times for Scheduling>Catalog Type: <Base (Sales Document)> | System message shows that Combination is Created. |  |

##### Configure Activity Attributes

Purpose

This process step shows you how to determine durations and working times for logistical activities when scheduling with Business Process Scheduling. Configure Activity Attributes (F6439) serves as a more granular possibility to determine durations and working times in addition to Basic Business Process Scheduling (6JM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager - Scheduling. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Activity Attributes (F6439).Note: In case the app is not available per default, add it using the App Finder.Make sure the Durations tab is selected as default. | The Configure Activity Attributes screen displays. |  |
| 3 | Create a New Access for Durations | To create a new access, choose as the following:Catalog Type: <Base (Sales Document)>Scheduling Activity: e.g. <Pick>Choose Go to load already defined accesses for this activity, then select Create.Select the combination you created in the previous chapter and set the status to Active.Note Make sure there are no active accesses defined with higher sequence for the same activity and characteristics. If so, set their status to Inactive. | A new access is created and Assigned Scheduling Durations screen displays. |  |
| 4 | Enter Values for Characteristic Combinations | Choose Add and enter values for the characteristic:Sales Organization: 3310Distribution Channel: 10Division: 00Duration in Days: 2Duration in Hours: 0 |  |  |
| 5 | Save | Choose Create. |  |  |
| 6 | Repeat Previous Steps | Repeat steps 3-5 for scheduling activities Load, Transportation Planning, Transport, Unload. |  |  |
| 7 | Switch to Working Times Tab | Choose Working Times tab. |  |  |
| 8 | Create a New Access for Working Times | To create a new access, choose as the following:Catalog Type: <Base (Sales Document)>Scheduling Activity: e.g. <Pick>Choose Go to load already defined accesses for this activity, then select Create.Select the combination you created in previous chapter and set the status to Active.Note Make sure there are no active accesses defined with higher sequence for the same activity and characteristics. If so, set their status to Inactive. | A new access is created and Assigned Scheduling Working Times screen displays. |  |
| 9 | Enter Values for Characteristics Combination | Choose Add and enter values for the characteristic:Sales Organization: 3310Distribution Channel: 10Division: 00Factory Calendar: AEWorking Times: empty |  |  |
| 10 | Save | Choose Create. |  |  |
| 11 | Repeat Previous Steps | Repeat steps 8-10 for scheduling activities Load, Transportation Planning, Transport, Unload. |  |  |

#### Scheduling with Days Granularity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule logistically relevant date types available at schedule line level in a sales order (for example, material availability date, delivery date) with the new scheduling solution Business Process Scheduling (BPS). As attribute determination for scheduling, values maintained in Configure Activity Attributes for durations and working times are used. Time granularity for scheduling is ‘Days’.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Documents screen displays. |  |
| 3 | Create a Sales Order | Enter the following values and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Create Order Data | On the Create Standard Order: Overview screen, make the following entries and choose Save:Sold-to Party: 33100003Ship-to Party: 33100003Cust.Reference: <Customer Reference>Material Number: TG11, Quantity: <50>Material Number: TG12, Quantity: <100>Note The system proposes the current date as the requested delivery date at header level (which is derived for all items automatically). |  |  |
| 5 | Maintain Order Shipping Data | On the overview screen, go to the tab Shipping for item 10 and 20 and enter Route TR0101.Press Enter. |  |  |
| 6 | Check Results | Select item 10 and choose the Schedules Lines for Item button.Select the confirmed schedule line and choose the tab Shipping. Repeat for item 20. | The scheduled date types (delivery date, goods issue date, etcetera) are displayed. |  |
| 7 | Verify Results (Optional) | To verify and understand the retrieved scheduling results, you can compare the durations and working times of activities maintained in Configure Activity Attributes (F6439). |  |  |
| 8 | Review Scheduling Result | You can also display useful background information about the scheduling process via Review Availability Check Result. Choose the Confirmed Del. Date with hyperlink, on the result screen, you can:Display Schema, Scheduling and Order details in the header section.See scheduling activities and their total and net durations.Check activity determined attributes with values and the source of the determinations.Display information about the scheduling process leading to the results. | The Review Scheduling Result details display. |  |
| 9 | Save Sales Order | Save the sales order. |  |  |

## Appendix

### Delete Availability Check Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule the deletion of logs created by Available-to-Promise.

Prerequisites

Before you can delete any logs containing ATP results, at least one log has to have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open ILM Data Destruction (F2662). | The ILM Data Destruction screen displays. |  |
| 3 | Choose Data Destruction Object | Choose the Data Destruction Objects tab. In the Not Scheduled section, find and select the checkbox for object ATP_CHECK_LOG_DESTRUCTION. | The Schedule is selectable. |  |
| 4 | Schedule Delete | Choose Schedule on the tool bar. Choose Delete in the Schedule Delete dialog box. | Destruction run is scheduled. |  |

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
- related-to :: [[08-sales-order-management/basic-available-to-promise-processing-2ln-ae-test-script-832]]
- related-to :: [[08-sales-order-management/test-script-advanced-available-to-promise-consumer-products-6n0-ae-117]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1JW_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 98,614 chars in the whole document
