---
id: 15-retail-operations/test-script-omnichannel-sales-promotion-opps-consumer-products-7t7-ae
title: "Test Script: Omnichannel Sales Promotion (OPPS) – Consumer Products (7T7_AE) (7T7_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script, scope item 7T7_AE: OPPS promotion rules (free item, discount, combined), prerequisites and sales order tests, AE/AED."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/omnichannel-promotions]
aliases: [7T7_S4CLD2608_BPD_EN_AE]
keywords: [Omnichannel Promotion Pricing for Sales Orders, omnichannel promotion pricing, promotion rules, free item promotions, special discount promotions, combined promotion rules, sales order creation, scope item testing, opps configuration, pricing procedure configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7T7_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1224
topic: 15-retail-operations/omnichannel-promotions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Omnichannel Sales Promotion (OPPS) – Consumer Products (7T7_AE) (7T7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7T7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Omnichannel Promotion Pricing for Sales Orders** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 28-08-26 |
| --- | --- |
|  | Omnichannel Sales Promotion (OPPS) – Consumer Products (7T7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc239511887)

[2 Prerequisites 4](#_Toc239511888)

[2.1 System Access 4](#_Toc239511889)

[2.2 Roles 4](#_Toc239511890)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc239511891)

[2.4 Additional Manual Configuration 6](#_Toc239511892)

[2.5 Business Conditions 7](#_Toc239511893)

[2.6 SSCUIs 7](#_Toc239511894)

[2.6.1 **Maintain Relevance for Omnichannel Sales Promotions – ID “107197”** 7](#_Toc239511895)

[2.6.2 Set Pricing Procedure – ID “101117” 8](#_Toc239511896)

[2.6.3 Set Pricing Procedure - Customer 10](#_Toc239511897)

[2.6.4 Set Pricing Procedure Determination – ID “101118” 11](#_Toc239511898)

[2.7 Preliminary Steps 12](#_Toc239511899)

[2.7.1 Set Initial Stock for Material 12](#_Toc239511900)

[2.7.2 SAP Omnichannel Sales Promotion Setup 13](#_Toc239511901)

[2.7.2.1 Configure Omnichannel Promotion Pricing – Number Ranges 13](#_Toc239511902)

[2.7.2.2 Configure Omnichannel Promotion Pricing – Configurations 14](#_Toc239511903)

[2.7.2.3 Configure Omnichannel Promotion Pricing – Identifier Formats 15](#_Toc239511904)

[3 Overview Table 17](#_Toc239511905)

[4 Test Procedures 20](#_Toc239511906)

[4.1 Promotion Rule - Single 20](#_Toc239511907)

[4.1.1 Promotion Rule – “Free Item Alpha” 20](#_Toc239511908)

[4.1.1.1 Maintain Promotion Rule - "Free Item Alpha" 20](#_Toc239511909)

[4.1.1.2 Create Sales Order 22](#_Toc239511910)

[4.1.2 Promotion Rule – “Free Item Beta" 24](#_Toc239511911)

[4.1.2.1 Maintain Promotion Rule - “Free Item Beta” 24](#_Toc239511912)

[4.1.2.2 Create Sales Order 27](#_Toc239511913)

[4.1.3 Promotion Rule – “Free Item Gamma" 28](#_Toc239511914)

[4.1.3.1 Maintain Promotion Rule - “Free Item Gamma” 28](#_Toc239511915)

[4.1.3.2 Create Sales Order 31](#_Toc239511916)

[4.1.4 Promotion Rule – “Free Item Alpha - Value" 33](#_Toc239511917)

[4.1.4.1 Maintain Promotion Rule - “Free Item Alpha - Value” 33](#_Toc239511918)

[4.1.4.2 Create Sales Order 35](#_Toc239511919)

[4.1.5 Promotion Rule – “Free Item Beta - Value" 37](#_Toc239511920)

[4.1.5.1 Maintain Promotion Rule - “Free Item Beta – Value ” 37](#_Toc239511921)

[4.1.5.2 Create Sales Order 40](#_Toc239511922)

[4.1.6 Promotion Rule – “Free Item Gamma - Value" 42](#_Toc239511923)

[4.1.6.1 Maintain Promotion Rule - “Free Item Gamma - Value” 42](#_Toc239511924)

[4.1.6.2 Create Sales Order 44](#_Toc239511925)

[4.1.7 Promotion Rule – “Special Discount” 46](#_Toc239511926)

[4.1.7.1 Maintain Promotion Rule - “Special Discount” 46](#_Toc239511927)

[4.1.7.2 Create Sales Order 49](#_Toc239511928)

[4.1.8 Promotion Rule – “Special Discount - Value” 51](#_Toc239511929)

[4.1.8.1 Maintain Promotion Rule - “Special Discount - Value” 51](#_Toc239511930)

[4.1.8.2 Create Sales Order 53](#_Toc239511931)

[4.1.9 Promotion Rule – “Special Discount - Price” 55](#_Toc239511932)

[4.1.9.1 Maintain Promotion Rule - “Special Discount - Price” 55](#_Toc239511933)

[4.1.9.2 Create Sales Order 58](#_Toc239511934)

[4.1.10 Promotion Rule – “Special Discount – Price and Value” 60](#_Toc239511935)

[4.1.10.1 Maintain Promotion Rule - “Special Discount – Price and Value” 60](#_Toc239511936)

[4.1.10.2 Create Sales Order 62](#_Toc239511937)

[4.2 Promotion Rule - Combined 64](#_Toc239511938)

[4.2.1 Promotion Rule – “Free Item Alpha – Combined” 64](#_Toc239511939)

[4.2.1.1 Maintain Promotion Rule - “Free Item Alpha - Combined” 64](#_Toc239511940)

[4.2.1.2 Create Sales Order 68](#_Toc239511941)

[4.2.2 Promotion Rule – “Free Item Beta – Combined” 70](#_Toc239511942)

[4.2.2.1 Maintain Promotion Rule - “Free Item Beta - Combined” 70](#_Toc239511943)

[4.2.2.2 Create Sales Order 74](#_Toc239511944)

## Purpose

Overview

SAP Omnichannel Promotion Pricing is a cloud solution that supports use across various sales channel applications, including SAP S/4HANA Cloud Public Edition. In this scenario, users can access related apps to set up rules that define eligibility criteria for omnichannel sales promotions and the associated rewards. The functionality integrates with price management and sales order management and processing. With the correct settings, the Calculation service runs each time users save a sales order or when it is manually triggered. This service verifies whether the order qualifies for promotions. If the order meets the criteria for one or more promotions, the service returns this information along with details about any free goods or discounts to be granted. The system then adds these rewards to the sales order.

You may need a separate license. For further information, contact your SAP Account Executive.

Your rule administrator can define criteria (such as the validity time frame for specific promotions, the distribution chain associated with these promotions, or the discount percentage a customer should receive). For every sales order that an internal sales representative creates, changes or when it is manually triggered the system determines if these predefined criteria are met. If so, the system grants one of the following rewards, according to what has been defined in the promotional rules:

- Automatically creates one or more new items with free goods
- Adapts the price data by adding a discount to one or more items or the entire sales order

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

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/87807ffd176c4dbca23d97ff1ec0705c.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

The following roles are provided by OPPS Management in the BTP:

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

For more information refer to the [Setting-up-roles-and-authorizations in OPPS](https://help.sap.com/docs/omnichannel-promotion-pricing/administration-guide/setting-up-roles-and-authorizations).

| Role | Role Name | Description |
| --- | --- | --- |
| Promotion Planner | Maintain_OPPS_Promotions | Role for users to create, edit and cancel promotions.Responsible for the creation of promotions and the maintenance of price derivation rules to offer rewards to customers based on certain eligibility criteria. |

### Master Data, Organizational Data, and Other Data

This scope item requires new master data set to be created and the needed master data objects are mentioned below:

Material Master Data:

Material Masters mentioned in this document are to be created for plant 3310.

| Data | Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0511 | Carton 12 x 1kg Bags Medium Beans Arabica | Batch administrated, best before date |
| Material | FG0512 | Carton 12 x 1kg Bags Dark Beans Arabica | Batch administrated, best before date |
| Material | TG0501 | Thermo Coffee Cup 0,4l | No serial number, no batch |
| Material | TG0504 | Thermo Coffee Pot 0,75l | No serial number, no batch |

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

Below mentioned Customers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33 105006 | Domestic CP Customer 06 |  |
| Ship-to Party | 33 105006 | Domestic CP Customer 06 |  |
| Payer | 33 105011 | Domestic CP Customer 11 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BET | Create Sales Pricing Condition - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/481a748da85f4284dc863f3b8c63d243)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### SSCUIs

#### Maintain Relevance for Omnichannel Sales Promotions – ID “107197”

Purpose

In this process step the combinations of sales organizations and sales order types that are relevant for omnichannel sales promotions are defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. | Perform the following steps to update Omnichannel Sales Promotions Relevance to Sales Document Types. |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Basic Functions | All entries display in All Items section. |  |
| 5 | Select entry | Find the entry with item name Omnichannel Sales Promotions and choose arrow at the item end. | Configure Your Solution - Omnichannel Sales Promotions screen displays. |  |
| 6 | Access configuration | In Configuration Steps section, choose Configure in column Actions for step Maintain Relevance for Omnichannel Sales Promotions. | The Maintain Relevance for Omnichannel Sales Promotions: Change screen displays. |  |
| 7 | Maintain entry | In the Maintain Relevance for Omnichannel Sales Promotions: Change screen select New Entries and enter the following data:Sales Org.: 3310Sales Doc. Type: <OR>Relevant : <X>Choose Save. | Sales Document Type set to relevant for Omnichannel Sales Promotion. |  |

#### Set Pricing Procedure – ID “101117”

Purpose

In this activity, the necessary Pricing Procedure will be configured.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Select Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Price Management | All entries display in All Items section. |  |
| 5 | Select entry | Find the entry with item name Pricing and choose arrow at the item end. | The Configure Your Solution – Pricing screen displays. |  |
| 6 | Access configuration | In Configuration Steps section, choose Configure in column Actions for step Set Pricing Procedures. | The Set Pricing Procedures: Change screen displays. |  |
| 7 | Create Pricing Procedure | Click on the Position and enter the following data in the popup window:Procedure: A33002Choose Continue.Mark the tick box for the corresponding line item and Select Copy asIn the Set Pricing Procedures: Change: Selected Set screen change the name of the Procedure e. g. Z33002 and click on Copy.In the Specify object to be copied Popup window select copy all.Click on Continue on the Information popup windows.Choose Save. | New Pricing Procedure is created. |  |
| 8 | Add Condition Type to Pricing Procedure | In the Set Pricing Procedures: Change screen, mark the tick box for the Procedure created in step before.Double click on Procedures – Control Data.Select New Entries.Maintain the entries as per the below table:Step NoCondition TypeStatisticalPrint TypeSubtotalRequirementAltCnd BaseValueAccount Key101OCI1X112112ERS102OCI2X112113ERS103OCT1b112114ERS104OCT2b112114ERS105D100a95528ERS106OCT3b112114ERS107OCT4b112114ERS108OCT5b112114ERS109OCT6b112114ERS110OCT7b112114ERSChoose Save. | Condition Types added to Pricing Procedure. |  |

#### Set Pricing Procedure - Customer

Purpose

In this activity, you set the Customer Pricing Procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Business Partner (BP) fiori app. | The Maintain Business Partner screen displays. |  |
| 3 | Enter Customer | Enter the following data and press Enter:Bus. Partner: 33105006Double click on the BP entry in ALV list. | 1 Business Partner Found message appears. |  |
| 4 | Change BP Role | Choose Switch Between Display and Change.Enter below entry and Choose Sales and Distribution:BP Role: FLCU01 CustomerOn the Orders tab, navigate to Pricing/Statistics section and Enter below entry:Cust.Pric.Procedure: OC |  |  |
| 5 | Save | Choose Save. | Changes have been saved message appears. |  |

#### Set Pricing Procedure Determination – ID “101118”

Purpose

In this activity, you set the Pricing Procedure Determination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area : SalesSub Application Area : Price Management | All entries display in All Items section. |  |
| 5 | Select entry | Find the entry with item name Pricing and choose arrow at the item end. | Configure Your Solution – Pricing screen displays. |  |
| 6 | Access configuration | In Configuration Steps section, choose Configure in column Actions for step Set Pricing Procedure Determination. | The Set Pricing Procedure Determination: Change screen displays. |  |
| 7 | Create new entry | In the Set Pricing Procedure Determination: Change screen, click on New Entries and enter the following data:Sales Organization: 3310Distribution Channel: 10Division: 00Doc.PricingProc.: e.g.<Y1>Cust.Pric.Proc.: e.g.<OC>Pricing Procedure: e.g. Z33002Choose Save. | New Pricing Procedure Determination is created. |  |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | Movement Type entered. |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material: FG0511 | Material entered. |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entries, and choose Enter:Qty in Unit of Entry: 500Unit of Entry: <PC> | Quantity entered. |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A | Plant and Storage Location entered. |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Batch data entered.Note Only relevant for batch relevant materials. |  |
| 8 | Repeat steps | Repeat steps 3-7 for Material: FG0512Repeat steps 3-6 for Material: TG0501Repeat steps 3-6 for Material: TG0504 |  |  |
| 9 | Check | Choose Check. | The document is ready to be posted. |  |
| 10 | Save Your Entries | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

#### SAP Omnichannel Sales Promotion Setup

##### Configure Omnichannel Promotion Pricing – Number Ranges

Purpose

In this process step, the number ranges for configuring Omnichannel Promotion Pricing are defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP OPPS launchpad as a Configuration Specialist. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Configure Omnichannel Promotion Pricing app. | The Configure Omnichannel Promotion Pricing screen is displayed. |  |
| 3 | Access Number Ranges tab | In the Configure Omnichannel Promotion Pricing screen click on the Number Ranges tab. | The Number Ranges Tab is visible |  |
| 4 | Maintain Number Range | In the Number Ranges subscreen choose Create.Maintain the following data in the Create Number Range:Entity Name: <Price Derivation Rules>Start Range: e.g.<1>End Range: e.g.<10000>Choose Create. | Number Range created. |  |
| 5 | Maintain additional Number Ranges | Repeat step 4 for Entity Names: <Price Derivation Rule Eligibilities>, <Additional Bonus Price Derivation Items>,<Promotions>, <Mix-and-Match Price Derivation Items> and <Promotion Price Derivation Rules> | Number Ranges created. |  |

##### Configure Omnichannel Promotion Pricing – Configurations

Purpose

In this process step, the configurations for configuring Omnichannel Promotion Pricing are defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP OPPS launchpad as a Configuration Specialist. | The SAP OPPS launchpad displays. |  |
| 2 | Access the App | Open Configure Omnichannel Promotion Pricing app. | The Configure Omnichannel Promotion Pricing screen is displayed. |  |
| 3 | Access Configurations tab | In the Configure Omnichannel Promotion Pricing screen Choose Configurations tab. | The Configurations tab is visible. |  |
| 4 | Create Configuration | In the Configurations subscreen choose Create.Maintain the following data in the New Configuration screen:General InformationValid- From Date: <today>Description: <Configuration>Configuration SettingsDefault Master Data Source System: <Example System>Transaction Discount Method:<TRIGGER>Enhance Unit of Measure Evaluation:<Selected>Enhance Exclusion Criteria Evaluation: <Selected>Enhance External Action Evaluation: <Selected>Enable Tolerant Price Handling: <Selected>Maximum Number of Promotional Rules: <5>Collision Handling for Promotional Rules: <Greedy>Threshold for Single Item Creation: <10>Extended Settings:Rounding Method for Prorated Discounts: <Commercial>Rounding Method for Prorated Points: <Commercial>Rounding Time for Percentage Points: <AFTER>Points Factor: <0,1>Points Rating: <0,5>Threshold Percentage: <75>Maximum Number of Recommendations: <10>Choose Create. | Configuration is created. |  |

##### Configure Omnichannel Promotion Pricing – Identifier Formats

Purpose

In this process step, the Identifier Formats for Configure Omnichannel Promotion Pricing are defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP OPPS launchpad as a Configuration Specialist. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Configure Omnichannel Promotion Pricing app. | The Configure Omnichannel Promotion Pricing screen is displayed. |  |
| 3 | Access Identifier Formats | In the Omnichannel Promotion Pricing screen choose Identifier Formats tab. | The Identifier Formats tab is visible. |  |
| 4 | Create Identifier Format | In the Identifier Formats subscreen choose Create.Note In case a warning pop-up window appears, choose OK.In the Create an Identifier Format Configuration pop-up window enter the following data:Field ID: <Customer>Total Size: <10>Total Numeric Size: <10>Choose Create. | Identifier Format is created. |  |
| 5 | Create second Identifier Format | Repeat step 4 with following data:Field ID: <Product>Total Size: <40>Total Numeric Size: <18>Display Length: <18> | Identifier Format is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Promotion Rule - Single |  |  |  |
| Promotion Rule - "Free Item Alpha" |  |  |  |
| [Maintain Promotion Rule - "Free Item Alpha"](#unique_17) [page ] 20 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_18) [page ] 22 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Free Item Beta" |  |  |  |
| [Maintain Promotion Rule - “Free Item Beta”](#unique_19) [page ] 24 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_20) [page ] 27 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Free Item Gamma" |  |  |  |
| [Maintain Promotion Rule - “Free Item Gamma”](#unique_21) [page ] 28 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_20) [page ] 27 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Free Item Alpha - Value" |  |  |  |
| [Maintain Promotion Rule - “Free Item Alpha - Value”](#unique_22) [page ] 33 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_23) [page ] 35 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Free Item Beta - Value" |  |  |  |
| [Maintain Promotion Rule - “Free Item Beta – Value ”](#unique_24) [page ] 37 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_25) [page ] 40 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Free Item Gamma - Value" |  |  |  |
| [Maintain Promotion Rule - “Free Item Gamma - Value”](#unique_26) [page ] 42 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_27) [page ] 44 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Special Discount" |  |  |  |
| [Maintain Promotion Rule - “Special Discount”](#unique_28) [page ] 46 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_29) [page ] 49 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Special Discount - Value" |  |  |  |
| [Maintain Promotion Rule - “Special Discount - Value”](#unique_30) [page ] 51 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_31) [page ] 53 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Special Discount - Price" |  |  |  |
| [Maintain Promotion Rule - “Special Discount - Price”](#unique_32) [page ] 55 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_33) [page ] 58 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Special Discount - Price and Value" |  |  |  |
| [Maintain Promotion Rule - “Special Discount – Price and Value”](#unique_34) [page ] 60 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_35) [page ] 62 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - Combined |  |  |  |
| Promotion Rule - "Free Item Alpha – Combined" |  |  |  |
| [Maintain Promotion Rule - “Free Item Alpha - Combined”](#unique_36) [page ] 64 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_37) [page ] 68 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |
| Promotion Rule - "Free Item Beta – Combined" |  |  |  |
| [Maintain Promotion Rule - “Free Item Beta - Combined”](#unique_38) [page ] 70 | Configuration Specialist | Maintain Promotions | Promotion Rule is created. |
| [Create Sales Order](#unique_39) [page ] 74 | Internal Sales Representative | Manage Sales Orders (F1873) / Manage Sales Orders - Version 2 (F3893) | Sales order is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Promotion Rule - Single

#### Promotion Rule – “Free Item Alpha”

##### Maintain Promotion Rule - "Free Item Alpha"

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Alpha” is defined in OPPS. This promotion rule adds one Free Item TG0501 in case 2 pieces of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item AlphaDescription: Buy two packages of two different products and get an additional product for freeStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Alpha>Sequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Quantity (QUT)Threshold Quantity: 2Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Quantity (QUT)Threshold Quantity: 2Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product.Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 1Unit of Measure: PCClick on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy two packages of two different products and get an additional product for freeClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Sold-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 3Create additional line with MaterialFG0512 with Order Quantity3.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions.To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions.Check the Amount / Condition Value of Condition Type D100 for the material TG0501. | OPPS is triggered. All Free Goods items of material TG0501 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 is displayed.Note One Free Item TG0501 is added in case 2 pieces of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Free Item Beta"

##### Maintain Promotion Rule - “Free Item Beta”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Beta” is defined in OPPS. This promotion rule adds two Free Item TG0501 in case 6 pieces of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item BetaDescription: Buy six packages of two different products and get two additional product for freeStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: Free Item BetaSequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Quantity (QUT)Threshold Quantity: 6Limit Quantity: 99,999.000Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Quantity (QUT)Threshold Quantity: 6Limit Quantity: 99,999.000Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 2Unit of Measure: PCClick on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy six packages of two different products and get two additional product for freeClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 7Create additional line with Material FG0512 with Order Quantity 7.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type D100 for the material TG0501. | OPPS is triggered. All Free Goods items of material TG0501 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 is displayed.Note Two Free item TG0501 are added in case 6 pieces of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Free Item Gamma"

##### Maintain Promotion Rule - “Free Item Gamma”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Gamma” is defined in OPPS. This promotion rule adds one Free Item TG0501 and one Free Item TG0504 in case 5 pieces of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item GammaDescription: Buy five packages of two different products and get two additional product for freeStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Gamma>Sequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Quantity (QUT)Threshold Quantity: 5Limit Quantity: 99,999.000Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Quantity (QUT)Threshold Quantity: 5Limit Quantity: 99,999.000Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 1Unit of Measure: PCRepeat the above step for material TG0504Click on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy five packages of two different products and get two different additional products for freeClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 5Create additional line with Material FG0512 with Order Quantity 5.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type D100 for the material TG0501 and TG0504. | OPPS is triggered. All Free Goods items of material TG0501 and TG0504 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 and TG0504 is displayed.Note One Free Item TG0501 and one Free Item TG0504 is added in case 5 pieces of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Free Item Alpha - Value"

##### Maintain Promotion Rule - “Free Item Alpha - Value”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Alpha - Value” is defined in OPPS. This promotion rule adds one Free Item TG0501 in case 300 AED of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item Alpha - ValueDescription: Buy 300 AED of two different products and get an additional product for freeStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Alpha - Value>Sequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Amount (AMT)Mixing Forbidden: YesThreshold Amount: 300Limit Amount: 99,999Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Amount (AMT)Mixing Forbidden: YesThreshold Amount: 300Limit Amount: 99,999Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 1Unit of Measure: PCClick on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy 300 AED of two different products and get an additional product for freeClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01.Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 3Create additional line with Material FG0512 with Order Quantity 3.Note Net Value of each line item must exceed 300 AED.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type D100 for the material TG0501. | OPPS is triggered. All Free Goods items of material TG0501 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 is displayed.Note One Free item TG0501 is added in case 300 AED of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Free Item Beta - Value"

##### Maintain Promotion Rule - “Free Item Beta – Value ”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Beta - Value” is defined in OPPS. This promotion rule adds two Free Item TG0501 in case 600 AED of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item Beta - ValueDescription: Buy 600 AED of two different products and get two additional product for freeStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Beta - Value>Sequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Amount (AMT)Threshold Amount: 600Mixing Forbidden: YesLimit Amount: 99,999Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Amount (AMT)Threshold Amount: 600Mixing Forbidden: YesLimit Amount: 99,999Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 2Unit of Measure: PCClick on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy 600 AED of two different products and get two additional product for freeClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 10Create additional line with Material FG0512 with Order Quantity 10.Note Net Value of each line item must exceed 600 AEDPress Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type D100 for the material TG0501. | OPPS is triggered. All Free Goods items of material TG0501 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 is displayed.Note Two free item TG0501 are added in case 600 AED of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Free Item Gamma - Value"

##### Maintain Promotion Rule - “Free Item Gamma - Value”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Gamma - Value” is defined in OPPS. This promotion rule adds one Free Item TG0501 and one Free item TG0504 in case 500 AED of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item Gamma - ValueDescription: Buy 500 AED of both products A and B and get product C and product D for freeStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Gamma - Value>Sequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Amount (AMT)Threshold Amount: 500Mixing Forbidden: YesLimit Amount: 99,999Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Amount (AMT)Mixing Forbidden: YesThreshold Amount: 500Limit Amount: 99,999Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 1Unit of Measure: PCRepeat above step for material TG0504Click on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy 500 AED of both products A and B and get product C and product D for freeClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 5Create additional line with Material FG0512 with Order Quantity 5.Note Net Value of each line item must exceed 500 AEDPress Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type D100 for the material TG0501 and TG0504. | OPPS is triggered. All Free Goods items of material TG0501 and TG0504 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 and TG0504 is displayed.Note One Free Item TG0501 and one Free item TG0504 are added in case 500 AED of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Special Discount”

##### Maintain Promotion Rule - “Special Discount”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Special Discount” is defined in OPPS. This promotion rule calculates a special discount 10% for all items of product FG0511 in case 5 pieces two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Special DiscountDescription: Buy five packages of two different products and get a special discount 10% for all items of product AStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: Special DiscountSequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Quantity (QUT)Threshold Quantity: 5Limit Quantity: 99,999.000Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Quantity (QUT)Threshold Quantity: 5Limit Quantity: 99,999.000Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Mix and Match > Product .Enter the following data in the Product subscreen:Product ID: FG0511Unit of Measure: PCPrice Modification: Percent Discount (RP)Price Modification Amount Percentage: 10.00Check if switch is switched to OR.Click on Change next to the field Limit Count.In the Change Limit Count popup window enter the following:Enter Limit Count: 99.999Click on Change.Click on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy five packages of two different products and get a special discount 10% for all items of product AClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 5Create additional line with Material FG0512 with Order Quantity 5.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type OCT3 for the material FG0511. | OPPS is triggered and special discount is applied to the sales order.In the Condition Value column a 10% discount for the material FG0511 is displayed.Note A special discount 10% for all items of product FG0511 is applied in case 5 pieces two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Special Discount - Value”

##### Maintain Promotion Rule - “Special Discount - Value”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Special Discount - Value” is defined in OPPS. This promotion rule calculates a special discount 10% for all items of product FG0511 in case 50 AED of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Special Discount - ValueDescription: Buy 50 AED of two different products and get a special discount 10% for all items of product AStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: Special Discount - ValueSequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Amount (AMT)Threshold Amount: 50Limit Amount: 99,999Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Amount (AMT)Threshold Amount: 50Limit Amount: 99,999Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Mix and Match > Product .Enter the following data in the Product subscreen:Product ID: FG0511Unit of Measure: PCPrice Modification: Percent Discount (RP)Price Modification Amount Percentage: 10.00Check if switch is switched to OR.Click on Change next to the field Limit Count.In the Change Limit Count popup window enter the following:Enter Limit Count: 99.999Click on Change.Click on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy 50 AED of two different products and get a special discount 10% for all items of product AClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 5Create additional line with Material FG0512 with Order Quantity 5.Note Net Value of each line item must exceed 50 AEDPress Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type OCT3 for the material FG0511. | OPPS is triggered and special discount is applied to the sales order.In the Condition Value column a 10% discount for the material FG0511 is displayed.Note A special discount 10% for all items of product FG0511 is applied in case 50 AED of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Special Discount - Price”

##### Maintain Promotion Rule - “Special Discount - Price”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Special Discount - Price” is defined in OPPS. This promotion rule calculates a special fixed prize of 20 AED for all items of product FG0511 in case 5 pieces two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Special Discount - PriceDescription: Buy five packages of two different products and get a special fixed price for product AStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: Special Discount - PriceSequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Quantity (QUT)Threshold Quantity: 5Limit Quantity: 99,999.000Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Quantity (QUT)Threshold Quantity: 5Limit Quantity: 99,999.000Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Mix and Match > Product .Enter the following data in the Product subscreen:Product ID: FG0511Unit of Measure: PCPrice Modification: Promotion Price (PS)New Price Amount: 20.0Check if switch is switched to OR.Click on Change next to the field Limit Count.In the Change Limit Count popup window enter the following:Enter Limit Count: 99.999Click on Change.Click on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy five packages of two different products and and get a special fixed price for product AClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 5Create additional line with Material FG0512 with Order Quantity 5.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type OCT3 for the material FG0511. | OPPS is triggered and a special fixed price is applied to the sales order.Special Price is applied for all items of FG0511.Note A special fixed prize of 20 AED for all items of product FG0511 is applied in case 5 pieces of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Special Discount – Price and Value”

##### Maintain Promotion Rule - “Special Discount – Price and Value”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Special Discount - Price and Value” is defined in OPPS. This promotion rule calculates a special fixed price of 20 AED for all items of product FG0511 in case 20 AED of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Special Discount - ValueDescription: Buy 20 AED of two products and get a special fixed price for product AStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: Special Discount - Price and ValueSequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Amount (AMT)Threshold Amount: 20Limit Amount: 99,999.000Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Amount (AMT)Threshold Amount: 20Limit Amount: 99,999.000Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Mix and Match > Product .Enter the following data in the Product subscreen:Product ID: FG0511Unit of Measure: PCPrice Modification: Promotion Price (PS)New Price Amount: 20.00Check if switch is switched to OR.Click on Change next to the field Limit Count.In the Change Limit Count popup window enter the following:Enter Limit Count: 99.999Click on Change.Click on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Buy 20 AED of two products and get a special fixed price for product AClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 5Create additional line with Material FG0512 with Order Quantity 5.Note Net Value of each line item must exceed 20 AEDPress Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type OCT3 for the material FG0511. | OPPS is triggered and fixed price is applied to the sales order.Special Price is applied for all items of FG0511.Note A special fixed price of 20 AED for all items of product FG0511 is applied in case 20 AED of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

### Promotion Rule - Combined

#### Promotion Rule – “Free Item Alpha – Combined”

##### Maintain Promotion Rule - “Free Item Alpha - Combined”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Alpha - Combined” is defined in OPPS. This promotion rule adds one Free Item TG0501 in case [2;5] pieces of two different products (FG0511 and FG0512) are added to the Sales Order or adds two Free Item TG0501 in case [6;∞) pieces of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item Alpha - CombinedDescription: Free Item Promotion Rules CombinedStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Alpha – Combined Rule 1>Sequence: e. g. 1Resolution: e. g. 0Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Quantity (QUT)Mixing Forbidden: YesThreshold Quantity: 2Limit Quantity: 5Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Quantity (QUT)Mixing Forbidden: YesThreshold Quantity: 2Limit Quantity: 5Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 1Unit of Measure: PCClick on Save.Go back to the Promotion screen.On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Alpha – Combined Rule 2>Sequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Quantity (QUT)Mixing Forbidden: YesThreshold Quantity: 6Limit Quantity: 99,999.000Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Quantity (QUT)Mixing Forbidden: YesThreshold Quantity: 6Limit Quantity: 99,9999.000Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 2Unit of Measure: PCClick on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Free Item Promotion Rules CombinedClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview tab and enter the following data:Material: FG0511Order Quantity: 3 or 6Create additional line with Material FG0512 with Order Quantity 3 or 6.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type D100 for the material TG0501. | OPPS is triggered. All free goods items of material TG0501 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 is displayed.Note One Free Item TG0501 is added in case [2;5] pieces of two different products (FG0511 and FG0512) are added to the Sales Order or two Free Item TG0501 are added in case [6;∞) pieces of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

#### Promotion Rule – “Free Item Beta – Combined”

##### Maintain Promotion Rule - “Free Item Beta - Combined”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the promotion rule “Free Item Beta - Combined” is defined in OPPS. This promotion rule adds one Free Item TG0501 in case [300 AED;599,99 AED] of two different products (FG0511 and FG0512) are added to the Sales Order or adds two Free Item TG0501 in case [600 AED;∞) of two different products (FG0511 and FG0512) are added to the Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP OPPS launchpad as a Promotion Planner. | The SAP OPPS launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Promotions app. | The Maintain Promotions screen is displayed. |  |
| 3 | Select Create | Click on Create. | The Promotion screen is displayed. |  |
| 4 | Enter General Information | On the Promotion screen maintain the following entries:Promotion Name: Free Item Beta - CombinedDescription: Free Item Value Promotion Rules CombinedStart Date: <today>End Date: <end of this year>Master Data Source System: <system for data source>Distribution Chain: 3310\|10Click on Create. | The Promotional Rules, Merchandise Sets, Business Units and Promotional Texts tabs appear. |  |
| 5 | Create Promotional Rules | On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Beta – Combined Rule 1>Sequence: e. g. 1Resolution: e. g. 0Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Amount (AMT)Threshold Amount: 300Mixing Forbidden: YesLimit Amount: 599,99Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Amount (AMT)Threshold Amount: 300Mixing Forbidden: YesLimit Amount: 599,99Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 1Unit of Measure: PCClick on Save.Go back to the Promotion screen.On the Promotion screen select Create in the Promotional Rules subscreen.Enter data as outlined below:Rule Name: <Free Item Beta – Combined Rule 2>Sequence: e. g. 1Resolution: e. g. 1Sales and Returns Type: For Sales OnlyClick on Create.In the Maintain Promotions screen click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0511Threshold Type: Amount (AMT)Threshold Amount: 600Mixing Forbidden: YesLimit Amount: 99,999Unit of Measure: PCClick on Save.Click on Edit.In the Drop Down Add Eligibility select Product.Enter the following data in the Product subscreen:Product ID: FG0512Threshold Type: Amount (AMT)Threshold Amount: 600Mixing Forbidden: YesLimit Amount: 99,9999Unit of Measure: PCCheck if switch is switched to AND.In the Drop Down Add Reward, select Additional Bonus > Product .Enter the following data in the Product subscreen:Product ID: TG0501Quantity: 2Unit of Measure: PCClick on Save.Go back to the Promotion screen. | The Promotional Rule is created. |  |
| 6 | Create Business Units | In the Promotion screen click on Create in the Business Units subscreen.In the Add Business Units pop-up window enter the following data:Business Unit Type: CustomerBusiness Unit ID: 33105006Click on Add button. | The Business Units are created. |  |
| 7 | Create Promotional Texts (optional) | In the Promotion screen, click on Create in the Promotional Texts subscreen.In the New Promotional Text pop-up window enter the following data:Language Code: EnglishDescription: Free Item Value Promotion Rules CombinedClick on Add button. | The Promotional Text is created. |  |
| 8 | Activate Promotion Rule | In the Promotion screen click on Activate. | The Promotion Rule is activated. |  |

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order to trigger omnichannel promotional pricing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Note For creating a Sales Order alternatively the app Manage Sales Orders - Version 2 (F3893) can be used. OPPS is triggered when saving the Sales Order. | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Order Details | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105006Ship-To Party: 33105006Cust. Reference: <Reference number>Incoterms: DAPCust. Ref. Date: <today>Go-to Item Overview TabMaterial: FG0511Order Quantity: 2 or 10Create additional line with Material FG0512 with Order Quantity 2 or 10.Note Adjust the Order quantity so the net Value of each line item exceeds 300 AED or 600 AED.Press Enter. | Material FG0511 and FG0512 are added to the Sales Order. |  |
| 6 | Maintain Cross-item pricing date | Select Display header details, choose Sales tab and maintain the following data in Pricing and Statistics section:CrItm.Prc Date: <end date of promotion>Choose Back. | Cross-item pricing date maintained. |  |
| 7 | Trigger OPPS | To trigger omnichannel sales promotions:Select Menu > Edit > Additional Functions > Omnichannel Sales Promotions .To check if omnichannel sales promotions are applied:Navigate back to the Create Standard Order: Overview screen.Choose Select All icon and navigate to Menu > Goto > Item > Conditions .Check the Amount / Condition Value of Condition Type D100 for the material TG0501. | OPPS is triggered. All free goods items of material TG0501 are added to the Sales Order.In the Condition Value column a 100% discount for the Free Goods item TG0501 is displayed.Note One Free Item TG0501 is added in case [300 AED;599,99 AED] of two different products (FG0511 and FG0512) are added to the Sales Order or two Free Items TG0501 are added in case [600 AED;∞) of two different products (FG0511 and FG0512) are added to the Sales Order. |  |
| 8 | Save | Choose Create. Make a note of the sales order number. | Sales order with customer 33105006 is created. |  |

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
> Flagged while digesting this document, not verified: Role naming is inconsistent inside the document: the Overview Table lists 'Configuration Specialist' as the business role for Maintain Promotion Rule steps, while the Roles prerequisite table and the step instructions use 'Promotion Planner' (Maintain_OPPS_Promotions); 'Configuration Specialist' (used for OPPS number ranges, configurations and identifier formats) is not defined in the Roles table.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/omnichannel-sales-promotions-for-sales-orders-in-retail-7z6-ae-test-sc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7T7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 112,667 chars in the whole document
