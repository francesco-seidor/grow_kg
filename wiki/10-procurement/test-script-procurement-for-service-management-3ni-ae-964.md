---
id: 10-procurement/test-script-procurement-for-service-management-3ni-ae-964
title: "Test Script: Procurement for Service Management (3NI_AE) (3NI_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 3NI: procurement of consumption materials and external workforce integrated with service orders."
cluster: 10-procurement
tags: [kb/procurement, topic/procurement-of-services, topic/service-order-management-and-billing]
aliases: [3NI_S4CLD2608_BPD_EN_AE]
keywords: [Procurement of Services, service management procurement, purchase requisitions, purchase order creation, purchase order approval, flexible workflow, service entry sheets, goods receipt, supplier invoices, evaluated receipt settlement]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NI_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-964
topic: 10-procurement/procurement-of-services
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Procurement for Service Management (3NI_AE) (3NI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Procurement of Services** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Procurement for Service Management (3NI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232853391)

[2 Prerequisites 5](#_Toc232853392)

[2.1 System Access 5](#_Toc232853393)

[2.2 Roles 5](#_Toc232853394)

[2.3 Master Data, Organizational Data, and Transactional Data 6](#_Toc232853395)

[2.4 Business Conditions 8](#_Toc232853396)

[2.5 Preliminary Steps 9](#_Toc232853397)

[2.5.1 Open New MM Period 9](#_Toc232853398)

[2.5.2 Create Info Record 9](#_Toc232853399)

[2.5.2.1 Create Info Record for Consumption Materials Procurement (Optional) 9](#_Toc232853400)

[2.5.2.2 Create Info Record for External Workforce Procurement (Optional) 10](#_Toc232853401)

[2.5.3 Manage Source Lists 12](#_Toc232853402)

[2.5.3.1 Manage Source Lists for Consumption Materials Procurement (Optional) 12](#_Toc232853403)

[2.5.3.2 Manage Source Lists for External Workforce Procurement (Optional) 13](#_Toc232853404)

[2.5.4 Activate Flexible Workflow for Purchase Order Approval (Optional) 14](#_Toc232853405)

[2.5.5 Configure Flexible Workflow for Purchase Order (Optional) 15](#_Toc232853406)

[2.5.6 Configure Flexible Workflow for Service Entry Sheets 16](#_Toc232853407)

[2.5.7 Activate Flexible Workflow for Supplier Invoice 17](#_Toc232853408)

[2.5.8 Configure Flexible Workflow for Supplier Invoice 19](#_Toc232853409)

[2.5.9 Create Master Data for Automatic Purchase Order Creation from Purchase Requisition 21](#_Toc232853410)

[2.5.9.1 Change Material Master Data for Consumption Material (Optional) 21](#_Toc232853411)

[2.5.9.2 Change Material Master Data for External Workforce (Optional) 22](#_Toc232853412)

[2.5.9.3 Change Supplier Master Data - Purchasing Organization Data (Optional) 23](#_Toc232853413)

[2.5.10 Create Master Data for Evaluated Receipt Settlement (Optional) 23](#_Toc232853414)

[2.5.11 Assign Condition Type to Item Categories 24](#_Toc232853415)

[2.5.12 Account Assignment Category for Service Management Integration (Optional) 26](#_Toc232853416)

[2.5.12.1 Maintain Account Assignment Category (Optional) 26](#_Toc232853417)

[2.5.12.2 Define Combination of Item Categories/Account Assignment Categories (Optional) 29](#_Toc232853418)

[2.5.12.3 Define Account Assignment Category for Procurement (Optional) 31](#_Toc232853419)

[2.5.13 Check Service Material for External Workforce 32](#_Toc232853420)

[3 Overview Table 34](#_Toc232853421)

[4 Test Procedures 37](#_Toc232853422)

[4.1 Check Purchase Requisitions (Optional) 37](#_Toc232853423)

[4.2 Create Purchase Order against Purchase Requisition 38](#_Toc232853424)

[4.2.1 Option A: Automatic Purchase Order Creation from Purchase Requisition 38](#_Toc232853425)

[4.2.2 Option B: Convert Purchase Requisitions to Purchase Orders for Consumption Materials 40](#_Toc232853426)

[4.2.3 Option C: Convert Purchase Requisitions to Purchase Orders for External Workforce 41](#_Toc232853427)

[4.3 Approve Purchase Order (Optional) 43](#_Toc232853428)

[4.4 Reject Purchase Order (Optional) 44](#_Toc232853429)

[4.5 Change Purchase Order (Optional) 45](#_Toc232853430)

[4.6 Monitor Purchase Order Assignment in Service Document 46](#_Toc232853431)

[4.6.1 Monitor Purchase Order Assignment in Service Order (Optional) 47](#_Toc232853432)

[4.6.2 Monitor Purchase Order Assignment in Repair Order (Optional) 47](#_Toc232853433)

[4.7 Check Purchasing Document List (Optional) 48](#_Toc232853434)

[4.8 View Purchase Order Output 49](#_Toc232853435)

[4.9 Post Goods Receipt of Material Items for Consumption Materials 50](#_Toc232853436)

[4.10 Maintain Service Entry Sheet for External Workforce (Optional) 51](#_Toc232853437)

[4.11 Maintain Service Entry Sheet with Service and Spare Part (Optional) 53](#_Toc232853438)

[4.12 Approve Service Entry Sheet for External Workforce (Optional) 54](#_Toc232853439)

[4.13 Monitor Goods Receipt in Service Document for Consumption Materials 55](#_Toc232853440)

[4.13.1 Monitor Goods Receipt in Service Order for Consumption Materials (Optional) 56](#_Toc232853441)

[4.13.2 Monitor Goods Receipt in Repair Order for Consumption Materials (Optional) 56](#_Toc232853442)

[4.14 Check Goods Receipt Details for Consumption Material (Optional) 57](#_Toc232853443)

[4.15 Check Service Entry Sheet Details for External Workforce 58](#_Toc232853444)

[4.15.1 Check Service Entry Sheet Details for External Workforce in Service Order (Optional) 58](#_Toc232853445)

[4.15.2 Check Service Entry Sheet Details for External Workforce in Repair Order (Optional) 59](#_Toc232853446)

[4.16 Reverse Goods Receipt for Consumption Materials (Optional) 60](#_Toc232853447)

[4.17 Monitor Reverse Goods Receipt In Service Document for Consumption Materials 61](#_Toc232853448)

[4.17.1 Monitor Reverse Goods Receipt in Service Order for Consumption Materials (Optional) 61](#_Toc232853449)

[4.17.2 Monitor Reverse Goods Receipt in Repair Order for Consumption Materials (Optional) 62](#_Toc232853450)

[4.18 Create Supplier Invoice with PO Reference 63](#_Toc232853451)

[4.18.1 Option A: Create Supplier Invoice with PO Reference without Flexible Workflow 63](#_Toc232853452)

[4.18.2 Option B: Create Supplier Invoice with PO Reference with Flexible Workflow 65](#_Toc232853453)

[4.18.2.1 Create Supplier Invoice with PO Reference 65](#_Toc232853454)

[4.18.2.2 Release Completed Supplier Invoice (Optional) 68](#_Toc232853455)

[4.18.2.3 Reject Supplier Invoice (Optional) 68](#_Toc232853456)

[4.18.2.4 Change Supplier Invoice (Optional) 69](#_Toc232853457)

[4.18.3 Option C: Create Supplier Invoice via Evaluated Receipt Settlement for External Workforce 70](#_Toc232853458)

[4.19 Monitor Supplier Invoice Assignment In Service Document 72](#_Toc232853459)

[4.19.1 Monitor Supplier Invoice Assignment in Service Order (Optional) 72](#_Toc232853460)

[4.19.2 Monitor Supplier Invoice Assignment in Repair Order (Optional) 73](#_Toc232853461)

[5 Appendix 75](#_Toc232853462)

[5.1 Process Integration 75](#_Toc232853463)

[5.1.1 Preceding Processes 75](#_Toc232853464)

[5.1.2 Succeeding Processes 75](#_Toc232853465)

## Purpose

Overview

The scope item covers the integration of service management with procurement of non-stock materials and external workforce. This facilitates automatic purchase requisition creation against service order line items and corresponding purchase order processing. A message is sent to the service order regarding purchase order creation. The purchasing manager can use a workflow to approve the purchase order. The goods receipt is executed, resulting in subsequent update of costs against the service order line item. The goods receipt against the purchase order sends a message to the service order.

The supplier invoice posting also updates the procurement costs in the confirmation against the service order line item. In case of billing the customer on sales price basis rather than the cost-plus basis, the sales price is copied from the sales condition instead of procurement costs. A workflow can be used to approve parked supplier invoices by the purchaser.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Customer Service Manager | SAP_BR_CUSTOMER_SRV_MANAGER | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |
| Master Data Specialist - Product Data. | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Employee - Procurement | SAP_BR_EMPLOYEE_PROCUREMENT | Self Services - Procurement | SAP_MM_SPT_EMPLOYEE_SERVICES_PC |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT | My Inbox / My Inbox - Buying | SAP_CORE_SPT_MYINBOX_PC / SAP_MM_SPT_BUYING_MYINBOX_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Customer Service Manager - In-House Repair | SAP_BR_CUST_SRVC_MGR_REPA | In-House Repair | SAP_BR_CUST_SRVC_MGR_REPA |  |

### Master Data, Organizational Data, and Transactional Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The service orders or repair orders and service confirmations or repair confirmations of your 3rd party application can be mapped to the following master and organizational data that is delivered by SAP Best Practices, or they can be mapped to your own master and organizational data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 |  | You must either assign the customer pricing procedure 01 (Procedure 01) or ensure that the customer is not assigned to a pricing procedure.To check the assignment, use business role SAP_BR_BUPA_MASTER_SPECIALIST and access Manage Customer Master Data (F0850A). |
| Employee |  | < Use your own employee ID that is assigned to your user ID.> |  |
| Sales Organization | 3310 |  |  |
| Material | SRV_01 | Service | Note SRV_01 is also used for external workforce procurement process. When you create a service order with SRV_01 for external workforce, you need to switch the item category from service item to external service item. |
| Material | SRV_03 | Spare Part | Note SRV_03 is used for consumption material procurement process and SRV_03 as a dummy material will not be supported for automatic purchase order creation from purchase requisition. |
| Material | SRV_04 | Managed Spare Part (Non-Stock) | Note SRV_04 is used for consumption material procurement process. |
| Supplier | 33300001 |  |  |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |
| Purchasing Organization | 3310 |  |  |
| Purchasing Group | 001 |  |  |
| Chart of Accounts | YCOA |  |  |
| G/L Account | 65100000 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the steps described in Create New Open MM Posting Period - MDS. The posting period must be up to date. |
| 3D2 - Service Order Management and Monitoring | You have completed all of the mandatory prerequisites. |
| 3XK - In-House Repair | You have completed all of the mandatory prerequisites. |
| 3MO - Service Contract Management | You have completed all of the mandatory prerequisites. |
| 4GA - Service Quotation | You have completed all of the mandatory prerequisites. |

### Preliminary Steps

#### Open New MM Period

Purpose

Information on material stock and certain valuation data such as total stock value, total stock, evaluation elements class, price control indicator, and price unit are held by the financial posting period. The period must be set up at the beginning of each new posting period to ensure values and goods movement are posted to the correct period. Usually, only the current posting period is open for posting, all other posting periods are closed.

A back posting to a previous period is only possible if the corresponding flag is set in the control record. This flag is automatically set at initialization and after each period change. In certain cases, however, it may be necessary to set the indicator manually.

Procedure

You must complete the steps described in Create New Open MM Posting Period - MDS (BNZ).

#### Create Info Record

##### Create Info Record for Consumption Materials Procurement (Optional)

Purpose

In this procedure, you create info records for consumption materials procurement process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Create New Info Record | Choose Create. | The New Purchasing Info Record screen displays. |  |
| 4 | Maintain Header Data | Under Header, make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: SRV_04Plant: 3310Purchasing Group: 001 |  |  |
| 5 | Maintain Additinoal Data | Make the following entries:Available From: <valid from date>Available To: <valid to date> |  |  |
| 6 | Maintain Delivery and Quantity Data | Under Delivery and Quantity, make the following entries:Delivery Time in Days: for example, 5Under Delivery Tolerance in %: for example, 10Over Delivery Tolerance in %: for example, 10Tax Code: <Input Tax Code>Order Unit: for example, EAStandard Order Quantity: for example, 1Goods-Receipt-Based Invoice Verification: Selected |  |  |
| 7 | Maintain Condition Data | Under Condition, choose Add and make the following entries:Valid From: <valid from date>Amount: for example, 60Pricing Unit: for example, 1Valid To: <valid to date>Currency: for example, AEDChoose Apply. |  |  |
| 8 | Save | Choose Save. | The purchasing info record is saved. |  |

##### Create Info Record for External Workforce Procurement (Optional)

Purpose

In this procedure, you create info records for external workforce procurement process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Create New Info Record | Choose Create. | The New Purchasing Info Record screen displays. |  |
| 4 | Maintain Header Data | Under Header, make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: SRV_01Plant: 3310Purchasing Group: 001 |  |  |
| 5 | Maintain Additional Data | Make the following entries:Available From: <valid from date>Available To: <valid to date> |  |  |
| 6 | Maintain Delivery and Quantity Data | Under Delivery and Quantity , make the following entries:Tax Code: <Input Tax Code>Order Unit: for example, HRStandard Order Quantity: for example,1Goods-Receipt-Based Invoice Verification: Selected |  |  |
| 7 | Maintain Condition Data | Under Condition, choose Add and make the following entries:Valid From: <valid from date>Amount: for example, 60Pricing Unit: for example, 1Valid To: <valid to date>Currency: for example, AEDChoose Apply. |  |  |
| 8 | Save | Choose Save. | The purchasing info record is saved. |  |

#### Manage Source Lists

##### Manage Source Lists for Consumption Materials Procurement (Optional)

Purpose

In ths step, you create a source list.

If you have more than one supplier, choose one fixed supplier in the source list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Choose Manage Source Lists (F1859). | The Manage Source Lists screen sisplays. |  |
| 3 | Create Source List | Choose Create. | The Source List screen displays. |  |
| 4 | Enter General Information | Under General Information, make the following entries:Material: for example, SRV_04Plant: for example, 3310Choose Generate. |  |  |
| 5 | Search | On the Generated Sources screen, make the following entries:Valid From: <valid from date>Valid To: <valid to date>Choose Go. |  |  |
| 6 | Choose Sources | Under Sources, select an item and choose Replace Existing.If you have warning message, choose OK. |  |  |
| 7 | Set Status | Under Source Lists, make the following entry for your supplier:Status: Fixed Status (Fixed) | The supplier is assigned the status. |  |
| 8 | Save | Choose Save. | The source list is created. |  |

##### Manage Source Lists for External Workforce Procurement (Optional)

Purpose

In ths step, you create a source list.

If you have more than one supplier, choose one fixed supplier in the source list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Choose Manage Source Lists (F1859). | The Manage Source Lists screen sisplays. |  |
| 3 | Create Source List | Choose Create. | The Source List screen displays. |  |
| 4 | Enter General Information | Under General Information, make the following entries:Material: for example, SRV_01Plant: for example, 3310Choose Generate. |  |  |
| 5 | Search | On the Generated Sources screen, make the following entries:Valid From: <valid from date>Valid To: <valid to date>Choose Go. |  |  |
| 6 | Choose Sources | Under Sources, select an item and choose Replace Existing.If you have warning message, choose OK. |  |  |
| 7 | Set Status | Under Source Lists, make the following entry for your supplier:Status: Fixed Status (Fixed) | The supplier is assigned the status. |  |
| 8 | Save | Choose Save. | The source list is created. |  |

#### Activate Flexible Workflow for Purchase Order Approval (Optional)

Purpose

In this procedure, you activate flexible workflow for purchase order approval.

If you want to use the flexible workflow to approve the purchase order, you must complete the following steps:

- Activate Flexible Workflow for Purchase Order Approval
- Configure Flexible Workflow for Purchase Order

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement |  |  |
| 5 | Open | Open Purchase Order Processing. |  |  |
| 6 | Select Configuration Step | For the Activate Flexible Workflow for Purchase Orders step, choose Configure. |  |  |
| 7 | Activate Flexible Workflow | Make sure the following entries are checked. If not, make the following entries and choose Save:Document Type: NBScenario based workflow: X | The scenario based workflow is active for purchase orders with document type NB.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens. |  |
| 3 | Activate Flexible Workflow | Make sure the following entries are checked. If not, make the following entries and choose Save:Document Type: NBScenario based workflow: X | The scenario based workflow is active for purchase orders with document type NB.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

#### Configure Flexible Workflow for Purchase Order (Optional)

Purpose

In this procedure, you configure your release conditions for purchase order approval.

Make sure that the flexible workflow for purchase document type NB has is activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Workflows for Purchase Orders Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Activate Workflow | Make sure the status of workflow Automatic Release of Purchase Order is Active. If not, select it and choose Activate.The system will check workflows with an Active status by their order. The first workflow whose preconditions are met will be executed. | The workflow is activated. |  |
| 4 | Create Workflow | Choose CreateMake following entries:Workflow Name: for example, Test Workflow for Purchase OrderUnder Start Conditions, make the following entries:Purchasing group of purchase order is: for example, 001Choose Creat another condition (+) and make the following entries:Total net amount of purchase order is greater than: 500AEDUnder Steps, choose Create and make the following entries:Step Type: Release of Purchase OrderAssignment By: UserUser: PURCHASING_MANAGERStep to be completed by：One recipientRequired Action: Do nothingAction Result: ContinueChoose Create.Choose Save. | The workflow is configured. |  |

#### Configure Flexible Workflow for Service Entry Sheets

Purpose

In this step, you make sure Flexible Workflow for Service Entry Sheets is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Workflows for Service Entry Sheets - Lean Services (F3173). | The Manage Workflows screen displays. |  |
| 3 | Activate Workflow | Make sure the status of workflow Automatic Release of Service Entry Sheetis Active. If not, select it and choose Activate.The system will check workflows with an Active status by their order. The first workflow whose preconditions are met will be executed. | The workflow is activated. |  |
| 4 | Create Manage Workflow | Choose Create and make the following entries:Name: Released by Customer Service Manager (total net amount > 100)Under Start Conditions, make the following entries:Total net amount of service entry sheet is greater than, with: 100AEDAccount assignment category 'Service Order" is used: Yes.Under Steps, choose Create and make the following entries:Step Type: Release Service Entry SheetUnder Recpients, make the following entries :Assignment By: RoleRole: Person Responsible for Service OrderStep to be completed by: One recipient.Choose Create. |  |  |
| 5 | Save | Choose Save. | The workflow is configured. |  |
| 6 | Activate Workflow | On the Manage Workflow screen, select the workflow and choose Activate. | The workflow is activated. |  |

#### Activate Flexible Workflow for Supplier Invoice

Purpose

In this procedure, you activate flexible workflow for supplier invoice.

If you want to use the flexible workflow to approve the purchase order, you must complete the following steps:

- Activate Flexible Workflow for Supplier Invoice
- Configure Flexible Workflow for Supplier Invoice

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area:Sourcing and ProcurementSub Application Area: Invoice Processing |  |  |
| 5 | Open | Open Incoming Invoice. |  |  |
| 6 | Select Configuration Step | For the Activate Flexible Workflow for Supplier Invoices step, choose Configure. | The Activate Flexible Workflow for Supplier Inv..: Change: Details screen displays. |  |
| 7 | Activate Workflow | Make the following entires and choose Save:Release Completed Invoice: Flexible Workflow is Active: Selected | The worklow is activated.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Active Flexible Workflow.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Flexible Workflow for Supplier Inv..: Change: Details screen displays. |  |
| 3 | Activate Workflow | Make the following entires and choose Save:Release Completed Invoice: Flexible Workflow is Active: Selected | The worklow is activated.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

#### Configure Flexible Workflow for Supplier Invoice

Purpose

In this procedure, you create a workflow for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Workflows for Supplier Invoices (F2873). | The Manage Workflows screen is displayed |  |
| 3 | Create Workflow for Parked Invoice as Complete | In Workflows dropdown list, choose Workflow for Parked Invoice as Complete.Choose Create and make the following entries:Workflow Name: <name>Description: <description>Valid From: <valid from date>Valid To: <valid to date>Start Conditions: (None)Under Steps, choose Create.Make following entries:Step Name: <name>Step Type: Release of Complete InvoiceAssignment By: RoleRole: Creator of Purchase OrderStep to be completed by: One of the recipientsUnder Step Conditions, make the following entries:Invoice is based on Purchase OrderNote You can use the Rework Invoice action under Exception Handling to return rejected invoices to the invoicing party.When this action is set, the workflow is cancelled and the invoicing party must rework the invoice. If the invoice is saved as complete, a new workflow is triggered.Choose Apply.Choose Save. | The new workflow for Parked Invoice as Complete is created and configured. |  |
| 4 | Activate Workflow for Parked Invoice as Complete | On the Manage Workflow screen, select the workflow you created and choose Activate.Note You should consider the following when maintaining workflows:The start conditions are only evaluated for active workflows.Predelivered workflows have the highest order number. Their start conditions are evaluated at the very end, only if the start conditions for all previous active workflows were not met.The workflow with the lowest order number is evaluated and started first.If you have defined several workflows, the start conditions are checked in the order you have defined them. As soon as the start conditions for a workflow are met, the workflow is used. This ensures that only one workflow in the list of your defined workflows is started, even if several workflows have matching start conditions.Note If a recipient of a workflow doesn't have acces to My Inbox (F0862), you need to assign business catalogs SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to role of the user. | The workflow is activated. |  |

#### Create Master Data for Automatic Purchase Order Creation from Purchase Requisition

|  |
| --- |
| Note If you want to perform the step Automatic Purchase Order Creation from Purchase Requisition, you must complete this step as a prerequisite. |

Prerequisite

You have completed the creation of master data, including material master data, vendor master data, and info records.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |

##### Change Material Master Data for Consumption Material (Optional)

Purpose

In this step, you change material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen displays. |  |
| 3 | Search foe Product | On the Manage Product Master Data screen, make the following entries:Product: for example, SRV_04Choose Go |  |  |
| 4 | View Product | Select the Product from the list and choose Edit. | The Product screen displays. |  |
| 5 | View Plant | Under Plants, choose your plant, for example, 3310 | The Plant screen displays. |  |
| 6 | Maintain Data | Unnder Purchasing, make the following entries:Automatic Purchase Order Allowed: Selected |  |  |
| 7 | Apply Change | Choose Apply. | The Product screen displays. |  |
| 8 | Save | Choose Save. | The change is saved. |  |

##### Change Material Master Data for External Workforce (Optional)

Purpose

In this step, you change material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen displays. |  |
| 3 | Search foe Product | On the Manage Product Master Data screen, make the following entries:Product: for example, SRV_01Choose Go |  |  |
| 4 | View Product | Select the Product from the list and choose Edit. | The Product screen displays. |  |
| 5 | View Plant | Under Plants, choose your plant, for example, 3310 | The Plant screen displays. |  |
| 6 | Maintain Data | Unnder Purchasing, make the following entries:Automatic Purchase Order Allowed: Selected |  |  |
| 7 | Apply Change | Choose Apply. | The Product screen displays. |  |
| 8 | Save | Choose Save. | The change is saved. |  |

##### Change Supplier Master Data - Purchasing Organization Data (Optional)

Purpose

In this step, you change supplier master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | Make the following entries and choose Enter:Business Partner: for example, 33300001 | The Change Organization: XXXXXXXX screen displays. |  |
| 4 | Change Role | Make the following entries:Change in BP role: Supplier(defined) |  |  |
| 5 | Open Purchasing Organization Data | Choose Purchasing. | The Change Organization: XXXXXXXX, role Supplier screen displays. |  |
| 6 | Enter Purchasing Data | Choose Switch Organization.Make the following data and choose Enter:Purch. Organization: for example, 3310 |  |  |
| 7 | Maintain Data | Under Additional Purchasing Data, make the following entries:Automatic PO: Selected |  |  |
| 8 | Save | Choose Save. | The change is saved. |  |

#### Create Master Data for Evaluated Receipt Settlement (Optional)

Purpose

In this step, you change supplier master data in order to create supplier invoice via evaluated receipt settlement for external workforce.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | Make the following entries and choose Enter:Business Partner: for example, 33300001 | The Change Organization: XXXXXXXX screen displays. |  |
| 4 | Change Role | Make the following entries:Display in BP role: Supplier(defined) |  |  |
| 5 | Open Purchasing Organization Data | Choose Purchasing. | The Change Organization: XXXXXXXX, role Supplier screen displays. |  |
| 6 | Enter Purchasing Data | Choose Switch Organization.Make the following data and choose Enter:Purch. Organization: for example, 3310 |  |  |
| 7 | Maintain Data | Under Purchasing Data, make the following entries:AutoEvalGRSetmt Ret.: Selected |  |  |
| 8 | Save | Choose Save. | The change is saved. |  |

#### Assign Condition Type to Item Categories

Purpose

In this step, you maintain condition types for item categories.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Item Pricing. |  |  |
| 6 | Select Configuration Step | For the Assign Condition Type to Item Categories step, choose Configure. |  |  |
| 7 | Maintain Condition Type for Item Categories | The default condition type for item categories is PMP0.Change the condition type according to your requirement, for example PPR0.Choose Save. | Note The condition type set in the confirmation item will take over the price from the supplier invoice or purchase order. Then it could go for billing if the item categories are billing-relevant.If we set the condition type as empty, then it can go for billing based on the sale price, if the item categories are billing-relevant.The condition type set in service order items will be taken as the valuation price for automatic purchase requisition. As for the dummy spare part SRV_03, no additional data for example purchasing info records, source list is maintained. When you create service orders or repair orders with SRV_03, a price against the condition type that is set for the item category is needed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Condition Type to Item Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Condition Type for Item Categories | The default condition type for item categories is PMP0.Change the condition type according to your requirement, for example PPR0 and choose Save. | Note The condition type set in the confirmation item will take over the price from the supplier invoice or purchase order. Then it could go for billing if the item categories are billing-relevant.If we set the condition type as empty, then it can go for billing based on the sale price, if the item categories are billing-relevant.The condition type set in service order items will be taken as the valuation price for automatic purchase requisition. As for the dummy spare part SRV_03, no additional data for example purchasing info records, source list is maintained. When you create service orders or repair orders with SRV_03, a price against the condition type that is set for the item category is needed. |  |

#### Account Assignment Category for Service Management Integration (Optional)

The default account assignment category for service management integration is R. It is recommended to use R for service integration. If it's not possible to use this account assignemtn category for service management, you need to create a new one for service integration. In this case, you must change purchase requisitions created out of service orders and maintain the new account assignment category.

##### Maintain Account Assignment Category (Optional)

Purpose

In this step, you create a new account assignment category

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement |  |  |
| 5 | Open | Open Account Assignment. |  |  |
| 6 | Select Configuration Step | For the Maintain Account Assignment Categories step, choose Configure. |  |  |
| 7 | Create New Account Assignment Categories | Choose New Entries.Make the following entries:Acct Assignment Cat.: for example, 9Description: for example, Service OrderConsumption Posting: V (Consumption)Distribution: 1 (Single Account Assignment)AA Chgable at IR: SelectedAccount Modification: VBRPartial Invoice: 2 (Apportion IR quantities to GR quantities proportionately)ID: AcctAssgt Scrn: 1Single Account AssigGoods Receipt: SelectedInvoice Receipt: SelectedUnder Fields, make following entries:Field LabelMand.Ent.Opt.EntryDeletion indicatorSelectedDetails account assgt. blockSelectedGeneral Ledger AccountSelectedGoods recipient/ship-to partySelectedQty./percent. mat. acct. assgtSelectedService OrderSelectedUnloading pointSelected |  |  |
| 8 | Save | Choose Save. | The entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Account Assignment Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create New Account Assignment Categories | Choose New Entries.Make the following entries:Acct Assignment Cat.: for example, 9Description: for example, Service OrderConsumption Posting: V (Consumption)Distribution: 1 (Single Account Assignment)AA Chgable at IR: SelectedAccount Modification: VBRPartial Invoice: 2 (Apportion IR quantities to GR quantities proportionately)ID: AcctAssgt Scrn: 1Single Account AssigGoods Receipt: SelectedInvoice Receipt: SelectedUnder Fields, make following entries:Field LabelMand.Ent.Opt.EntryDeletion indicatorSelectedDetails account assgt. blockSelectedGeneral Ledger AccountSelectedGoods recipient/ship-to partySelectedQty./percent. mat. acct. assgtSelectedService OrderSelectedUnloading pointSelected |  |  |
| 4 | Save | Choose Save. | The entry is saved. |  |

##### Define Combination of Item Categories/Account Assignment Categories (Optional)

Purpose

In this step, you define combinations of item categories and account assignment categories.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement |  |  |
| 5 | Open | Open Account Assignment. |  |  |
| 6 | Select Configuration Step | For the Define Combination of Item Categories/Account Assignment Categories step, choose Configure. |  |  |
| 7 | Create New Entry | Make the following entires and choose Save:AAC: for example, 9 | The entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Combination of Item Categories/Account Assignment Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create New Entry | Make the following entires and choose Save:AAC: for example, 9 | The entry is saved. |  |

##### Define Account Assignment Category for Procurement (Optional)

Purpose

In this step, you define a account assignment category for service integration.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Account Assignment Category for Procurement. |  |  |
| 6 | Select Configuration Step | For the Define Account Assignment Category for Procurement in Service Transactions step, choose Configure. |  |  |
| 7 | Maintain Account Assignment Category | The default account assignment category for service integration with procurement is R.Change it according to your requirement, for example 9, then choose Save. | The change is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Account Assignment Category for Procurement in Service Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Account Assignment Category | The default account assignment category for service integration with procurement is R.Change it according to your requirement, for example 9, then choose Save. | The change is saved. |  |

#### Check Service Material for External Workforce

Purpose

In this step, you change material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen displays. |  |
| 3 | Search foe Product | On the Manage Product Master Data screen, make the following entries:Product Number: for example, SRV_04Choose Go |  |  |
| 4 | View Product | Select the Product from the list and choose Edit. | The Product screen displays. |  |
| 5 | View Plant | Under Plants, choose your plant, for example, 3310 | The Plant screen displays. |  |
| 6 | Check Purchasing Details | Under Purchasing, check for the following entry:Purchasing group: 001 |  |  |
| 7 | Return to Main View | Choose Apply to return to the Product screen. | The Product screen appears. |  |
| 8 | Check Valuation Areas | Under Valuation Areas, make the following entries.Valuation Area: 3310Valuation Class: 3200 |  |  |
| 9 | Save | Choose Save. | The prodcut is saved. |  |

## Overview Table

This scope item consists of several steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Check the Purchase Requisitions (Optional)](#unique_30) | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The purchase requisition details are checked. |
| [Create Purchase Order against Purchase Requisition](#unique_31) |  |  |  |
| [Option A: Automatic Purchase Order Creation from Purchase Requisition](#unique_32) | Purchaser | Schedule Purchasing Jobs - Advanced (F1702) | The purchase order is created from purchase requisition automatically through scheduled job. |
| [Option B: Convert Purchase Requisitions to Purchase Orders for Consumption Material](#unique_33) | Purchaser | Create Purchase Order - Advanced (ME21N) | The purchase requisition is converted to purchase order. |
| [Option C: Convert Purchase Requisitions to Purchase Orders for External Workforce](#unique_34) [page ] 41 | Purchaser | Create Purchase Order - Advanced (ME21N) | The purchase requisition is converted to purchase order. |
| [Approve Purchase Order (Optional)](#unique_35) [page ] 43 | Purchasing Manager | My Inbox - All Items (F0862) | The purchase order which needs approval is released. |
| [Reject Purchase Order (Optional)](#unique_36) [page ] 44 | Purchasing Manager | My Inbox - All Items (F0862) | The purchase order which needs approval is rejected. |
| [Change Purchase Order (Optional)](#unique_37) [page ] 45 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order is changed. |
| [Monitor Purchase Order Assignment in Service Document](#unique_38) [page ] 46 |  |  |  |
| [Monitor Purchase Order Assignment in Service Order (Optional)](#unique_39) [page ] 47 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The Purchase order you created for this service order, is displayed as one line of Transaction History. |
| [Monitor Purchase Order Assignment in Repair Order (Optional)](#unique_40) [page ] 47 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | The Purchase order you created for this repair order, is displayed as one line of Transaction History. |
| [Check Purchasing Document List (Optional)](#unique_41) [page ] 48 | Purchaser | My Purchasing Document Items - Professional (F0547B) | The purchase order details are checked. |
| [View Purchase Order Output](#unique_42) [page ] 49 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order is viewed in PDF form. |
| [Post Goods Receipt of Material Items for Consumption Materials](#unique_43) [page ] 50 | Warehouse Clerk | Post Goods Receipt (MIGO_GR) | The system message confirms that the goods receipt is posted successfully. |
| [Maintain Service Entry Sheet for External Workforce (Optional)](#unique_44) [page ] 51 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | Service Entry Sheet is maintained for external workforce. |
| [Maintain Service Entry Sheet with Service and Spare Part (Optional)](#unique_45) [page ] 53 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | Service Entry Sheet is maintained for performed services and spare parts. |
| [Approve Service Entry Sheet for External Workforce (Optional)](#unique_46) [page ] 54 | Customer Service Manager | My Inbox - All Items (F0862) | The service entry sheet is approved and its goods. |
| [Monitor Goods Receipt in Service Document for Consumption Materials](#unique_47) [page ] 55 |  |  |  |
| [Monitor Goods Receipt in Service Order for Consumption Materials (Optional)](#unique_48) [page ] 56 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The material document is displayed as one entry of Transaction History. |
| [Monitor Goods Receipt in Repair Order for Consumption Materials (Optional)](#unique_49) [page ] 56 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | The material document is displayed as one entry of Transaction History. |
| [Check Goods Receipt Details for Consumption Material (Optional)](#unique_50) [page ] 57 | Warehouse Clerk | Material Documents Overview (F1077) | The relevant data for the goods receipt is displayed. |
| [Check Service Entry Sheet Details for External Workforce](#unique_51) [page ] 58 |  |  |  |
| [Check Service Entry Sheet Details for External Workforce in Service Order (Optional)](#unique_52) [page ] 58 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The relevant data for the service entry sheet is displayed. |
| [Check Service Entry Sheet Details for External Workforce in Repair Order (Optional)](#unique_53) [page ] 59 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | The relevant data for the service entry sheet is displayed. |
| [Reverse Goods Receipt for Consumption Materials (Optional)](#unique_54) [page ] 60 | Warehouse Clerk | Material Documents Overview (F1077) | The goods receipt is reversed. |
| [Monitor Reverse Goods Receipt In Service Document for Consumption Materials](#unique_55) [page ] 61 |  |  |  |
| [Monitor Reverse Goods Receipt in Service Order for Consumption Materials (Optional)](#unique_56) [page ] 61 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The material document for reverse is displayed as one entry of Transaction History. |
| [Monitor Reverse Goods Receipt in Repair Order for Consumption Materials (Optional)](#unique_57) [page ] 62 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | The material document for reverse is displayed as one entry of Transaction History. |
| Create Supplier Invoice with PO Reference |  |  |  |
| [Option A: Create Supplier Invoice with PO Reference without Flexible Workflow](#unique_58) [page ] 63 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | The supplier invoice with PO/GR relation is created. |
| Option B: Create Supplier Invoice with PO Reference with Flexible Workflow |  |  |  |
| [Create Supplier Invoice with PO Reference](#unique_59) [page ] 65 | Accounts Payable Accountant | Park Supplier Invoices (MIR7) | The selected completed supplier invoice is released. |
| [Release Completed Supplier Invoice (Optional)](#unique_60) [page ] 68 | Purchaser | My Inbox - All Items (F0862) | The supplier invoice is released. |
| [Reject Supplier Invoice (Optional)](#unique_61) [page ] 68 | Purchaser | My Inbox - All Items (F0862) | The selected supplier invoice is rejected. |
| [Change Supplier Invoice (Optional)](#unique_62) [page ] 69 | Accounts Payable Accountant | Park Supplier Invoices (MIR7) | The selected supplier invoice is updated and saved as completed again. |
| [Option C: Create Supplier Invoice via Evaluated Receipt Settlement for External Workforce](#unique_63) [page ] 70 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs - Advanced (F1683) | The supplier invoice with PO/GR relation is created. |
| [Monitor Supplier Invoice Assignment In Service Document](#unique_64) [page ] 72 |  |  |  |
| [Monitor Supplier Invoice Assignment in Service Order (Optional)](#unique_65) | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The supplier invoice is displayed as one entry of Transaction History. |
| [Monitor Supplier Invoice Assignment in Repair Order (Optional)](#unique_66) [page ] 73 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | The supplier invoice is displayed as one entry of Transaction History. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Check Purchase Requisitions (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check whether the purchase requisition initiated from service management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions - Professional screen displays. |  |
| 3 | Search for Purchase Requisition | Make the following entries and choose Go:Purchase Requisition: <purchase requisition>Choose your purchase requisition.Note The purchase requisition number can be found in corresponding service order item under Transaction History. | The Display Purchase Requisition screen displays. |  |
| 4 | Check the Purchase Requisition Item | Under Item Detail, check the following fields:Material Data > MaterialQuantities/Dates > QuantityAccount Assignment > AccAssCatAccount Assignment > ServiceDocContact Person > Crea. ind.Note It’s possible to enable flexible workflow for purchase requisitions. If purchase requisition is rejected, the corresponding service order item will be set to completed. | The material should be the same as the one in the corresponding service order item.Note If the purchase requisition is derived from a service order item for an external workforce scenario, the proposed service performer in service order item will be passed to the purchase requisition and purchase order.The quantity should be the quantity you input in the service order item.The AccAssCat should be the one set in Define Account Assignment Category for Procurement and the ServiceDoc should be a combination of the service document type, service document ID and service document item ID of the corresponding service document item.The Crea. ind. should be S4CRM Service Order. |  |

### Create Purchase Order against Purchase Requisition

If purchase requisitions are derived for consumption materials, please complete one of the following steps:

If purchase requisitions are derived for external workforce, please complete one of the following steps:

|  |
| --- |
| Note There is a follow-up quotation process which can be created for service orders involving consumption materials and external workforce items for purchase requisitions. You can refer to the process described in the test script Service Quotation (4GA) for details. |

#### Option A: Automatic Purchase Order Creation from Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create purchase orders automatically from purchase requisitions through a scheduled job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Schedule Purchasing Jobs - Advanced (F1702). | The Application Jobs screen is displayed |  |
| 4 | Create a New Job | Choose Create.Make the following entries:Job Template: for example, Automatic Creation of Purchase Orders from RequisitionsJob Name: for example, Automatic Creation of Purchase Orders from RequisitionsChoose Step 2.Make the following entries:Start Immediately: SelectedJob Start (Local Time): <current time>If the job needs to be run on a regular basis, choose Define Recurrence Pattern.Choose Step 3.Make the following entries:Per Company Code: SelectedPer Requisition: SelectedAcct Assignment Cat.: <from Define Account Assignment Category for Procurement (Optional)>Contract: DeselectedChoose Schedule. | The job is scheduled. |  |
| 5 | Check Status | On the Application Jobs screen, check that the status of your job changes to Finished. |  |  |
| 6 | Check Result | Choose the icon in the Log column of your job. | The Job Log screen displays.Under Run Details, it displays that the selected purchase requisitions were converted to purchase orders.Note Automatic Purchase Order creation from Purchase Requisition will only succeed if all fo the required attributes to automate purchase order creation are supplied.The attributes are described in the step Create Master Data for Automatic Purchase Order Creation from Purchase Requisition. |  |

#### Option B: Convert Purchase Requisitions to Purchase Orders for Consumption Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you convert a purchase requisition into purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. |  |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Open Document Overview | Choose Document Overview On. | The Document Overview displays. |  |
| 4 | Access Purchase Requisitions | Choose Selection variant > Purchase Requisitions. | The Purchase Requisitions screen displays. |  |
| 5 | Filter Purchase Requisitions | Make the following entires and choose Run:Purchase Requisition Number: <purchase requisition> | The Document Overview lists the selected purchase requisitions. |  |
| 6 | Adopt Purchase Requisition | Select the purchase requisition and choose Adopt. | The contents of the selected purchase requisition are copied to the purchase order. |  |
| 7 | Create Purchase Order | On the Create Purchase Order screen, make following entries:Order Type: Standard PO.Supplier: 33300001Under Org. Data, make the following entries:Purch. Org.: Code: 3310In the Item Detail area, under Conditions, make the following entries:Condition Type: PMP0Amount: for example, 5Press Enter.Note The address data under Delivery Address is copied from the delivery address of the purchase requisition item.The delivery address of the corresponding purchase requisition item is derived as follows:If in the corresponding service order spare part item, the spare part recipient is maintained as one of the partner functions, this address is used.Otherwise, the purchase requisition item’s plant or storage location address is used.Choose Save. | The purchase order is created.Note If you want the purchase order assigned to an approver, then the purchase order must meet one of the active workflows’ preconditions which you defined in Configure Flexible Workflow for Purchase Order.If the purchase order is assigned to an approver, you should complete the steps Approve Purchase Order (Optional) and Change Purchase Order (Optional). |  |

#### Option C: Convert Purchase Requisitions to Purchase Orders for External Workforce

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you convert a purchase requisition into purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / CommentNew table |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Open Document Overview | Choose Document Overview On. | The Document Overview displays. |  |
| 4 | Access Purchase Requisitions | Choose Selection variant > Purchase Requisitions. | The Purchase Requisitions screen displays. |  |
| 5 | Filter Purchase Requisitions | Make the following entires and choose Run:Purchase Requisition Number: <purchase requisition> | The Document Overview lists the selected purchase requisitions. |  |
| 6 | Adopt Purchase Requisition | Select the purchase requisition and choose Adopt. | The contents of the selected purchase requisition are copied to the purchase order. |  |
| 7 | Create Purchase Order | On the Create Purchase Order, make the following entries.Order Type: Standard POSupplier: 10300001Under Org. Data, make the following entries:Purch. Org.: Code: 1010In the Item Detail area, under Conditions, make the following entries:Condition Type: PMPOAmount: for example, 5Press EnterChoose SaveNote Please make sure the fields Goods Receipt and GR-Based Inv. Verif. have the same value. If a service entry sheet is to be created, both fields need to be selected. | The purchase order is created.Note If you want the purchase order assigned to an approver, then the purchase order must meet one of the active workflows’ preconditions which you defined in Configure Flexible Workflow for Purchase Order.If the purchase order is assigned to an approver, you should complete the steps Approve Purchase Order (Optional) and Change Purchase Order (Optional). |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release a purchase order.

|  |
| --- |
| Note If your user does not have My Inbox (F0862), check whether business catalog SAP_PRC_BC_PURCHASING_MNGR is assigned to your user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. |  |  |
| 2 | Access App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Select Purchase Order | Select the purchase order from the left and choose Approve. | The Submit Decision dialog box displays. |  |
| 4 | Approve Purchase Order | Choose Submit.Note You can maintain a Decision Note if needed. | The purchase order is approved. |  |

### Reject Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reject a purchase order.

|  |
| --- |
| Note If your user does not have My Inbox (F0862), check whether business catalog SAP_PRC_BC_PURCHASING_MNGR is assigned to your user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. |  |  |
| 2 | Access App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Select Purchase Order | Select the purchase order from the left and choose Reject. | The Submit Decision dialog box displays. |  |
| 4 | Reject Purchase Order | Choose Submit.Note You can maintain a Decision Note if needed. | The purchase order is rejected. |  |

### Change Purchase Order (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Choose a Purchase Order | Make the following entries and choose Go:Purchase Order: <purchase order>Company Code: 3310Choose your purchase order. |  |  |
| 4 | Change Field Values | Choose Edit.Change field values of the purchase order.Note You can change the following fields:Company CodePurchasing GroupPurchasing OrganizationMaterialOrder QuantityNet Order PriceStorage LocationNote Make sure the storage location is empty for spare part items if you want to complete the step Maintain Service Entry Sheet with Service and Spare Part (Optional). Once the service entry sheet is approved, the goods receipt for the spare part and service is automatically created for the purchase order. |  |  |
| 5 | Check Purchase Order | Choose Purchase Order > Check .If the system displays a message, you must correct entries in the purchase order.If no message occurs, the purchase order is complete. Choose Continue in the dialog box. | The purchase order is valid. |  |
| 6 | Save | Choose Save. | The purchase order is saved.Note Depending on the configured flexible workflows for purchase orders (refer to Configure Flexible Workflow for Purchase Order), the purchase order may trigger the workflow and be sent to approval.Refer to test step Approve Purchase Order (Optional) for more details. |  |

### Monitor Purchase Order Assignment in Service Document

If your purchase requisition is derived from a service order, please complete the step Monitor Purchase Order Assignment in Service Order (Optional).

If your purchase requisition is derived from a repair order, please complete the step Monitor Purchaser Order Assignment in Repair Order (Optional).

#### Monitor Purchase Order Assignment in Service Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the purchase order you created for a service order spare part. You verfiy that it is shown in the transaction history of the service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Search for Service Order | Make the following entries and choose Go:Service Order: <service order> |  |  |
| 4 | Choose Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Check Transaction History | Under Transaction History, find the transation for your service part item. | The purchase order you created for this service order can be found in the transaction history. |  |

#### Monitor Purchase Order Assignment in Repair Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the purchase order you created for a spare part. You verfiy that it is shown in the transaction history of the repair order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Customer Service Manager - In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen is displays. |  |
| 3 | Search for Repair Order | Make the following entries and choose Go:Repair Order: <repair order> |  |  |
| 4 | Choose Repair Order | Choose your repair order from the Repair Order column.Choose Display Repair Order. | The Repair Orders screen displays. |  |
| 5 | Check Transaction History | Under Transaction History, find the transation for your service part item. | The purchase order you created for this repair order can be found in the transaction history. |  |

### Check Purchasing Document List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check purchase orders based on your search criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open My Purchasing Document Items - Professional (F0547B). | The My Purchasing Document Items screen displays. |  |
| 3 | Filter Item List | Make the following entries and choose Go:Supplier: 33300001Purchasing Group: 001Plant: 3310 |  |  |
| 4 | Switch to Purchase Orders View | Choose the Purchase Orders tab. |  |  |
| 5 | View Goods Receipts or Supplier Invoices | Choose the Goods Receipts tab or the Supplier Invoices tab. |  |  |
| 6 | Check Purchasing Document Details | Choose either the Purchase Requisitions tab or the Purchase Orders tab.Note You cannot view Goods Receipts and Supplier Invoices with the Purchaser role. |  |  |
| 7 | View the Purchasing Document | Choose a purchasing document item. | The Purchase Requisition or Purchase Order Item screen displays. |  |

### View Purchase Order Output

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you preview an existing purchase order form.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Login | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Choose a Purchase Order | Make the following entries and choose Go:Purchase Order: <purchase order>Choose your purchase order. | The Display Purchase Order screen displays. |  |
| 4 | View Output | Choose Edit.Choose Output Preview and select the channel. | The Display Pur. Order :: Output screen displays.The selected purchase order displays as a PDF. |  |

### Post Goods Receipt of Material Items for Consumption Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open Post Goods Receipt (MIGO_GR). | The Goods Receipt Purchase Order screen displays. |  |
| 3 | Maintain Data | Make the following entries:Trans./Event:Goods ReceiptReference Document: Purchase OrderPurchase Order:<purchase order>Item Number of Purchase Order: <purchase order item>Press Enter. | The purchase order item is referenced as an item of the goods receipt. |  |
| 4 | Select Item | Select the line for which a goods receipt is to be posted.Make the following entries:OK: Selected | The Post Goods Receipt screen displays. |  |
| 5 | Post | Choose Post. | The goods receipt is posted. |  |

### Maintain Service Entry Sheet for External Workforce (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you report the performed services in the service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen displays. |  |
| 3 | Maintain Data | Choose Create.On the Service Entry Sheets screen, make the following entries:Name of Service Entry Sheet: <name>Reference Purchase Order: <purchase order>Under Items, make the following entries for each item:Performance Period: <date range>Service Performer: <service performer>Stated Quantity: for example, 10Choose Apply.Note Refer to section 4.4.2.2 of scope item JB1 for detailed instructions on how to maintain a service performer for a supplier or vendor. |  |  |
| 4 | Add Attachments (Optional) | Under Attachments, you can choose Upload or Add a Link to create an attachment.Note You can view the attachments and save them on your own device regardless of the status of the service entry sheet.You can add and delete attachments only if you edit the service entry sheet.The service entry sheet must be in status In Process. |  |  |
| 5 | Save the Service Entry Sheet | Choose Create. | The service entry sheet is created. |  |
| 6 | Send to Approval | Choose Send to Approval. | The service entry sheet is sent for approval. |  |
| 7 | Check Service Entry Sheet | On the Manage Service Entry Sheets screen, check the status of your service entry sheetIf the service entry sheet is approved, you can skip the step [Approve Service Entry Sheet for External Workforce (Optional)](#unique_46) [page ] 54. | Note If service entry sheet is approved, the goods receipt is automatically created for purchase order.Once the goods receipt is created successfully, the service confirmation for its corresponding service order will be created automatically with an Open status.The service performer is copied over from service entry sheet when the service confirmation is created. |  |

### Maintain Service Entry Sheet with Service and Spare Part (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you report the performed services and spare parts in the service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen displays. |  |
| 3 | Maintain Data | Choose Create.On the Service Entry Sheets screen, make the following entries:Name of Service Entry Sheet: <name>Reference Purchase Order: <purchase order>Under Items, make the following entries for each item:Performance Period: <date range>Service Performer: <service performer>Stated Quantity: for example, 1Choose Apply.Note Refer to section 4.4.2.2 of scope item JB1 for detailed instructions on how to maintain a service performer for a supplier or vendor. |  |  |
| 4 | Add Attachments (Optional) | Under Attachments, you can choose Upload or Add a Link to create an attachment.Note You can view the attachments and save them on your own device regardless of the status of the service entry sheet.You can add and delete attachments only if you edit the service entry sheet.The service entry sheet must be in status In Process. |  |  |
| 5 | Save the Service Entry Sheet | Choose Create. | The service entry sheet is created. |  |
| 6 | Send to Approval | Choose Send to Approval. | The service entry sheet is sent for approval. |  |
| 7 | Check Service Entry Sheet | On the Manage Service Entry Sheets screen, check the status of your service entry sheetIf the service entry sheet is approved, you can skip the step [Approve Service Entry Sheet for External Workforce (Optional)](#unique_46) [page ] 54. | Note If service entry sheet is approved, the goods receipt is automatically created for purchase order.Once the goods receipt is created successfully, the service confirmation for its corresponding service order will be created automatically with an Open status.The service performer is copied over from service entry sheet when the service confirmation is created. |  |

### Approve Service Entry Sheet for External Workforce (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you approve the service entry sheet. The service recipient can send an invoice (in case of ERS) for the approved amount to the service provider/vendor or vice versa.

|  |
| --- |
| Note The flexible workflows were defined in the step Configure Flexible Workflow for Service Entry Sheets. |

|  |
| --- |
| Note If you user doesn't have My Inbox (F0862), you need to assign business catalog SAP_CA_BC_MYINBOX_PC and SAP_MM_BC_SES_WIAPPROVE_PC to the business role of your user. This is necessary to process incoming approval requests as part of the workflow for the service entry sheet. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP as a Customer Service Manager |  |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Select Service Entry Sheet | Select the service entry sheet from the left and choose Approve. | The Submit Decision dialog box displays. |  |
| 4 | Approve Service Entry Sheet | Choose Submit.Note You can maintain a Decision Note if needed. | Service Entry Sheet is approved.Note If the service entry sheet is approved, the goods receipt is automatically created for the purchase order.Once the goods receipt is created successfully, the service confirmation or the repair confirmation will be created automatically with the status Open.The service performer is copied over from service entry sheet to external workforce item in confirmation. |  |

### Monitor Goods Receipt in Service Document for Consumption Materials

If the purchase requisition is derived from a service order, please complete the step Monitor Goods Receipt in Service Order for Consumption Materials (Optional).

If the purchase requisition is derived from a repair order, please complete the step Monitor Good Receipt in Repair Order for Consumption Materials (Optional).

#### Monitor Goods Receipt in Service Order for Consumption Materials (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the material document in the transaction history of the service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Search for Service Order | Make the following entries and choose Go:Service Order: <service order> |  |  |
| 4 | Choose Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Check Transaction History | Under Transaction History, find the material document. | The material document for this service order can be found in the transaction history. |  |

#### Monitor Goods Receipt in Repair Order for Consumption Materials (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the material document in the transaction history of the repair order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Customer Service Manager - In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen is displays. |  |
| 3 | Search for Repair Order | Make the following entries and choose Go:Repair Order: <repair order> |  |  |
| 4 | Choose Repair Order | Choose your repair order from the Repair Order column.Choose Display Repair Order. | The Repair Orders screen displays. |  |
| 5 | Check Transaction History | Under Transaction History, find the material document. | The material document for this repair order can be found in the transaction history. |  |

### Check Goods Receipt Details for Consumption Material (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open Material Documents Overview (F1077). | The Material Documents Overview screen displays. |  |
| 3 | Search for Goods Receipts | Make the following entries and choose Go:Material: SRV_03 or SRV_04 |  |  |
| 4 | Select Goods Receipts | Choose your goods receipt. | The goods receipt displays. |  |

### Check Service Entry Sheet Details for External Workforce

If the purchase requisition is derived from a service order, please complete the step Check Service Entry Sheet Details for External Workforce in Service Order (Optional).

If the purchase requisition is derived from a repair order, please complete the step Check Service Entry Sheet Details for External Workforce in Repair Order (Optional)

#### Check Service Entry Sheet Details for External Workforce in Service Order (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Search for Service Order | Make the following entries and choose Go:Service Order: <service order> |  |  |
| 4 | Choose Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Check Service Item | Under Items, choose the external workforce item. | The Service Order Item screen displays. |  |
| 6 | Check Service Entry Sheet | Under Transaction History, choose the service entry sheet. | The Service Entry Sheet screen displays. |  |

#### Check Service Entry Sheet Details for External Workforce in Repair Order (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Customer Service Manager - In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen is displays. |  |
| 3 | Search for Repair Order | Make the following entries and choose Go:Repair Order: <repair order> |  |  |
| 4 | Choose Repair Order | Choose your repair order. | The Plan Repair Details screen displays. |  |
| 5 | Check Transaction History | Under Transaction History, find the service entry sheet. | The service entry sheet for this repair order can be found in the transaction history. |  |

### Reverse Goods Receipt for Consumption Materials (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open Material Documents Overview (F1077). | The Material Documents Overview screen displays. |  |
| 3 | Search for Goods Receipts Material Documents | Make the following entries and choose Go.Material: SRV_03 or SRV_04Note Alternatively, in the Material Document field, enter the material document number. |  |  |
| 4 | Select Material Document for Goods Receipt | Choose the goods receipt you need to reverse. | The Material Document screen displays. |  |
| 5 | Reverse | Choose Reverse. | The Reverse Goods Receipt dialog box displays. |  |
| 6 | Confirm Reversal | Make the following entries:Posting Date: <posting date>Additional Note: <optional note>Select your material document item from the list and choose OK. | The document is reversed. |  |

### Monitor Reverse Goods Receipt In Service Document for Consumption Materials

If the purchase requisition is derived from a service order, please complete step Monitor Reverse Goods Receipt in Service Order (Optional).

If the purchase requisition is derived from a repair order, please complete the step Monitor Reverse Good Receipt in Repair Order (Optional).

#### Monitor Reverse Goods Receipt in Service Order for Consumption Materials (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the material document for the reverse goods receipt in the transaction history of the service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Search for Service Order | Make the following entries and choose Go:Service Order: <service order> |  |  |
| 4 | Choose Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Check Service Item | Under Items, choose the spare part item. | The Service Order Item screen displays. |  |
| 6 | Check Transaction History | Under Transaction History, find the material document for the reversal. | The material document for the reversal can be found. |  |

#### Monitor Reverse Goods Receipt in Repair Order for Consumption Materials (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the material document for the reverse goods receipt in the transaction history of the repair order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Customer Service Manager - In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen is displays. |  |
| 3 | Search for Repair Order | Make the following entries and choose Go:Repair Order: <repair order> |  |  |
| 4 | Choose Repair Order | Choose your repair order from the Repair Order column.Choose Display Repair Order. | The Repair Orders screen displays. |  |
| 5 | Check Transaction History | Under Transaction History, find the material document for the reversal. | The material document for the reversal can be found. |  |

### Create Supplier Invoice with PO Reference

#### Option A: Create Supplier Invoice with PO Reference without Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation and post it directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:33300001For now, if you move the mouse to the Invoicing Party in the header of the supplier invoice, then click the Invoicing Party, the Company Date with Address and Contact Details are displayed.In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Caution In case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in chapter 2.Invoice Party:33300001Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Exchange Rate should be changed from USD to EUR according to the customizing settings.The Exchange Rate is changeable. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References section, add the references.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Add Notes (Optional) | Enter notes on Note tab if you want to add more detailed long text for the supplier invoice. |  |  |
| 6 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 7 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 8 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 9 | Block invoice on item level (optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Click Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Click Back to Supplier Invoice. | The item is blocked with a blocking reason. |  |
| 10 | Check the balance | Calculate the tax by choosing Propose Tax. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 11 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated. |  |
| 12 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

#### Option B: Create Supplier Invoice with PO Reference with Flexible Workflow

##### Create Supplier Invoice with PO Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the supplier invoice with a PO/GR reference. The invoice is sent for approval as part of the flexible workflow for supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Park Supplier Invoices (MIR7). | The Enter Company Code dialog box displays. |  |
| 3 | Enter General Data | Make the following entries and choose Continue:Company Code: 3310For purchase orders created with the local currency, make the following entries.Transaction: InvoiceCompany Code: 3310Amount: <amount>Currency: AEDInvoice Date: <today's date>Posting Date: <today's date>Reference: <reference invoice number>Invoice Party: 33300001For purchase orders created with a foreign currency, make the following entries:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <amount>Currency: <currency>Invoice Date: <today's Date>Posting Date: <today's date>Reference:<reference invoice number>Invoice Party: 33300001Under Details, make the following entries:Exchange Rate: <exchange rate>Caution In case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in chapter 2. | The Park Supplier Invoice screen displays. |  |
| 4 | Enter Purchase Order References | Under PO Reference, make the following entries:Purchase Order/ Scheduling Agreement<purchasing document>.Press Enter. | All items of the referenced purchase order are added to the as invoice items. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create an invoice for. | You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items Data | Check the Amount, the Quantity, and the Tax Code (there may already be a tax code that was copied from the purchase order). | The amount, quantity, and tax code are consistent. |  |
| 7 | Check Tax Code | Under Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax code, specify the tax code. |  |
| 9 | Check Balance | Make the following entries:Calculate Tax: SelectedMake sure that the balance is zero. | The balance is zero. |  |
| 10 | Simulate Supplier Invoice | Choose Simulate. | The supplier invoice is ready to post. |  |
| 11 | Save Invoice | Choose Save as Completed.Note You can choose Save Parked Document to park the invoice first. After that, you can edit the supplier invoice and choose Save as Completed. | The system message Invoice document XXXXXXXXXX has been saved as completed displays.Note If the invoice triggers the Workflow for Parked Invoice as Complete, approval details will be shown in the supplier invoice.If the workflow is triggered, you should complete the following steps as needed: |  |

##### Release Completed Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release a supplier invoice.

|  |
| --- |
| Note If your user does not have My Inbox (F0862), check whether business catalogs SAP_MM_BC_INV_DOC_DSP_PC and SAP_MM_BC_INV_WIAPPROVE_PC are assigned to the business role of your user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | My Inbox screen displays. |  |
| 3 | Check Supplier Invoice Status | Select the supplier invoice from the left and choose Release. | The Submit Decision dialog box displays. |  |
| 4 | Release Supplier Invoice | Choose Submit.Note You can maintain a Decision Note if needed. | The invoice is released. |  |

##### Reject Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reject a supplier invoice.

|  |
| --- |
| Note If your user does not have My Inbox (F0862), check whether business catalogs SAP_MM_BC_INV_DOC_DSP_PC and SAP_MM_BC_INV_WIAPPROVE_PC are assigned to the business role of your user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | My Inbox screen displays. |  |
| 3 | Check Supplier Invoice Status | Select the supplier invoice from the left and choose Reject. | The Submit Decision dialog box displays. |  |
| 4 | Reject Supplier Invoice | Choose Submit.Note You can maintain a Decision Note if needed. | The invoice is rejected. |  |

##### Change Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you change the supplier invoice that you created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Park Supplier Invoices (MIR7). | The Enter Company Code dialog box displays. |  |
| 3 | Check Supplier Invoice | Make the following entries and choose Continue:Company Code: 3310Choose Other Invoice Document.Make the following entries:Invoice Document No.: <your invoice document>Fiscal Year: <year>Choose Continue. | The Park Supplier Invoice screen displays. |  |
| 4 | Save Changes | Make a change to the invoice.Choose Save as Completed. | The supplier invoice is saved. |  |

#### Option C: Create Supplier Invoice via Evaluated Receipt Settlement for External Workforce

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a supplier invoice with a PO reference through a scheduled job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Schedule Supplier Invoice Jobs - Advanced (F1683). | The Application Jobs screen displays. |  |
| 3 | Define a Job | Choose Create.Make the following entries:Job Template: Evaluated Receipt Settlement (ERS)Job Name: for example, Evaluated Receipt Settlement (ERS)Choose Step 2.Make the following entries:Start Immediately: SelectedJob Start (Local Time): <current time>If the job needs to be run on a regular basis, choose Define Recurrence Pattern.Choose Step 3.Make the following entries:Purchasing Document: <purchase order for external workforce>Test Run: DeselectedChoose Schedule. | The job is scheduled. |  |
| 4 | Check Status | On the Application Jobs screen, check that the status of your job changes to Finished. |  |  |
| 5 | Check Result | Choose the icon in the Log column of your jobs. | The Job Log screen displays.Under Run Details, it displays that invoice was created.Note The preliminary step Create Master Data Update for Evaluated Receipt Settlement (Optional) is mandatory for the ERS process. |  |

### Monitor Supplier Invoice Assignment In Service Document

If the purchase requisition is derived from a service order, please complete the step Monitor Supplier Invoice Assignment in Service Order (Optional).

If the purchase requisition is derived froma repair order, please complete the step Monitor Supplier Invoice Assignment in Repair Order (Optional).

#### Monitor Supplier Invoice Assignment in Service Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the supplier invoice in the transaction history of the service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Search for Service Order | Make the following entries and choose Go:Service Order: <service order> |  |  |
| 4 | Choose Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Check Service Item | Under Items, choose the service part item. | The Service Order Item screen displays. |  |
| 6 | Check Transaction History | Under Transaction History, find the supplier invoice. | The supplier invoice can be found. |  |
| 7 | Check Price Details | On the Service Order Item screen, choose Confirmations under Items.If a service confirmation exists, choose one.Check the Price Details. | The Service Confirmation Item screen displays.The purchasing price from the supplier invoice can be copied to condition type PMP0 of the service confirmation item until it is released for billing.If you set condition type empty, the sale price will go for billing to the customer if the item categories are billing relevant.Note When a supplier invoice is cancelled, the service confirmation item price of condition type PMP0 will revert to the price of the purchase order itemThe total confirmed quantity in the confirmations should be less than or equal to the delivery quantity in the goods receipt. |  |

#### Monitor Supplier Invoice Assignment in Repair Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the supplier invoice in the transaction history of the repair order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Customer Service Manager - In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen is displays. |  |
| 3 | Search for Repair Order | Make the following entries and choose Go:Repair Order: <repair order> |  |  |
| 4 | Choose Repair Order | Choose your repair order from the Repair Order column.Choose Display Repair Order. | The Repair Orders screen displays. |  |
| 5 | Check Transaction History | Under Transaction History, find the supplier invoice. | The supplier invoice can be found. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can precede this process.

| Process | Business Condition |
| --- | --- |
| 3D2 - Service Order Management and Monitoring | A new line item in the service order is created for a spare part to be procured or a new line item in the service order is created for external workforce. |
| 3XK - In-House Repair | A new line item in the repair order is created for a spare part to be procured. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J60 - Accounts Payable |  |

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
> Flagged while digesting this document, not verified: Option C (external workforce PO conversion) uses Supplier 10300001 and Purch. Org. 1010, whereas the stated master data and all other steps use supplier 33300001 and org 3310.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[10-procurement/test-script-service-and-material-procurement-project-based-services-j1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 119,122 chars in the whole document
