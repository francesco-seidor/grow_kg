---
id: 14-maintenance-service-and-projects/solution-order-advanced-product-bundling-6bu-ae-1163
title: Solution Order – Advanced Product Bundling (6BU_AE) (6BU_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud test script for scope item 6BU_AE: prerequisites, roles, sample data and steps to create, configure and release a solution order bundle."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [6BU_S4CLD2608_BPD_EN_AE]
keywords: [Solution Orders and SAP CPQ Quotations, solution bundles, solution order management, test scripts, solution order creation, bundle configuration, bundle release, header discounts, bundle specific pricing, purchasing info records]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BU_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1163
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Solution Order – Advanced Product Bundling (6BU_AE) (6BU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Solution Order – Advanced Product Bundling (6BU_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Solution Order – Advanced Product Bundling (6BU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858487)

[2 Prerequisite 4](#_Toc232858488)

[2.1 System Access 4](#_Toc232858489)

[2.2 Roles 4](#_Toc232858490)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232858491)

[2.4 Additional Manual Configuration 12](#_Toc232858492)

[2.5 Business Condition 12](#_Toc232858493)

[2.6 Preliminary Steps 13](#_Toc232858494)

[2.6.1 Maintain a Billing Profile 13](#_Toc232858495)

[2.6.2 Create Condition Records (Optional) 14](#_Toc232858496)

[2.6.3 Create Purchasing Info Record - Sales Item for Third-Party with Shipping Notification (CB1) 15](#_Toc232858497)

[2.6.4 Create Purchasing Info Record - Sales Item for Third-Party without Shipping Notification (CB2) 16](#_Toc232858498)

[2.6.5 Create Purchasing Info Record - Bought-In Item (CBAB) 18](#_Toc232858499)

[2.6.6 Maintain Price Conditions for Bundle Specific Price (Optional) 20](#_Toc232858500)

[2.6.7 Set default item category for solution order items (Optional) 21](#_Toc232858501)

[3 Overview Table 23](#_Toc232858502)

[4 Test Procedures 24](#_Toc232858503)

[4.1 Solution Order 24](#_Toc232858504)

[4.1.1 Create Solution Order 24](#_Toc232858505)

[4.1.2 Add Solution Bundle 25](#_Toc232858506)

[4.1.3 Configure Solution Bundle 26](#_Toc232858507)

[4.1.4 Provide Header Discount for Solution Order (Optional) 27](#_Toc232858508)

[4.1.5 Release Solution Bundle 28](#_Toc232858509)

[4.1.6 Execute Solution Order 29](#_Toc232858510)

[4.1.7 Print Solution Order (Optional) 30](#_Toc232858511)

## Purpose

Overview

Solution bundles in Solution Order Management help customers evolve their business from selling single products to offering holistic solutions.

It enables selling different types of products in a single document and provides an overview of the fulfillment through individual follow-up documents.

The solution bundle can include groups of sales, services, subscription products​, and projects. It may also include configurable sales and service products.​ With an intuitive progress view, situation handling, and cross-object navigation, customers always have an overview of the fulfillment status of the different solution order items.

This process can be combined with the solution order management process for configurable products (6HY).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisite

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test should be conducted with the following system:

Note For system details contact your System Administrator.

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Solution Order Specialist | SAP_BR_SOLN_ORDER_SPCLST | Solution Order Management | SAP_BR_SOLN_ORDER_SPCLST | Your system administrator provides the user and password information. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | Your system administrator provides the user and password information. |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST | Your system administrator provides the user and password information. |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC | Your system administrator provides the user and password information. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Your system administrator provides the user and password information. |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT | Your system administrator provides the user and password information. |
| Sales Manager | SAP_BR_SALES_MANAGER |  |  | Your system administrator provides the user and password information. |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT | Your system administrator provides the user and password information. |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | Your system administrator provides the user and password information. |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | Purchasing / Sourcing and Contracting | SAP_BR_PURCHASING_MANAGER | Your system administrator provides the user and password information. |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK | Your system administrator provides the user and password information. |
| Billing Specialist - Projects | SAP_BR_PROJ_BILLG_SPCLST | Project Billing | SAP_BR_PROJ_BILLG_SPCLST | Your system administrator provides the user and password information. |
| Project Manager - Commercial Services | SAP_BR_PROJ_MANAGE_COMM |  |  | Your system administrator provides the user and password information. |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Your system administrator provides the user and password information. |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC | Your system administrator provides the user and password information. |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Sample Value | Details | Comments |
| --- | --- | --- | --- | --- | --- |
| Customer |  |  | 33100001 | Domestic Customer | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure.to check the assignment, use Business Role SAP_BR_BUPA_MASTER_SPECIALIST - tile Manage Customer Master Data in the Sales Area Data. |
| Employee |  |  | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Bundle Product |  |  | SO_BUND_02 | Bundle Product |  |
| Sales Organization |  |  | 3310 | Dom. Sales Org |  |
| Controlling area |  |  | A000 | Controlling Area |  |
| Company code |  |  | 3310 | Company Code |  |
| Plant |  |  | 3310 | Plant |  |
| Material |  |  | TG10 | Sales Product |  |
| Material |  |  | TG11 | Sales Product |  |
| Material |  |  | TG14 | Sales Product |  |
| Material |  |  | TG15 | Sales Product |  |
| Material |  |  | SM0001 | Service Material 01 |  |
| Material |  |  | NS0002 | Non-Stock Material 02 (No MRP planning) |  |
| Material |  |  | SRV_01 | Services Product |  |
| Material |  |  | SRV_02 | Service Expense Item |  |
| Material |  |  | SRV_03 | Service Part (Undefined) |  |
| Material |  |  | SRV_04 | Service Part (Defined) |  |
| Material |  |  | SRV_05 | Service Spare Part |  |
| Material |  |  | SRV_CONTRACT | Service Contract Product |  |
| Material |  |  | SRV_CONTRACT | Service Contract Product |  |
| Material |  |  | PROJECT | Project |  |
| Material |  |  | CAR-WASH_CONF | Service Order Configurable Product |  |
| Material |  |  | SRV_CONTR_CONFIG | Service Contr.Configurable Product |  |
| Material |  |  | CM-FL-V00 | Configurable Forklifter | Single-level structure |
| Material |  |  | CM-MLFL-KM-VXX | Configurable Forklifter | Multi-level structure |
| Material |  |  | SDBOMERLAHD | SD BOM Header ERLA (with Pricing, inventory management) |  |
| Material |  |  | SDBOMLUMFHD | SD BOM Header LUMF(No pricing, no inventory) |  |
| Material |  |  | SDBOMCPFHHD | SD BOM Header CPFH(with pricing, subitems with inventory) |  |
| Material |  |  | RP002 | Sales returnable product |  |
| Characteristic |  |  | AVC_CR_SOLOQTY_VXX | Component Quantity |  |
| Characteristic |  |  | TG10 | TG10 |  |
| Characteristic |  |  | TG11 | TG11 |  |
| Characteristic |  |  | TG14 | TG14 |  |
| Characteristic |  |  | TG15 | TG15 |  |
| Characteristic |  |  | SM0001 | SM0001 |  |
| Characteristic |  |  | NS0002 | NS0002 |  |
| Characteristic |  |  | SRV_01 | SRV_01 |  |
| Characteristic |  |  | SRV_02 | SRV_02 |  |
| Characteristic |  |  | SRV_03 | SRV_03 |  |
| Characteristic |  |  | SRV_04 | SRV_04 |  |
| Characteristic |  |  | SRV_05 | SRV_05 |  |
| Characteristic |  |  | SRV_CONTRACT | SRV_CONTRACT |  |
| Characteristic |  |  | PROJECT | PROJECT |  |
| Characteristic |  |  | CAR-WASH_CONF | CAR-WASH_CONF |  |
| Characteristic |  |  | SRV_CONTR_CONFIG | SRV_CONTR_CONFIG |  |
| Characteristic |  |  | CM-FL-V00 | CM-FL-V00 |  |
| Characteristic |  |  | CM-MLFL-KM-VXX | CM-MLFL-KM-VXX |  |
| Characteristic |  |  | SDBOMERLAHD | SDBOMERLAHD |  |
| Characteristic |  |  | SDBOMLUMFHD | SDBOMLUMFHD |  |
| Characteristic |  |  | RP002 | RP002 |  |
| Class |  |  | SO_BUND_02_C | Solution Bundle | Variant Class (type: 300) |
| Configuration Profile |  |  | SO_BUND_02 |  |  |
| BOM Item |  |  | SO_BUND_02 |  |  |
| Dependency |  |  | AVC_OD_TG10_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_TG11_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_TG13_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_TG14_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SM0001_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_NS0002_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SRV_01_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SRV_02_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SRV_03_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SRV_04_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SRV_05_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SRV_CONTRACT_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_PROJECT_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_ CAR-WASH_CONF_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SRV_CONTR_CONFIG_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SDBOMHDERLA_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_SDBOMHDLUMF_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_CM_FL_V00_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_CM_MLFL_KM_VXX_V00_VXX | Set Quantity |  |
| Dependency |  |  | AVC_OD_RP002_VXX | Set Quantity |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 2T7 | Create Product Master of Type "Configurable Material" |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

| Set-up Instructions | Links |
| --- | --- |
| 4GT | [Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/aeb2022503fd818f451d81421c9186f3) |
| 6HY | [Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/8463ac36c9a9aef9b9f9c5cf6efec22b) |

### Business Condition

Before this test script can be tested, the following business conditions must be met. Ensure the below scope items are activated.

| Scope Item | Business Condition |
| --- | --- |
| 4GT - Solution Order Management | Must be run before this test script. |
| 6HY - Solution Order Management with Advanced Variant Configuration | Must be run before this test script. |
| 22T - Set Up Configurable Model Using Variant Configuration | To model and simulate configurable materials, this scope item must be activated. |

### Preliminary Steps

#### Maintain a Billing Profile

Purpose

This step allows you to add a billing profile, and to define material determination based on the criteria according to your needs.

Prerequisites

Make sure the corresponding materials, activity types, and G/L accounts are created before maintaining materials determination.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Filter Out SSCUI | Choose Configure Your Solution.Select Enterprise Portfolio & Project Management from the Application Area dropdown list; select Billing from the Sub Application Area dropdown list. |  |  |
| 4 | Maintain the Billing Profile | Choose the Billing Profile item in the All Items table.On the Configure Your Solution – Billing Profile screen, choose the Configuration Steps tab. For Maintain Billing Profile, choose Configure. For more details, choose the dropdown arrow of the Configure button, and select Configuration Help.Note Configuring the billing profile, materials determination, and the criteria is mandatory to the new project billing process. | The Configure Your Solution – Billing Profile screen displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Billing Profile.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Note Configuring the billing profile, materials determination, and the criteria is mandatory to the new project billing process. | The Configure Your Solution – Billing Profile screen displays. |  |

#### Create Condition Records (Optional)

Purpose

In case you have fine tuned the access sequence of SAP pre-shipped condition types, the relative condition records need to be created accordingly. This process step shows you how to create condition records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111) app. | The Manage Prices - Sales screen displays. |  |
| 3 | Change Sales Price | Select PSP0 from the Condition Type dropdown list and press Enter.To create a new condition record, choose Create and enter the following entries:Condition Type: PSP0Condition Table: 305 {Customer/material with release Status}Customer: 10100001Sales Organization: 3310Distribution Channel : 10Product: for example, T001Valid From: <Jan 1st of last year>Condition Amount or Ratio: for example, 100.00 EURPricing Unit: for example, 1 HourChoose Save. |  |  |

#### Create Purchasing Info Record - Sales Item for Third-Party with Shipping Notification (CB1)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a purchase info record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Initial screen displays. |  |
| 3 | Enter Data | Make the following entries:Supplier: 33300001/ 33300002Material: TG10Purchasing Organization: 3310Plant: 3310And Choose Enter | The Create Info Record: General Data screen displays. |  |
| 4 | Navigate to Purch. Org. Data 1 | Choose Purch. Org. Data 1. |  |  |
| 5 | Enter Purchasing Data | Make the following entries:Delivery Time in Days: 2 DaysPurchasing Group: 001Standard Quantity: 10Tol. Underdl: 10Tol. Overdl: 10Tax Code: <Input Tax Code>Net Price: 12.35Incoterm: EXWIncoterm Location 1:VENDOR | Purchasing Data is added. |  |
| 5 | Save Your Data | Choose Save. | A purchasing info record is saved. |  |

#### Create Purchasing Info Record - Sales Item for Third-Party without Shipping Notification (CB2)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Purchase Info Record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad displays. |  |
| 3 | Open Create Purchasing Info Records | Choose the Create Purchasing Info Record (ME11). | The Create Info Record: Initial Screen displays. |  |
| 4 | Enter Data | Make the following entries:Supplier: 33300001 / 33300002Material: TG13Purchasing Organization: 3310Plant: 3310And press Enter. | The Create Info Record: General Data screen displays. |  |
| 5 | EnterPurchasing Data | Choose Purch. Org. Data 1, then make the following entries:Delivery Time in Days: 2 DaysPurchasing Group: 001Standard Quantity: 10Tol. Underdl. 10Tol. Overdl: 10Tax Code: <Input Tax Code>TxValidFrm: MM/DD/YYYYNote When TDT is active for country of company code and Tax Code is given, the Tax Valid From field is mandatory. When TXA is active for company code and Tax Code is given, the Tax Country field is mandatory."Net Price: <Net Price>Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 6 | Save your data | Choose Save. | A purchasing info record is saved. |  |

#### Create Purchasing Info Record - Bought-In Item (CBAB)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create purchasing info record.

|  |
| --- |
| Note If the Info Record for the material TG14 and suppliers 33300001 already exists in the system, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Purchasing Info Records | Choose Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Material: TG14Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10%Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: 10Select the following entries:Goods-Receipt-Based Invoice Verification (GR-Bsd_IV)No Evaluated Receipt Settlement (No ERS) | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create. Enter the following data:Valid From: TodayValid To: 12/31/9999Amount: 300Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

|  |
| --- |
| Note Material TG14 and Supplier 33300001, its net price is 35 AED. |

|  |
| --- |
| Note Repeat the above step to create the Info Record for Material TG14 and Supplier 33300001, its purchase group is 001. Repeat the above steps to create the Info Record for Material TG14 , its net price is 25 AED. Repeat the above steps and for step 7, don’t select No Evaluated Receipt Settlement. |

#### Maintain Price Conditions for Bundle Specific Price (Optional)

Purpose

This step show you how to add pricing conditions for bundle specific prices for one-time and recurring priced bundle components. This is needed in case you want to allow different prices for the products if they are sold as part of a solution bundle. The condition types are PSBP for one-time priced products like physical sales products and PSMB for recurring priced products like service contract products.

Prerequisites

Make sure the corresponding materials, activity types, and G/L accounts are created before maintaining materials determination. Make sure that TG11 and SRV_CONTRACT are part of the solution bundle SO_BUND_02

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays |  |
| 2. | Access the App | Open Manage Prices - Sales(F4111). | The Manage Prices – Sales screen displays. |  |
| 3. | Add condition record for PSBP and product TG11 | Choose Create.Make the following entries:Condition Type: PSBPCondition Table: 100Pricing Reference Material of Main Item: SO_BUND_02 <bundle product with item category SOBU>Sales Organization: 1710Distribution Channel: 10Product : TG11Condition Amount: 14.95 USDCondition Description : bundle specific priceOther fields could be adjusted as you need or left as they are.Choose Save. |  |  |
| 4. | Add condition record for PSMB and product SRV_CONTRACT | Choose Create.Make the following entries:Condition Type: PSMBCondition Table: 100Pricing Reference Material of Main Item: SO_BUND_02 <bundle product with item category SOBU>Sales Organization: 1710Distribution Channel: 10Product : SRV_CONTRACTCondition Amount: 80.00 USDCondition Description: bundle specific priceOther fields could be adjusted as you need or left as they are.Choose Save. | The Configure Your Solution – Billing Profile screen displays. |  |
| 5. | Add condition record for PSMB and product SRV_CONTRACT | Choose Create.Make the following entries:Condition Type: PSBPCondition Table: 100Pricing Reference Material of Main Item: SO_BUND_02 <bundle product with item category SOBU>Sales Organization: 1710Distribution Channel: 10Product : SRV_01Condition Amount: 10.00 USDCondition Description: bundle specific priceOther fields could be adjusted as you need or left as they are.Choose Save. | The Configure Your Solution – Billing Profile screen displays. |  |

#### Set default item category for solution order items (Optional)

Purpose

This step show you how to set up the default item category for solution order items in case the standard delivered default item category does not meet your business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays |  |
| 2. | Access the App | Open Manage Your Solutionapp.Click config your solutionApplication area: ServiceSub application area: General SettingOpen select item category determination. | The Item category determination screen displays. |  |
| 3. | Change item category determination | Click Configure to change the item category determination. You can:Change the default item category.Delete the alternative item categories which are not used. | Item category changed successfully. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the project experience in SAP Central Business Configuration. | The Fiori Launchpad is displayed. |  |
|  | Open Change Item Category Determination. Adjust the item category determination if necessary. | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Change Item Category DeterminationChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change Item Category Determination screen is displayed.Item category determination for solution order can be changed. |  |

## Overview Table

This process variant starts with the creation of a solution order.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Solution Order](#unique_17) [page ] 24 | Solution Order Specialist | Manage Solution Order | A solution order has been created |
| [Add Solution Bundle](#unique_18) [page ] 25 | Solution Order Specialist | Manage Solution Order | Solution bundle has been added |
| [Configure Solution Bundle](#unique_19) [page ] 26 | Solution Order Specialist | Manage Solution Order | Solution bundle has been configured |
| [Provide Header Discount for Solution Order (Optional)](#unique_20) [page ] 27 | Solution Order Specialist | Manage Solution Order | Header discount has been provided for the solution order |
| [Release Solution Bundle](#unique_21) [page ] 28 | Solution Order Specialist | Manage Solution Order | Solution bundle has been released |
| [Execute Solution Order](#unique_22) [page ] 29 | Solution Order Specialist | Manage Solution Order | Solution bundle has been executed |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Solution Order

#### Create Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new solution order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose Manage Solution Orders application tile. | The list report page is displayed. |  |
| 3 | Create Solution Order | Choose Create button from the solution order list page | Create Solution Order window will be displayed |  |
| 4 | Maintain Solution Order data | Enter the following data to create a solution order:Description: <your description>External Reference: <your reference>Sold-To Party: 33100003 (Domestic UAE Customer 3)Note: Select the sales organization (3310) and contact person from the popup | Required header data for the Solution order has been maintained. |  |
| 5 | Save the Solution Order | Choose SaveNote down the ID of the Solution Order you have just created. | Solution Order is saved. |  |

#### Add Solution Bundle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to add solution bundle line item to solution order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Order application is displayed. |  |
| 2. | Open Manage Solution Order application | Choose Manage Solution Order application tile. | The list report page is displayed. |  |
| 3. | Find Solution Order | In the search area on the top,enter the ID of your solution order in the ID field.Press the button Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4. | Open Solution Order in Edit mode | Choose the Solution Order and click Edit in the Solution Order Details tab | The edit view of the Solution Order will be opened. |  |
| 5. | Add Solution Bundle Item | Choose Edit List in Items tab,Maintain the following bundle ItemProduct ID: for example, SO_BUND_02Quantity: for example, 1Unit: for example, EAChoose Enter. | The bundle item is now added to Solution Order.(Optional) If bundle price is set for TG11 and TG11 is part of SO_BUND_02 then check if the price is correctly derived. |  |
| 6. | Save the Solution Order | Choose Save | Solution Order is saved |  |

#### Configure Solution Bundle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to configure solution bundle line item in solution orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Order application is displayed. |  |
| 2 | Open Manage Solution Order application | Choose Manage Solution Order application tile. | The list report page is displayed. |  |
| 3 | Find Solution Order | In the search area on the top, enter the ID of your solution order in the ID field.Press the button Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4 | Open Solution Order in the Edit mode | Choose the Solution Order and click Edit in the Solution Order Details tab | The edit view of the Solution Order will be opened. |  |
| 5 | Configure Solution Bundle | In the Actions column, choose Configure Product to navigate to the Solution Order: New - Variant Configuration view in edit mode.Note For Configurable material, refer to the 6HY test script.Choose Done. | The Solution Bundle in configured. |  |

#### Provide Header Discount for Solution Order (Optional)

Purpose

This step describes how to provide header discount for solution order. The discount conditions are inherited to the subcomponents of solution bundle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Order application is displayed. |  |
| 2. | Open Manage Solution Order application | Choose Manage Solution Order application tile. | The list report page is displayed. |  |
| 3. | Find Solution Order | In the search area on the top, enter the ID of your solution order in the ID field.Press the button Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4. | Open Solution Order in the Edit mode | Choose the Solution Order and click Edit in the Solution Order Details tab | The edit view of the Solution Order will be opened. |  |
| 5. | Enter discount conditions in solution order header price details | Scroll down to Price Details section. Click on Add and select DRG1 in the value help.Click on Add and select DRN1 in the value help. | The discount conditions DRG1 and DRN1 added to price details. |  |
| 6. | Enter values for discount conditions | Enter DRG1 = 1% and press Enter.Enter DRN1 = 1 EUR and press Enter.Choose Save. | Check that the Net Value is adjusted accordingly. Check that the DRG1 and DRN1 are also copied into price details of the subcomponents of solution bundle. |  |
| 7. |  |  |  |  |

#### Release Solution Bundle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to configure solution bundle line item in solution order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Order application is displayed. |  |
| 2 | Open Manage Solution Order application | Choose Manage Solution Order application tile. | The list report page is displayed. |  |
| 3 | Find Solution Order | In the search area on the top,enter the ID of your solution order in the ID field.Press the button Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4 | Open Solution Order in the Edit mode | Choose the Solution Order and click Edit in the Solution Order Details tab. | The edit view of the Solution Order will be opened. |  |
| 5 | Release Solution Bundle | In the tab area Items, change the Status for the bundle item to Released.Choose Save.Note It is also possible to release the bundle item with the action Release All Items in the All Items view of the Items tab area. |  |  |

#### Execute Solution Order

For further processes please refer to the following chapters from scope items Solution Order Management (4GT) and Solution Order Management with Advanced Variant Configuration (6HY).

| Processes | Chapter | Scope Item |
| --- | --- | --- |
| For Sales Order | Manage Sales Order | 4GT |
| For Service Order | Manage Service Order | 4GT |
| For Service Contract | Manage Service Contracts | 4GT |
| For Customer Project | Manage Customer Project | 4GT |
| For Sales Order (Configurable Sales item) | Manage Sales Order | 6HY |
| For Service Order (Configurable Service Order item) | Manage Service Order | 6HY |
| For Service Contract (Configurable Service Contract item) | Manage Service Contracts | 6HY |
| For Billing related processes | Manage Billing Document | 4GT |

#### Print Solution Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Solution Order Specialist prints out the solution order or sends it as e-mail to the customers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Order application is displayed. |  |
| 2 | Open Manage Solution Order application | Choose Manage Solution Order application tile. | The list report page is displayed. |  |
| 3 | Find Solution Order | In the search area on the top,enter the ID of your solution order in the ID field.Press the button Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4 | Open Solution Order and navigate to Output Items | Choose the Solution Order and go to Output Items tab | The Output Items for solution order is displayed. |  |
| 5 | Check Output Condition | Select a line with the Channel you want to use.Choose Send Output to print the document or send it via e-mail. | Document is sent to the selected output channel. |  |
| 6 | Display Print Preview | To display the document, in the Display column choose Display Document. Optionally save a local copy of the PDF document. | A PDF document is displayed. |  |

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
> Flagged while digesting this document, not verified: The bought-in info record (CBAB) step enters condition Amount 300 AED, while the following note says the net price for material TG14 and supplier 33300001 is 35 AED (and a repeat at 25 AED).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Master data and order steps use sales organization 3310 and customer 33100001/33100003, but the bundle-specific price condition steps and the PSP0 condition record use sales organization 1710, customer 10100001 and USD/EUR currency, while the AE info record uses AED.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,931 chars in the whole document
