---
id: 08-sales-order-management/test-script-advanced-available-to-promise-consumer-products-6n0-ae-117
title: "Test Script: Advanced Available-to-Promise - Consumer Products (6N0_AE) (6N0_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 6N0 (aATP, Alternative-Based Confirmation, Supply Protection), AE localization, dated 19-06-26."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/availability-check-atp]
aliases: [6N0_S4CLD2608_BPD_EN_AE]
keywords: [Available-to-Promise and Backorder Processing, advanced available-to-promise, alternative-based confirmation, supply protection, substitution strategy, product substitution, storage location substitution, sales order availability check, product allocation, alternative control]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N0_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1178
topic: 08-sales-order-management/availability-check-atp
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Advanced Available-to-Promise - Consumer Products (6N0_AE) (6N0_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N0_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Available-to-Promise and Backorder Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Available-to-Promise – Consumer Products (6N0_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858695)

[2 Prerequisites 4](#_Toc232858696)

[2.1 System Access 4](#_Toc232858697)

[2.2 Roles 4](#_Toc232858698)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232858699)

[2.4 Business Conditions 7](#_Toc232858700)

[2.5 Preliminary Steps 7](#_Toc232858701)

[2.5.1 Set Initial Stock for Material 7](#_Toc232858702)

[2.5.2 Self-Service Configuration to Activate Product Allocation (PAL) 9](#_Toc232858703)

[2.5.3 Self-Service Configuration to Activate Alternative-Based Confirmation (ABC) 11](#_Toc232858704)

[2.5.4 Self-Service Configuration to Activate Supply Protection (SUP) 12](#_Toc232858705)

[3 Overview Table 16](#_Toc232858706)

[4 Test Procedures 18](#_Toc232858707)

[4.1 Manage Characteristic Combinations 18](#_Toc232858708)

[4.2 Configure Alternative Determination (Optional) 19](#_Toc232858709)

[4.3 Configure Substitution Strategy 20](#_Toc232858710)

[4.4 Configure Alternative Control 21](#_Toc232858711)

[4.5 Create Reason for Storage Location Substitution (Optional) 23](#_Toc232858712)

[4.6 Create Storage Location Substitution 24](#_Toc232858713)

[4.7 Create Reason for Product Substitution (Optional) 25](#_Toc232858714)

[4.8 Create Product Substitution 26](#_Toc232858715)

[4.9 Configure Supply Protection (SUP) Characteristics (Optional) 28](#_Toc232858716)

[4.10 Create Master Data for Supply Protection (SUP) 29](#_Toc232858717)

[4.11 Check Availability in Sales Order 31](#_Toc232858718)

[4.11.1 Sales Order before Jubilee Period 31](#_Toc232858719)

[4.11.2 Sales Order during Jubilee Period 33](#_Toc232858720)

[4.11.3 Large Sales Order during Jubilee Period 35](#_Toc232858721)

[4.11.4 Large Sales Order during Jubilee Period with SUP 36](#_Toc232858722)

## Purpose

Overview

The scope item outlines the process for configuring and checking availability in several key areas. It allows you to replace the original requirement in an order document with a default storage location using Alternative-Based Confirmation (ABC). This feature is particularly useful when substituting a product for a specific period, such as during a company's jubilee celebration with a limited edition product. Once the limited edition stock is depleted, the remaining quantity will be fulfilled with the originally requested product using ABC.

Furthermore, you can optimize product availability during order creation and modification by prioritizing incoming demand through Supply Protection (SUP).

This scope item builds upon the capabilities provided by Basic Available-to-Promise Processing (2LN).

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

For more information, refer to How to Create a Business Role for the Administrator in the product assistance for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | Role (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP |  |
| Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR | Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new material master data set to be created and the needed master data objects are mentioned below:

Table 1: Material Master Data:

| Data | Sample Value | Description | Other Attribute |
| --- | --- | --- | --- |
| Material | TG0502 | Drinking Glass 250ml | Trading Good (No serial number, no batch) |
| Material | TG0503 | Drinking Glass 250ml - Jubilee Ed | Trading Good (No serial number, no batch) |

Table 2: Organization Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost Center | 33101301 | Manufacturing 1 (AE) |  |

Table 3: Customer:

| Master Data | Value | Master Data details | Comments |
| --- | --- | --- | --- |
| Sold-to party | 33105001 | Domestic CP Customer 01 |  |
| Ship-to party | 33105001 | Domestic CP Customer 01 |  |
| Sold-to party | 33105002 | Domestic CP Customer 02 |  |
| Ship-to party | 33105002 | Domestic CP Customer 02 |  |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Company Code | 3310 | Company Code 3310 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 4: Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays.Note It only displays this way if it was your last transaction. So, the action for the user should be to select Reference Document for MIGO Transaction > Other. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Trans/Event: Goods ReceiptReference Document: Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : TG0502 |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 3000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: 3310Storage Location: 331A |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |
| 9 | Repeat all steps from above | Use Material: TG0503 |  |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&Fin Bal |

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

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| [Manage Characteristic Combinations](#unique_12) [page ] 18 | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | Open Manage Characteristic Combinations (F5303). | The Characteristic Combination screen is displayed. |
| [Configure Alternative Determination (Optional)](#unique_13) [page ] 19 | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | Open Configure Alternative Determination (F5354). | The screen Configure Substitution Strategy displays. |
| [Configure Substitution Strategy](#unique_14) [page ] 20 | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | Open Configure Substitution Strategy (F2699). | The screen Configure Substitution Strategy displays. |
| [Configure Alternative Control](#unique_15) [page ] 21 | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | Open Configure Alternative Control (F2698). | The Configure Alternative Control screen displays. |
| [Create Reason for Storage Location Substitution (Optional)](#unique_16) [page ] 23 | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | Open Manage Substitution Reasons - Locations (F5313). | The Manage Substitution Reasons - Locations screen is displayed. |
| [Create Storage Location Substitution](#unique_17) [page ] 24 | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | Open Manage Substitutions - Locations (F5314). | The Manage Substitutions - Location screen displays. |
| [Create Reason for Product Substitution (Optional)](#unique_18) [page ] 25 | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | Open Manage Substitution Reasons - Products (F4789). | The Manage Substitution Reasons - Products screen is displayed. |
| [Create Product Substitution](#unique_19) [page ] 26 | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | Open Manage Substitutions - Products (F4785). | The Manage Substitutions - Products screen displays. |
| [Configure Supply Protection (SUP) Characteristics (Optional)](#unique_20) [page ] 28 | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | Open Manage Characteristic Catalogs (F3829). | The screen Manage Charateristic Catalogs displays. |
| [Create Master Data for Supply Protection (SUP)](#unique_21) [page ] 29 | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | Open Manage Supply Protection (F4569). | The Manage Supply Protection screen displays. |
| Check Availability in Sales Order |  |  |  |
| [Sales Order before Jubilee Period](#unique_22) [page ] 31 | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |
| [Sales Order during Jubilee Period](#unique_23) [page ] 33 | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |
| [Large Sales Order during Jubilee Period](#unique_24) [page ] 35 | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |
| [Large Sales Order during Jubilee Period with SUP](#unique_25) [page ] 36 | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Characteristic Combinations

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

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Characteristic Combinations (F5303). | The Manage Characteristic Combinations screen is displayed. |  |
| 3 | Choose Create | In the Manage Characteristic Combinations view, choose Create. | The Characteristic Combination screen is displayed. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Combination: <Enter the Combination Name>Combination Description: <Enter the Description of the Combination>Usage: <Alternative-Based Confirmation>Catalog Type: <Base (Sales Document)>For the usage 'Alternative-Based Confirmation', the catalog type is "Base (Sales Document)".Combination, Usage and Catalog Type are mandatory to create a substitution. |  |  |
| 5 | Assign Characteristics | In the Characteristics section, the Characteristic can be assigned by clicking on Assign:On the Select Characteristics dialog box that displays, choose Expand All, select Sales Organization and Material Number.Choose Assign.The Navigation Up arrow and Down arrow button can be used to set the order of the Characteristics. |  |  |
| 6 | Save Your Data | Choose Create. | System message shows that Combination is Created. |  |

### Configure Alternative Determination (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to decide which substitutes are to be used to confirm requests. It states how available alternatives are to be prioritized.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Alternative Determination (F5354). | The screen Configure Alternative Determination displays. |  |
| 3 | Create a New Determination | Choose Create from Template, select from the following pre-configured determinations and choose Continue:Alternative Determination: <On-Time Confirmation>On the New Determination screen, make the following entries and choose Create:Determination Name: <On-Time Confirmation>Determination Description: <On-Time Confirmation> | The determination is saved. |  |

### Configure Substitution Strategy

Purpose

This process step shows you how to configure a substitution strategy in which you define a substitution method and a determination rule.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Substitution Strategy (F2699). | The screen Configure Substitution Strategy displays. |  |
| 3 | Create a New Strategy | To Create a new strategy, choose Create and make the following entries:Strategy Name: <your strategy name>Strategy Description:<your strategy description>Substitution Item Type: (Recommended value) Force Subitem GenerationTwo item types can be selected (Force Inline Substitution item type isn't valid for Storage Location and Product Substitution):Force Subitem Generation: The requested data for the original requested item is always stored as a main item. Subitems are always generated for the confirmed data. If requirements are substituted, several subitems may be created for one main item. For each confirmation of a plant, product, and storage location, at least one corresponding subitem is generated. A subitem is also generated when the original request is confirmed fully without using substitutes.Allow Inline Substitution and Subitem Generation: The system chooses the optimal solution based on stock availability in the potentially relevant delivering plants: if a single delivering plant can confirm the requested product, inline substitution is possible and is used; Otherwise, subitems are generated, which states the new plant or storage location and the product or substitute product used to confirm the requirement, as well as the confirmed delivery date and quantity.Consider Alternatives: AlwaysRemaining Open Quantity Assignment: Leading SubstitutionSubstitution Methods: <Storage Location Substitution> and <Product Substitution>You can also add another method.Note To define master data for product substitution, you can refer to master data script 4VO- Create Product Substitution.Alternative Determination: (On-Time Confirmation or The alternative determination created in the previous test step.) | The Strategy Definition screen displays. |  |
| 4 | Assign Master Data for Substitution | For product substitution click on the right most chevron on the line. | Detail screen for this Substitution Method displays. |  |
| 5 | Set Substitution Method Source | In field Substitution Method Source select <Substitution Master Data> from the value list.Choose Apply. | The Strategy Definition screen displays. |  |
| 6 | Save Your Strategy | Choose Create. | The strategy is saved. |  |

### Configure Alternative Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an alternative control in which you can activate substitution strategy for a specific sales organization and material.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Configure Alternative Control (F2698). | The Configure Alternative Control screen displays. |  |
| 3 | Create Access | Enter the following details in the pop up and Click on Create Combination : Choose the Combination displayed in the F4 help for combination (combination created in the previous step can be used).Status: Active | The user is navigated to the details screen of the Access. |  |
| 4 | Add Characteristic Value Combination | Choose Add, a new row is added and defaulted with *.Change the characteristic values with the following entries:Sales Organization: 3310Material Number: TG0502Substitution Strategy: <Your Previously Created Strategy> Enter a strategy in the Strategy field using F4 (Strategy created in the previous step can be used)Execute ABC: Yes | The Alternative Control / Access is Saved. | Note The Characteristics displayed depends on the Combination selected during Access creation. |
| 5 | Add new row | Choose Add. | A new row is added and defaulted with *. |  |
| 6 | Add Characteristic Value Combination | Change the characteristic values with the following entries:Sales Organization: 3310Material Number: TG0503Substitution Strategy: <Your Previously Created Strategy> Enter a strategy in the Strategy field using F4 (Strategy created in the previous step can be used).Execute ABC: Yes | The Alternative Control / Access is Saved. |  |
| 7 | Create the Access | Choose Create. | The access is created. |  |

### Create Reason for Storage Location Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating reason for storage location substitution/exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Reasons - Locations (F5313). | The Manage Substitution Reasons - Locations screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Reasons - Locations screen, choose Create. | The Reason screen is displayed. |  |
| 4 | Enter Reason | In the Header section, make the following entry.Location Type: <Storage Location>Reason: <Enter the new Reason code for Storage Location substitution, for example, NEW_SLOC> |  |  |
| 5 | Create Your Data | Choose Create. | System message shows Reason is created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Reason Description screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for reason, for example, EN English>Reason Description: <Enter text to describe the reason, for example, New storage location is available> |  |  |
| 8 | Create Your Data | Choose Create. | System message shows Description Created. |  |

### Create Storage Location Substitution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Storage Location Substitution, that permanently sets this storage location as delivery location into the sales order. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitutions - Locations (F5314). | The Manage Substitutions - Location screen displays. |  |
| 3 | Choose Storage Location | On the Manage Substitutions screen, choose the Storage Location tab. | The Manage Substitutions - Locations (Storage Location) screen is displayed. |  |
| 4 | Choose Create | In the Storage Location tab, choose Create. | The Manage Substitutions - Locations flexible column layout with create screen is displayed. |  |
| 5 | Enter Header Data | In the Header section, make the following entries:Plant: 3310Storage Location: <Leave Empty>Substitute Storage Location: 331APlant and Substitute Storage Location data are mandatory to create a substutition while Storage Location is optional. Plant is selected by default when Storage Location is selected. |  |  |
| 6 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for creating substitute. Example NEW_SLOC>Valid From Date:<Leave Empty>Valid From Time:<Leave Empty>Valid To Date:<Leave Empty>Valid To Time:<Leave Empty>Time Zone:<Leave Empty>Lead Indicator:<Check>The above entries are optional. | . |  |
| 7 | Create Your Data | Choose Create. | System message shows Substitution Created. |  |
| 8 | Activate Storage Location Substitution Data | Choose Choose Set to Active. | System message shows Status Changed. |  |

### Create Reason for Product Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create Reason for Product substitution/exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Reasons - Products (F4789). | The Manage Substitution Reasons - Products screen displays. |  |
| 3 | Choose Create | On the Manage Substitution Reasons - Products screen, choose Create. | The Reason screen displays. |  |
| 4 | Enter Reason | In the Header section, make the following entry:Reason: <Enter the new Reason code for substitution, for example, Upgrade> |  |  |
| 5 | Save Your Data | Choose Create. | System message displays that Object is saved. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Reason Description screen displays. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter language key applicable for the Reason, for example, EN for English>Reason Description: <Enter text to describe the Reason, for example, Applicable for Products undergoing upgrades> |  |  |
| 8 | Save Your Data | Choose Create. | System message displays that Description created. |  |
| 9 | Create Reason | Repeat Steps 3-8 with the following data:Reason: <Enter the new Reason code for substitution, for example, Jubilee>Reason Description: <Enter text to describe the Reason, for example, Applicable for Products undergoing Jubilee> | New reason is created. |  |

### Create Product Substitution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Product Substitution. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitutions - Products (F4785). | The Manage Substitutions - Products screen displays. |  |
| 3 | Choose Create | In the Manage Substitutions - Products view, choose Create. | The Manage Substitutions - Products flexible column layout with create screen is displayed. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Product: <TG0502>Substitute Product: <TG0503>Plant: 3310Product and Substitute Product data is mandatory to create a substitution. |  |  |
| 5 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for creating substitute. Example Jubilee>Valid From Date: <First of the month after next month>Valid From Time:<Empty>Valid To Date: <Last of the month after next month>Valid To Time: <Empty>Time Zone: <UTC>Sequence: <-10> |  |  |
| 6 | Save Your Data | Choose Create. | System message shows that Substitution created. |  |
| 7 | Activate Product Substitution Data | Choose Set to Active. | System message shows that Status changed. |  |
| 8 | Choose Create | Go back to the substitution overview screen.Choose Create. | The Manage Substitutions - Products flexible column layout with create screen is displayed. |  |
| 9 | Enter Header Data | In the Header section, make the following entries:Product: <TG0503>Substitute Product: <TG0502>Plant: 3310Product and Substitute Product data is mandatory to create a substitution. |  |  |
| 10 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for creating substitute. Example Upgrade>Valid From Date: <Empty>Valid From Time: <Empty>Valid To Date: <Empty>Valid To Time: <Empty>Time Zone: <Empty>Lead Indicator:<check>Sequence: <-5> |  |  |
| 11 | Save Your Data | Choose Create. | System message shows that Substitution created. |  |
| 12 | Activate Product Substitution Data | Choose Set to Active. | System message shows that Status changed. |  |

### Configure Supply Protection (SUP) Characteristics (Optional)

Purpose

The following procedure provides instructions for creating Product Substitution. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Characteristic Catalogs (F3829). | The screen Manage Charateristic Catalogs displays. |  |
| 3 | Open the Catalog | On the Manage Characteristic Catalogs screen, find the catalog using the below filter criteria and choose the entry:Catalog Use Type: <Supply Protection>Catalog Type: <Base (Sales Document)> | The Characteristic Catalog screen displays. |  |
| 4 | Add the characteristic | On the Characteristic Catalog screen, choose EditOn the Characteristics tab, choose Add. On the Select Characteristics pop-up screen, choose Customer Number by expanding the folder Business Partners and then expanding the folder Sold-to Party.Choose Ok. | The characteristic Sold-to Party - Customer Number is added to the catalog. |  |
| 5 | Adjust Existence Check Type | On the characteristic entry Sold-to Party - Customer Number, setValue existence check type: <No Existence Check>Choose Save. | System message displayed Catalog is saved. | If you want to set an existence check for this characteristic, please ensure that the Order Fulfillment manager role has authorization to find/read business partners. |

### Create Master Data for Supply Protection (SUP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create master data for supply protection in which you can protect quantities of a material of a specific plant for other demands.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Supply Protection (F4569). | The Manage Supply Protection screen displays. |  |
| 3 | Define General Information | In the Manage Supply Protection screen, choose Create for the new supply protection object.On the General Information tab,enter the followingName: <Protection Object for TG0503>Material: <TG0503>Plant: 3310Choose the checkbox of Sales Document for Planning Context. |  |  |
| 4 | Define Core Protection | On the Core Protection tab, in the Core characteristics area, enter the following:Characteristic 1: <Sales Organization>Value 1: 3310Characteristic 2: <Sold-to Party – Customer Number>Value 2: 33105001In the Planning Horizon tab, enter the following:Planned Period Type: <One Period>Planning Start Date: <Start date of the Jubilee edition>Planning End Date: <End date of the Jubilee Edition>Choose Create. | System displays message - Object was created. Other entries are available for further definition. | If you have set an existence check for Sold to party – Customer Number characteristic, please ensure that the Order Fulfillment manager role has authorization to find/read business partners. |
| 5 | Edit Supply Protection | On the Supply Protection screen, choose Edit. | The supply protection object can be edited. |  |
| 6 | Define Protection Group | On the Protection Groups tab, choose Create. A new row displays:Enter Priority: 1Enter specific quantity for time buckets, for example, <500>, then choose Save. | The protection group with time buckets is saved. |  |
| 7 | Activate Supply Protection | On the Supply Protection screen, choose Activate. | The supply protection object is activated now. |  |

### Check Availability in Sales Order

#### Sales Order before Jubilee Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you will create a sales order to be delivered BEFORE the jubilee period starts.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen choose Create, then select Create Sales Orders - VA01. |  |  |
| 4 | Enter Order Details | On the Create Sales Document screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Enter:Sold-To Party: 33105001Ship-To Party: 33105001Customer Reference: <Reference number>Enter a customer purchase order number as reference.Customer Reference Date: <today>On Sales tab:Requested Delivery Date: <Enter a requested delivery date that considers sufficient buffer for the earliest possible delivery date as per the shipping times.>Goto Item Overview tab:Product: <TG0502>Order Quantity: <100> | An ATP check is carried out and will include ABC.In general, ABC is executed based on the originally requested material/plant combination. Based on the substitution strategy, together with the order line for TG0502 there is a sub item for TG0502.In the shipping data of the sub item you see the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA. |  |
| 6 | Choose Delivery Proposal | On the Review Availability Check Result screen, you can choose Apply to directly confirm the delivery proposal. You can also choose the item for which you want to finetune/optimize confirmations. | In general, ABC is executed based on the originally requested material/plant combination. |  |
| 7 | Storage Location and Product Substitution | If storage location substitution is configured in substitution strategy in the prerequisite step, storage location substitution is executed. And based on the substitution item type in substitution strategy, there could be different behavior in sales order.Substitution item type: Force Subitem Generation (S)Item category is changed to TAPA for main item 10.A new line item with item category TAN is created, and storage location is substituted to 331A.Substitution item type: Allow both Inline Substitution and Subitem Generation (B)Depends on the stock situation:If a single delivering plant and storge location can confirm the requested product, inline substitution is possible and is used. Otherwise, subitems are generated and state the new storage location and the product or substitute product used to confirm the requirement, as well as the confirmed delivery date and quantity. | Based on the substitution strategy, together with the order line for TG0502 there is a sub item for TG0502. In the shipping data of the sub item you see the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA. |  |

#### Sales Order during Jubilee Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you will create a sales order to be delivered DURING the jubilee period. The order quantity should be lower than the stock created by you.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen choose Create, then select Create Sales Orders - VA01. |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Initial screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Enter:Sold-To Party: 33105001Ship-To Party: 33105001Customer Reference: <Reference number>Enter a customer purchase order number as reference.Customer Reference Date: <today>On Sales tab:Requested Delivery Date: <any day in Jubilee period>Goto Item Overview tab:Product: <TG0502>Order Quantity: <100> | An ATP check is carried out and will include ABC.In general, ABC is executed based on the originally requested material/plant combination. Based on the substitution strategy, together with the order line for TG0502 there is a sub item for TG0503.In the shipping data of the sub item you see the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA. |  |
| 6 | Choose Delivery Proposal | On the Review Availability Check Result screen, you can choose Apply to directly confirm the delivery proposal. You can also choose the item for which you want to finetune/optimize confirmations. | In general, ABC is executed based on the originally requested material/plant combination. |  |
| 7 | Storage Location and Product Substitution | If storage location substitution is configured in substitution strategy in the prerequisite step, storage location substitution is executed. And based on the substitution item type in substitution strategy, there could be different behavior in sales order.Substitution item type: Force Subitem Generation (S)Item category is changed to TAPA for main item 10.A new line item with item category TAN is created, and storage location is substituted to 331ASubstitution item type: Allow both In-line Substitution and Subitem Generation (B)Depends on the stock situation:If a single delivering plant and storge location can confirm the requested product, inline substitution is possible and is used. Otherwise, subitems are generated and state the new storage location and the product or substitute product used to confirm the requirement, as well as the confirmed delivery date and quantity. | Storage location is substituted and subitem is generated. Based on the substitution strategy, together with the order line for TG0502 there is a sub item for TG0503. In the shipping data of the sub item you see the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA. |  |

#### Large Sales Order during Jubilee Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you will create a sales order to be delivered DURING the jubilee period. The order quantity is greater than the combined quantities of both products.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen choose Create, then select Create Sales Orders - VA01. |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Initial screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Enter:Sold-To Party: 33105001Ship-To Party: 33105001Customer Reference: <Reference number>Enter a customer purchase order number as reference.Customer Reference Date: <today>On Sales tab:Requested Delivery Date: <any day in Jubilee period>Goto Item Overview tab:Product: <TG0502>Order Quantity: <7000> | An ATP check is carried out and will include ABC.In general, ABC is executed based on the originally requested material/plant combination. Based on the substitution strategy, together with the order line for TG0502 there are 2 sub items generated. The shipping data of each sub item shows the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA.The quantity of the sub item for TG0503 shows a quantity of <3000>, the total available stock for this material. The item is fully ATP-confirmed.The quantity of the sub item for TG0502 shows a quantity of <4000>. The item is partially ATP-confirmed to <3000>. |  |
| 6 | Choose Delivery Proposal | On the Review Availability Check Result screen, you can choose Apply to directly confirm the delivery proposal. You can also choose the item for which you want to finetune/optimize confirmations. | In general, ABC is executed based on the originally requested material/plant combination. |  |
| 7 | Storage Location and Product Substitution | If storage location substitution is configured in substitution strategy in the prerequisite step, storage location substitution is executed. And based on the substitution item type in substitution strategy, there could be different behavior in sales order.Substitution item type: Force Subitem Generation (S)Item category is changed to TAPA for main item 10.A new line item with item category TAN is created, and storage location is substituted to 331ASubstitution item type: Allow both In-line Substitution and Subitem Generation (B)Depends on the stock situation:If a single delivering plant and storge location can confirm the requested product, inline substitution is possible and is used. Otherwise, subitems are generated and state the new storage location and the product or substitute product used to confirm the requirement, as well as the confirmed delivery date and quantity. | Storage location is substituted and subitem is generated.Based on the substitution strategy, together with the order line for TG0502 there are 2 sub items generated. The shipping data of each sub item shows the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA.The quantity of the sub item for TG0503 shows a quantity of <3000>, the total available stock for this material. The item is fully ATP-confirmed.The quantity of the sub item for TG0502 shows a quantity of <4000>. The item is partially ATP-confirmed to <3000>. |  |

#### Large Sales Order during Jubilee Period with SUP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you will create a sales order to be delivered DURING the jubilee period. The order quantity is greater than the combined quantities of both products. As there is a supply protection for a different customer, he should not get the complete available stock of the jubilee material.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen choose Create, then select Create Sales Orders - VA01. |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Initial screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Enter:Sold-To Party: 33105002Ship-To Party: 33105002Customer Reference: <Reference number>Enter a customer purchase order number as reference.Customer Reference Date: <today>On Sales tab:Requested Delivery Date: <any day in Jubilee period>Goto Item Overview tab:Product: <TG0502>Order Quantity: <7000> | An ATP check including supply protection is carried out. Only stock which is not restricted can be confirmed.In general, ABC is executed based on the originally requested material/plant combination. Based on the substitution strategy, together with the order line for TG0502 there are 2 sub items generated. The shipping data of each sub item shows the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA.The quantity of the sub item for TG0503 shows a quantity of <2500>, the total available stock for this material. The item is fully ATP-confirmed.The quantity of the sub item for TG0502 shows a quantity of <4500>. The item is partially ATP-confirmed to <3000>. |  |
| 6 | Choose Delivery Proposal | On the Review Availability Check Result screen, you can choose Apply to directly confirm the delivery proposal. You can also choose the item for which you want to finetune/optimize confirmations. | In general, ABC is executed based on the originally requested material/plant combination. |  |
| 7 | Storage Location and Product Substitution | If storage location substitution is configured in substitution strategy in the prerequisite step, storage location substitution is executed. And based on the substitution item type in substitution strategy, there could be different behavior in sales order.Substitution item type: Force Subitem Generation (S)Item category is changed to TAPA for main item 10.A new line item with item category TAN is created, and storage location is substituted to 331ASubstitution item type: Allow both In-line Substitution and Subitem Generation (B)Depends on the stock situation:If a single delivering plant and storge location can confirm the requested product, inline substitution is possible and is used. Otherwise, subitems are generated and state the new storage location and the product or substitute product used to confirm the requirement, as well as the confirmed delivery date and quantity. | Storage location is substituted and subitem is generated. Based on the substitution strategy, together with the order line for TG0502 there are 2 sub items generated. The shipping data of each sub item shows the storage location is set to 331A, the value chosen in the location substitution. Item category of the main item is changed to TAPA.The quantity of the sub item for TG0503 shows a quantity of <2500>, the total available stock for this material minus the stock protection for another customer. The Item is fully ATP-confirmed.The quantity of the sub item for TG0502 shows a quantity of <4500>. The item is partially ATP-confirmed to <3000>. |  |

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
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-advanced-available-to-pro]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N0_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 65,657 chars in the whole document
