---
id: 11-inventory-warehouse-and-transportation/test-script-stock-transfer-without-delivery-bmh-ae-sap-s-4hana-cloud-p
title: "Test Script: Stock Transfer Without Delivery (BMH_AE) - SAP S/4HANA Cloud Public Edition (BMH_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (BMH_AE, plants 3310/3320) for stock transfer without delivery via stock transport orders, with prerequisites and Fiori app steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/intracompany-stock-transfers]
aliases: [BMH_S4CLD2608_BPD_EN_AE]
keywords: [Stock Transfers Within a Company Code, stock transfer without delivery, stock transport order, test script prerequisites, mrp run, flexible workflow, stock transport order approval, overdue stock in transit, goods issue, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMH_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1288
topic: 11-inventory-warehouse-and-transportation/intracompany-stock-transfers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Stock Transfer Without Delivery (BMH_AE) - SAP S/4HANA Cloud Public Edition (BMH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Stock Transfers Within a Company Code** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Stock Transfer Without Delivery (BMH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862290)

[2 Prerequisites 4](#_Toc232862291)

[2.1 System Access 4](#_Toc232862292)

[2.2 Roles 4](#_Toc232862293)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862294)

[2.4 Additional Manual Configuration 6](#_Toc232862295)

[2.5 Business Conditions 7](#_Toc232862296)

[2.6 Preliminary Steps 7](#_Toc232862297)

[2.6.1 Optional: Create Planned Independent Requirements 7](#_Toc232862298)

[2.6.2 Create Stock in Supplying Plant 8](#_Toc232862299)

[2.6.3 Optional: Configure Flexible Workflow for Stock Transport Order 9](#_Toc232862300)

[2.6.3.1 Optional: Check Flexible Workflow for Stock Transport Order Approval 9](#_Toc232862301)

[2.6.3.2 Configure Flexible Workflow for Stock Transport Order 11](#_Toc232862302)

[2.6.4 Optional: Prerequisite for Overdue Stock in Transit 12](#_Toc232862303)

[2.6.4.1 Manage Teams and Responsibilities 12](#_Toc232862304)

[2.6.4.2 Manage Situation Types 14](#_Toc232862305)

[3 Overview Table 16](#_Toc232862306)

[4 Test Procedures 17](#_Toc232862307)

[4.1 MRP Run for Single Item 17](#_Toc232862308)

[4.2 Evaluate Stock/Requirements Situation 18](#_Toc232862309)

[4.3 Process Stock Transport Requisition (with MRP) 19](#_Toc232862310)

[4.4 Change Stock Transport Order (with MRP) 21](#_Toc232862311)

[4.5 Optional: Create Stock Transport Order (Without MRP) 22](#_Toc232862312)

[4.6 Optional: Create Stock Transport Order in App Transfer Stock-Cross Plant 23](#_Toc232862313)

[4.7 Optional: Approve Stock Transport Order 25](#_Toc232862314)

[4.7.1 Optional: Check Stock Transport Order Approval Details 26](#_Toc232862315)

[4.8 Post Goods Issue for Stock Transport Order 27](#_Toc232862316)

[4.9 Check Status of Stock Transfer 28](#_Toc232862317)

[4.9.1 Check Status of Stock Transfer with Stock- Single Material 28](#_Toc232862318)

[4.9.2 Check Status of Stock Transfer with Overdue Materials - Stock in Transit (Optional) 29](#_Toc232862319)

[4.10 Post Goods Receipt for Stock Transport Order 30](#_Toc232862320)

[5 Appendix 32](#_Toc232862321)

[5.1 Additional Features 32](#_Toc232862322)

## Purpose

Overview

The process begins with a requirement to transfer material from one plant to another within the same company code. The stock transfer without delivery can be performed in two different ways.

A one-step transfer posting at the issuing plant moves the stock immediately from the issuing plant to the receiving plant. This is useful if the distance between the two plants is short and there is no need for stock-in-transit stock overview.

A buyer at the receiving plant requests material with a stock transport order. This is useful if the issuing plant needs a formal request to send material to the receiving plant or the distance between the two plants is longer.

There are no master data requirements beyond the material master to support the stock transfer process. The material master must exist in both the procuring (receiving) plant and the providing (issuing) plant. Also, stock transfer purchase orders are not subject to approval like other purchase orders.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via FIORI Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Plant | 3320 | Plant 2 AE | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionNote The second set of organization entity IDs here is an example. In an evaluation project of the SAP Central Business Configuration environment, the ID follows the naming rule described in [Using the Set Up Organizational Structure App](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/d020ff461d504421bcc55d87cbc0ae57.html). |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 332A | Std. storage 1 | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionShop floor w/o lean WM |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 /002 | Group 001 /Group 002 | Depending on material |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections Business Conditions and Preliminary Steps. |

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/085031c9175a7a349ebb789f213c319a)

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Complete all relevant steps. |
| 31N - Situation Handling | Install this scope item for the situation handling steps. |

### Preliminary Steps

#### Optional: Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Planned independent requirements are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/ Fail/ Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Maintain PIRs screen, choose the user icon, and select App Settings.On MRP Settings screen, choose Area of Responsibility.Check only this entry is displayed there: Plant 1 AE/001 (MRP Controller 001) | If the entry Plant 1 AE/001 is not present on the Area of Responsibility screen does not exist, choose Add and then choose OK.For other plant entries on the Area of Responsibility screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Yes, No, N/ASearch: TG11 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Select Material Item | Choose the material item, and choose Edit PIRs in the upper right. | The Edit PIRs view displays. |  |
| 7 | Edit PIRs | Enter quantities per period, for example:PIR: 100 PC for next 12 periodsVersion is Active: YES |  |  |
| 8 | Save PIRs Draft | Choose Save (bottom right). | The PIRs Draft is saved. |  |

#### Create Stock in Supplying Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a real business case, the materials are usually purchased from external suppliers; in that case, that process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Material | Make the following entry and press Enter.Material: TG11Plant: 3320 |  |  |
| 4 | Select Stock | Choose the icon beside the stock that you want to add initial stock, for example:Storage Location: 332AUnrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: enter a number, for example, 100 | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

#### Optional: Configure Flexible Workflow for Stock Transport Order

##### Optional: Check Flexible Workflow for Stock Transport Order Approval

Purpose

In this procedure, you check flexible workflow for purchase order approval.

Make sure Flexible Workflow for Purchase Order with UB document is activated, and flexible workflow for purchase order approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version . | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, and then choose Go.Select the line of the item and go to next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of Activate Flexible Workflow for Purchase Orders the configuration step. | The Document Types Purchase Order Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: UBScenario based workflow: XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, and then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: UB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Flexible Workflow for Purchase Orders screen displays. |  |
| 3 | Activate Flexible Workflow for PO Approval | Make sure to make the following entries:Document Type: UBScenario based workflow: XYou may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: UB. |  |

Result

The Scenario based workflow is active for Document Type: UB.

##### Configure Flexible Workflow for Stock Transport Order

Purpose

In this procedure, you configure your release conditions for purchase order approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type UB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Add and make following entry:Name: Test Workflow for Stock Transport Order UBGo to the Preconditions area and choose Document type of purchase order is: Stock Transp. OrderDel (UB)Choose Add and make the following entry:Purchasing group of purchase order is: 003Go to the Step Sequence area, and choose Add, then make the following entry on the next screen:Type: Release Purchase OrderGo to the Recipients area:User: Select User with Purchasing_manager from F4 help.Step to be completed by：One of the recipients.Choose Add.Choose Save. | The workflow for stock Transport order is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The workflow item is activated. |  |

#### Optional: Prerequisite for Overdue Stock in Transit

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to link the list of users who are supposed to receive overdue stock in transit notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Check Existing Teams | Make the following entries and choose Go:Type: SINVOVDUEMIn the Teams area, choose the row of the filtered team, and check if Warehouse Clerk and Inventory Manager are maintained in the Team Members section. If they are, the team is already created, and you can skip the following steps; if not maintained, then please preceed with the following steps. | A list of teams is displayed, or no team can be found. |  |
| 4 | Create Team | Choose Create and make the following entries:Name: SiT OVERDUE MONITORINGStatus: Ready to UseType: SINVOVDUEMGo to the Team Members area and choose Create.On the Select: Business Partner screen, make the following entry in the upper left Search box and press Enter:WarehouseclerkSelect the item with last name WarehouseClerk and choose OK.In the Functions field, choose Search Help.On the Select: Functions screen, in the Items area, select SMMIM_WC and choose OK.Repeat the above step to add Inventory Manager as a team member.Go to the Team Members area and choose Create.On the Select: Business Partner screen, make the following entry in the upper left Search box and press Enter.Inventory ManagerSelect the item with last name Inventory Manager and choose OK.In the Functions field, choose Search Help.On the Select: Functions screen, in the Items area, select SMMIM_IM and choose OK. | Warehouse Clerk and Inventory Manager are assigned to the Sit Overdue Monitoring team. |  |
| 5 | Save Team | Choose Create. | The team has been created and saved. |  |

##### Manage Situation Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set up the situation types by using template.

|  |
| --- |
| Note Please make sure 31N - Situation Handling is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Types screen displays. |  |
| 3 | Check Existing Situation Types | Choose the Situation Types tab, make the following entry, and choose Go:Name (In search box): MAN_MATLOVERDUESITSITNChoose the row of the filtered Situation Types and check whether existing types can be reused for Overdue Stock in Transit.If so, skip step 4 and only modify Start Batch Job in the step; if not, continue the following steps to create new one. | A list of situation types is displayed, or no situation type can be found. |  |
| 4 | Copy Standard Situation Template | On the Manage Situation Types screen, there are Situation Templates and Situation Types tabs.Choose the Situation Templates tab and choose Go to search the Standard Situation Templates: MAN_MATLOVERDUESITSITNSelect the checkbox before the standard situation template: MAN_MATLOVERDUESITSITN and choose Copy. | The situation type has been copied. |  |
| 5 | Create Custom Situation Template | On the Situation Type screen, make the following entries:ID: ZMAN_MATLOVERDUESITSITNName: Material Overdue SiT MonitoringDisplay Sequence: HighIn the Conditions area, check added filters:For example:Delivery Completed = BlankPosting Date (PO) = Previous 180 DaysQuantity (GI) = greater than 0Please add other filters if other conditions need to be applied.In the Recipients area, remove all Responsibility Rules and make the following entry:Filter by Member Function: Inventory Manager and Warehouse ClerkIn the Situation Monitoring area, make the following entry:Monitor Instances: SelectedIn the Batch Job Scheduling area, make the following entries:Time Zone: UTCStart Batch Job At: <Time you want your team members to get notification>(For example, if you want to let your team members receive the notification at UTC 8:00, then enter UTC 8:00.)Choose Create. | The situation type has been created. |  |
| 6 | Enable Situation Template | Scroll to the top and choose Enable. | The situation is enabled. |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/ App Name | Expected Results |
| --- | --- | --- | --- |
| [MRP Run for Single Item](#unique_15) [page ] 17 | Material Planner - External Procurement | Schedule MRP Runs (F1339) | A purchase requisition will be created. |
| [Evaluate Stock/Requirements Situation](#unique_16) [page ] 18 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Process Stock Transport Requisition (with MRP)](#unique_17) [page ] 19 | Purchaser | Assign and Process Purchase Requisitions (ME57) | A stock transport order will be created. |
| [Change Stock Transport Order (with MRP)](#unique_18) [page ] 21 | Purchaser | Change Purchase Order - Advanced (ME22N) | The stock transport order will be changed. |
| [Optional: Create Stock Transport Order (Without MRP)](#unique_19) [page ] 22 | Purchaser | Create Purchase Order - Advanced (ME21N) | A stock transport order will be created. |
| [Optional: Create Stock Transport Order in App Transfer Stock-Cross Plant](#unique_20) [page ] 23 | Inventory Manager | Transfer Stock - Cross-Plant (F1957) | A stock transport order will be created. |
| [Optional: Approve Stock Transport Order](#unique_21) [page ] 25 | Purchasing Manager | My Inbox - All Items (F0862) | A Stock Transport Order is approved |
| [Optional: Check Stock Transport Order Approval Details](#unique_22) [page ] 26 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Post Goods Issue for Stock Transport Order](#unique_23) [page ] 27 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| Check Status of Stock Transfer |  |  |  |
| [Check Status of Stock Transfer with Stock- Single Material](#unique_24) [page ] 28 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Check Status of Stock Transfer with Overdue Materials - Stock in Transit (Optional)](#unique_25) [page ] 29 | Warehouse Clerk | Overdue Materials - Stock in Transit (F2139) | Stock transport order with overdue stock in transit displays. |
| [Post Goods Receipt for Stock Transport Order](#unique_26) [page ] 30 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around <Enter a duration, for example, 60 minutes>.

### MRP Run for Single Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The trading goods (TG11) is planned at plant level. There is now a requirement for the material TG11 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create a New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP forTG11>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.Choose 4 Parameters and make the following entries:Plant: 3310Material: TG11Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message is displayed: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job status, enter TG11 in the search box and choose Go in the top right section of the screen. | The new job is created and displayed in the Application Jobs table when refreshed.Note If there is enough stock or inward goods movement to fulfill the independent requirement, then no purchase requisition is created. |  |

### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the requirement planning has been performed, you want to display the stock/requirements situation for the Trading Goods (TG11) in the stock/requirements list.

Prerequisite

Requirement planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material and Show Shortages | In the search area, make the following entries and choose Go.Material: TG11Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Verify Purchase Requisitions that are Available | In the Stock/Requirements List, to find available purchase requisitions, look for rows with PurRqs items. | The MRP has created purchase requisitions that can be used for the Procurement of Direct Materials (J45) test script. |  |

### Process Stock Transport Requisition (with MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign a purchase requisition for stock transfer and create a corresponding purchase order.

If you want to use the Save Draft feature in this app, you have to use a personalized user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Assign and Process Purchase Requisitions (ME57). | The Assign and Process Purchase Requisitions screen displays. |  |
| 3 | Search for Purchase Requisitions | On the Assign and Process Purchase Requisitions screen, make the following entries:Material: TG11Plant: 3310Assigned Purchase Requisitions: XPartly Ordered Requisitions: XRequisitions for Overall Release: XRequisitions for Item-Wise Release: XThen choose Execute (F8). | The Assign and Process Purchase Requisitions screen with purchase requisition items shows. |  |
| 4 | Select Purchase Requisitions | Select the purchase requisition you want to process.To convert the assigned purchase requisitions into stock transfer orders, choose Edit ItemsEnter the following data in the purchase requisition item:Item Category: USupplying Plant: 3320Storage Location: 331AThen press Enter.The plant 3320 is shown as source of supply on the tab Assignments in the upper area.Choose Save. | The supplying plant 3320 show as a line in the Assignments section: Supplier/Supplying plant XXXX. |  |
| 5 | Process Assignments | Select the line with the supplying plant on the Assignments tab, and choose Create purchaser order. | The Create Purchaser Order screen displays. |  |
| 6 | Adopt the Purchase Requisition and Create a Purchase Order | In the dialog box, check the entriesOrder Type: UB (Stock Transp. Order)Doc. Date: todayPurchase Group: 002Purchase Organization: 3310Company Code: 3310The Purchase Requisition is shown on the left in the Document Overview.Select this purchase requisition and choose Adopt. | The Create Purchase Order screen displays.All the information of the purchase requisition is copied into the stock transfer order. |  |
| 7 | Save the Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | The system displays a message:Stock Transp. Order created under the number 45xxxxxxxx. |  |

### Change Stock Transport Order (with MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed when changes within the stock transfer purchase order have to be made. This process step shows you how to change stock transport order (with MRP).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N). | Selected stock transport order is displayed. |  |
| 3 | Enter Stock Transportation Order | Enter the stock transfer order number created in the previous step and choose Other Document or choose Enter. |  |  |
| 4 | Change Data (Text) | Open header details or items details.Choose the Texts tab. Select the type of text to be entered, and enter text. | Selected stock transfer order is displayed. |  |
| 5 | Change Data (Storage Location) | Open items overview:1. Check the storage location and change if different from 331A.2. Change the Delivery Date to tomorrowSave the changes by choosing Save | The stock transfer order has been changed. |  |

### Optional: Create Stock Transport Order (Without MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to create stock transport order(without MRP).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | Create Purchase Order screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UB (Stock Transp. Order)Then choose Enter. |  |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplying Plant: 3320Header / Org. Data:Purchasing Org.: 3310Purchasing Group: 002Company Code: 3310Item Overview:Material: TG11Quantity: x pcDelivery Date: any date in the futurePlant: 3310Storage Location: 331AThen choose Enter. | All data are entered. The item detail screen opens. |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new purchase order is created. Purchase order number is displayed.Write down the stock transport order number for further usage. |  |

### Optional: Create Stock Transport Order in App Transfer Stock-Cross Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to crate stock transport order in app Transfer Stock - Cross-Plant (F1957).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Transfer Stock - Cross-Plant (F1957). | The Transfer Stock- Cross Plant screen displays. |  |
| 3 | Enter Material Data | Enter the following data and press Enter:Material: for example TG11 | A list of transfer stock data is displayed. |  |
| 4 | Select Stocks for Cross-Plant Transfer | Choose the icon beside the Unrestricted-Use Stock in the plant that you want to transfer from, for example, 3320.Choose Unrestricted-Use Stock on the pop-up card.Choose the icon beside the Unrestricted-Use Stock in another plant that you want to transfer to, for example, 3310. | A dialog box opens. The Issuing Plant, Issuing Storage Location, Stock Type, Current Quantity, Receiving Plant, Stock Type and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Post Transfer | Make the following entries:Issuing Storage Location: Std. storage 1 332AReceiving Storage Location: Std. storage 1 331ADocument Date: <today>Posting Date: <today>Quantity: <X PC> | All data are entered, the function Stock Transport Order becomes active. |  |
| 6 | Create Stock Transport Order | Choose Create Stock Transport Order and when the Success screen with a new stock transport order displays, write it down for further use. | A new stock transport order is created. Purchase order number is displayed.Write down the stock transport order number for further usage. |  |
| 7 | Close the Success Screen | Choose Close to go back to the Transfer Stock - Cross-Plant screen. |  |  |
| 8 | (Optional) Display Stock Transport Order | Choose the success message with the new stock transport order number on the Success window. | The Purchase Order screen displays with the details of the new stock transport order. |  |

### Optional: Approve Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, the Purchase Manager releases a stock transport order.

A prerequisite is the existence of a stock transport order that can be released. Purchasing group is 003 and all stock transport order is UB require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of already created purchase orders displays. |  |
| 3 | Search for Purchase Order Status | Enter the stock transport order number in the search area, then choose Search. | The purchase orders without follow-on documents (w/o status Follow-On Documents) and purchase group 0003 have the status in approval. |  |
| 4 | Open Approve Purchase Orders | On the My Inbox screen, select the purchase order from the left screen. | The My Inbox screen displays. |  |
| 5 | Approve Purchase Order | On the Release Purchase Order screen confirm your created purchase Order information.Choose Approve.On the Submit Decision screen, add note if necessary and choose Submit. | Stock transport order is approved. |  |

#### Optional: Check Stock Transport Order Approval Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing stock transport order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen displays. |  |
| 3 | Search for Stock Transport Order | Enter the stock transport order number in the search area, and then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the purchase order you want to preview, and then go to the Purchase Order screen. | The Purchase Order screen displays. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The purchase order's approval details display. |  |

### Post Goods Issue for Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issue for stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Receipt Purchase Order screen displays. |  |
| 3 | Select Goods Issue Other | On the following screen, make the following entries and press Enter:Trans./Event: Goods IssueReference Document: Purchase OrderPurchase Order: Purchase document number(Movement Type): 351 | The items for the selected purchase order displays. |  |
| 4 | Enter Detail Data | Make the following entries:Quantity: quantity , for example, <100>Storage Location: 332AMake sure TG11 have stock in the storage location. If no, please do initial stock for them. |  |  |
| 5 | Item OK | Check if the Item OK indicator is set. |  |  |
| 6 | Post | Choose Post. |  |  |

### Check Status of Stock Transfer

#### Check Status of Stock Transfer with Stock- Single Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the status of stock transfer with stock-single material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Access the APP | Open Stock - Single Material (F1076). | The Stock Single Material screen displays. |  |
| 3 | Enter Transfer Order Data | Enter material TG11 and press Enter. | You receive an overview of the materials. This concerns all materials that have left the supplying plant and haven’t yet reached the receiving plant. |  |

#### Check Status of Stock Transfer with Overdue Materials - Stock in Transit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how notifications for overdue stock in transit send to the selected responsible team member. The detection process is automatically triggered by the system on a regular basis based on the batch job scheduling parameters maintained in preliminary step Create Situation Types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Check Notifications | On the home screen, choose the Notifications icon in the upper right corner. | The following notification displays:Stock Transport Order XXXXXXXXXX/00XX is overdue. |  |
| 3 | Navigate to Overdue Material Stock in Transit App | Choose the detailed notification line Stock Transport Order XXXXXXXXXX/00XX is overdue. | The Overdue Materials - SiT screen displays.Note The notified user, for example, Warehouse Clerk, can be navigated to detailed information in Overdue Material – Stock in Transit App from the alert because the role has proper authorization. |  |
| 4 | Check information on Overdue Stock Transport Order | Choose Stock Transport Order line of that have overdue alert. | Situation displays as Stock Transport Order is overdue. |  |

### Post Goods Receipt for Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the stock transport order and post goods receipt.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Purchasing Document screen displays. |  |
| 3 | Search for Purchasing Document | Open Purchasing Document Search. | A list of purchasing documents displays. |  |
| 4 | Select the Stock Transport Order | Select your purchase order. | The system displays the data for the goods receipt on the Post Goods Receipt screen. |  |
| 5 | Enter Delivery Note | Make the following entries and press Enter:Delivery Note: xxxPrinting (Controls output management after posting): Individual slip |  |  |
| 6 | Select Item and Post Goods Receipt | Select the items for which a goods receipt is to be posted.Enter the following data:Storage Location: for example, 331AChoose Post. | The Post is activated. The Post Goods Receipt screen displays. The system shows Material document xxx posted message. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Open Overdue Materials Stock in Transit | Open Overdue Materials - Stock in Transit (F2139). | The Overdue Materials – SIT screen displays. |  |
| 3 | Select Criteria | Enter the following data:Material: TG11Choose Go. |  |  |
| 4 | Check the Stock Transport Order | Check the quantity under the goods issue quantity for your stock transport order. | You will see the goods issue quantity. |  |
| 5 | Post Goods Receipt for Purchasing Document | Select the purchasing document, choose Post Goods Receipt for Purchase order. | The Goods Receipt screen displays. |  |
| 6 | Post | Choose Select item, enter storage location and choose Post. | The material document 5xxxxxxxxx posted system message displays. |  |

## Appendix

### Additional Features

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In order to track the status of all user's situation, you can log on system as an Employee - Situation Handling and continue testing the feature of My Situations the Fiori App.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Employee - Situation Handling. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Situations (F4154). | The My Situations screen displays. |  |
| 3 | Check Situations | Check all the situations in the system. | Different types of situations are displayed. |  |

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
> Flagged while digesting this document, not verified: Approval section mentions purchasing group 003 and 0003 inconsistently, and the Purpose says stock transfer POs are not subject to approval while the optional section says all UB orders require approval.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-cross-plant-transfer-posting-1p7-ae-752]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 53,013 chars in the whole document
