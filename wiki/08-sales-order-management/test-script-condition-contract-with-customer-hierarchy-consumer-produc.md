---
id: 08-sales-order-management/test-script-condition-contract-with-customer-hierarchy-consumer-produc
title: "Test Script: Condition Contract with Customer Hierarchy – Consumer Products (6V0_AE) (6V0_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6V0_AE: sell from stock, then rebate condition contracts on a customer hierarchy and final settlement."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/condition-contract-settlement]
aliases: [6V0_S4CLD2608_BPD_EN_AE]
keywords: ["Rebates, Commissions and Royalties Settlement", condition contracts, customer hierarchy, sales rebate settlement, business volume, test scripts, sales order processing, credit management, outbound delivery, goods issue]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6V0_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1190
topic: 08-sales-order-management/condition-contract-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Condition Contract with Customer Hierarchy – Consumer Products (6V0_AE) (6V0_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6V0_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rebates, Commissions and Royalties Settlement** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Condition Contract with Customer Hierarchy – Consumer Products (6V0_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859080)

[2 Prerequisites 4](#_Toc232859081)

[2.1 System Access 4](#_Toc232859082)

[2.2 Roles 4](#_Toc232859083)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232859084)

[2.4 SSCUI 7](#_Toc232859085)

[2.4.1 Assign Customer Hierarchy Relevance to Sales Document Types – ID “105807” 7](#_Toc232859086)

[2.5 Business Conditions 8](#_Toc232859087)

[2.6 Preliminary Steps 9](#_Toc232859088)

[2.6.1 Set Initial Stock for Material 9](#_Toc232859089)

[2.6.2 Set a Credit Limit (Optional) 11](#_Toc232859090)

[2.6.3 Create Customer Hierarchy 12](#_Toc232859091)

[2.6.4 Define Process Variant for Business Volume Selection Criteria Usage 15](#_Toc232859092)

[3 Overview Table 18](#_Toc232859093)

[4 Test Procedures 20](#_Toc232859094)

[4.1 Sell from Stock 20](#_Toc232859095)

[4.1.1 Create Sales Order 20](#_Toc232859096)

[4.1.2 Review and Release or Reject  a Sales Order 22](#_Toc232859097)

[4.1.2.1 Review Sales Order (Optional) 22](#_Toc232859098)

[4.1.2.2 Release Sales Order (Optional) 24](#_Toc232859099)

[4.1.2.3 Reject Sales Order (Optional) 25](#_Toc232859100)

[4.1.3 Create Delivery 26](#_Toc232859101)

[4.1.4 Execute Picking 28](#_Toc232859102)

[4.1.5 Check Batches (Optional) 29](#_Toc232859103)

[4.1.6 Post Goods Issue 30](#_Toc232859104)

[4.1.7 Confirm Proof of Delivery 31](#_Toc232859105)

[4.1.8 Create Billing Document 32](#_Toc232859106)

[4.1.9 Create Invoice List 34](#_Toc232859107)

[4.2 Condition Contract Maintenance and Settlement 36](#_Toc232859108)

[4.2.1 Create Condition Contracts 37](#_Toc232859109)

[4.2.2 Check Business Volume (Optional) 39](#_Toc232859110)

[4.2.3 Final Settlement 40](#_Toc232859111)

[4.2.4 Check Settlement Documents for Final Settlement (Optional) 41](#_Toc232859112)

## Purpose

Overview

This scope item describes a sales process in the consumer products industry focusing on the subsequent settlement of rebate agreements using customer hierarchy.

For this purpose, three agreements (condition contracts) are created for different levels of the customer hierarchy:

- An agreement for the entire customer hierarchy
- A special agreement only for the customers in a particular state (on a particular customer hierarchy node)
- A third agreement applies to the entire customer hierarchy except the customer hierarchy node with the special agreement

The process starts with the creation of standard sales orders. After confirming stock availability, the shipping specialist creates the outbound deliveries. When the goods issue is posted, the costs of the goods sold are recorded in Financial Accounting.

Once the goods are delivered and the proof of delivery (POD) is confirmed by the ship-to party, you can bill the delivery. After the invoice is posted and transferred to FI, you have the basis for a subsequent settlement of rebate agreements with your customers, the business volume base.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new master data set to be created and the needed master data objects are mentioned below:

Material Master Data:

| Data | Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0504 | Sweets (Carton) | Batch administrated, best before date |

Organization Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

Customer:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33105001 | Domestic CP Customer 01 | This Business Partner is setup for the VSiT Process (Incoterm DAP) |
| Ship-to Party | 33105001 | Domestic CP Customer 01 | This Business Partner is setup for the VSiT Process (Incoterm DAP) |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sold-to Party | 33105002 | Domestic CP Customer 02 |  |
| Ship-to Party | 33105002 | Domestic CP Customer 02 |  |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sold-to Party | 33105005 | Domestic CP Customer 05 |  |
| Ship-to Party | 33105005 | Domestic CP Customer 05 |  |
| Payer | 33105005 | Domestic CP Payer Customer 05 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BET | Create Sales Pricing Condition - MDS |
| BND | Create Customer Master - MDS |

### SSCUI

#### Assign Customer Hierarchy Relevance to Sales Document Types – ID “105807”

Customer hierarchy needs to be updated for analytics purpose. For this a sales document type needs to be assigned to the “customer hierarchy relevance".

Purpose

In this activity, you assign Customer Hierarchy Relevance to Sales Document Types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Configure your Solution | Choose Configure Your Solution | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Sales Master Data Management | All entries display in All Items section. |  |
| 5 | Select Entry | Find the entry with item name Business Partner and choose arrow at the item end. | Configure Your Solution – Business Partner screen displays. |  |
| 6 | Select Configuration | In Configuration Steps section, choose Configure in column Actions for step Assign Customer Hierarchy Relevance to Sales Document Types (ID 105807) | Change View “Assign Customer Hierarchy Relevance to Sales Document Types”: Change screen displays. |  |
| 7 | Maintain Customer Hierarchy Relevance | Update Entries, enter the following data and choose Save.SaTy: For example: ORCustomer Hierarchy Relevance: 01 Basic Hierarchy Determination | Customer Hierarchy Relevance is updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  | Perform the following steps to update Customer Hierarchy Relevance to Sales Document Types. |
| 2 | Open Assign Customer Hierarchy Relevance to Sales Document Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Customer Hierarchy Relevance to Sales Document Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display View Assign Customer Hierarchy Relevance to Sales Document Types screen displays. |  |
| 3 | Open Maintain Customer Hierarchy Relevance | Update Entries, make the following data and choose Save.SaTy:For example: ORCustomer Hierarchy Relevance: 01 Basic Hierarchy Determination | Customer Hierarchy Relevance is updated. |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FIN_FSCM_REBUILD_DCD | Rebuild DCD functionality |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays.Note It only displays this way if it was your last transaction. So, the action for the user should be to select Reference Document for MIGO Transaction > Other. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Trans./Event: Goods ReceiptReference Document for MIGO Transaction: Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : FG0504 |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 500Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |

#### Set a Credit Limit (Optional)

Purpose

In this activity, you set a credit limit for the customer. The credit limit currency in all company codes is set to use the group currency, which is defined when the solution is activated.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency that is defined when the solution is activated. |

|  |
| --- |
| Note If you use the Create Credit Segment configuration step, if you want to set the Credit Segment 1000 in the FLEXIBLE_CHECK field to a value of 3 on the Main Segment and Segment levels, you must also enter a credit limit for Credit Segment 0000. |

Prerequisite

Business partner master record 33105005 is already created with credit management profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). | The Manage Credit Accounts (F4596) view is displayed. |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: 33105005For the row in the Worklist, choose Details (>). |  |  |
| 4 | Maintain Credit Profile | Choose the Scoring tab.Choose Edit.Make the following entries:Calculation Rule: Standard rule without Automatic calculationRisk Class: Medium Default RiskCredit Check Rule: 01 Default - All Checks Active |  |  |
| 5 | Maintain Credit Segment | Choose the Credit Segments tab. Review or enter the following values in the Credit Segment field:Credit Segment: 1000 Credit Segment 1000 (Maintained)Credit Limit: 5.00Go to the Credit Segment line and make the following entry and choose Apply:Limit Valid To: <End of Year>Note If the Valid To field is not visible, you can go into View Settings and select it to display it.Note Repeat this step to set a credit limit on Credit Segment 0000 to avoid the sales order being blocked at headquarter credit check. | The amount and validity date are set for the credit limit. |  |
| 6 | Save | Save your entries. | Changes have been saved. |  |

#### Create Customer Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a customer hierarchy for the existing customers. The customers in this script will belong to the same hierarchy.

|  |
| --- |
| Note In case a customer hierarchy already exists from script 5HL, this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Hierarchies (F5794). | The Manage Customer Hierarchies screen opens. |  |
| 3 | Create new Hierarchy | Choose Create. | The screen to create a new customer hierarchy is displayed. |  |
| 4 | Enter new Hierarchy | Make the following entries:Type: Customer Hierarchy – SalesHierarchy ID: AE05_0001Hierarchy Description: CP Customer CorporationStart Date: <First of current month>Sales Organization: 3310Distribution Channel: 10Division: 00Choose Create. | The Hierarchy List shows the new hierarchy with status Draft. |  |
| 5 | Create Customer Hierarchy Nodes | Click on the details (>) chevron on the right side of the list entry for the newly created customer hierarchy. | The view pane for the Hierarchy AE05_0001 appears on the right side of the screen. |  |
| 6 | Add new Nodes | Choose Edit. | The pane switches to Edit Mode. |  |
| 7 |  | Choose the Fast Entry Icon on the right hand side of the line for the top-node in the Nodes section. | Fast Entry Screen for Nodes appears. |  |
| 8 | Fast Entry of Nodes | Choose Subnodes and mark them as pricing relevant:ID: RE_WEST_HQ; Description: Headquarter Region WestID: RE_SOUTH_HQ ; Description: Headquarter Region SouthID: RE_MIDDLE_HQ; Description: Headquarter Region MiddleChoose OK. | The subnodes are created. |  |
| 9 | Enter next level nodes | On the line for RE_WEST_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 10 |  | Enter the following data:ID:Description:Pricing Relevant: CheckedChoose OK. | Subnode is created. |  |
| 11 | Enter next level nodes | On the line for RE_SOUTH_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 12 |  | Enter the following data:ID:Description:Pricing Relevant: CheckedChoose OK. | Subnode is created. |  |
| 13 | Enter next level nodes | On the line for RE_MIDDLE_HQ choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 14 |  | Enter the following data:ID:Description:Pricing Relevant: CheckedChoose OK. | Subnode is created. |  |
| 15 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 16 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105005Choose OK. | Business Partner Subnode is created. |  |
| 17 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 18 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105001Choose OK. | Business Partner Subnode is created. |  |
| 19 | Enter business partner nodes | On the line for choose the Add Icon to create a single subnode. | The screen to create a single subnode appears. |  |
| 20 |  | Enter the following data:Business Partner: CheckedID: from the value help select business partner 33105002Choose OK. | Business Partner Subnode is created. |  |
| 21 | Save your data | Choose Save. | The hierarchy is saved with status Draft. |  |
| 22 | Activate the Hierarchy | Choose Activate. | The hierarchy status changes from Draft to Active. |  |

#### Define Process Variant for Business Volume Selection Criteria Usage

Purpose

In this activity, you create a condition contract process variant to change the usage of business volume selection criteria defined in the relevant set of field combinations.

To allow high flexibility in the business volume selection, the set of field combinations for sales rebate settlement provides many business volume selection criteria. However, this larger number can complicate the maintenance of business volume selection criteria in the condition contract as the user needs to find the desired field combination in a long list when he wants to enter a new line. With a suitable condition contract process variant, you can reduce the scope of business volume selection criteria to the relevant ones.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants (ID 102667) configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZSC1 Selection with Customer HierarchyChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S02Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Sales RebateField Combination: select 0069 from field help list.Usage of Field Combination: select from the dropdown list as used.Choose Save. | The usage of field combination is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants(ID 102667).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZSC1 Selection with Customer HierarchyChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S02Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Sales RebateField Combination: select 0069 from field help list.Usage of Field Combination: select from the dropdown list as used.Choose Save. | The usage of field combination is changed with the process variant. |  |

## Overview Table

This scope item consists of several process steps provided in the attached file below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Sell from Stock](#unique_13) [page ] 20 |  |  |  |
| [Create Sales Order](#unique_14) [page ] 20 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Review and Release or Reject a Sales Order](#unique_15) [page ] 22 |  |  |  |
| [Review Sales Order (Optional)](#unique_16) [page ] 22 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The blocked sales order is reviewed. |
| [Release Sales Order (Optional)](#unique_17) [page ] 24 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is released. |
| [Reject Sales Order (Optional)](#unique_18) [page ] 25 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The Sales order is rejected. |
| [Create Delivery](#unique_19) [page ] 26 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created. |
| [Execute Picking](#unique_20) [page ] 28 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Delivery is picked. |
| [Check Batches (Optional)](#unique_21) [page ] 29 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch updated for outbound delivery. |
| [Post Goods Issue](#unique_22) [page ] 30 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods Issue is posted. |
| [Confirm Proof of Delivery](#unique_23) [page ] 31 | Shipping Specialist | Deliveries Worklist - Proof of Delivery (VLPODL) | POD is confirmed. |
| [Create Billing Document](#unique_24) [page ] 32 | Billing Clerk | Create Billing Documents (F0798) | Invoice is created for billing document - Invoice is created and sent from the SAP S/4HANA system (supplier side) to the Buyer system. |
| [Create Invoice List](#unique_25) [page ] 34 | Billing Clerk | Manage Invoice Lists (F2740) | Invoice list document number created. |
| [Condition Contract Maintenance and Settlement](#unique_26) [page ] 36 |  |  |  |
| [Create Condition Contracts](#unique_27) [page ] 37 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) | Sales rebate condition contract is created. |
| [Check Business Volume (Optional)](#unique_28) [page ] 39 | Billing Clerk | Display Business Volume - Condition Contracts (WB2R_BUSVOL) | Business Volume for condition contract is checked. |
| [Final Settlement](#unique_29) [page ] 40 | Billing Clerk | Settle Condition Contracts (WB2R_SC) | Customer Condition Contract final Settlement is created. |
| [Check Settlement Documents for Final Settlement (Optional)](#unique_30) [page ] 41 | Billing Clerk | Manage Settlement Documents (F3254) | Settlement document is checked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Sell from Stock

With the following sales process we will create a basis for the settlement (business volume) of the rebate condition contracts which will be created later. The settlement will be based on posted invoices that are transferred to FI.

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order-VA01. |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Initial screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-to Party: 33105001Ship-to Party: 33105001Cust. Reference: <Reference number> Enter a customer purchase order number as reference.Cust.Ref.Date: <today>Incoterms: FHGoto Item Overview tab and enter the following entries:Material: FG0504Order Quantity: 1 |  |  |
| 6 | Check Customer Hierarchy (optional) | Go to Menu > Goto > Header > Additional Functions > Customer Hierarchy . | The screen with the Customer Hierarchy Root node and its sub nodes relevant for this customer are displayed. |  |
| 7 | Save | Choose Save. Make a note of the sales order number:___________. | Sales order with customer 33105001 is created. |  |
| 8 | Create More Sales Orders | Repeat above steps from 1 to 7 to create 2 more sales orders: with Sold-to party 33105002 & 33105005. | Sales orders are created respectively for customers 33105002 & 33105005. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go, for example, enter sales order number in field Sales Order. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

Repeat this step for all sales orders created earlier.

#### Review and Release or Reject  a Sales Order

Context

The sales order failed the credit check. In the following procedures, you review blocked sales orders and resolve any credit issues.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

Credit case has been assigned to a Credit Analyst or Person Responsible.

##### Review Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you review blocked sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to a credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view is displayed. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33105005Credit Segment: 1000Note Use appropriate filter to get documents. | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. | The Document with Credit Block view is displayed. |  |
| 5 | Enable Editing | Choose Edit. | Updates data. |  |
| 6 | Update | Update the DCD fields.Credit Analyst: <Your user with HR Master Record created> | The DCD data is changed. |  |
| 7 | Save | Save your entries. | The changes are saved. |  |
| 8 | Set In Process | Choose Set To In Process | Status changed to In Process. |  |

##### Release Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you release the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: <your business partner>Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. |  |  |
| 5 | Release | Choose Release. On the Release dialog box, enter an approval note and choose Release. | The log is displayed and under the Classification and Changes facet, the Last Action is Release. |  |

##### Reject Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you reject the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The documented credit decision is assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33105005Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select Case | Select the row of the documented credit decision you generated in the previous step.Choose Details (>). | The Document with Credit Block view displays. |  |
| 5 | Reject | Choose Reject. | The Reject dialog box displays. |  |
| 6 | Select Rejection Reason | Make the following entry and choose Reject:Rejection Reason: for example, Rejected by ApproverRejection Note: <any note> | The sales order/service order/service contract is rejected and the DCD Status changes to Closed and the Notes are updated with the note of type Rejection Reason. |  |

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three deliveries from three sales orders created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Order: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales orders and choose Create Deliveries. | Deliveries are triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. The failed entries will display in Messages tab. The delivery number will display in the Deliveries tab.Three deliveries are created, for customer 33105001, 33105002 and 33105005. |  |

|  |
| --- |
| Note At delivery creation, the scope item settings for check availability use available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities and does not start the warehouse management picking process. As soon as there is sufficient stock at delivery creation, the system creates a delivery with further picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.- You may increase replenishment lead time that is used during the availability check (must be larger than the selection period used for delivery creation).- You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.- You may change the customizing settings for the used delivery item category.The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, created by and Additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | Choose your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.Note Sales BOM sub item materials are not relevant for the logistics process i.e. batch or picking quantity update.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |
| 10 | Repeat | Repeat step 4 to 9 for other deliveries (if any). |  |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assigned to the material.

Prerequisites

Execute this step for batch managed product FG0504.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <outbound delivery number>, and choose Enter. |  |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, go to the Batch field, and check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries - VL06O screen is displayed. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 | The Goods Issue for Outbound Deliveries to be Posted screen is displayed. |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | The goods issues are posted for the chosen deliveries. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Goods (FERT) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the delivery number and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Delivery Note Output Type and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Confirm Proof of Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm proof of delivery. Either the customers sends you a confirmation that the goods were actually received or you assume it after a certain period for example two working days after goods issue. Only if you have the proof of delivery confirmed the invoice can be created.

|  |
| --- |
| Tip This step is necessary depending on the business partner data for this customer. In the shipping data you can see if a Proof of Delivery is expected or not. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Deliveries Worklist - Proof of Delivery (VLPODL). | The Deliveries for Proof of Delivery screen displays. |  |
| 3 | Select the Delivery | No entries necessary. Choose Execute. | The list of deliveries relevant for POD-confirmation is displayed. Status for your delivery is red (POD confirmation Status). |  |
| 4 | Confirm Proof of Delivery | Mark the delivery you posted Goods Issue in the previous step.Choose Confirm.On the Confirmation Prompt choose Continue. | The POD Confirmation Log displays with a message that Proof of Delivery for your delivery has been confirmed.If you return to the worklist the status of your delivery is now green. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing: Create three billing documents referring to the deliveries created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose button Create Billing Document. | There is one window Creating Billing Documents displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose OK. | The draft billing document with ID TMPxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save. The draft version billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

|  |
| --- |
| Note After this step, the Electronic Nota Fiscal must be handled. This is part of scope item 1J5_BR (section Electronic Fiscal Documents). |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | Enter G/L Acc 1210000012100000 Description. | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | In the billing document number recorded in previous step, choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, add, delete and update the text. Save your changes by pressing the button Save in the footer bar. |  |  |

#### Create Invoice List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create invoice list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). | The Manage Invoice Lists (F2740) screen displays. |  |
| 3 | Navigate to Edit Worklist for Invoice Lists Screen | Choose Create. | The Edit Worklist for Invoice Lists screen displays. |  |
| 4 | Search Billing Documents | Make the following data in section Customer Data and choose Display Worklist for Invoice Lists:Payer: 33105010 | Billing documents displays in the result. |  |
| 5 | Select item(s) for Invoice List | Select the rows of Billing documents created previously and choose Collective Billing Document. | The system generates an invoice list for billing. |  |
| 6 | Check Invoice List Document | On the Edit Worklist for Invoice Lists screen, choose Log Display. And then choose Documents, make a note of the invoice list document number in SD Document column: __________. | Invoice list document number displays. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | 44002000 Sales Disc Domestic22000000 Output tax (MWS) | Enter G/L Acc 1210000012100000 Description. | none |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). |  |  |
| 3 | Search for Invoice List | Enter search term(s) in filter bar and choose Go:For example, enter invoice list number in field Invoice List. | The invoice list is displayed in result list. |  |
| 4 | Navigate to Invoice List Overview Screen | Click invoice list number 9XXXXXXX and choose Display Invoice Lists (VF23). | The Invoice List Display: Invoice List Items Overview screen displays. |  |
| 5 | Check Output Condition | Choose Output. | The Invoice List Display: Output screen displays. |  |
| 6 | Display Print Preview | Select the line already created for the print output and choose Display Document. | The printing form is displayed. |  |

|  |
| --- |
| Note The invoice list can consolidate a list of billing documents: Not only standard invoices with type F2 as above, but also debit memos, credit memos, and convergent billing types (CBD1, CBD2 and CBC1). To simulate invoice lists from debit memo，credit memo, or convergent billing, firstly complete all activities till debit memo/credit memo / convergent billing generation in the following scope item(s) using the data listed in chapter Master Data, Organizational Data, and Other Data:1F1 - Debit Memo Processing1IU - Customer ConsignmentBDD - Lean Customer ReturnsBKP - Customer Returns1EZ - Credit Memo Processing1MC - Omnichannel Convergent Billing |

### Condition Contract Maintenance and Settlement

Now rebate condition contracts will be created, their business volume checked and finally settled. Topics like partial settlements and accruals are covered in scope item Sales Rebate Processing (1B6).

#### Create Condition Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The created condition contracts will illustrate the following scenario:

- There is a general agreement on a rebate for all customers in the hierarchy of 1% for the business volume (= invoice value).
- There is a special additional agreement with one state of 3% for the business volume.
- For the same purpose there is another agreement with the whole hierarchy for 1,5% of the business volume which shall exclude the state with the special agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Create Contract | Choose Create. | Screen Select Condition Contract Type appears. |  |
| 4 | Select Condition Contract Type | On Select Condition Contract Type pop-up window, choose Sales Rebate – Multiple Customers (0S02) | The Create Sales Rebate screen displays. |  |
| 5 | Enter Contract Details | On the Create Sales Rebate – Multiple Customers screen, make the following entries and choose Enter:From: <First of current month>To: <end of the current month> |  |  |
| 6 | Enter Basic Data | Process Variant: ZSC1 Selection with Customer HierarchyExternal Identifier: General Agreement |  |  |
| 7 | Enter Sales Data | On the Sales tab page, make the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 8 | Enter Business Volume Base | On the Business Volume Selection Criteria tab page, select New Line. Make the following entries and choose Enter:Field Combination: 0069 Customer HierarchyInclusion Indicator (Incl/Excl): InclusiveCH Rt. Nd. ID: AE05_0001Customer Hierarchy Root Note ID: AE05_0001Cust. Hier Nd. Type: ROOT_NODENote If you need to enter more selection criteria select again New Line. |  |  |
| 9 | Enter Settlement Data | On the Settlement Data tab page, make the following entries and choose Enter:Settlement Material: FG0504Settlement Type Customer: As Accounts ReceivableNote The settlement material is optional. The settlement material is only needed if no business volume is available or no invoice documents are created for a defined settlement date. |  |  |
| 10 | Enter Condition Record for Rebate | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition, make the following entries and choose Enter.Condition Type: RES1 RebateCondition Rate: <1%>Validity Dates are proposed from the contract validity and shall not be changed for this test case. |  |  |
| 11 | Release Condition Contract | Choose Release. |  |  |
| 12 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

Repeat the steps 3 – 12 for 2 more condition contracts where the following data are different to the first contract:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | External Identifier | Condition Rate | CH Rt. Nd. ID | Customer Hierarchy Root Note ID | Cust. Hier Nd. Type | Inclusion Indicator (Incl/Excl) |
| Contract 2 | Supplemental Agreement A | 3% | AE05_0001 |  | TEXT_NODE | Inclusive |
| Contract 3 | Supplemental Agreement B | 1.5% | AE05_0001 | AE05_0001 | ROOT_NODE | Inclusive |
| AE05_0001 |  | TEXT_NODE | Exclusive |  |  |  |

#### Check Business Volume (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the business volume for the condition contract.

Prerequisite

Use this step if you have prepared transactional data for the customer condition contract.

|  |
| --- |
| Note You can repeat this process step at every point in time in the test procedure. It’s recommendable to check the business volume before you start a settlement run to enable a control of the business volume determined for a settlement document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Business Volume - Condition Contracts (WB2R_BUSVOL). | The Business Volume for Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Business Volume for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract created before>Business Volume Base: From ContractOutput Level Business Volume: Settlement Date and Split Criteria |  |  |
| 4 | Check Business Volume for Condition Contracts | Choose Execute. | Business volume value REBV is determined based on the existing customer invoices. | The results will be depending on the contracts as following:1st Contract: 3 Customers with business volume2nd Contract: 1 Customer with business volume3rd Contract: 2 Customers with business volume |

#### Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a final settlement for the condition contract. In this step, you also reverse the accruals posted before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts (WB2R_SC). | The Settlement of Customer Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Customer Condition Contracts screen, make the following entries and choose Execute.Settlement Date: <end of current month>Settlement Date Type: Final SettlementCondition Contract: <Number of condition contract created before>Posting Date:<today's date>Document Date: <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive runMessage Log Filter: No FilterTake a note of the number of the credit memo created. | The Log for Customer Condition Contract Settlement screen displays. Customer credit memo is created. Accruals are reversed.The results will be depending on the created condition contracts as following: Settlement Documents for the cases:1st contract: 3 Customer Credit Memos created.2nd contract: 1 Customer Credit Memo created3rd contract: 2 Customer Credit Memos created. |  |
| 4 | Optional: Check | Note If the workflow is activated, in this step, you will see the following messages including:Contract XXXXXXXXXXX locked after final settlementDocument XXXXXXXXXXX with document status Workflow Release Required is blocked for follow-on documentsDocument XXXXXXXXXXX saved (no accounting document generated)Document XXXXXXXXXXX is processed with reference XXXXXXXXXXX | Now the credit memo for the condition contract is created but the journal entry is not yet created. |  |

#### Check Settlement Documents for Final Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the settlement document and accounting document for partial settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Documents screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the final settlement and choose the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data , check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Partner Data | Under Partner Data, check the partner information. | You see the partner data maintained in the master data. |  |
| 7 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the Settlement Document Items table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type REBV Rebate Business Vol. The system has calculated the rebate amount with condition type RES1 maintained in the condition contract and the output tax with the percentage for full tax. |  |
| 9 | Check Output | Go back to the Settlement Document screen, under Output Items, check the output items.Find the item with Channel: Printout and choose Open File under Display. | You see the output print form. |  |
| 10 | Check Journal Entries | Under Document Flow, choose the main customer journal entries. Click the icon right to the box and select Display Journal Entries - New Version from the pop-up window. | You see the financial posting as below.The accruals reversal amount is the difference between the amount of reversed accruals and the excess accruals as mentioned in step 8. |  |
| 11 | Check Texts | Go back to the Manage Settlement Documents screen.In the Settlement Documents table, click the settlement document number and select Display Settlement Document from the pop-up window.Choose Header Texts. Under Texts, check the text information. | For text type Contract Text for Output/Forms, you see the text maintained in the condition contract for text type Text for Settlement Document. |  |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 12100000 (Receivables Domestic) | 0 | <Sales rebate amount + Output tax> |
| 44001000 (Sales Rebates) | <Sales rebate amount> | 0 |
| 22000000 (Output tax (MWS)) | <Output tax> | 0 |

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
- related-to :: [[08-sales-order-management/margin-optimization-sap-solution-extensions-by-vistex-7uq-test-script]]
- related-to :: [[08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[08-sales-order-management/sales-rebate-processing-1b6-ae-test-script-sap-s-4hana-cloud-public-ed]]
- related-to :: [[08-sales-order-management/test-script-sales-commissions-external-sales-representative-2tt-ae-863]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6V0_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 73,412 chars in the whole document
