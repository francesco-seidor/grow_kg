---
id: 14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-solution-order-management
title: Test Script SAP S/4HANA Cloud Public Edition - Solution Order Management (4GT_AE) (4GT_S4CLD2608_BPD_EN_AE)
description: "Test script (UAE, release 2608) for scope item 4GT Solution Order Management: prerequisites, roles, test data, and end-to-end steps from solution order to billing, credit memo and returns."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [4GT_S4CLD2608_BPD_EN_AE]
keywords: [Solution Orders and SAP CPQ Quotations, solution order management, solution order creation, solution order release, business roles, test master data, third-party sales, customer projects, billing documents, credit memo requests]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GT_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1027
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Solution Order Management (4GT_AE) (4GT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Solution Order Management (4GT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232855060)

[2 Prerequisites 5](#_Toc232855061)

[2.1 System Access 5](#_Toc232855062)

[2.2 Roles 5](#_Toc232855063)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232855064)

[2.3.1 Additional Manual Configuration 11](#_Toc232855065)

[2.4 Business Conditions 11](#_Toc232855066)

[2.5 Settings for Situation Handling 12](#_Toc232855067)

[3 Preliminary Steps 14](#_Toc232855068)

[3.1 Maintain a Billing Profile 14](#_Toc232855069)

[3.2 Create Condition Records (Optional) 15](#_Toc232855070)

[3.3 Create Purchasing Info Record - Sales Item for Third-Party with Shipping Notification (CB1) 16](#_Toc232855071)

[3.4 Create Purchasing Info Record - Sales Item for Third-Party without Shipping Notification (CB2) 17](#_Toc232855072)

[3.5 Create Purchasing Info Record - Bought-In Item (CBAB) 19](#_Toc232855073)

[3.6 Assign Condition Type to Pricing Procedure (Optional) 21](#_Toc232855074)

[3.7 Maintain Price Conditions for Sales Kit type LUMF Specific Price (Optional) 24](#_Toc232855075)

[3.8 Set default item category for solution order items (Optional) 26](#_Toc232855076)

[4 Overview Table 28](#_Toc232855077)

[5 Test Procedures 31](#_Toc232855078)

[5.1 Solution Order 31](#_Toc232855079)

[5.1.1 Create Solution Order 31](#_Toc232855080)

[5.1.2 Release Solution Order Line Items 39](#_Toc232855081)

[5.1.3 Print Solution Order (Optional) 43](#_Toc232855082)

[5.2 Manage Sales Order 44](#_Toc232855083)

[5.2.1 Display Sales Order 44](#_Toc232855084)

[5.2.2 Standard Sales Item 45](#_Toc232855085)

[5.2.2.1 Create Delivery 45](#_Toc232855086)

[5.2.2.2 Execute Picking 47](#_Toc232855087)

[5.2.2.3 Post Goods Issue 48](#_Toc232855088)

[5.2.3 Sales Item for 3rd Party with SN 49](#_Toc232855089)

[5.2.3.1 Display List of Purchase Requisitions to be Assigned 49](#_Toc232855090)

[5.2.3.2 Convert Assigned Requisitions into Purchase Orders 50](#_Toc232855091)

[5.2.3.3 Check the Status of the 3rd Party with SN Sales Item in the Solution Order 51](#_Toc232855092)

[5.2.3.4 Post Statistical Goods Receipt 52](#_Toc232855093)

[5.2.3.5 Create Invoice 54](#_Toc232855094)

[5.2.4 Sales Item for 3rd Party w/o SN 56](#_Toc232855095)

[5.2.4.1 Display List of Purchase Requisitions to be Assigned 56](#_Toc232855096)

[5.2.4.2 Convert Assigned Requisitions to Purchase Orders 57](#_Toc232855097)

[5.2.4.3 Check the Status of the 3rd Party w/o SN Sales Item in the Solution Order 58](#_Toc232855098)

[5.2.4.4 Create Supplier Invoice 59](#_Toc232855099)

[5.2.5 Bought-In Item 62](#_Toc232855100)

[5.2.5.1 Create Purchase Order 62](#_Toc232855101)

[5.2.5.2 Post Goods Receipt 63](#_Toc232855102)

[5.2.5.3 Check the Status of the Bought-In Item Sales Item in the Solution Order 65](#_Toc232855103)

[5.2.5.4 Create Supplier Invoice 66](#_Toc232855104)

[5.2.6 Sales Item for Services 68](#_Toc232855105)

[5.2.7 Sales Item for Non-Stock 69](#_Toc232855106)

[5.2.7.1 Check the Status of the Non-Stock Item in the Solution Order 69](#_Toc232855107)

[5.2.8 Sales Kits 70](#_Toc232855108)

[5.2.9 Customer Down Payment (Optional) 70](#_Toc232855109)

[5.2.10 Advanced Intercompany Sales (Optional) 70](#_Toc232855110)

[5.2.11 Digital Payments (Optional) 71](#_Toc232855111)

[5.2.12 SEPA Direct Debit Handling (Optional) 71](#_Toc232855112)

[5.2.13 Returnable Sales Item 71](#_Toc232855113)

[5.2.13.1 Create Delivery 71](#_Toc232855114)

[5.2.13.2 Execute Picking 73](#_Toc232855115)

[5.2.13.3 Post Goods Issue 74](#_Toc232855116)

[5.2.14 Sales Order Fulfillment (Optional) 76](#_Toc232855117)

[5.3 Manage Service Order 76](#_Toc232855118)

[5.4 Manage Service Contract 77](#_Toc232855119)

[5.5 Manage Subscription Billing 78](#_Toc232855120)

[5.6 Manage Customer Project 79](#_Toc232855121)

[5.6.1 Display Customer Project 79](#_Toc232855122)

[5.6.2 Plan Customer Project 80](#_Toc232855123)

[5.6.3 Check Sales Price 83](#_Toc232855124)

[5.6.4 Time Recording for Staffed Resources(Optional) 84](#_Toc232855125)

[5.6.5 Create Supplier Invoice for Travel Expenses(Optional) 85](#_Toc232855126)

[5.6.6 Check Billing Element and Create Billing Document Request 85](#_Toc232855127)

[5.7 Manage Billing Document 86](#_Toc232855128)

[5.7.1 Create Billing Document 86](#_Toc232855129)

[5.7.2 Create Billing Document (Project Item) 88](#_Toc232855130)

[5.7.3 Display Billing Document 89](#_Toc232855131)

[5.8 Credit Memo Request 90](#_Toc232855132)

[5.8.1 Create Credit Memo Request with reference to invoice 90](#_Toc232855133)

[5.8.2 Approve Credit Memo Request 91](#_Toc232855134)

[5.8.3 Create Credit Memo 92](#_Toc232855135)

[5.9 Customer Returns 93](#_Toc232855136)

[5.10 Solution Order Profitability Dashboard (Optional) 94](#_Toc232855137)

[6 Appendix 96](#_Toc232855138)

[6.1 Equipment linkage 96](#_Toc232855139)

[6.2 Further supported Scope Items 98](#_Toc232855140)

## Purpose

Overview

Solution Order Management helps customers to evolve their business from selling single products to offering holistic solutions: they can manage complex solutions of physical goods, services, projects, and subscriptions in an integrated end-to-end order. With an intuitive progress view, situation handling, and cross object navigation, customers always have an overview of the fulfillment status of the different solution order items. Solution Order Management also comes with embedded pricing, omni-channel convergent billing, and seamless integration into revenue recognition and controlling. This gives customers a consolidated financial view of their solution portfolio. Solution Order Management is supported by a built-in analytics dashboard.

This process can be combined with the respective solution order management for configurable products (6HY).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/4GT_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

The test should be conducted with the following system:

|  |
| --- |
| Note For system details contact your System Administrator. |

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

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

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure.To check the assignment, use Business Role SAP_BR_BUPA_MASTER_SPECIALIST - tile Manage Customer Master Data in the Sales Area Data. |
| Employee | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Sales Product | TG10 | Sales Product | Trading Good for regular Trading (MRP planning) with item category group CBORNo serial number; no batch. |
| Sales Product | TG11 | Sales Product |  |
| Sales Product | TG13 | Sales Product | Trading Good for Regular Trading (reorder point planning) with item category group CBNANo batch |
| Sales Product | TG14 | Sales Product | Trading material with item category group CBAB (Reorder point planning, bought in item)No batch |
| Material | SM0001 | Service Material 01 | If you use ANC procedure to extend the new country content, you need to manually extend the materials according to Master Data Script 31X |
| Material | NS0002 | Non-Stock Material 02 (No MRP planning) | If you use ANC procedure to extend the new country content, you need to manually extend the materials according to Master Data Script 31Y |
| Service product (Material) | SRV_01 | Services Product | SRV_01 is also used for external workforce procurement process. When we create service order with SRV_01 for external workforce, we need to switch the item category from service item to external service item. |
| Material | SRV_02 | Service Expense Item |  |
| Material | SRV_03 | Service Part (Undefined) | Material Type Non-Stock MaterialSRV_03 is used for consumption material procurement process and SRV_03 as a dummy material will not be supported for automatic purchase order creation from purchase requisition. |
| Material | SRV_04 | Service Part (Defined) | Material Type Non-Stock MaterialSRV_04 is used for consumption material procurement process. |
| Material | SRV_05 | Service Spare Part |  |
| Material | SRV_CONTRACT | Service Contract Product | SRV_CONTRACT is also used for price adaption. When we create service contract with SRV_CONTRACT for price adaption, we need to switch the item category from service contract product to SC Itm (Pri. Adptn.). |
| Subscription Product | P-CLOUD_STORAGE | Subscription Product | You need to manually create the Products according to Master data document 5BD. |
| Subscription Product Rate Element | R-OneTime | One-Time Activation Fee | You need to manually create the Products according to Master data document 5BD. |
| Subscription Product Rate Element | R-Seats | Seat-Based Monthly Fee | You need to manually create the Products according to Master data document 5BD. |
| Subscription Product Rate Element | R-Traffic | Traffic-Based Usage Fee | You need to manually create the Products according to Master data document 5BD. |
| Project Product | PROJECT | Project |  |
| Material | P001 | Project Type 1 | Material which is used in order to describe different services being provided to the customer. |
| Material | P002 | Project Type 2 | Material which is used in order to describe different services being provided to the customer. |
| Material | T001 | Junior Consultant | The material determination must have been defined in SSCUI Maintain Project Billing Profile.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |
| Material | E002 | Airfare | The material determination must have been defined in SSCUI Maintain Project Billing Profile.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |
| Sales Product | SDBOMERLAHD | SD BOM Header ERLA (with Pricing, inventory management) |  |
| Sales Product | SDBOMLUMFHD | SD BOM Header LUMF(No pricing, no inventory) |  |
| Sales Product | SDBOMCPFHHD | SD BOM Header CPFH(with pricing, subitems with inventory) |  |
| Sales Product | RP002 | Sales Product (Returnable non-valuated product) |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Controlling area | A000 | Controlling Area A000 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Supplier | 33300001 | Domestic Supplier 1 |  |
| Plant | 3310 | Plant 1 AE |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| 5BD | Create Subscription Product Sales Billing - MDS |
| 5TO | Create Service Product for Project - MDS |
| 31X | Create Product Master of type "Service Product" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |

#### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/aeb2022503fd818f451d81421c9186f3)

### Business Conditions

Before this test script can be tested, the following business conditions must be met. Ensure the below scope items are activated.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this test script, the materials must be available in stock. If you are using trading goods (HAWA), you can either:Run through the Procurement of Direct Materials(J45) processOr create stock via role Warehouse Clerk (for details see section Preliminary Steps) |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period (BNZ) master data script. Posting Period is up to date. |
| 3D2 - Service Order Management and Monitoring | Has to be executed before testing this scope item. |
| 3MO - Service Contract Management | Has to be executed before testing this scope item. |
| BD9 - Sell from Stock | Has to be executed before testing this scope item. |
| 3NI - Procurement for Service Management | Has to be executed before testing this scope item. |
| 57Z - Subscription Management with Sales Billing | Has to be executed before testing this scope item. |
| J11 - Customer Project Management – Project-Based Services | Has to be executed before testing this scope item. |
| 4E9 - Project Billing – Project-Based Services | Has to be executed before testing this scope item. |
| BD3 - Sales Processing using Third-Party with Shipping Notification | Has to be executed before testing this scope item. |
| BDK - Sales Processing Using Third-Party Without Shipping Notification | Has to be executed before testing this scope item. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Has to be executed before testing this scope item. |
| BKJ - Sales Order Processing with Customer Down Payment | Has to be executed before testing this scope item. |
| 2EQ - Sale of Services | Has to be executed before testing this scope item. |
| 2ET - Sales Order Processing for Non-Stock Material | Has to be executed before testing this scope item. |
| 31N - Situation Handling | This scope item must be activated for situation handling steps. |
| 31Q - Sales Order Processing for Sales Kits | Has to be executed before testing this scope item. |
| 7S7 - Sell from Stock with Down Payment Processing | Has to be executed before testing this scope item. |
| 5D2 - Advanced Intercompany Sales | Has to be executed before testing this scope item. |
| 1Z1 - Digital Payments – Sales | Has to be executed before testing this scope item. |
| BKX - Sales Order Processing – SEPA Direct Debit Handling | Has to be executed before testing this scope item. |

### Settings for Situation Handling

Purpose

Situation handling recognizes business situations by evaluating conditions (rules) on business facts. A business situation occurs when a business object changes its status relevant to a user, when critical deadlines are passed, or a KPI passes a threshold.

Prerequisite

Notifications are only created in the system when the required configuration in the situation template (including notification recipient settings) are set up.

These additional configuration steps should be carried out by customers to activate situation handling.

|  |
| --- |
| Note If you want to use situation handling with Solution Order scope item, you have to include also scope item Situation Handling (31N). |

To set up situation handling, create your ready-to-use situation type, maintain the message to be displayed, define the conditions when the situation will be triggered, define recipient groups who will receive notifications, and monitor the instances. For more information, see the Set-Up Instructions for the scope item Situation Handling (31N).

The following standard situation templates are defined and delivered by SAP for Solution Order:

- SOLO_DELIVDTE_CHGD_ITMREL
- SOLO_DELIVDTE_RCHD_ITMREL
- SOLO_PLNDDTE_CHGD_ITMREL
- SOLO_PLNDDTE_RCHD_ITMREL
- SOLN_SOLO_SLSITM_DELIVDATE_CHGD
- SOLN_SOLO_SLSITM_NOT_DLVRD
- SOLN_SOLO_SRVCITM_NOT_CMPLTD
- SOLN_SOLO_SRVCITM_NOT_SCHEDLD
- SOLN_SOLO_SRVCITM_PLNDDTE_CHGD
- SOLN_SOLO_SRVCITM_NOT_SCHEDLD
- SOLN_SOLO_PROJITM_DATE_CHGD
- SOLN_SOLO_PROJITM_NETVALUE_CHGD
- SOLN_SOLO_FUP_CREDIT_BLOCKED

For each situation template, a corresponding responsibility rule is defined in which the responsible person to be notified can be assigned.

For more information and situation template details (default settings, conditions, notification recipients), see documentation [Situation Templates for Solution Orders.](https://help.sap.com/viewer/a376cd9ea00d476b96f18dea1247e6a5/latest/en-US/40110bff6b874b1c8b2630b944b95a60.html) on SAP help portal.

|  |
| --- |
| Note If you want to test situation handling with Solution Order scope item, run the steps that are described in the Test Script of scope item Situation Handling (31N). |

## Preliminary Steps

### Maintain a Billing Profile

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

### Create Condition Records (Optional)

Purpose

In case you have fine tuned the access sequence of SAP pre-shipped condition types, the relative condition records need to be created accordingly. This process step shows you how to create condition records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111) app. | The Manage Prices - Sales screen displays. |  |
| 3 | Change Sales Price | Select PSP0 from the Condition Type dropdown list and press Enter.To create a new condition record, choose Create and enter the following entries:Condition Type: PSP0Condition Table: 305 {Customer/material with release Status}Customer: 10100001Sales Organization: 3310Distribution Channel : 10Product: for example, T001Valid From: <Jan 1st of last year>Condition Amount or Ratio: for example, 100.00 EURPricing Unit: for example, 1 HourChoose Save. |  |  |

### Create Purchasing Info Record - Sales Item for Third-Party with Shipping Notification (CB1)

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

### Create Purchasing Info Record - Sales Item for Third-Party without Shipping Notification (CB2)

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

### Create Purchasing Info Record - Bought-In Item (CBAB)

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

### Assign Condition Type to Pricing Procedure (Optional)

Prepare Proration for Royalties Settlement (Optional)

This section describes the preliminary steps that are required to consider proration in the royalties settlement between company codes or with an external licensor as subsequent processes to subscription billing 55I - Royalties Settlement for Sales

To calculate royalties per license and your subscription model includes prorated recurring fees, SAP Subscription Billing has to hand over not only the actual billed, prorated amount as condition type PMP2Recurring Price, but also a statistical amount as condition type PMP4Recurring Price Base, that reflects the non-prorated recurring amount. With the ratio of PMP2 to PMP4, the royalties settlement application can determine the proration factor to calculate the correct royalties amount.

1. Create a new Price Element Specification in SAP Subscription Billing for the settlement base like described in Create Settlement Base as a new Price Element Specification section.
2. Add settlement base as a step to your pricing scheme in SAP Subscription Billing to calculate the Pricing Scheme like described in Add Settlement Base to pricing Scheme section.
3. Enhance your relevant pricing procedures in SAP S/4HANA Cloud Public Edition with condition type PMP4 as described in theEnhance Pricing Procedure with PMP4 section.

Create Settlement Base as a new Price Element Specification

In this activity you create a new Price Element Specification in SAP Subscription Billing to reflect the Settlement Base.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to the SAP Subscription Billing launchpad as Configuration Expert - Business Process Configuration. | The SAP Subscription Billing launchpad displays. |  |
| 3 | Access the Manage Price Element Specifications app | Open Manage Price Element Specification. | The Manage Price Element Specification screen displays. |  |
| 4 | Copy Price Element Specification for Recurring Fees | Select the Price Element Specification that is used for calculating the recurring fees.Choose Copy to copy the price configuration into a new Price Element Specification. | A new Price Element Specification is created with the same price configuration as the existing one for recurring fees. |  |
| 5 | Change the code of the Price Element Specification | On the Header tab, enter the string Settlement Base in the code field. Optional: In the Header tab, chooseadd/change the description. | The name of the Price Element Specification is changed from to . |  |
| 6 | Add/Change PMP4 as the Output Attribute. | In the Custom Output Attributes tab, check if the following values are available:Field: ConditionTypeType: StringOrigin: ConstantValue: PMP2 | Condition type, PMP4 is maintained as the output attribute. |  |
| 7 | Save Price Element Specification | Save the new Price Element Specification by choosing Create. | Price Element Specification Settlement Base is created. |  |

Add Settlement Base to Pricing Scheme

In this activity you add the Settlement Base to your Pricing Scheme in SAP Subscription Billing

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Subscription Billing launchpad as Configuration Expert - Business Process Configuration. | The Fiori Launchpad is displayed. |  |
| 2 | Access the Manage Pricing Schemes app | Open Manage Pricing Schemes. | The Manage Pricing Schemes screen displays |  |
| 3 | Select the Pricing Scheme to add Settlement base | Select the Pricing Scheme that is used in your product that you want to calculate royalties for. | The details of the pricing scheme are displayed. |  |
| 4 | Add Settlement Base to pricing steps | Choose Edit.Add a new Pricing Step and maintainStep: <Enter a number not yet used>Price Element Specification: Choose Settlement BaseName: Enter Settlement BaseSign: Choose + iconStatistical: check the box | A new pricing step Settlement Base is added to the Pricing Scheme as statistical |  |
| 5 | Save Pricing Scheme | Choose Save. | Pricing Scheme is saved |  |

Enhance Pricing Procedure with PMP4

In this activity you add PMP4 to your existing pricing procedure in SAP S/4HANA Cloud Public Edition.

The following steps provide you with information on the assignment of the condition type to the pricing procedure.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The Fiori Launchpad is displayed. |  |
| 2 | Access the Manage Your Solution App | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure pricing for customers and materials in sales | Search with the following criteria:Application Area: SalesSub Application Area: Price ManagementChoose Configure pricing for customers and materials in sales.On the Pricing page, under Configure your solution screen, Choose Set Pricing Procedure.Choose Configure. | The Pricing screen is displayed. |  |
| 4 | Set Procedure - Control Data | On the IMGActivity-execute Screen, Search for procedure A17024 for solution order and procedure A17027 for subscription.Choose Copy As and provide any Z* name under the Procedure field. Choose Copy.A pop-up, specify Object to be copied displays, choose Copy All. A message pop up is displayed, choose continue.Select the Procedure created in the above step and Choose Procedure - Control Data on the left side panel.On the Procedure- Control Data screen, search for the following values:Step Number: 88 and Counter : 0. Enter theControl Type value as: PMP4Choose SaveA new entry is created under Procedures- Control Data. | The Procedure - Control Data is maintained. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The Fiori Launchpad is displayed. |  |
| 2 | Open Configure pricing for customers and materials in sales | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure pricing for customers and materials in sales.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configured pricing for customers and materials in the sales screen is displayed. |  |
| 3 | Set Procedure - Control Data | On the IMGActivity-execute Screen, Search for procedure A17024 for solution order and procedure A17027 for subscription.Choose Copy As and provide any Z* name under the Procedure field. Choose Copy.A pop-up, specify Object to be copied displays, choose copy all. A message pop up is displayed, choose continue.Select the Procedure created in the above step and Choose Procedure - Control Data on the left side panel.On the Procedure- Control Data screen, search for the following values:Step Number: 88 and Counter : 0. Enter the Control Type value as: PMP4Choose SaveA new entry is created under Procedures- Control Data. | The Procedure - Control Data is maintained. |  |

### Maintain Price Conditions for Sales Kit type LUMF Specific Price (Optional)

Purpose

This step show you how to add pricing conditions for specific prices for sales kits of type LUMF on component level. This is needed in case you want to allow different prices for the products if they are sold as part of a sales kit of type LUMF using the condition type is PSSK.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays |  |
| 2. | Access the App | Open Manage Prices - Sales(F4111). | The Manage Prices – Sales screen displays. |  |
| 3. | Add condition record for PSSK for product SDBOMLUMFIT01 | Choose Create.Make the following entries:Condition Type: PSSKCondition Table: 100Pricing Reference Material of Main Item: SDBOMLUMFHD <SD BOM Header LUMF (SDBOMLUMFHD)>Sales Organization: 1010Distribution Channel: 10Product : SDBOMLUMFIT01Condition Amount: 12.98 EURCondition Description : sales kit specific priceOther fields could be adjusted as you need or left as they are.Choose Save. | The Manage Prices – Sales screen shows the success message „Condition record <NN>is created and valid from <YYYY/MM/DD>to <YYYY/MM/DD>.“ |  |
| 4. | Add condition record for PSSK for product SDBOMLUMFIT02 | Choose Create.Make the following entries:Condition Type: PSSKCondition Table: 100Pricing Reference Material of Main Item: SDBOMLUMFHD <SD BOM Header LUMF (SDBOMLUMFHD)>Sales Organization: 1010Distribution Channel: 10Product : SDBOMLUMFIT02Condition Amount: 23.00 EURCondition Description: sales kit specific priceOther fields could be adjusted as you need or left as they are.Choose Save. | The Manage Prices – Sales screen The Manage Prices – Sales screen shows the success message „Condition record <NN>is created and valid from <YYYY/MM/DD>to <YYYY/MM/DD>.“. |  |
| 5. |  |  |  |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the project experience in SAP Central Business Configuration. | The Fiori Launchpad is displayed. |  |
|  | Open Configure pricing for customers and materials in sales | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure pricing for customers and materials in sales.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configured pricing for customers and materials in the sales screen is displayed. |  |
|  | Set Procedure - Control Data | On the IMGActivity-execute Screen, Search for procedure A17024 for solution order and procedure A17027 for subscription.Choose Copy As and provide any Z* name under the Procedure field. Choose Copy.A pop-up, specify Object to be copied displays, choose copy all. A message pop up is displayed, choose continue.Select the Procedure created in the above step and Choose Procedure - Control Data on the left side panel.On the Procedure- Control Data screen, search for the following values:Step Number: 88 and Counter : 0. Enter the Control Type value as: PMP4Choose SaveA new entry is created under Procedures- Control Data. | The Procedure - Control Data is maintained. |  |

### Set default item category for solution order items (Optional)

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

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Sub Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- | --- |
| Solution Order |  |  |  |  |
|  | [Create Solution Order](#unique_18) [page ] 31 | Solution Order Specialist | Manage Solution Order | A solution order has been created. |
|  | [Release Solution Order Line Items](#unique_19) [page ] 39 | Solution Order Specialist | Manage Solution Order | Items of the solution order has been released |
|  | [Print Solution Order (Optional)](#unique_20) [page ] 43 | Solution Order Specialist | Manage Solution Order | Solution order PDF is displayed |
| Manage Sales Order |  |  |  |  |
|  | [Display Sales Order](#unique_21) [page ] 44 | Internal Sales Representative | Manage Sales Orders | Sales Order is displayed |
|  | [Standard Sales Item](#unique_22) [page ] 45 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Sales Item for 3rd Party with SN](#unique_23) [page ] 49 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Sales Item for 3rd Party w/o SN](#unique_24) [page ] 56 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Bought-In Item](#unique_25) [page ] 62 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Sales Item for Services](#unique_26) [page ] 68 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Sales Item for Non-Stock](#unique_27) [page ] 69 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Sales Kits](#unique_28) [page ] 70 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Customer Down Payment (Optional)](#unique_29) [page ] 70 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Advanced Intercompany Sales (Optional)](#unique_30) [page ] 70 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Digital Payments (Optional)](#unique_31) [page ] 71 | Internal Sales Representative | Manage Sales Orders |  |
|  | [SEPA Direct Debit Handling (Optional)](#unique_32) [page ] 71 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Returnable Sales Item](#unique_33) [page ] 71 | Internal Sales Representative | Manage Sales Orders |  |
|  | [Sales Order Fulfillment (Optional)](#unique_34) [page ] 76 | Internal Sales Representative | Sales Order Fulfillment - Analyze Issues | Problems that occur during the sales order fulfillment process are addressed |
| Manage Service Order | [Manage Service Order](#unique_35) [page ] 76 | Customer Service Manager | Manage Service Orders | Service Order is displayed |
| Manage Service Contract | [Manage Service Contract](#unique_36) [page ] 77 | Customer Service Manager | Manage Service Contracts | Service Contract is displayed |
| Display Subscription | [Manage Subscription Billing](#unique_37) [page ] 78 | Solution Order Specialist | Subscription | Subscription is displayed |
| Manage Customer Project | [Display Customer Project](#unique_38) [page ] 79 | Project Manager - Professional Services | Plan Customer Projects | Customer Project is displayed |
|  | [Check Sales Price](#unique_39) [page ] 83 | Project Manager - Professional Services | Set Service Prices – Sales (VK12) |  |
|  | [Plan Customer Project](#unique_40) [page ] 80 | Project Manager - Professional Services | Plan Customer Projects (F0719) | Customer Project is planned and ready for execution |
|  | [Time Recording for Staffed Resources(Optional)](#unique_41) [page ] 84 | Project Manager - Professional Services | Notify Missing Time - Time Recording Status (F2556) |  |
|  | [Create Supplier Invoice for Travel Expenses(Optional)](#unique_42) [page ] 85 | Accounts Payable Accountant | Create Supplier Invoice (F0859) |  |
|  | [Check Billing Element and Create Billing Document Request](#unique_43) [page ] 85 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| Manage Billing Document |  |  |  |  |
|  | [Create Billing Document](#unique_44) [page ] 86 | Billing Clerk | >Create Billing Document | Invoice is created for Solution Order |
|  | [Create Billing Document (Project Item)](#unique_45) [page ] 88 | Billing Clerk | Create Billing Document(Project Item) | Invoice is created for Solution Order |
|  | [Display Billing Document](#unique_46) [page ] 89 | Billing Clerk | Display Billing Documents | Invoice is displayed |
| Credit Memo Request (Optional) | [Create Credit Memo Request with reference to invoice](#unique_47) [page ] 90 | Internal Sales Representative | Manage Credit Memo Requests | Credit Memo Request is created |
|  | [Approve Credit Memo Request](#unique_48) [page ] 91 | Sales Manager | My Inbox | Credit memo request has been approved. |
|  | [Create Credit Memo](#unique_49) [page ] 92 | Billing Clerk | Create Billing Documents | Credit memo has been created |
| Customer Returns | [Customer Returns](#unique_50) [page ] 93 | Returns and Refund Clerk | Manage Customer Returns | Customer Returns has been created |
| Solution Order Profitability | [Solution Order Profitability Dashboard (Optional)](#unique_51) [page ] 94 | Sales Manager | Solution Order Profitability |  |

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

This step describes how to create a new solution order and add line items (for example, salesitems, service items and service contract items) to solution order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage solution orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose the Manage Solution Ordersapplication tile. | The list report page is displayed. |  |
| 3 | Create Solution Order | Choose Create from the solution order listpage. | Create Solution Order window is displayed. |  |
| 4 | Maintain Solution Order data | Enter the following data to create a solution order:Description: <yourdescription>External Reference:<your reference>Sold-To Party: for example,33100001 for AE(Domestic UAE Customer 1)Note Select the sales organization (for example, 3310) and Contactperson from the popup appears. | Required header data for the Solution order has beenmaintained. |  |
| 5 | Add Sales Item | Maintain the following Sales Item in the solution order:Product ID: for example,TG11(Sales Item)Quantity: for example,1Unit: for example,PCChoose Enter.Note For free of charge sales Item change the Item Category to Sales Item FoC. Then follow Standard Sales Order chapter. | The Sales Order item is now added to Solution Order. |  |
| 6 | Add Sales Item(optional) for URR | Maintain the following Sales Item in the solution order:Product ID: for example, URR_MAT1_NORM (Sales Item)Quantity: for example, 1Unit: for example, PCChoose Enter.Note For free of charge sales Item change the Item Category to Sales Item FoC. Then follow Standard Sales Order chapter. PSAM pricing condition has been provided in solution order pricing procedure to support if material is enabled for universal revenue recognition. |  |  |
| 7 | Add Sales Item for 3rd Party with Shipping Notification | Maintain the following Sales Item for 3rd Party with Shipping Notification in the solution order:Product ID: for example, TG10(3rd Party with SN)Quantity: for example, 10Unit: for example, PCItem Category: for example, 3rd Party with SNChoose Enter.Note: For free of charge 3rd Party with SNItem change the Item Category to 3rd Party with SN FoC. Thenfollow sales Item for 3rd Party with SN chapter. | The sales item (3rd Party with SN) is added to the Solution Order. |  |
| 8 | Add Sales Item for 3rd Party w/o Shipping Notification | Maintain the following Sales Item for 3rd Party w/o Shipping Notification in the solution order:Product ID: for example, TG13(3rd Party w/o SN)Quantity: for example, 10Unit: for example, PCItem Category: for example, 3rd Party w/o SNChoose Enter.Note: For free of charge 3rd Party w/o SNItem change the Item Category to 3rd Party w/o SN FoC. Thenfollow sales Item for 3rd Party w/o SN chapter. | The sales items (3rd Party w/o SN) item is added to the Solution Order. |  |
| 9 | Add Bought-In Sales Item | Maintain the following Bought-In Sales Item in the solution order:Product ID: for example, TG14(Bought-In SalesItem)Quantity: for example, 10Unit: for example, PCItem Category: for example, Bought-In Sales ItemChoose Enter.Note: For free of charge Bought-In SalesItem change the Item Category to Bought-In Sales FoC. Thenfollow Bought-In Item chapter. | The bought-in sales item is added to the Solution Order. |  |
| 10 | Add Sales Item for Service | Maintain the following Bought-In Sales Item in the solution order:Product ID: for example, SM0001(Sales Item for Service)Quantity: for example, 1Unit: for example, HRItem Category: for example, Sales Itm f. ServiceChoose Enter.Note: For free of charge Sales Item forService change the Item Category to Sales f. Service FoC. Thenfollow Sales Item for Services chapter. | The sales item for service is added to the Solution Order. |  |
| 11 | Add Non-Stock Sales item | Maintain the following Non-Stock sales Item in the solution order:Product ID: for example, NS0002(Non-Stock Sales Item)Quantity: for example, 1Unit: for example, PCItem Category: for example, Sales Itm f. ServiceChoose Enter.Note: For free of charge Non-Stock Sales Item change the Item Category to Non-Stock Sales FoC. Then follow Sales Item for Non-Stock chapter. |  |  |
| 12 | Add Sales kits item(SDBOMERLAHD) | Maintain the following sales kit item in the solution order:Product ID: for example,SDBOMERLAHDQuantity: for example, 1Unit: for example, PCNote To process the entered sales kits item as a free of charge sales kits item, change the determined item category to FOC MainItmPr. (BOM) before pressing Enter. Alternatively, to process the entered sales kits items as a milestone billing item, change the determined item category to MnItPr (BOM) Milest. before pressing Enter. After changing the item category follow the sales kits chapter.Choose Enter.Note To add additional subitems to the initially added sales kits Item, enter the requiredproduct ID, quantity and the item number of the higherlevel item in Higher-Level Items column. | The sales item is added to the Solution Order. |  |
| 13 | Add Sales kits item(SDBOMLUMFHD) | Maintain the following sales kit item in the solution order:Product ID: for example,SDBOMLUMFHDQuantity: for example,1Unit: for example, PCNote To process the entered sales kits item as a free of charge sales kits Item, change the determined item category to FOC Pr. at Sub (BOM) before pressing Enter. Alternatively, to process the entered sales kits items as a milestone billing item, change the determined item category to MnItPr (BOM) Milest. before pressing Enter. After changing the item category follow the Sales Kits chapter.Choose Enter.Note To add additional sub items to the initially added sales kits Item, enter the required product ID, quantity and the item number of the higher level item in Higher-Level Items column. | The sales item is added to the Solution Order.In case you have maintained in step 3.7 a sales kit specific price, the a different price is determined on component level |  |
| 14 | Add Sales kits item(SDBOMCPFHHD) | Maintain the following sales kit item in the solution order:Product ID: for example,SDBOMCPFHHDQuantity: for example,1Unit: for example, PCNote To process the entered sales kits item as a free of charge sales kits Item, change the determined item category to Head FOC B/Log. Item before pressing Enter. Alternatively, to process the entered sales kits items as a milestone billing item, change the determined item category to Pr.Hd-Li Milest. before pressing Enter. After changing the item category follow the Sales Kits chapter.Choose Enter.Note To add additional sub items to the initially added sales kits Item, enter the required product ID, quantity and the item number of the higher level item in Higher-Level Items column.Note To execute sales kits(CPFH), create the material manually. You should also create the condition record for CPFH scenario. For more information, refer to the Preliminary Steps chapter in the 31Q test script. | The sales item is added to the Solution Order. |  |
| 15 | Add Returnable Sales item | Maintain the following returnable sales item in the solution orderProduct ID: for example, RP002(Returnable non-valuated Product)Quantity: for example,1Unit: for example, PCChoose Enter. | The sales item is added to the Solution Order. |  |
| 16 | Add Service Items | Maintain the following Service Items in the solution order:Product ID: for example,SRV_01(Service Item)Quantity: for example,1Unit: for example,HRChoose Enter.In the appearing contract assignment popup select No Assignment.Note For external service item, select Item Category: External Service Itm.Refer to 3NI test script for procurement of service management.For fix price service item, select item category: SrvItm (FxPrc).For fix price external service item, select item category: Ext.SrvItm (FxPrc).For ad-hoc billing service item, select item category: SrvItm (Ad Hoc Bill).For ad-hoc billing external service item, select item category: ExtSrv (Ad Hoc Bill). | The Service Order items are added to the Solution Order. |  |
| 17 | Add Service Expense Items | Maintain the following Service Expense Items in the solution order:Product ID: for example,SRV_02(Service Expense Item)Quantity: for example,1Unit: for example,EAChoose Enter.Note For fix price expense item, select item category ExpItm (FxPrc).For ad hoc billing expense item, select item category ExpItm (Ad Hoc Bill). | The Service Expense Item is added to the solution order. |  |
| 18 | Add Service Part (Undefined) | Maintain the following Service Expense Items in the solution order:Product ID: for example,SRV_03(( Service Part(Undefined)(Non-Stock))Quantity: for example,1Unit: for example,EAChoose Enter.Note For fix price non-stock service part item, select item category NonStk SrvPart FxPrc.For ad hoc billing non-stock service part item, select item category NonStk SrvPrt Ad Hoc. | The Service part is added to the solution order. |  |
| 19 | Add Service Part (Defined) | Maintain the following Service Expense Items in the solution order:Product ID: for example,SRV_04(( Service Part(Defined)(Non-Stock))Quantity: for example,1Unit: for example,EAChoose Enter. | The Service part is added to the solution order. |  |
| 20 | Add Service Spare Part Items | Maintain the following Service Spare Part Items in the solution order:Product IDSRV_05(Service Expense Item)Quantity: for example,1Unit: for example,PCChoose Enter.Note For fix price service part item, select item category SrvPart (FxPrc).For ad hoc billing service part item, select item category SrvPrt (Ad Hoc Bill). | The Service Spare Part Item is added to the Solution Order. |  |
| 21 | Add Service Bundle | Maintain the following Service Bundle Items in the solution order:Product ID SRV_BUNDLE_01(Service Bundle)Quantity: for example, 1Unit: for example, PCNote down the item number, e.g. 0190Choose Enter.Maintain the sub-item in the Service Bundle Main Item, for exampleProduct ID SRV_01 (Service Item)Quantity: for example, 1Unit: for example, PCMaintain the higher level Item No: 0190(from the step before)Choose Enter.The Service bundle main item and the related subitems are added to the solution order.Note Fix price partial billing service bundle item, select item category SrvcBndl(FPrc/PBLL).For ad hoc billing service bundle item, select item category SrvBndl (Ad Hoc Bll).For Service bundle, you could use product SRV_BUNDLE_02 (Service Bundle). |  |  |
| 22 | Add Service Contract Items | Maintain the following Service Contract Items in the solution order:Product ID: for example, SRV_Contract (Service Contract Item)Quantity: for example,1Unit: for example,AUChoose Enter.Note For service contract item with price adaption select Item Category: SC Itm (Pri.Adptn.).Refer to 3MO test script chapter Adapt Service Contract Prices for price adaption of service contract.For service contract item with Ad-hoc Billing select Item Category: SC Itm (Ad-hoc Bill).Refer to 3MO test script chapter Create a Service Contract Item forAd-hoc Billing of service contract. | The Service Contract Item is added to the Solution Order. |  |
| 23 | Add Subscription Billing Item | Maintain the following Subscription Billing Item in the solution orderProduct ID: for example,P-CLOUD_STORAGE (Subscription BillingItem)Quantity: for example,1Unit: for example,EAChoose Enter. | The Subscription Billing Item is added to the solution order. |  |
| 24 | Add Subscription Billing Item - Price Calculation Services | Maintain the following Subscription Billing Item in the solution orderProduct ID: for example, P-CLD_STORAGE_PCS(Subscription Billing Item for Price Calculation Services)Quantity: for example,1Unit: for example,EAChoose Enter.Note PSAM pricing condition have been provided in solution order pricing procedure to support if subscription is enabled for universal revenue recognition. | The Subscription Billing Item is added to the solution order. |  |
| 25 | Add Project Item | Maintain the following Project Item in the solution orderProduct ID: for example, PROJECT (Project Item)Quantity: 1Unit: for example, AUChoose Enter.Note: The customer project created from the solution order will have the description product / item.Click on Edit in Actions for Project Item, it navigates to Item details page.In Item details page make the following entries:Service Organization: Service Organization – Company USCost Center : Csltg Unit AProfit Center : <Consulting Unit A(YB101)>Project Start Date: <today>Project End Date: <today + 4 months>Note: Customer Projects created from a Solution Order are always created with the setting Use Project Billing (New): Yes.Note: To link an existing project to solution order by assigning a project in the field Linked Project ID: in ItemOverview page for project item.Note To link an existing project to solution orders, Click on Edit in Actions for Project Item, in Project Item Details tab assign the project ID in the field Linked ProjectID.In order to unlink a project by deleting the project from Transaction History tab in item overview page for project item | The Project Item is added to the solution order |  |
| 26 | Create Item Relationship for Items(optional) | Choose Edit List in Items tab.Select dependent item from items list and choose Define Item Relationship and a popup of Define Item Relationship is appearedchoose Insert and a row is added for selected itemselect the Item Relationship from the dropdown (Has dependency and Depends on)Enter the dependent item number in ItemNo. columnChoose Enter.Choose Close. | Item Relationships for items are created. |  |
| 27 | Save the Solution Order | Choose Save.Note down the ID of the Solution Order you have just created. | Solution Order with all the line items is saved. |  |

#### Release Solution Order Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the line items of the previously created solution order will be released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage SolutionOrders application is displayed. |  |
| 2 | Choose Manage Solution Order | Choose the Manage Solution Orders. | List of Solution Order is displayed. |  |
| 3 | Search Solution Order | In the search area on the top, enter the ID of your solutionorder in the Search field.Choose Go. | Your solution order is displayed. |  |
| 4 | Edit Solution Order | Choose the Solution Order and choose Editin the Solution Order Details tab. | Solution Order is displayed in edit mode. |  |
| 5 | Sales Order Simulation | In the tab area Items, from the dropdown list Show: choose Sales Items and choose Edit List. Click on Simulate Sales Order Creation to verify the sales order.Note: In case of error or incompletion a warning would be shown in the Solution Order. In addition to that temporary ATP information can be seen in the Confirmed Quantity and Last Confirmed Delivery Date. | Sales order creation simulated successfully. |  |
| 6 | Simulate Subscription and Change Subscription Parameters | In the tab area Items, ChooseEdit inActions for Subscription Item, itnavigates to Item details pageIn Item details page choose Simulate at top right, to simulate subscription itemClick on Insert in Subscription Parameters tab toChange the Subscription parameters.If you are simulating price scheme product, verify that theprice calculation tab shows One-TimeCharge, Recurring Charge,and Usage Bases Charge.Choose Back.Note Choose Overwrite Default Terms and then enter Expected term for example 12inSubscription Termsfield. | After the Simulation, rate elements, Subscription and parametersshould be populated on the Subscription details.Price information on the Subscription item are updated accordingto the adjusted user number |  |
| 7 | Release line items in Solution Order | In the tab area Items, change the Status for the individual item.Example-For Sales item: In sales item line change the Status from Open to ReleasedChoose Save.For Sales item 3rd Party with Shipping Notification: In 3rd Party with SN item line change the Status from Open to ReleasedChoose Save.For Sales item 3rd Party w/o Shipping Notification: In 3rd Party w/o SN item line change the Status from Open to ReleasedChoose Save.For Bought-In Sales Item: In Bought-In Sales Item line change the Status from Open to ReleasedChoose Save.For Sales Item for Service: In Sales Item for service line change the Status from Open to ReleasedChoose Save.For Non-Stock Sales Item: In Non-Stock Sales Item line change the Status from Open to ReleasedChoose Save.For Sales Kit Item: In Sales Kit Item change the Status fromOpen toReleased.Note Individual items can be released inside sales kits item.Choose Save.For Returnable Sales Item: In Returnable Sales Item line changethe Status fromOpen toReleased.Choose Save.For Service Order items (service, expense, spare part, and service bundle): In serviceorder item line change the Status fromOpen toReleasedChoose Save.For Service Contract item: In service contract item line change the Status from Open to ReleasedChooseSave.For Subscription item: In subscription item line change the Status from Open to ReleasedChoose Save.For Project item: In project item line change the Status from Open to ReleasedChoose Save.Note: It is also possible to release all the items in the solution order at the same time with the action Release All Items in the All Items view of the Items tab area. | Line item in solution order has been released |  |
| 8 | Verify Distribution Status | Under Items, Distribution Status should be Started.If not choose Refresh .Note If the Distribution Status shows as Distribution error thenverify if there is any issue in creation of solutionorder.Once the issue is resolved then choose RedistributeNote Choose Refresh to view the updated status. | Distribution Status for all line items are verified. |  |
| 9 | Verify Follow-up Transaction Data in Transaction History | The follow up transactions are created asynchronously, hence choose Refresh to viewthem.Under Transaction History,For sales item choose Transaction Type: Sales Order to navigateSales Order details view and verifythe following data:Items: <Same as sales Itemsadded in solution order>Note Only one sales order will be created for all sales items.If URR relevant product URR_MAT1_NORM was also added tosolution order then refer to section 4.1 of scope item 3KKto view the URR specific detailsFor service item choose Transaction Type: ServiceOrder to navigate Service Orderdetails view and verify the following data:Items: <Same as serviceItems added in solution order>For service contract item choose Transaction Type:Service Contract to navigate ServiceContract details view and verify the followingdata:Items: <Same as servicecontract Items added in solution order>For Subscription billing item choose Transaction: Subscription.It will navigate to SCP (SAP Cloud Platform) and verify thefollowing dataSubscription terms (Cancellation Policy, Duration, Renewal), Processing Data (Subscription Dates, Snapshot Data)Refer to 57Z test script for more detailed steps to verifysubscription billing details.For project item click on Transaction: Customer Project to navigate Plan Customer Projects view and verify the following dataInformation: <Same as project item added in solution order>Note down all the IDs of the follow-up transactions. | Line item in solution order has been verified. |  |

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
| 2 | Choose Manage Solution Order application | Choose the Manage Solution Order application tile. | A list with all Solution Order is displayed. |  |
| 3 | Search Solution Order | In the search area on the top,In the search field, enter the required solution order ID and Choose Go. | Your solution order is displayed. |  |
| 4 | Open Solution Order and navigate to Output Items | Choose the Solution Order and go to Output Items tab | Available Output Items are displayed. |  |
| 5 | Choose Output Condition | Choose the required output Channel and choose Send Output.Choose Send Output to print the document or send it via e-mail. | Document is sent to the selected output channel. |  |
| 6 | Display Print Preview | To display the document, in the Display column choose Display Document.Note Optionally save a local copy of the PDF document. | A PDF document is displayed. |  |

### Manage Sales Order

#### Display Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display the sales order created in solution order.

|  |
| --- |
| Note One sales order gets created for all the sales items. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Internal Sales Representative. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).From the menu, choose Sales Orders and Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Navigate to Display Sales Order Screen | On the Manage Sales Orders screen, enter the respective order number created in Create Solution Order step in the Sales Order and choose Go.Open the Sales Order factsheet by clicking on the Sales Order ID in the list and a second time in the popover. Validate the Solution Order Reference ID (Ref. Soltn Order ID) in the General Information and in the Process Flow area.Close the Sales Order factsheet and from the result list choose the sales order line that displays. | The sales order is displayed. |  |

#### Standard Sales Item

Note: You can refer to this chapter if solution order has standard sales item(TG11).

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully. Delivery number displays on Deliveries tab. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management. |

To avoid open deliveries, ensure there is sufficient inventory quantity at the time for delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.

You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).

You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.

You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation Rejected with An Error Message.

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) |  |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery Number, and choose Continue.From the Outbound Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Outbound Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the DELIVERY_PICK_LIST Output Type, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

##### Execute Picking

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
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |

##### Post Goods Issue

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose Post Goods Issues.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested, the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount displays.To check the financial document, use the Warehouse Clerk role, and access the Display Material Document List - Deprecated (MB51) app. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Sales Item for 3rd Party with SN

Note: You can refer to this chapter if solution order has 3rd Party with SN item(TG10).

##### Display List of Purchase Requisitions to be Assigned

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed when you want to review your Purchase Requisitions and assign them to a vendor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is listed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The purchase requisition is selected. |  |
| 5 | Assign Supplier | Choose the Assign Source of Supply button. Select one source and choose the Assign button. | The Source of Supply is assigned.The Purchase Requisition is updated successfully. |  |

##### Convert Assigned Requisitions into Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to convert the assigned requisitions into purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is listed. |  |
| 3 | Search for Purchase Requisition | Enter the purchase requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The purchase requisition is selected. |  |
| 5 | Create Purchase Order | Choose the purchase requisition where the assigned supplier is displayed and choose Create Purchase Orders.Note Choose Yes to continue the process if any warning message occurs. | The Purchase Order screen displays. |  |

##### Check the Status of the 3rd Party with SN Sales Item in the Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to verify the Status of a 3rd Party with SN Sales Item in Solution Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose the Manage Solution Orders application tile. | The list report page is displayed. |  |
| 3 | Find Solution Order | In the search area on the top, enter the ID of your solution order in the Search field.Choose Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4 | Open Solution Order in the Edit Mode | Choose the Solution Order and choose Display in the Solution Order Details tab. | The display view of the Solution Order will be opened. |  |
| 5 | Verify the Status of 3rd Party with SN Sales Item | In the tab area Items, under the field Status verify the status changed to Completed.Choose Refresh to verify the Status changed to Completed. | The Status is Completed. |  |

|  |
| --- |
| Note Succeeding Processes: After completing the status check, proceed with Create Inbound Delivery chapter from test script BD3 Sales Processing using Third-Party with Shipping Notification. |

##### Post Statistical Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vendor has sent the shipping notification, you post a statistical goods receipt

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). | The Goods Receipt Purchase Order - warehouse screen displays. |  |
| 3 | Choose Good Receipt | Make the following entries:From the Trans./Event pull-down, select Goods ReceiptFrom the Reference Document pull-down menu, select Purchase orderIn thePurchase Orderfield, enter a <PO number>GR goods receipt: 101Choose Enter: | The Goods Receipt Purchase Order XXXXXXXXXX screen displays. |  |
| 4 | Change the quantity if necessary | If necessary, change the quantity in Detail Data section, Quantity tab. |  |  |
| 5 | Enter Goods Recipient | In Detail Data section, choose Where tab.Make the following entry:Goods Recipient: for example 331AChoose Enter. |  |  |
| 6 | Select Item OK | Select the Item OK checkbox at the bottom of the screen. |  |  |
| 7 | Save the documents | Choose Post. | The system generates a material document.You may record down the posted material document number at the bottom. |  |

|  |
| --- |
| Note To view the material document in FLP, open Display Material Documents List. |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000 (Inv Chg COGS w/CE) | 21120000 GR/IR | none |

##### Create Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation. You have two options to create the supplier invoice:

Option A: Create Supplier Invoice with PO/GR relation.

Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction).

You can choose either option A or option B to execute the supplier invoice creation with PO/GR relation. For more information, see the next two tasks.

Only choose either option A or B (not both).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad displays. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | Local Currency: If a purchase order was created with local currency in your system, make the following entries:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx> (reference invoice number from invoicing party)Invoicing Party:Foreign Currency: If a purchase order was created using foreign currency in your system, make the following entries:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx> (reference invoice number from invoicing party)Invoicing Party:Select See More at header area, make the following entries. :Exchange Rate: <XXX> | The Exchange Rate should be changed from USD to AED according to the customizing settings.The Exchange Rate is interchangeable. |  |
| 4 | Enter Purchase Order References | In Purchase Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Verify the Invoice Items data | Verify the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Verify Tax code | In the section Tax, verify if there is tax code information and enter the tax amount if the tax code value is greater than zero.In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code> . |  |  |
| 8 | Block invoice on item level (optional) | From the Purchase Order References section, choose the invoice item arrow (located on the right side of the item) to navigate to the item details.Select Manually Blocked.Select Check from the lower part of the details screen. The Blocking Reasons section shows the text Manual.Choose Back to Supplier Invoice . | The Create Supplier Invoice screen displays.The item is blocked with a blocking reason. |  |
| 9 | Verify the Balance | Calculate the tax by choosing Propose Tax. Verify the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose the Simulate button.You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier Invoice is simulated. |  |
| 11 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

#### Sales Item for 3rd Party w/o SN

Note:You can refer to this chapter if solution order has 3rd Party without SN item(TG13).

##### Display List of Purchase Requisitions to be Assigned

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed when you want to review your Purchase Requisitions and assign them to a vendor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is listed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The purchase requisition is selected. |  |
| 5 | Assign Supplier | Choose the Assign Source of Supply button. Select one source and choose the Assign button. | The Source of Supply is assigned.The Purchase Requisition is updated successfully. |  |

##### Convert Assigned Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If you want to use the Save Draft feature in this app, you have to use a personalized user. |

Purpose

You perform this activity to convert the assigned requisitions into purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is listed. |  |
| 3 | Search for Purchase Requisition | Enter the purchase requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The purchase requisition is selected. |  |
| 5 | Create Purchase Order | Choose the purchase requisition where the assigned supplier is displayed and choose Create Purchase Orders.Note Choose Yes to continue the process if any warning message occurs. | The Purchase Order screen displays. |  |

|  |
| --- |
| Note The print-out of the order confirmation is executed after the Purchase Order is created automatically and immediately.For handling print and for processing of purchase orders, see Building Block Procurement of Direct Materials, Step Review Purchase Order. |

##### Check the Status of the 3rd Party w/o SN Sales Item in the Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to verify the Status of a 3rd Party without SN Sales Item in Solution Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose the Manage Solution Orders application tile. | The list report page is displayed. |  |
| 3 | Find Solution Order | In the search area on the top, enter the ID of your solution order in the Search field.Choose Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4 | Open Solution Order in the Edit Mode | Choose the Solution Order and choose Display in the Solution Order Details tab. | The display view of the Solution Order will be opened. |  |
| 5 | Verify the Status of 3rd Party w/o SN Sales Item | In the tab area Items, under the field Status verify the status changed to Completed.Choose Refresh to verify the Status changed to Completed. | The Status is Completed. |  |

##### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation. You have two options to create the supplier invoice:

Option A: Create Supplier Invoice with PO/GR relation.

Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction)

You can choose either option A or option B to execute the supplier invoice creation with PO/GR relation. For more information, see the next two tasks.

|  |
| --- |
| Note Only choose either option A or B (not both). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoicing Party:Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Exchange Rate should be changed from USD in EUR according to the customizing settings. The Exchange Rate is changeable |  |
| 4 | Enter Purchase Order References | In Purchasing Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Block invoice on item level (optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Click Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Click Back to Supplier Invoice. | The item is blocked with a blocking reason. |  |
| 9 | Check the balance | Calculate the tax by choosing Propose Tax. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 11 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated. |  |
| 12 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

#### Bought-In Item

Note: You can refer to this chapter if solution order has Bought-In item(TG14).

##### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A purchase order is the request or instruction from a purchasing organization to a vendor (external supplier) or a plant to deliver a certain quantity of material or to perform services at a certain date. This process step shows you how to create purchase order.

Prerequisite

A purchase requisition has been generated through the sales order in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions (F1048A) screen displays. |  |
| 3. | Find the Purchase Requisition | Input the filters in Filter Bar and choose Go if necessary.Plant: 3310 | You can find the purchase requisition number in step Create Sales Order. |  |
| 4. | Choose the Sources of Supply | Click the sources in the line of your purchase requisition, and choose one by click |  |  |
| 5. | Create Purchase Order | Choose the purchase requisition and click Create Purchase Order at the right side center of the screen.If there is any warning message display, choose OK | The Purchase Orders Preview screen displays |  |
| 6. | Submit the Purchase Order | Select the purchase order type: Standard PO, and then choose Save.The purchase order number would be shown in the screen. | The purchase order is created in the SAP system. The system creates a message for the purchase order, so that the information from the purchase order can be transmitted to the vendor |  |

|  |
| --- |
| Note The print-out of the order confirmation is executed after the Purchase Order is created automatically and immediately. |

##### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A goods receipt is the physical entry of the goods and materials on-stock. The goods receipt usually comes from external suppliers or from in-house production. All goods receipts increase the stock. This process step shows you how to post goods receipt.

|  |
| --- |
| Note In this test script, the goods receipt is posted to an individual sales order stock. The valuation results from the purchase order. |

Prerequisite

The purchase order is created and the purchased material (bought-in-item) has arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Choose Field | Make the following entries and choose Enter:Executable Action in Transaction MIGO: <Goods Receipt>Reference Document for MIGO Transaction: <Purchase Order> |  |  |
| 4 | Input Purchase Order Number | Make the following entries, and choose Enter:Movement Type: GR Goods receipt 101Field next to Purchase Order: <Purchase Order Number> |  |  |
| 5 | Change Quantity | Change the quantity in Unit of Entry in Item details, Quantity tab, from 10 to 9.Note The delivered quantity (9 PC) varies from the ordered quantity (10 PC). |  |  |
| 6 | Enter Goods Recipient | In Detail data, navigate to Where tab, Make the following entries, and choose EnterStorage Location For example: 331A |  |  |
| 7 | Select Item OK | Select the item OK checkbox at the bottom of the screen |  |  |
| 8 | Save the Documents | Click Post button. | The goods receipt for the purchase order was posted to the sales order stock (look on the Where tab).You may record down the posted material document number at the bottom. |  |

|  |
| --- |
| Note As soon as the goods receipt is posted, you get a system message regarding the document number of the goods receipt. To view the material document in FLP, In the Materials Management Warehouse Processing group, open Material Documents Overview. |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory TrandingGd | 21120000 GR/IR | none |

##### Check the Status of the Bought-In Item Sales Item in the Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to verify the Status of a Bought-In Sales Item in Solution Order.

Prerequisite

Before checking the status, you need to complete Create Delivery, Execute Picking, and Post Goods Issue sections from Standard Sales Item chapter

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose the Manage Solution Orders application tile. | The list report page is displayed. |  |
| 3 | Find Solution Order | In the search area on the top, enter the ID of your solution order in the Search field.Choose Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4 | Open Solution Order in the Edit Mode | Choose the Solution Order and choose Display in the Solution Order Details tab. | The display view of the Solution Order will be opened. |  |
| 5 | Verify the Status of Bought-In Item Sales Item | In the tab area Items, under the field Status verify the status changed to Completed.Choose Refresh to verify the Status changed to Completed.Note The Status gets updated to Completed only after the delivery of bought-in item | The Status is Completed. |  |

##### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation. You have two options to create the supplier invoice:

Option A: Create Supplier Invoice with PO/GR relation.

Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction)

You can choose either option A or option B to execute the supplier invoice creation with PO/GR relation. For more information, see the next two tasks.

|  |
| --- |
| Note Only choose either option A or B (not both). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountantrole. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Exchange Rate should be changed from USD in EUR according to the customizing settings. The Exchange Rate is changeable |  |
| 4 | Enter Purchase Order References | In Purchase Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code> . |  |
| 8 | Block invoice on item level (optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Click Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Click Back to Supplier Invoice. | The item is blocked with a blocking reason. |  |
| 9 | Check the balance(optional) | Calculate the tax by choosing Propose Tax. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 11 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated. |  |
| 12 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

#### Sales Item for Services

|  |
| --- |
| Note You can refer to this chapter if solution order has Sales item of Service (SM0001).Note: No activity required for sales item for service, once the sales order is created proceed for create billing document chapter. |

#### Sales Item for Non-Stock

|  |
| --- |
| Note You can refer to this chapter if solution order has Non-Stock item(NS0002). |

##### Check the Status of the Non-Stock Item in the Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to verify the Status of a Non-Stock Sales Item in Solution Order.

Prerequisite

Before checking the status, you need to complete Create Delivery section from Standard Sales Item chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose the Manage Solution Orders application tile. | The list report page is displayed. |  |
| 3 | Find Solution Order | In the search area on the top, enter the ID of your solution order in the Search field.Choose Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4 | Open Solution Order in the Edit Mode | Choose the Solution Order and choose Display in the Solution Order Details tab. | The display view of the Solution Order will be opened. |  |
| 5 | Verify the Status of Bought-In Item Sales Item | In the tab area Items, under the field Status verify the status changed to Completed.Choose Refresh to verify the Status changed to Completed.Note: The Status gets updated to Completed only after the delivery. | The Status is Completed. |  |

Note: Succeeding Processes: After completing the status check proceed with Post Goods Issue chapter from test script 2ET Sales Order Processing for Non-Stock Material.

#### Sales Kits

|  |
| --- |
| Note You can refer to this chapter if solution order has sales kit items (SDBOMERLAHD or SDBOMLUMFHD or SDBOMCPFHHD). |

|  |
| --- |
| Note Refer to test script Sales Order Processing for Sales Kits (31Q) |

#### Customer Down Payment (Optional)

You can refer to the scope item: 7S7 or BKJ for more information.

|  |
| --- |
| Note Once the sales order is created in solution orders, navigate to the sales order and modify the item category to CBAO Milestone-Bill.Plan then proceed with the follow-up process. |

#### Advanced Intercompany Sales (Optional)

You can refer to the scope item: 5D2 for more information.

|  |
| --- |
| Note Once the sales order is created in solution orders, navigate to the sales order app and proceed with the follow-up process. |

#### Digital Payments (Optional)

You can refer to the scope item: 1Z1 for more information.

|  |
| --- |
| Note Once the sales order is created in solution orders, navigate to the sales order app and proceed with the follow-up process. |

#### SEPA Direct Debit Handling (Optional)

You can refer to the scope item: BKX for more information.

#### Returnable Sales Item

You can refer to this chapter if the solution order has returnable sales items (RP002).

|  |
| --- |
| Note As RP002 is a non-billable item, the invoice is not required. |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully. Delivery number displays on Deliveries tab. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management. |

To avoid open deliveries, ensure there is sufficient inventory quantity at the time for delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.

You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).

You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.

You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation Rejected with An Error Message.

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) |  |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery Number, and choose Continue.From the Outbound Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Outbound Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the DELIVERY_PICK_LIST Output Type, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

##### Execute Picking

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
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |

##### Post Goods Issue

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose Post Goods Issues.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested, the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount displays.To check the financial document, use the Warehouse Clerk role, and access the Display Material Document List - Deprecated (MB51) app. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Sales Order Fulfillment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to address the problems that occur during the sales order fulfillment process.

Procedure

Refer to the test script BKK - Sales Order Fulfillment Monitoring and Operations for detailed procedure.

### Manage Service Order

Test Administration

Customer project: Fill in the project-specific parts.

| Test Case ID | <X.XX> | Tester Name | Testing Date | Enter a test date. |
| --- | --- | --- | --- | --- |
| Business Role(s) |  |  |  |  |
| Responsibility | <State the Service Provider, Customer or Joint Service Provider and Customer> |  | Duration | Enter a duration. |

Purpose

In this step the service order previously created in solution order will be processed for service conformation.

Note: Refer to chapters mentioned in the below table from test scripts Service Order Management and Monitoring (3D2) and Procurement for Service Management (3NI)

| Process | Material | Chapters to Refer from 3D2 and 3NI Test Script |
| --- | --- | --- |
| Service Item | SRV_01 | Create Confirmation(3D2), Release Confirmation for Billing(3D2) |
| Service Expense Item | SRV_02 | Create Confirmation(3D2), Release Confirmation for Billing(3D2) |
| Service Part (Undefined) | SRV_03 | Create Confirmation(3D2)Convert Purchase Requisitions to Purchase Orders for Consumption Materials(3NI)Goods Receipt of Material Items for Consumption Materials(3NI)Create Supplier Invoice with PO Reference without Flexible Workflow(3NI)Release Confirmation for Billing(3D2) |
| Service Part (Defined) | SRV_04 | Create Confirmation(3D2)Convert Purchase Requisitions to Purchase Orders for Consumption Materials(3NI)Goods Receipt of Material Items for Consumption Materials(3NI)Create Supplier Invoice with PO Reference without Flexible Workflow(3NI)Release Confirmation for Billing (3D2) |
| Service Item (Service Part picked from stock) | SRV_05 | Create Confirmation (3D2), Release Confirmation for Billing (3D2) |
| Service Bundle | SRV_BUNDLE_01 | Fixed Price Service Bundle (3D2) |

### Manage Service Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the service contract previously created in solution order will be processed for billing document request.

| Process | Material | Chapters to Refer from 3MO Test script |
| --- | --- | --- |
| Service Contract Item | SRV_CONTRACT | Schedule Billing Document Request Creation, Manage Billing Document Request |

### Manage Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the subscription previously created in solution order will be processed for pre-billing.

Note: Refer to test script Subscription Management with Sales Billing (57Z) sections Display Subscription in SAP Subscription Billing and Display Provider Contract to view the subscription and provider contract.

| Process | Material | Chapters to Refer from 57Z Test Script |
| --- | --- | --- |
| Subscription Billing | P-CLD_STORAGENote If you are using price calculation scenario, then use product: P-CLD_STORAGE_PCS. | Display Pre-Bill in SAP Subscription Billing |

### Manage Customer Project

#### Display Customer Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the customer project previously created in solution order will be displayed and verified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Project Manager – Professional Services. | The Fiori Launchpad with access to the Plan Customer Projects application is displayed. |  |
| 2 | Open Plan Customer Projects | Choose Plan Customer Projects application tile. |  |  |
| 3 | Find Customer Project | In the search area on the top,enter <your project name> or enter the project ID from the transaction history of the Solution Order.Hit Enter.Note: The Project ID is a concatenation of Solution Order ID and item number. | Your customer project is displayed in the Plan Customer Projects application. |  |
| 4 | Verify Customer Project | Verify that the basic project details in the information view fit to the maintained data in the solution order. | The basic project details are verifiedNote: Customer Projects created from a Solution Order cannot be deleted and the setting for Use Project Billing (New): Yes cannot be changed. |  |
| 5 | Change project duration | Adjust some basic project details in the information view.Choose Edit.Change the Duration by extending the end date by a month. | Project dates are updated in Solution Order, situation is raised in case dependent items exist.Note: After the release of the project item in the Solution Order the item details cannot be changed. But the following information from the Customer Project are kept in sync till the stage of In Execution is reached:Project NameProject ManagerProject DurationProfit Center |  |

#### Plan Customer Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the customer project previously created in solution order will be planed and released for execution.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Project Manager – Professional Services. | The Fiori Launchpad with access to the Plan Customer Projects application is displayed. |  |
| 2 | Open Plan Customer Projects | Choose Plan Customer Projects application tile. |  |  |
| 3 | Find Customer Project | In the search area on the top,enter <your project name> or enter the project ID from the transaction history of the Solution Order.Hit Enter.Note: The Project ID is a concatenation of Solution Order ID and item number. | Your customer project is displayed in the Plan Customer Projects application. |  |
| 4 | Maintain Work Packages and Time-Based Planning for Fixed Price Item | On the Plan Customer Projects screen, choose Work Packages view and choose Edit.Create a new work packages by choosing Create.In the Add Work Package dialog box, make the following entries and choose OK:Name: <BBP1>Duration: <today - 2 days> to <today + 1 monthDescription: <Blue Print Phase 1>Work Package Type: Resource Based (Time)Choose Select in the Work Item column. In the Select Work Items dialog box, select <P001> work item line and choose OK.Choose › at the end of the work package item line. On the I-1000 details page, in the Team section, choose Add Team Role. In the Add Role dialog box, maintain a new role with below entries and choose Add:Role: <Junior Consultant>Delivery Organization: <Service Organization – Company DE>Work Item: <work item>Effort: 100You can select Billable or Non Billable from Billing Control Category dropdown list. Choose Settings icon to display Billing Control Category field in the table.Note: Refer to Maintain Work Packages and Time-Based Planning section in Customer Project Management – Project-Based Services (J11) test script for more details.Choose < icon and go back to the Plan Customer Projects screen. |  |  |
| 5 | Maintain Work Packages and Time-Based Planning for Time and Expense Item | On the Plan Customer Projects screen, choose Work Packages view and choose Edit.Create a new work packages by choosing +.In the Add Work Package dialog box, make the following entries and choose OK:Name: <BBP2>Duration: <today - 2 days> to <today + 1 monthDescription: <Blue Print Phase 2>Work Package Type: Resource Based (Time)Choose Select in the Work Item column. In the Select Work Items dialog box, select <P001> work item line and choose OK.Choose › at the end of the work package item line. On the I-1000 details page, in the Team section, choose +. In the Add Role dialog box, maintain a new role with below entries and choose OK:Role: <Junior Consultant>Delivery Organization: <Service Organization – Company DE>Work Item: <work item>Effort: 9You can select Billable or Non Billable from Billing Control Category dropdown list. Choose Settings icon to display Billing Control Category field in the table.Note: Refer to Maintain Work Packages and Time-Based Planning section in Customer Project Management – Project-Based Services (J11) test script for more details.Choose ‹ icon and go back to the Plan Customer Projects screen. |  |  |
| 6 | Maintain Work Package Staffing | In the Team section, choose Add Resource for Staffed Resource. Choose the employee in the Resource dialog box, and choose Add to Role.Choose Save.Note: Refer to Maintain Work Package Staffing (Without Scope Item 6JO - Advanced Resource Management- Project-Based Services) section in Customer Project Management – Project-Based Services (J11) test script for more details. |  |  |
| 7 | Maintain Customer Project Billing | Choose Information view and choose Edit. In the Stage field, choose Contract Preparation.In the message box“Please review the preferred billing solution for this project as you cannot change this setting after the Contract Preparation stage. To update this setting, change the stage to In Planning”Choose Close.Choose Save.Choose Billing view, and make the following entries:For fix price:Contract Type: Fixed PriceDescription: <Description>Assigned Work Packages: BBP1Profit Center: <profit center>Amount to be billed: 500.00Choose › icon and go to Billing Details page. On the Billing Due Dates tab, make the following entry:Billing Due Date: <today>Amount: 500.00Choose ‹ icon and go back to the Plan Customer Projects – Billing screen.For Time & Expense:Contract Type: Time and ExpensesDescription: <Description>Assigned Work Packages: BBP2Profit Center: <profit center>Amount to be billed: 1000.00Choose › icon and go to Billing Details page. On the Billing Due Dates tab, make the following entry:Billing Due Date: <today>Amount: 1000.00Choose ‹ icon and go back to the Plan Customer Projects screen. Choose Save and choose Information view. In the Stage field, choose In Execution.Choose Save.Refer to Maintain Customer Project Billing section in Customer Project Management – Project-Based Services (J11) test script for more details. |  |  |

#### Check Sales Price

Purpose

This process step shows you how to check the sales price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111). | The Manage Prices - Sales screen displays. |  |
| 3 | Check Sales Price | Make the following entries and choose Go:Condition Type: PSP0Service Organization: 3310Sales Org.: 3310Distribution Channel: 10Product: From T001 to T005Kindly be aware that according to your business requirements, another two condition types PCP0 and SOV2 can be defined here for project-specific sales price and employee overtime sales price. | The sales prices are maintained for the five materials/roles.Project planned revenues for different roles are calculated based on these values. |  |

#### Time Recording for Staffed Resources(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to do time recording for staffed resources. Refer to Time Recording through Manage My Timesheet section of Time Recording – Project-Based Services (J12) test script for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Time Recording for Staffed Resources | Refer to J12 test script sections Time Recording for Staffed Resources. |  |  |

#### Create Supplier Invoice for Travel Expenses(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create supplier invoice for travel expenses. Refer to Posting Expenses for Internal Employees w/o PO Relation section of Service and Material Procurement – Project-Based Services (J13) test script for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Time Recording for Staffed Resources | Refer to J13 test script sections Posting Expenses for Internal Employees w/o PO Relation . |  |  |

#### Check Billing Element and Create Billing Document Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can check if the amounts are displayed correctly in Manage Project Billing(F4374) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check and create Billing Document Request for Fixed Price Items | Refer to 4E9 test script sections Billing For Fixed Price Item. | Billing Document Request Created |  |
| 2 | Prepare Billing for Time and Expense items including Postponement and Write Off | Refer to 4E9 test script sections Billing For Time and Expense Item | Billing Document Request Created |  |

### Manage Billing Document

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the billing clerk creates an invoice for the solution order items.

Note: It is possible to create combined invoice of solutionorder document and include the project items . For more information, see the scopeitem Omnichannel Convergent Billing (1MC) to create the invoice. However, credit anddebit memo requests creation from this invoice is not possible.If you need this,refer to the [Create Billing Document (Project Item)](#unique_45) [page ] 88.

Refer to the SAP note 3413050 for an example on how to create combined invoice ofsolution order document.

Note: A proforma invoice can be created for solution ordersales items with the billing type F8(for delivery related billing) or billing typeF5(for order related billing).

The items for billing type F8: Standard sales item, Bought-in item, and Sales item fornon-stock materials.

The items for billing type F5: Sales item for 3rd party with SN, Sales item for 3rd partywithout SN, and Sales item for service.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen isdisplayed. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar, you can make the following settings asbelow:Set billing date and type before billing:ONCreate separate billing document for each item of billingdue list: OFFAutomatically post billing documents:ONDisplay billing documents after creation:ON | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Search for Billing Due List | In the search condition, adapt the filter to use the Solution Order ID as searchcriteria. | All billing due list items belonging to the Solution Order should be displayed:- Delivery- Billing Document Requests (from Service Order, Service Contract and Subscription) |  |
| 5 | Select Item(s) for Billing | Select row(s) in the Billing Due List created previously and choose CreateBilling Documents.Note It is possible to combine all the items in the solution orderand create a single invoice, at the same time individual invoicecan be created for different items in solution order by choosingthe individual billing due list items. | The Create Billing Document screen is displayed. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice(F2) and maintain billing date, for example currentdate, then choose OK. |  |  |
| 7 | Save Billing Document | On the Billing Document screen, chooseSave.The draft version billing document with ID Sxxxxxxxx turns into asaved billing document with ID xxxxxxxx, make a note of thebilling document number: __________.Note In case the Billing Due List cannot be combined into a singleinvoice a Split Analysis button willbe displayed. In that case you will have to createindividual billing documents.If URR relevant product URR_MAT1_NORM was also added tosolution order then refer to section 4.1 of scope item 3KKto view the URR specific details | The system generates an invoice for billing.Billing status of the individual items in the Solution Order isupdated. |  |

#### Create Billing Document (Project Item)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a customer invoice. An Invoices and Journal Entries are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents(F0798) - Billing Due List Items. | The Billing Due List screen displays. |  |
| 3 | Select Document to be Invoiced | In the search condition, adapt the filter to use the Solution Order ID as search criteria.Select the billing document request you created and choose Create Billing Documents.SD Document Category: Billing Document RequestBilling Date: <today> | The Create Billing Documents screen displays. |  |
| 4 | Enter Billing Details | Enter the following and choose OK:Billing Type: Invoice (CI01)Billing Date: <today> | The draft bill ing document with ID Sxxxxxxxx display. |  |
| 5 | Save Billing Document | On the Maintain Billing Document screen, select Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________ | The system generates an invoice for billing. |  |
| 6 | Check Billing Element | Log on to the SAP Fiori launchpad as Billing Specialist.Open Manage Project Billing app, make the filter to find out the Billing item with your project.Choose the Billed link. Related Invoices screen comes out.Check if amounts are displayed correctly. | The Unbilled column is 400 EUR, To Be Billed column 0, Written Off column 300 EUR, Billing In Process 0 . Billed 300 EUR, |  |

#### Display Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step displays the solution order billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Billing Documents (VF03). | The Display Billing Documents screen is displayed. |  |
| 3 | Search the Billing Document Created in Previous Step | Enter <the Billing document number recorded in Create Billing Document step>.Choose Continue. | The billing document is displayed. |  |
| 4 | Display Output | On the Invoice XXXXXXXX(F2) Display: Overview of Billing Items screen, choose More > Goto > Header > Output. | The Invoice XXXXXXXX(F2) Display: Output screen is displayed. |  |
| 5 | Display Print Preview | Select the output line and choose Display Document. | Print preview for PDF file is displayed. The Solution Order is available on the print form. |  |

### Credit Memo Request

#### Create Credit Memo Request with reference to invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the internal sales representative creates a credit memo request for the invoice that was created for solution order in the previous step.

Table 2: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal sales representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Credit Memo Requests. | The Manage Credit Memo Requests screen is displayed. |  |
| 3 | Navigate to Create Credit Memo Request | Click on button Create Credit Memo request | The Create Sales Documents Screen is displayed |  |
| 4 | Create Credit Memo Request | Make the following entries :Order Type: CR (Credit Memo Request)Choose Create with Reference,In the field Billing Document,enter the Invoice number (Solution order invoice number)Choose CopyPress Enter | The Create Credit Memo Request overview screen is displayed. |  |
| 5 | Enter Order Reason | On the Sales tab enter an Order Reason for example: Poor Quality | The order reason is recorded. |  |
| 6 | Save | Choose SaveNote the ID of the Credit Memo DocumentNote If the message “Enter a valid Business Transaction for Brazil” appears, go to the Country tab at the item level, select the Additional Fiscal Data button, enter the country specific attributes and confirm. | The Credit Memo Request is created. |  |

#### Approve Credit Memo Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the Sales Manager approves the credit memo request.

Prerequisite

Approval status of the Credit Memo Request is In Approval

Table 3: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Receive Notification | Open My Inbox -All Items.You can also choose Notification icons on the top right corner to navigate to My Inbox screen | Then Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve | You receive the notification of the credit memo request. Choose the option Release on the bottom bar. | The Submit Decision dialog box displays. |  |
| 5 | Submit | Enter some comments and choose Submit. | The Credit Memo request has been approved. |  |

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the billing clerk creates a credit memo for the credit memo request created in the previous step .

Table 4: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen is displayed. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Find Credit Memo Request in Search | Maintain the following search criteria :SD Document Category: <Credit Memo Request>SD Document:<Credit Memo Request ID created in previous step>Choose Go | Your credit memo request is displayed in the list. |  |
| 5 | Choose Credit Memo Request | Select your credit memo request in the listChoose Create Billing Documents. | The Create Billing Documents (F0798) screen displays.. |  |
| 6 | Maintain Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, for example <current date>.Choose OK. | The new billing document is created. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The credit memois created |  |

### Customer Returns

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a return order.

|  |
| --- |
| Note The return order can be created either with reference to the original billing document or with reference to the sales order which is generated from the solution order. |

Prerequisite

You must have billing document, pro-forma invoice or sales order as reference

|  |
| --- |
| Note If the return order is created with reference to sales order an outbound delivery must be created, this is applicable for the standard sales items, bought-in sales item, and sales item for non-stock materials. |

Procedure

Refer to the test script BKP - Customer Returns for detailed procedure.

|  |
| --- |
| Note For Returnable Sales Items create the return order with reference to the sales order, which was generated from the solution order |

### Solution Order Profitability Dashboard (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP Analytics Cloud (SAC) provides a comprehensive tool for strategic live-data analysis in solution business. The Purpose is to help the Sales Manager to review the net value of incoming solution orders as well as reviewing the profitability of one or more solution orders.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Choose Solution Order Profitability under Solution Order Analytics. | The Screen is Navigated to the Overview Page, which shows the following:Net Value of Incoming Solution Orders, Revenue and Profit MarginNet value of Incoming Solution Order Items by Geography, Sold-To Party, Lifecycle Status and ProductNet value of Incoming Solution Order Items by time period. |  |
| 3 | Solution Order List | Choose the Solution Order List dropdown. | The Solution Order List screen shows the following:No. of Released Solution Orders, No. of Solution Orders in Execution excl Life Cycle Status CompletedSolution Order Details. |  |
| 4 | Profitability | Choose the Profitability dropdown. | The Profitability screen shows the following:Recognized Margin, Profit Margin, Recognized Revenue, Recognized Cost, Net Value of Incoming Solution Orders, Revenue, Cost, Profit by Month and ProductSolution Order Item Details. |  |

## Appendix

### Equipment linkage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to assign an equipment in sales order and link to service contract item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose Manage Solution Orders application tile. | The list report page is displayed. |  |
| 3 | Create Solution Order | Choose Create button from the solution order list page | Create Solution Order window will be displayed |  |
| 4 | Maintain Solution Order data | Enter the following data to create a solution order:Description: <your description>External Reference: <your reference>Sold-To Party: e.g. 17100001 for US (Domestic Customer US 1)Note: Select the sales organization (e.g. 1710) and Contact person from the popup appears | Required header data for the Solution order has been maintained. |  |
| 5 | Add Sales Item and service contract item | Maintain the following Sales Item and Service Contract item in the solution order:Product ID: for example, FG126 (Sales Item)Quantity: for example, 1Unit: for example, PCChoose Enter.Product ID: for example, SRV_CONTRACT (Service Contract Item)Quantity: for example, 1Unit: for example, AUChoose Enter. | The Sales Order items are now added to Solution Order |  |
| 6 | Assign item relationship between sales and service contract item | Select Sales item and choose Define Item Relationship.In Item Relationship choose Serviced by from the drop down.In Item No. Choose service contract item from F4 help.Choose OK.Choose Save. | Assigned relationship between sales and service contract item |  |
| 7 | Release line items in Solution Order | In the tab area Items, choose Release All Items in the All Items view.Note: Note down the IDs of the follow-up transactions. | Items in solution order has been released |  |
| 8 | Create Delivery | Refer to section Create Delivery from test script Sell from Stock(BD9)Note: Choose Delivery Type - LF |  |  |
| 9 | Execute Picking and Assign Equipment | Refer to section Execute Picking from test script Sell from Stock(BD9).To assign equipment: In Service number tab choose add and assign an equipment.Choose Save. |  |  |
| 10 | Post Goods Issue | Refer to section Post Goods Issue from test script Sell from Stock(BD9) |  |  |

### Further supported Scope Items

| Scope Item | Business Condition |
| --- | --- |
| 1EZ: Credit Memo Processing | This scope item can be used in the context of solution order management |
| 1F1: Debit Memo Processing | This scope item can be used in the context of solution order management |
| BDQ: Invoice Correction Process with Debit Memo | This scope item can be used in the context of solution order management |
| BKL: Invoice Correction Process with Credit Memo | This scope item can be used in the context of solution order management |
| 1MC: Omnichannel Convergent Billing | This scope item can be used in the context of solution order management |
| BKZ: Sales Order Processing with Invoice List and Collective Billing | This scope item can be used in the context of solution order management |
| 3TE: Customer Returns for Non-Stock and Service Materials | This scope item can be used in the context of solution order management |
| 5CX: Customer Returns for Sales Kits | This scope item can be used in the context of solution order management |
| BKP: Customer Returns | This scope item can be used in the context of solution order management |
| 1JW: Advanced Available-to-Promise Processing | This scope item can be used in the context of solution order management |
| BD6: Basic Credit Management | This scope item can be used in the context of solution order management |
| 1HO: Intercompany Sales Order Processing – Domestic | This scope item can be used in the context of solution order management |
| 1MX: Intercompany Sales Order Processing – International | This scope item can be used in the context of solution order management |
| 2F4: Intercompany Process for Customer Returns | This scope item can be used in the context of solution order management |
| 1WO: Extended Intercompany Processes for Sales | This scope item can be used in the context of solution order management |
| 1W8: Legal Control | This scope item can be used in the context of solution order management |
| 1WC: Embargo Control | This scope item can be used in the context of solution order management |
| 1WE: Restricted Party Screening with SAP Watch List Screening | This scope item can be used in the context of solution order management |
| 3G8: Dangerous Goods in the Value Chain | This scope item can be used in the context of solution order management |
| 6W2: Manual Transportation Planning | This scope item can be used in the context of solution order management |
| 6W3: Transportation Execution | This scope item can be used in the context of solution order management |
| 6W4: Freight Settlement | This scope item can be used in the context of solution order management |
| 21D: Make-to-Stock Production with Variant Configuration | This scope item can be used in the context of solution order management |
| 5IK: Subscription Management with Convergent Invoicing | This scope item can be used in the context of solution order management |
| 43Y: Contract Accounting – Integration with Sales Documents | This scope item can be used in the context of solution order management |
| BKJ: Sales Order Processing with Customer Down Payment | This scope item can be used in the context of solution order management |
| 7S7: Sell from Stock with Down Payment Processing | This scope item can be used in the context of solution order management |
| 7Z1: | This scope item can be used in the context of solution order management |
| 7SZ: |  |
| 1Z1: Digital Payments – Sales | This scope item can be used in the context of solution order management |
| BKX: Sales Order Processing – SEPA Direct Debit Handling | This scope item can be used in the context of solution order management |
| 3KK: Contract-Based Revenue Recognition – IFRS | This scope item can be used in the context of solution order management to use Universal Revenue Recognition for IFRS |
| 3VS: Contract-Based Revenue Recognition – US GAAP | This scope item can be used in the context of solution order management to use Universal Revenue Recognition for US GAAP |
| 5SW: Subscription Management for Software | This scope item can be used in the context of solution order management |

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
> Flagged while digesting this document, not verified: Bought-in purchasing info record (TG14, supplier 33300001) is created with condition Amount 300 AED and purchasing group 002, but follow-on notes say net price is 35 AED, then repeat with purchasing group 001 and net price 25 AED; values are not clearly reconciled.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Billing Document (Project Item) expected result lists Unbilled 400 EUR, Written Off 300 EUR, Billed 300 EUR, which does not obviously match the planned billing amounts of 500.00 (fixed price) and 1000.00 (time and expense) in Plan Customer Project.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 168,723 chars in the whole document
