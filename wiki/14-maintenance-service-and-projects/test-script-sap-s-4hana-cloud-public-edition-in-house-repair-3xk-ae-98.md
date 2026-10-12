---
id: 14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-in-house-repair-3xk-ae-98
title: Test Script SAP S/4HANA Cloud Public Edition - In-House Repair (3XK_AE) (3XK_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 3XK In-House Repair (AE, release 2608): prerequisites, config steps, roles, and step-by-step procedures from returns to repair, billing and invoice."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/in-house-repair]
aliases: [3XK_S4CLD2608_BPD_EN_AE]
keywords: [In-House Repair, business roles, customer returns, repair quotations, repair orders, repair diagnosis, repair confirmations, billing, master data, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3XK_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-988
topic: 14-maintenance-service-and-projects/in-house-repair
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - In-House Repair (3XK_AE) (3XK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3XK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **In-House Repair** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | In-House Repair (3XK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232854109)

[2 Prerequisites 5](#_Toc232854110)

[2.1 System Access 5](#_Toc232854111)

[2.2 Roles 5](#_Toc232854112)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232854113)

[2.3.1 Business Partner 7](#_Toc232854114)

[2.3.2 Organizational Unit 8](#_Toc232854115)

[2.3.3 Master Data 9](#_Toc232854116)

[2.4 Business Conditions 11](#_Toc232854117)

[2.5 Preliminary Steps 12](#_Toc232854118)

[2.5.1 Configure Service Management and Monitoring 12](#_Toc232854119)

[2.5.2 Configure Credit Check Management (Optional) 12](#_Toc232854120)

[2.5.3 Specify Settings for Returns Orders as Follow-Up 14](#_Toc232854121)

[2.5.4 Configure Customer Returns (Optional) 16](#_Toc232854122)

[2.5.4.1 Specify Settings for In-House Repair (Service) as Follow-Up Activity 16](#_Toc232854123)

[2.5.4.2 Specify Storage Locations for Follow-Up Activities 17](#_Toc232854124)

[2.5.4.3 Define Serial Number Profiles 19](#_Toc232854125)

[2.5.5 Maintain Customer, Customer Warranty and Vendor Warranty (Optional) 20](#_Toc232854126)

[2.5.6 Configure Service Teams 21](#_Toc232854127)

[2.5.6.1 Define Service Team Profile 22](#_Toc232854128)

[2.5.6.2 Assign Service Team Profile to Repair Transactions 24](#_Toc232854129)

[2.5.6.3 Create a Service Team 26](#_Toc232854130)

[2.5.7 Configure Output Management 27](#_Toc232854131)

[2.5.8 Configure Situation Handling (Optional) 30](#_Toc232854132)

[2.5.9 Configure Service Contract Management (Optional) 31](#_Toc232854133)

[2.5.9.1 Specify Contract Determination for Transaction Types 31](#_Toc232854134)

[3 Overview Table 33](#_Toc232854135)

[4 Test Procedures 36](#_Toc232854136)

[4.1 Create In-House Repair 36](#_Toc232854137)

[4.1.1 Option A: Start With Customer Returns and Process In-House Repair 36](#_Toc232854138)

[4.1.1.1 Create Customer Returns Order 36](#_Toc232854139)

[4.1.1.2 Execute Picking 38](#_Toc232854140)

[4.1.1.3 Post Goods Receipt 39](#_Toc232854141)

[4.1.1.4 Perform Material Inspection 40](#_Toc232854142)

[4.1.1.5 Display Returns Overview 41](#_Toc232854143)

[4.1.2 Option B: Start With In-House Repair 42](#_Toc232854144)

[4.1.2.1 Create In-House Repair and Add Repair Objects 42](#_Toc232854145)

[4.1.2.2 Create Returns Order 44](#_Toc232854146)

[4.1.2.3 Execute Picking 47](#_Toc232854147)

[4.1.2.4 Post Goods Receipt 48](#_Toc232854148)

[4.1.2.5 Perform Material Inspection 49](#_Toc232854149)

[4.2 Decide Follow-Up Steps (Optional) 50](#_Toc232854150)

[4.3 Perform Prechecks 52](#_Toc232854151)

[4.3.1 Perform Precheck and Decide Follow-Up Steps 52](#_Toc232854152)

[4.4 Quotation Selected in Follow-Up Steps (Optional) 54](#_Toc232854153)

[4.4.1 Create Quotation 54](#_Toc232854154)

[4.4.2 Send Repair Quotation to Customer 56](#_Toc232854155)

[4.4.3 Accept or Reject Repair Quotation 58](#_Toc232854156)

[4.5 Create Repair Order or Create Fixed Price Repair Order selected in Follow-Up Steps 59](#_Toc232854157)

[4.5.1 Create Repair Order or Create Fixed Price Repair Order 59](#_Toc232854158)

[4.5.2 Trigger Diagnosis Planning, Plan Diagnosis, Trigger Diagnosis and Perform Diagnosis in Repair Order (Optional) 63](#_Toc232854159)

[4.5.2.1 Trigger Diagnosis Planning in Repair Order 63](#_Toc232854160)

[4.5.2.2 Plan Diagnosis 64](#_Toc232854161)

[4.5.2.3 Trigger Diagnosis in Repair Order 65](#_Toc232854162)

[4.5.2.4 Perform Diagnosis 66](#_Toc232854163)

[4.5.2.5 Trigger Follow-Up Actions for Diagnosis 67](#_Toc232854164)

[4.5.2.6 Create Diagnosis Follow-Up 69](#_Toc232854165)

[4.6 Trigger Repair Planning in Repair Order 70](#_Toc232854166)

[4.6.1 Plan Repairs 71](#_Toc232854167)

[4.6.1.1 Trigger Repair 73](#_Toc232854168)

[4.6.2 Perform Repairs 75](#_Toc232854169)

[4.6.2.1 Create Repair Confirmation 76](#_Toc232854170)

[4.6.2.2 Cancel Repair Confirmation (Optional) 78](#_Toc232854171)

[4.7 Prepare and Release for Billing 79](#_Toc232854172)

[4.8 Return to Customer (Optional) 81](#_Toc232854173)

[4.9 Complete Repair Object and Finalize In-House Repair (Optional) 82](#_Toc232854174)

[4.10 Create Invoice (Optional) 83](#_Toc232854175)

[4.11 Create Repair Template (Optional) 85](#_Toc232854176)

[5 Appendix 87](#_Toc232854177)

[5.1 Process Integration 87](#_Toc232854178)

[5.1.1 Preceding Processes 87](#_Toc232854179)

[5.1.2 Succeeding Processes 87](#_Toc232854180)

## Purpose

Overview

The scope item covers the in-house repair process in SAP S/4HANA Cloud Public Edition.

The in-house repair supports selecting the repair objects, performing prechecks, run a diagnosis and aiding in decision making to provide a repair quotation or repair order. Warranty and service contracts are considered. When the customer agrees to the repair, repair orders are created automatically.

The repair order is then planned and released for execution. Credit checks and ATP/reservation for spare parts safeguard the repair. A purchase requisition is created automatically for the applicable spare parts or external service items.

In repair execution, repair confirmations are posted against the repair order. The time-sheet entry, spares cost, and expenses are posted to finance and controlling.

Once the repair is done, the recorded effort is released for billing, automatically creating a billing document request to invoice the customer.

For logistics, in-house repair integrates with customer returns.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/3XK_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Business User Roles |  |  |  |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Customer Service Representative - In-House Repair | SAP_BR_CUST_SRVC_REP_REPA | In-House Repair | SAP_BR_CUST_SRVC_REP_REPA |  |
| Customer Service Manager - In-House Repair | SAP_BR_CUST_SRVC_MGR_REPA | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |
| Service Technician - In-House Repair | SAP_BR_CUST_SRVC_TEC_REPA | In-House Repair | SAP_BR_CUST_SRVC_TEC_REPA |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Controller | SAP_BR_CREDIT_CONTROLLER |  |
| Expert Roles |  |  |  |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents products, equipment, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

#### Business Partner

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer (Sold-To Party) | 3310000133100002 |  | You must either assign the customer pricing procedure 01 (Procedure 01) or ensure that the customer is not assigned to a pricing procedure.To check the assignment, use business role SAP_BR_BUPA_MASTER_SPECIALIST and access Manage Customer Master Data (F0850A). |
| Contact Person | 3391000533910006 |  | The contact person is assigned to your customer. |
| Payer | 33100001 |  |  |
| Supplier | 3330000133300002 |  |  |

#### Organizational Unit

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Sales Office | 330 |  |  |
| Distribution Channel | 10 |  |  |
| Shipping Point | 3310 |  |  |
| Purchasing Organization | 3310 |  |  |
| Purchasing Group | 001 |  |  |
| Plant | 3310 |  |  |
| Storage Location | 331A331B331R |  |  |
| Cost Center | 3310110133101701 |  |  |
| Profit Center | YB700 |  |  |
| Employee | <employee> | Use the employee ID that is assigned to your user. |  |
| G/L Account | 516000006100800065008300(3310)6510000094311000 | Consumption - Trading GoodsTravel Expenses - MiscellaneousService - GeneralOffice SuppliesService Time |  |
| Controlling Area | A000 |  |  |

#### Master Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Service Product (Service) | SRV_01 | Services | The service product SRV_01 represents the service itself, e.g., an installation, a repair, or maintenance.Note A service is usually performed by an internal employee. Alternatively, it can be procured from a third-party (external workforce procurement). In that case, the scope item 3NI is required. |
| Service Expense | SRV_02 | Service Expenses | The service product SRV_02 represents the expense that occurs from the service, for example, travel cost or fuel. |
| Service Part (Undefined) | SRV_03 | Service Part (Undefined) | Non-Stock Material |
| Service Part (Defined) | SRV_04 | Service Part (Defined) | Non-Stock MaterialNote If you want to test a spare part which is procured, scope item 3NI must be activated.The purchasing info record, source supplier, and sales price are needed. |
| Service Product(Service Part Picked from Stock) | SRV_05 | Stock Service Part | The service product SRV_05 represents a material that will be taken from stock (pick-from-stock scenario).Note If you are using a material with the item category group stock service part (SVST), this material will be taken from the default storage location of the plant. |
| Service Product (Service Part Picked from Stock) | SRV_06 | Stock Service Part with Serial Number Profile |  |
| Service Bundle (Time and Material) | SRV_BUNDLE_02 | Service Bundle | You can use service bundles to offer customers service products, service parts, and expense items as a package.Your customer is not invoiced the main item of the time and material service bundle. You can use standard subitems where your customer is billed the actual consumption of labor and materials and you can also use fixed price subitems where your customer is billed previously agreed prices. |
| Service Bundle (Fixed Price) | SRV_BUNDLE_01 | Fixed Price Service Bundle | You can use service bundles to offer customers service products, service parts, and expense items as a package.A fixed price service bundle consists of a main item and one or more subitems. Your customer receives a billing document for the main item, subitems are not invoiced separately. |
| Product | TG30 233100901 | Trading Good, Return Order for Repair |  |
| Equipment | 233100901233100902 |  | If you create new equipment, you have to configure the serial number profile and assign it to the material master. |
| Service Product (Service Contract) | SRV_CONTRACT | Service Contract Product |  |
| Material BOM, Equipment BOM | SRV_BOM_* |  | If you want to use product proposals, you must maintain the BOM items as described in Create Material and Equipment BOM for Service - MDS (63J). |
| Material | <material> |  | If you want to test the integration of Customer Returns (BKP) with a standard sales process, create your material and assign the YSR1 serialization profile.You must complete the sales process for your material as described in theSell from Stock (BD9) test script.You will need the sales order ID, the billing document number, and the equipment (serial number) that is assigned to the delivery.Use this equipment (serial number) as the repair object in your in-house repair transaction. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| Master Data ID | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| 2J7 | Create Product Master of type "Spare Parts" - MDS |
| 31X | Create Product Master of type "Service Product" - MDS |
| 3U3 | Create Plant Maintenance Master Data for Service - MDSNote The in-house repair process only supports equipment created with a serial number.You have to configure the serial number profile and assign it to the material master. |
| BHD | Create Purchasing Info Record - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| 31Y | Create Product Master of type "Non-Stock Material" - MDS |
| BND | Create Customer Master - MDS |
| 63J | Create Material and Equipment BOM for Service - MDS |
| BNV | Create SEPA Mandate - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1LQ - Output Management | Must complete all mandatory prerequisite steps. |
| 3D2 - Service Order Management and Monitoring | Must be in scope as prerequisite. Preliminary steps must be completed. |
| 3NI - Procurement for Service Management | To use procured spare parts with in-house repair, must be in scope as prerequisite.To use external workforce procurement with in-house repair, must be in scope as prerequisite. |
| 31N - Situation Handling (Optional) | To use situation handling with in-house repair, must be run before this test script. |
| 3MO - Service Contract Management (Optional) | To use service contract management with in-house repair, must be run before this test script. |
| BKP - Customer Returns (Optional) | To use customer returns with in-house repair, must complete all mandatory prerequisites. |
| BD9 - Sell from Stock (Optional) | To use customer returns with a standard sales process, the sales process must be completed. |

### Preliminary Steps

#### Configure Service Management and Monitoring

Prerequisite

Scope item Service Order Management and Monitoring (3D2) must be activated as a prerequisite for In-House Repair.

The following steps described in the Service Order Management and Monitoring test script are mandatory for In-House Repair:

- (for example, as employee responsible)
- (for testing with stock service parts)
- (used to determine the internal cost)

|  |
| --- |
| Note In an intercompany scenario, special intercompany cost rates are required and must be maintained. You can refer to the step Maintain Cost Rates in the Service Order Management and Monitoring (3D2) test script. |

#### Configure Credit Check Management (Optional)

Purpose

You use Credit Management to minimize financial risks for your organization. It enables you to display a business partner's credit rating, or to perform a credit check when creating a transaction document.

Credit checks can be enabled for repair orders to maintain and check credit of relevant business partners.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: General Settings |  |  |
| 5 | Open | Open Credit Management. |  |  |
| 6 | Select Configuration Step | For the Activate Credit Management in Transactions step, choose Configure. | The Activate Credit Management in Transactions screen displays. |  |
| 7 | Maintain Data | To activate the credit management settings for service orders, make the following entires and choose Save:Trans. Type: RPO1Description: Repair OrderCredit Management: SelectedTrans. Type: RPO2Description: Fixed Price Repair OrderCredit Management: Selected | The credit management settings are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Credit Management in Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Credit Management in Transactions screen displays. |  |
| 3 | Maintain Data | To activate the credit management settings for service orders, make the following entires and choose Save:Trans. Type: RPO1Description: Repair OrderCredit Management: SelectedTrans. Type: RPO2Description: Fixed Price Repair OrderCredit Management: Selected | The credit management settings are saved. |  |

#### Specify Settings for Returns Orders as Follow-Up

Purpose

Before you can create and process a returns order as the follow-up document within the in-house repair process, you need to configure customer returns.

In this step, you configure the returns order type that is used as the follow-up document for the in-house repair type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: In-House Repair |  |  |
| 5 | Open | Open Integrating with Customer Returns. |  |  |
| 6 | Select Configuration Step | For the Specify Settings for Returns Orders as Follow-Up step, choose Configure. | The Specify Settings for Returns Orders as Foll..: Change screen displays |  |
| 7 | Specify Settings | Choose New Entries.Make the following entries and choose Save:Transaction Type: REP1Sales Document Type: CBAROrder Reason: 009Return Reason: 004Goods Movement: Selected | The entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Settings for Returns Orders as Follow-Up.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens. |  |
| 3 | Specify Settings | Choose New Entries.Make the following entries and choose Save:Transaction Type: REP1Sales Document Type: CBAROrder Reason: 009Return Reason: 004Goods Movement: Selected | The entry is saved. |  |

#### Configure Customer Returns (Optional)

Prerequisite

For logistics, the in-house repair application is integrated with the customer returns application.

If you want to use the customer returns as part of In-House Repair, Customer Returns (BKP) must be in scope and all mandatory configuration steps described in the test script must be completed.

##### Specify Settings for In-House Repair (Service) as Follow-Up Activity

Purpose

Before you can use the customer returns application, you must configure the in-house repair type that is used as the follow-up document type for the standard return type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: SalesSub Application Area: Claims, Returns, and Refund Management |  |  |
| 5 | Open | Open Follow-Up Activities for Customer Returns. |  |  |
| 6 | Select Configuration Step | For the Specify Settings for In-House Repair (Service) as Follow-Up Activity step, choose Configure. | The configuration activity opens. |  |
| 7 | Specify Settings | Choose New Entries.Make the following entries and choose Save:Ret. Order: CBARTrans. Type: REP1Goods Movement: Selected | The entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Settings for In-House Repair (Service) as Follow-Up Activity.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens. |  |
| 3 | Specify Settings | Choose New Entries.Make the following entries and choose Save:Ret. Order: CBARTrans. Type: REP1Goods Movement: Selected | The entry is saved. |  |

##### Specify Storage Locations for Follow-Up Activities

Purpose

Before you can use customer returns, you must specify a storage location.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: SalesSub Application Area: Claims, Returns, and Refund Management |  |  |
| 5 | Open | Open Follow-Up Activities for Customer Returns. |  |  |
| 6 | Select Configuration Step | For the Specify Storage Locations for Follow-Up Activities step, choose Configure. | The configuration activity opens. |  |
| 7 | Specify Storage Location | Make the following entries and choose Save:Plant: 3310Storage Location: 331AIn-House Repair (Service): for example, 331R | The entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Storage Locations for Follow-Up Activities.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens. |  |
| 3 | Specify Storage Location | Make the following entries and choose Save:Plant: 3310Storage Location: 331AIn-House Repair (Service): for example, 331R | The entry is saved. |  |

##### Define Serial Number Profiles

Purpose

If you want use customer returns with in-house repair, you must assign the serializing procedure ADVR to your serial number profile. This procedure controls whether an in-house repair can be created with the assigned serial number.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: LogisticsSub Application Area: Serial Number Management |  |  |
| 5 | Open | Open General Settings. |  |  |
| 6 | Select Configuration Step | For the Define Serial Number Profiles step, choose Configure. | The Define Serial Number Profiles: Change screen displays. |  |
| 7 | Verify Settings | Select your serial number profile, for example, YSR1.Double-click Serializing procedures on the left.Ensure that the serializing procedure ADVR is assigned. | The serializing procedure ADVR is assigned. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Serial Number Profiles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens. |  |
| 3 | Verify Settings | Select your serial number profile, for example, YSR1.Double-click Serializing procedures on the left.Ensure that the serializing procedure ADVR is assigned. | The serializing procedure ADVR is assigned. |  |

#### Maintain Customer, Customer Warranty and Vendor Warranty (Optional)

Purpose

A warranty is a commitment from a manufacturer, vendor, or salesperson to a customer that a product has no defects, and that services such as repairs and partial or complete exchange of defective parts are guaranteed for a particular period of time, without the customer being billed.

The in-house repair process supports and integrates warranties that are based on dates (warranty period). You can use the following warranty types with in-house repair:

- Customer warranty: A commitment that your company has made to the customer.
- Vendor warranty: A commitment that has been made by the vendor/supplier to your company.

If you have entered the end date for the customer warranty of equipment or the end date for the vendor warranty of equipment, the system checks if the warranty end date is prior to the creation date of the in-house repair. An icon indicates whether the creation date of the in-house repair is within the warranty period.

Before you can use the warranties for individual repair objects within your in-house repair process, you need to define the basic conditions and requirements.

You need to enter the warranty start date and warranty end date in the equipment master data. For the creation or maintenace of equipment warranties, you can refer to master data script Create Plant Maintenance Master Data for Service - MDS (3U3).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. |  |  |
| 2 | Access App | Open Change Material Serial Number (IQ02). | The Change Material Serial Number : Initial screen displays. |  |
| 3 | Enter Data | Make the following entries and press Enter:Material: <material>Serial Number: <serial number> | The Change Material Serial Number : SerNo.Detail screen displays. |  |
| 4 | Maintain Data | Under Customer data, make the following entries and choose Save:PartnersPartner Function: Ship-To PartyPartner: <customer> | The changes are saved. |  |

#### Configure Service Teams

Purpose

The service team is an organizational unit to which service employees are assigned for performing service tasks. It facilitates the assignment of service employees in service transactions, related analytics, and the search for service transactions.

|  |
| --- |
| Caution The service teams concept is not active by default for the in-house repair process.This section is only relevant if you want to use the service team concept. |

|  |
| --- |
| Note For more information, see [How to Use Service Teams in Service Transactions on SAP S/4HANA](https://s4hanacloud.community.sap/blogs/show/QFI5atByKCVVkwurEtxNsI). |

##### Define Service Team Profile

Purpose

A service team profile exists by default. It defines which determination rule is used and for which team types it is relevant. If you want to use a different profile, you can follow the procedure below to create a new entry.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Service Teams. |  |  |
| 6 | Select Configuration Step | For the Define Service Team Profile and Assign Service Team Types step, choose Configure. | The screen Define Service Team Profile and Assign Serv..: Change screen displays. |  |
| 7 | Define Team Profile | There should be at least one existing entry:Profile:SRV_IHR_PDescription:In-House Repair Team ProfileDetermination Rule:SHIP_TODescription:<country/region and postal code of ship-to party>Auto Redetermine:SelectedIf you want to use another profile, you have to create a new entry here. | A valid service team profile exists. |  |
| 8 | Specify Allowed Team Types | Select an existing team profile and doublc-click Specify Allowed Team Types in the Dialog Structure.For the team profile SRV_IHR_P, you should find the following entry:Team Type: SRV_IHRDescription: In-House RepairIf you have created and selected a new profile, maintain the allowed team types here. | A valid service team profile including allowed team types exists. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Service Team Profile and Assign Service Team Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The screen Define Service Team Profile and Assign Serv..: Change screen displays. |  |
| 3 | Define Team Profile | There should be at least one existing entry:Profile:SRV_IHR_PDescription:In-House Repair Team ProfileDetermination Rule:SHIP_TODescription:<country/region and postal code of ship-to party>Auto Redetermine:SelectedIf you want to use another profile, you have to create a new entry here. | A valid service team profile exists. |  |
| 4 | Specify Allowed Team Types | Select an existing team profile and doublc-click Specify Allowed Team Types in the Dialog Structure.For the team profile SRV_IHR_P, you should find the following entry:Team Type: SRV_IHRDescription: In-House RepairIf you have created and selected a new profile, maintain the allowed team types here. | A valid service team profile including allowed team types exists. |  |

##### Assign Service Team Profile to Repair Transactions

Purpose

If you want to use the service team concept, you should assign at least a service team profile to a repair transaction and to its related confirmation transaction.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Service Teams. |  |  |
| 6 | Select Configuration Step | For the Assign Service Team Profile to Service Transaction Type step, choose Configure. | The Assign Service Team Profile to Service Transaction screen displays. |  |
| 7 | Maintain Data | If you want to use the service team concept with repair orders, make the following entries and choose Save:Trans.Type: RPO1Description: Repair OrderService Team Profile: SRV_IHR_PDescription: In-House Repair Team ProfileTrans.Type: RPC1Description: Repair ConfirmationService Team Profile: SRV_IHR_PDescription: In-House Repair Team Profile | The service team concept has been activated for the standard repair order and its repair confirmation. |  |
| 8 | Maintain Data | If you want to use the service team concept with fixed price repair orders, make the following entries and choose Save:Trans.Type: RPO2Description: Fixed Price Repair OrderService Team Profile: SRV_IHR_PDescription: In-House Repair Team ProfileTrans.Type RPC2Description: Repair Confirmation (Cost Relevant)Service Team Profile: SRV_IHR_PDescription: In-House Repair Team Profile | The service team concept has been activated for the fixed price repair order and its repair confirmation. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Service Team Profile to Service Transaction Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Service Team Profile to Service Transaction screen displays. |  |
| 3 | Maintain Data | If you want to use the service team concept with repair orders, make the following entries and choose Save:Trans.Type: RPO1Description: Repair OrderService Team Profile: SRV_IHR_PDescription: In-House Repair Team ProfileTrans.Type: RPC1Description: Repair ConfirmationService Team Profile: SRV_IHR_PDescription: In-House Repair Team Profile | The service team concept has been activated for the standard repair order and its repair confirmation. |  |
| 4 | Maintain Data | If you want to use the service team concept with fixed price repair orders, make the following entries and choose Save:Trans.Type: RPO2Description: Fixed Price Repair OrderService Team Profile: SRV_IHR_PDescription: In-House Repair Team ProfileTrans.Type RPC2Description: Repair Confirmation (Cost Relevant)Service Team Profile: SRV_IHR_PDescription: In-House Repair Team Profile | The service team concept has been activated for the fixed price repair order and its repair confirmation. |  |

##### Create a Service Team

Purpose

If you want to use the service team concept, you have to create at least one service team to run the service process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create A New Team | Choose Create. | The Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and press Enter:Name: Repair_Team_AEDescription: Repair Team AEType: SRV_IHR |  |  |
| 5 | Enter Responsibility Definitions | Under Responsibility Definitions, make the following entries:Cost Center: <cost center>Country/Region: AEPostal Code: <empty>Service Part Plant: 3310Service Part Storage Location: 331A |  |  |
| 6 | Enter Team Owner | It is recommended to leave the default team owner. |  |  |
| 7 | Enter Team Members | Choose Create.Choose Edit.Enter data for each team member of this service team:Business Partner: for example, 9980000XXXFull Name: <team member's name>User ID: for example, CB9980000XXXFunction: Executing Service Employee (SRVC_EMPL)Choose Create. | A service team has been created successfully. |  |

#### Configure Output Management

Purpose

To meet your business needs for flexible output of repair quotations and repair orders, SAP provides applications and rules to manage output.

|  |
| --- |
| Note For more information, see [Output Management in SAP S/4HANA](https://blogs.sap.com/2021/04/26/output-management-in-sap-s-4hana/). |

Prerequisite

You must complete the configuration steps that are described in [Setting Up Output Management (1LQ)](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/1LQ_Set-Up_EN_XX.pdf).

Procedure

Output Parameter Determination

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Show Rules | Make the following entries:Show Rules for: Service Order Quotation or Service OrderDetermination Step: Output Type | The transaction types for the service order or the service order quotation display.Note The following output types are relevant for in-house repair:Repair OrderREPAIR_ORDER_SUMMARY_EXTREPAIR_ORDER_SUMMARY_INTRepair QuotationREPAIR_QUTAN_SUMMARY |  |
| 4 | Maintain Output Types | If the output types have been added by the system, you need to configure the following determination steps:ReceiverChannelPrinter SettingsEmail SettingsEmail RecipientForm TemplateOutput Relevance |  |  |
| 5 | Maintain Delivery Channel (Optional) | Make the following entries:Determination Step: ChannelChoose Edit.For each output type, make the following entires:Channel: EMAIL (Email)Channel: PRINT (Printout) | The delivery channels are added for the output types REPAIR_QTAN_SUMMARY, REPAIR_ORDER_SUMMARY_EXT,, and REPAIR_ORDER_SUMMARY_INT. |  |
| 6 | Maintain Templates (Optional) | Make the following entries:Determination Step: Email Settings or Form TemplateYou can specify the template that you use for repair quotation documents. | Note SAP delivers the following templates for repair quotations and repair orders:CRMS4_REPAIR_QTAN_SUMMARY_2 (Form Template for Repair Quotations)CRMS4_REPAIR_QTAN_EMAIL (Email Template for Repair Quotations)CRMS4_REPAIR_ORDER_SUMMARY_INT (Form Template for Repair Orders)CRMS4_REPAIR_ORDER_SUMMARY_EXT (Form Template for Repair Orders)CRMS4_REPAIR_ORDER_EMAIL_TMPL (Email Template for Repair Orders) |  |
| 7 | Maintain Output Relevance (Optional) | Make the following entries:Determination Step: Output RelevanceFor each output type, you configure the status that is relevant for the output generation.To add custom or missing condition columns, choose Edit.Choose Table Settings > Insert Column .Select the missing fields and choose OK. | The settings are maintained |  |
| 8 | Check and Activate Rules | Choose Check to verify that the settings are consistent.To activate the object for productive use, choose Activate. | The output management has been configured according to your requirements. |  |

Email and Form Templates

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. |  |  |
| 2 | Access App | Open Maintain Email Templates - Deprecated (F1306) or Maintain Form Templates (F1434). | The following Predelivered templates are available:Form TemplateCRMS4_REPAIR_QTAN_SUMMARY_2CRMS4_REPAIR_ORDER_SUMMARY_INT,CRMS4_REPAIR_ORDER_SUMMARY_EXTEmail TemplateCRMS4_REPAIR_QTAN_EMAILCRMS4_REPAIR_ORDER_EMAIL_TMPLNote You can make changes to the template with the Adobe LiveCycle Designer. |  |

#### Configure Situation Handling (Optional)

Purpose

Situation handling recognizes business situations by evaluating conditions (rules) on business facts. A business situation occurs when a business object changes a status relevant to a user, when critical deadlines are passed, or a KPI passes a threshold.

Prerequisite

If you want to use situation handling with In-House Repair, Situation Handling (31N) must be in scope. You must carry out the steps that are described in the Situation Handling (31N) test script.

For more information, see [Setting Up Situation Handling (31N)](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/31N_Set-Up_EN_XX.pdf)

Procedure

To set up situation handling, create your ready-to-use situation type, maintain the message to be displayed, define the conditions to determine when the situation will be triggered, define recipient groups who will receive notifications, and monitor the instances.

The following standard situation templates are defined and delivered by SAP for In-House Repair:

- SRVC_DELAY_IN_PRECHECK (Precheck of In-House Repair Delayed)
- SRVC_DELAY_IN_IHR_CONFIRMATION (In-House Repair Not Confirmed)
- SRVC_DELAY_IN_OBJECT_REPAIR (Object Repair Time Overdue)
- SRVC_DELAY_IN_IHR_PROCESSING (Processing of In-House Repair Overdue)
- SRVC_PENDING_REPAIRCONFIRMATION (Repair Confirmations Required)

For each situation template, a corresponding responsibility rule is defined in which the responsible person to be notified can be assigned.

For more information and situation template details (default settings, conditions, notification recipients), see [Situation Templates in Service](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/LATEST/en-US/9d6cee508b2e44a39e93474ee68e6ba9.html).

#### Configure Service Contract Management (Optional)

Purpose

Customer-specific price agreements can be defined and handled within service contracts. Service contract determination can be enabled for repair orders that are created with reference to a service contract – in this case, the contract and price details determined from the service contract are considered.

Prerequisite

If you want to use, service contract management with In-House Repair, Service Contract Management (3MO) must be in scope. You must carry out the steps described in the Service Contract Management test script.

##### Specify Contract Determination for Transaction Types

Purpose

To display the applicable service contracts for in-house repair, you can use service contract determination.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Contract Management |  |  |
| 5 | Open | Open Service Contract Determination. |  |  |
| 6 | Select Configuration Step | For the Specify Contract Determination Option for Trans. Types step, choose Configure. | The Specify Contract Determination Option for T..: Change screen displays |  |
| 7 | Specify Settings | Specify the Contract Determination that should be used for repair transation types and choose Save. | The entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Contract Determination Option for Trans. Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The configuration activity opens. |  |
| 3 | Specify Settings | Specify the Contract Determination that should be used for repair transation types and choose Save. | The entry is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Receive Repair Objects with Customer Returns (Optional) |  |  |  |
| [Create Customer Returns Order](#unique_27) [page ] 36 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | The returns order is created. |
| [Execute Picking](#unique_28) [page ] 38 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The delivery is picked. |
| [Post Goods Receipt](#unique_29) [page ] 39 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted. |
| [Perform Material Inspection](#unique_30) [page ] 40 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | The inspection result is recorded. |
| [Display Returns Overview](#unique_31) [page ] 41 | Returns and Refund Clerk | Manage Customer Returns (F1708) | A returns order is created from the inspection and is listed under Repair Processing. |
| [Create In-House Repair and Add Repair Objects](#unique_32) [page ] 42 | Customer Service Representative - In-House Repair | Manage In-House Repairs (F4025) | The in-house repair is created and saved. |
| [Decide Follow-Up Steps (Optional)](#unique_33) [page ] 50 | Customer Service Representative - In-House Repair | Manage In-House Repairs (F4025) | The follow-up action is triggered. |
| [Perform Prechecks](#unique_34) [page ] 52 |  |  |  |
| [Perform Precheck and Decide Follow-Up Steps](#unique_35) [page ] 52 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | The returns order is checked and the follow-up is decided. |
| [Create Quotation](#unique_36) [page ] 54 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | A repair quotation for a repair object is created. |
| [Send Repair Quotation to Customer](#unique_37) [page ] 56 | Customer Service Manager - In-House Repair | Process Repair Quotations (F4580) | The repair quotation is sent to the customer. |
| [Accept or Reject Repair Quotation](#unique_38) [page ] 58 | Customer Service Manager - In-House Repair | Process Repair Quotations (F4580) | The repair quotation is accepted or rejected. |
| [Create Repair Order or Create Fixed Price Repair Order](#unique_39) [page ] 59 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | The repair order is saved. |
| Trigger Diagnosis Planning, Plan Diagnosis, Trigger Diagnosis and Perform Diagnosis in Repair Order (Optional) |  |  |  |
| [Trigger Diagnosis Planning in Repair Order](#unique_40) [page ] 63 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | The Status of the repair object has changed to Diagnosis: Plan. |
| [Plan Diagnosis](#unique_41) [page ] 64 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | All diagnosis relevant items are entered. |
| [Trigger Diagnosis in Repair Order](#unique_42) [page ] 65 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | The Status of the repair object has changed to Diagnosis: Perform. |
| [Perform Diagnosis](#unique_43) [page ] 66 | Service Technician - In-House Repair | Perform Repairs (F4241) | A repair confirmation has been created. |
| [Trigger Follow-Up Actions for Diagnosis](#unique_44) [page ] 67 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | The Status of the repair object has changed to Diagnosis: Follow-Up. |
| [Create Diagnosis Follow-Up](#unique_45) [page ] 69 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | The repair object status changes to Repair: Plan. |
| [Trigger Repair Planning in Repair Order](#unique_46) [page ] 70 | Customer Service Representative - In-House Repair | Perform Prechecks (F4050) | The Status of the repair object has changed to Repair: Plan. |
| [Plan Repairs](#unique_47) [page ] 71 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | The data of the repair order have been updated. The planning has been finalized. |
| [Trigger Repair](#unique_48) [page ] 73 | Customer Service Manager - In-House Repair | Plan Repairs (F4152) | The status of the repair object changes to Repair: Perform and appears in the worklist of the service technician. |
| [Perform Repairs](#unique_49) [page ] 75 |  |  |  |
| [Overview Table](#unique_26) [page ] 33 | Service Technician - In-House Repair | Perform Repairs (F4241) | The repair confirmaiton is created.. |
| [Cancel Repair Confirmation (Optional)](#unique_50) [page ] 78 | Service Technician - In-House Repair | Perform Repairs (F4241) | The repair confirmation is canceled. |
| [Prepare and Release for Billing](#unique_51) [page ] 79 | Customer Service Representative - In-House Repair | Prepare for Billing (F4263) | The selected items are released for billing. |
| [Return to Customer (Optional)](#unique_52) [page ] 81 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted. |
| [Complete Repair Object and Finalize In-House Repair (Optional)](#unique_53) [page ] 82 | Customer Service Representative - In-House Repair | Prepare for Billing (F4263) | The status of the repair object is set to Completed. |
| [Create Invoice (Optional)](#unique_54) [page ] 83 | Billing Clerk | Create Billing Documents (F0798) | The billing document is created. |
| [Create Repair Template (Optional)](#unique_55) [page ] 85 | Customer Service Representative - In-House Repair | Manage Service Order Templates (F5007) | The repair template is saved and released.. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Create In-House Repair

#### Option A: Start With Customer Returns and Process In-House Repair

##### Create Customer Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before creating in-house repairs, users can create return orders and execute the posting of goods receipts. Integration with In-House Repair functionality enhances inbound and outbound logistics functionality for in-house repairs.

|  |
| --- |
| Note To test customer returns functionality with the In-House Repair scope item, include the Customer Returns (BKP) scope item.To use customer returns with In-House Repair, assign the SAP business roles SAP_BR_RECEIVING_SPECIALIST, SAP_BR_CUST_SRVC_REP_REPA, and SAP_BR_RETURNS_REFUND_CLERK to your test users. |

Procedure

This process step demonstrates how to create a custome returns order and describes the integration of Customer Returns (BKP) with In-House Repair (3XK) in SAP S/4HANA Cloud Public Edition.

Depending on the parallel processing progress of this customer return, the availability at the repair center of the repair objects can be:

- Not Tracked

No returns order has been created for the repair objects.

- Delivery to Repair Center Pending

The returns order has been created for the repair object, but the repair object has not yet arrived at the repair center. A material inspection has not yet been performed.

- Received by Repair Center

The repair object has arrived at the repair center and the material inspection in the customer returns process has been performed. Start the diagnosis or repair within the in-house repair process.

An outbound delivery can be triggered to send the repair object back to the customer.

- Delivery to Repair Center Canceled

The in-house repair process has been denied for the repair object in the returns order.

- Sent Back by Repair Center

An outbound delivery has been triggered to send the repair object back to the customer.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. |  |  |
| 2 | Access App | Open Manage Customer Returns - Version 2 (F4832).Note Alternatively, create a returns order without reference using Create Sales Orders - VA01 (VA01). After manually entering order type CBAR and other necessary data, choose Save to create a returns order without reference. | The Manage Customer Returns screen displays. |  |
| 3 | Create Returns Order | Choose Create.Make the following entries and choose Continue:Returns Order Type: Standard Return CBARSales Organization: for example, 1010Distribution Channel: for example, 10Division: for example, 00Choose Continue. | The New: Returns Order screen displays. |  |
| 4 | Enter Details | Make the following entries and choose Save:Sold-to Party: for example, 10100001Returns Order Reason: Standard Return | The returns order is created.The returns order number displays |  |
| 5 | Create Item | Choose Edit.On the Items tab, choose Create.Make the following entries:General InformationProduct: TG30Returned Quantity: 1Return Reason: for example, Product Defective (004)Storage Location: for example, 101AFollow-up ActivityFollow-up Activity: Receive into Plant (0001)RefundRefund Type: Credit MemoRefund Control: Decide laterChoose Apply. | The New: Returns Order Items displays. |  |
| 6 | Save and Release | Choose Save and Release.Choose Back. | The list report of returns orders displays. |  |
| 7 | Check Delivery Number | Select the row with the returns order you created.Choose the Process Flow tab.Make a note of the Returns Delivery. | The process flow displays. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, users perform picking of returns deliveries created previously. This process step demonstrates how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
|  | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The Manage Outbound Deliveries screen appears. |  |
|  | Enter Data | Choose For Picking.Make the following entries and select Execute:Shipping Point/Receiving Pt: 101R | The Outbound Deliveries for Picking screen appears. |  |
|  | Change Outbound Delivery | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
|  | Enter Picked Quantity | On the Picking tab, enter the quantity equal to the delivery quantity in the Picked Qty field. |  |  |
|  | Change Outbound Delivery | To maintain the serial number for material TG30, choose Menu delete> Extras > Serial Numbers.Make the following entries and select Continue:Serial Number: serial numberSelect Continue. | The list report of returns orders displays. |  |
|  | Save | Select Save. | The delivery is picked. |  |

##### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, a goods receipt is posted for the returns delivery. This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
|  | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The Manage Outbound Deliveries screen displays. |  |
|  | Enter Data | Choose For Goods Issue.Make the following entries and choose Execute:Shipping Point/Receiving Pt: 101R | The Outbound Deliveries for Goods Issue screen displays. |  |
|  | Post Goods Receipt | On the Goods Issue for Outbound Delivery to be Posted screen, select your delivery and choose Post Goods Issue.Make the following entries and choose Continue:Act. Gds Mvmnt Date: for example, <today's date> | The goods receipt is posted. |  |

##### Perform Material Inspection

Purpose

This process step guides you through performing a material inspection after the warehouse receives returned goods. Decisions are made regarding the further handling of these goods.

Prerequisite

Returned goods have been received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
|  | Access App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
|  | Maintain Selection Criteria | Make the following entries and choose Execute:Delivery Items Waiting for Inspection: SelectedDelivery: returns delivery number | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| X`4 | Maintain Inspection Result | Choose the Item tab.Under Inspection Result make the following entries:Inspection Code: for example, 0002 not okInspected Quantity: quantityPress Enter.If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
|  | Maintain Follow-up Activity | Under Logistical Follow-Up, make the following entries:Follow-Up Activity: 0026 Inhouse Repair (Service)Note If you started the repair process directly from in-house repair, enter 0027 (Continue In-House Repair (Service).In this case, continue with chapter Create Repair Quotation (Optional) or Create Repair Order.Press Enter. |  |  |
|  | Check Inspection Status | Choose the Header tab.Under Basic Data, verify that the Inspection Status displays Inspected, which means all received materials have been inspected completely. | All received materials have been inspected. |  |
|  | Save and Confirm | Select Save and Confirm. | The inspection result is recorded. |  |

##### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you check the return process' progress.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. |  |  |
|  | Access App | Open Manage Customer Returns (F1708) | The Manage Customer Returns screen is displayed. |  |
|  | Maintain Selection Criteria | Make the following entries and choose Go:Returns Order: order number |  |  |
|  | Select Returns Order | Choose your Returns Order. | The Returns Order screen displays. |  |
|  | Check Document Flow | Choose the Process Flow tab.Note down the in-house repair document number. | A returns order is created from the inspection and is listed under Repair Processing. |  |

|  |
| --- |
| Note You can now perform the in-house repair process starting with the step [Perform Prechecks](#unique_34) [page ] 52.It is not necessary to complete [Perform Prechecks](#unique_34) [page ] 52. The in-house repair and the repair object have already been created by performing the material inspection during the returns process. |

#### Option B: Start With In-House Repair

##### Create In-House Repair and Add Repair Objects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create an in-house repair. You provide organizational data, partner data and line items.

|  |
| --- |
| Note Note If you have enabled the service contract determination, you get notified if one or more valid contracts exist while creating an in-house repair.For more information, see Configure Service Contract Management (Optional). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Manage In-House Repairs (F4025). | The Manage In-House Repairs screen is displayed. |  |
| 3 | Create Repair | Choose Create. | The New In-House Repair screen is displayed. |  |
| 4 | Enter Data | Open the selection view for Sold-To Party.Make the following entries and choose Go:Customer: 10100001Select the row in the items list containing the following:Customer: 10100001Sales Organization: 1010 |  |  |
| 5 | Check Organizational Data | Ensure that the following values are maintained:Sales Organization: 1010Distribution Channel: 10Division: 00 | The data for the in-house repair are correct.Note If you do not enter a Sales Organization for the in-house repair, the system automatically adds the sales organization of the sold-to party. |  |
| 6 | Enter Employee | Make the following entries:Employee Responsible: <employee> | Note If you do not enter an Employee Responsible for the in-house repair, the system adds the current user. |  |
| 7 | Save Repair | Choose Create. | The in-house repair is created and saved.Note If you do not enter a Contact Person for the in-house repair, the system adds the contact person (if any) of the sold-to party. |  |
| 8 | Check In-House Repair | If the system displays a message, you must correct the entries in the in-house repair. Then, choose Save.If no message displays, the in-house repair is automatically saved. |  |  |
| 9 | Add Repair Objects | Under Repair Objects, you can add repair objects to the list.Choose Add.In the Add Repair Objects dialog box, you may remove the filter Current Customer to display all equipment.Choose Add. | An new row under Repair Objects is added.Note Equipment that has products with assigned serial numbers is supported.By default, only equipment that is assigned to the sold-to party is displayed in the search help. You can remove the filter Current Customer if you want to display other equipment. |  |
| 10 | Confirm Repair | To confirm the repair objects added, choose Confirm for the in-house repair. | The in-house repair is set to status In Process and the repair objects are set to status Precheck: Decision Pending.You cannot add further repair objects. |  |
| 11 | Reject repair | To reject the In-house repair, choose Reject for the in-house repair. Give a rejection reason in the Reject In-house repair dialog window, and click on Reject.Note Rejection can be done both at the header as well as item level. To reject any item, choose the item from the Items section and select "Reject" option at the Item level actions. | The in-house repair is marked as “Completed” with the specified rejection reason, and the repair objects’ statuses are updated to match the rejection reason defined at the header level. |  |

##### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can select multiple repair objects and trigger the following actions:

- Returns Order to manage the return of the repair objects by the customer.
- Create Repair Quotation or Create Fixed Price Repair Quotation.
- Create Repair Order or Create Fixed Price Repair Order to plan and perform the diagnosis or the repair.
- Outbound Delivery to send the repair object back to the customer (available if a returns order has been created and repair object is available in the repair center).
- Set Repair Object to Completed to finalize the in-house repair process for the repair object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Manage In-House Repairs (F4025). | The Manage In-House Repairs screen is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Go:In-House Repair: <repair ID> |  |  |
| 4 | Choose In-House Repair | Choose your In-House Repair from the list. | The Manage In-House Repair Details screen is displayed. |  |
| 5 | Select Repair Objects | Choose Repair Objects.Select the the items to be processed. | The Decide button is available.Note The Decide button is active only when at least one repair object is selected. |  |
| 6 | Display Decision Options | Choose Decide. | The Decide dialog box is displayed. |  |
| 7 | Make Decision for Repair Objects | Choose Returns Order:Alternatively, you can choose one of the following actions:Create Repair QuotationCreate Fixed Price Repair QuotationCreate Repair OrderCreate Fixed Price Repair OrderOutbound DeliverySet Repair Object to CompletedNote If multiple repair objects are selected, the Decide dialog box contains a list of actions that can be performed for the selected repair objects.The Outbound Delivery action is available if the repair object availability is set to Received by Repair Center status. | The Returns Order action is executed, the returns order is created. |  |
| 8 | Access App | Open Perform Prechecks (F4050). | The Perform Prechecks screen is displayed. |  |
| 9 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 10 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment.The following information is displayed for the repair object:Customer Warranty EndVendor Warranty EndEquipmentProductSerial NumberCustomer (Sold-To Party, Ship-To Party, Contact Person)Status: Precheck: Decision Pending | The Perform Precheck Details screen is displayed. In this mode, you cannot change any data.The repair object availability changes to Delivery to Repair Center Pending status.Note If you have enabled the service contract determination and your sold-to-party is associated with one or more service contracts, a list of all applicable contract items is displayed.If you have maintained the warranty end date for the equipment, an icon indicates whether the creation date of the in-house repair is within the warranty period of the related equipment.For more information, see the preliminary step [Maintain Customer, Customer Warranty and Vendor Warranty (Optional)](#unique_17) [page ] 20. |  |
| 11 | Check Returns Delivery | Under Transaction History, you find the Returns Order you have created.Choose the Returns Order > Display Customer Return .Under Returns Control, choose Returns Overview.Under Returns Steps, note down the Returns Delivery number. | The Tranasction History is displayed.If you completed [Create In-House Repair](#unique_57) [page ] 36, the Returns Order will have the status Completed. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, picking is done for the returns delivery created previously. This process step shows how to perform picking.

Prerequisite

Steps in [Create Returns Order](#unique_58) [page ] 44 were executed and a returns order was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen is displayed. |  |
| 3 | Enter Data | Choose For Picking.Make the following entries and choose Execute:Shipping Point/Receiving Pt: 101R | The Outbound Deliveries for Picking screen is displayed. |  |
| 4 | Change Outbound Delivery | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 5 | Enter Picked Quantity | On the Picking tab, enter the quantity equal to the delivery quantity in the Picked Qty field. |  |  |
| 6 | Change Outbound Delivery | To maintain the serial number for material TG30, choose > Extras > Serial Numbers .Make the following entries and choose Continue:Serial Number: <serial number>Note Alternatively, you can choose Create Serial Number automatically.Choose Continue. | The list report of returns orders is displayed. |  |
| 7 | Save | Choose Save. | The delivery is picked. |  |

##### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, a goods receipt is posted for the returns delivery. This process step shows you how to post a goods receipt.

Prerequisite

Steps [Execute Picking](#unique_59) [page ] 47 were executed and a returns order was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen is displayed. |  |
| 3 | Enter Data | Choose For Goods Issue.Make the following entries and choose Execute:Shipping Point/Receiving Pt: 101R | The Outbound Deliveries for Goods Issue screen is displayed. |  |
| 4 | Post Goods Receipt | On the Goods Issue for Outbound Delivery to be Posted screen, select your delivery and choose Post Goods Issue.Make the following entries and choose Continue:Act. Gds Mvmnt Date: for example, <today's date> | The goods receipt is posted. |  |

##### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform a material inspection after the warehouse received the returned goods. The further handling of the returned goods is decided.

Prerequisite

The returned goods have been received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. |  |  |
| 2 | Access App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen is displayed. |  |
| 3 | Maintain Selection Criteria | Make the following entries and choose Execute:Delivery Items Waiting for Inspection: SelectedDelivery: <returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen is displayed. |  |
| 4 | Maintain Inspection Result | Choose the Item tab.Under Inspection Result make the following entries:Inspection Code: for example, 0002 not okInspected Quantity: <quantity>Press Enter.If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 5 | Maintain Follow-up Activity | Under Logistical Follow-Up, make the following entries:Follow-Up Activity: 0026 Inhouse Repair (Service)Note In this case, continue with chapter Create Repair Quotation (Optional) or Create Repair Order.Press Enter. |  |  |
| 6 | Check Inspection Status | Choose the Header tab.Under Basic Data, verify that the Inspection Status displays Inspected, which means all received materials have been inspected completely. | All received materials have been inspected. |  |
| 7 | Save and Confirm | Choose Save and Confirm. | The inspection result is recorded. |  |

### Decide Follow-Up Steps (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can select multiple repair objects and trigger the following actions:

- Create Repair Quotation or Create Fixed Price Repair Quotation.
- Create Repair Order or Create Fixed Price Repair Order to plan and perform the diagnosis or the repair.
- Outbound Delivery to send the repair object back to the customer (available if a returns order has been created and repair object is available in the repair center).
- Set Repair Object to Completed to finalize the in-house repair process for the repair object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Manage In-House Repairs (F4025) | The Manage In-House Repairs screen is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Go:In-House Repair: <repair ID> |  |  |
| 4 | Choose In-House Repair | Choose your In-House Repair from the list. | The Manage In-House Repair Details screen is displayed. |  |
| 5 | Select Repair Objects | Choose Repair Objects.Select the items to be processed. | The Decide button is available.Note The Decide button is active only when at least one repair object is selected. |  |
| 6 | Display Decision Options | Choose Decide. | The Decide dialog box is displayed. |  |
| 7 | Make Decision for Repair Objects | Choose one of the following:Create Repair QuotationCreate Fixed Price Repair QuotationCreate Repair OrderCreate Fixed Price Repair OrderOutbound DeliveryNote If multiple repair objects are selected, the Decide dialog box contains a list of actions that can be performed for the selected repair objects.The Outbound Delivery action is available if the repair object availability is set to Received by Repair Center status. | The Repair Quotation is created. |  |

### Perform Prechecks

Purpose

In this procedure, you check the repair objects that have been sent back by the customer and define the follow-up step for each repair object.

You use the Perform Prechecks (F4050) app to document a (technical) precheck of the repair objects. As a result of the precheck, you need to decide whether the repair object is marked for diagnosis or repair, whether a repair quotation is required, or whether the repair object is sent back to the customer.

Repairs and diagnoses are billed to the customers based on the labor and material that are required to provide a service. For fixed price repairs and diagnosis, you have agreed a fixed price with your customer. Both types of repair orders (time & material or fixed price) use repair confirmations to record the actual consumption of labor and materials.

|  |
| --- |
| Note If you have enabled service contract determination and the system has determined a valid service contract while creating a repair quotation or a repair order, it automatically copies the service contract data to the repair quotation or repair order, or you are prompted to select a service contract item from a list if more than one service contract item has been determined. |

#### Perform Precheck and Decide Follow-Up Steps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check the repair objects that have been sent back by the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Perform Prechecks (F4050). | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID>Note Adapt the filters accordingly if the In-House Repair ID is not visible in the field status. | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment.The following information is displayed for the repair object:Customer Warranty EndVendor Warranty EndEquipmentProductSerial NumberCustomer (Sold-To Party, Ship-To Party, Contact Person)Status: Precheck: Decision Pending | The Perform Precheck Details screen is displayed. In this mode, you cannot change any data.Note If you have enabled the service contract determination and your sold-to-party is associated with one or more service contracts, a list of all applicable contract items is displayed.If you have maintained the warranty end date for the equipment, an icon indicates whether the creation date of the in-house repair is within the warranty period of the related equipment.For more information, see the preliminary step [Maintain Customer, Customer Warranty and Vendor Warranty (Optional)](#unique_17) [page ] 20. |  |
| 5 | Check Returns Delivery | Note This step is not relevant if you completed Receive Repair Objects with Customer Returns (Optional).Under Transaction History, you find the Returns Order you have created.Choose the Returns Order > Display Customer Return .Under Returns Control, choose Returns Overview.Under Returns Steps, note down the Returns Delivery number.Proceed to Receive Repair Objects with Customer Returns (Optional) and complete the following steps :Execute PickingPost Goods ReceiptPerform Material Inspection | The Tranasction History is displayed.If you completed [Perform Precheck and Decide Follow-Up Steps](#unique_35) [page ] 52, the Returns Order will have the status Completed. |  |
| 6 | Make Decision | On the Perform Precheck Details screen, choose the Decide tab.Choose one of the following to continue:Create Repair QuotationCreate Repair OrderCreate Fixed Price Repair OrderSend the Repair Object Back to the Customer | The repair objects are set to status Precheck: Order or Precheck: Quotation depending on your decision.Note You can no longer reject a repair object once a follow-up decision has been made. |  |

|  |
| --- |
| Note If Send the Repair Object Back to the Customer is selected, proceed to chapter [Return to Customer (Optional)](#unique_52) [page ] 81. |

### Quotation Selected in Follow-Up Steps (Optional)

Prerequisite

You chose Quotation when you completed [Perform Precheck and Decide Follow-Up Steps](#unique_35) [page ] 52.

#### Create Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use repair quotations to provide offers with fixed conditions made to a customer for the performance of repairs.

A Customer Service Manager - In-House Repair uses repair quotations to provide cost estimates before placing a repair order. Both repair order types, resource-related and fixed price cost estimates, have a validity period assigned to it. The validity period of the repair quotation can be changed by the Customer Service Manager - In-House Repair with an option to carry out repricing as per the new validity.

When you choose Quotation, you get additional options to create a repair quotation for the repair object or to add the repair object to an existing repair quotation.

After finalizing the repair quotation that contains the required services and the quoted price, the Customer Service Manager - In-House Repair can print or generate the repair quotation as a PDF, then attach it to an email that is sent to the customer.

When the repair quotation has been accepted by the customer, the system creates a repair order or a fixed price repair order as a follow-up transaction.

Prerequisite

You chose Quotation when you completed [Quotation Selected in Follow-Up Steps (Optional)](#unique_62) [page ] 54.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair |  |  |
| 2 | Access App | Open Perform Prechecks (F4050). | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID>Status: Precheck: Quotation | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Precheck Details screen is displayed. |  |
| 5 | Create Repair Quotation | Under Decide, choose one of the following:Create Repair QuotationCreate Fixed Price Repair QuotationNote You can also add the repair object to an existing repair quotation that contains multiple repair objects. | A repair quotation for a repair object is created.The options to create a repair quotation under Decide are no longer visible. |  |
| 6 | Check Transaction History | Choose Transaction History. | The repair quotation appears in the transaction history for the repair object under Perform Repair.The repair quotation is in status Open. |  |
| 7 | Display Repair Quotation | Under Transaction History, choose the Repair Quotation. | The Repair Quotation screen is displayed. |  |
| 8 | Add Items | Choose Edit.Under Items, make the following entries:Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRIf a pop-up Partner Selection Item XX appears, select the appropriate partner for the item.Note In addition, you can choose between fixed price, time and materials, and service bundle use cases by selecting the respective product and item category combinations.Choose Save. | Items are added to the repair quotation. |  |
| 9 | Maintain Fixed Price (Optional) | Note This step is only relevant if you chose to create a Fixed Price Repair Quotation.On the Price Details tab, choose Add to insert a new Price Element.Make the following entries and choose Save:Price Element: Manual Doc. AmountPrice: for example, 600Currency: EUR | A fixed price has been defined for the fixed price repair quotation. |  |

#### Send Repair Quotation to Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Customer Service Manager - In-House Repair can send the repair quotation to the customer by using the Send To Customer option in the repair quotation or fixed price repair quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager - In-House Repair |  |  |
| 2 | Access App | Open Process Repair Quotations (F4580). | The Process Repair Quotations screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | Choose your repair quotation. | The Process Repair Quotation Details screen is displayed. |  |
| 5 | Display Quotation | Under Transaction History, choose the Repair Quotation | The Display Repair Quotation screen is displayed. |  |
| 6 | Send Quotation | Choose Send To Customer.NoteYou can only send a repair quotation to the customer if the repair quotation is in display mode.You can only send repair quotations to the customer that do not contain any errors.Enter the current or future requested service date as mentioned below:Under Repair Items > Dates section add the Validity Start and Validity End . | The repair quotation is sent to the customer. The Quotation Status changes to Sent to Customer. |  |
| 7 | Check Output Control | Under Output Control, ensure that a template is maintained in the Form Template column for the output items. | The Form Template is displayed the form template used for the repair quotation.Note If there are no output items, refer to configuration step Configure Output Management. |  |
| 8 | Display Print Preview | For Output Items, choose Show More per Row.For the output item which uses the ChannelPrintout (PRINT), choose Display Document in the Display column. | The repair quotation or fixed price repair quotation is displayed as PDF file. |  |
| 9 | Check Email Details | For the output item which uses the ChannelEmail (EMAIL), choose Output Details in the Details column. | The following output details are displayed:SenderToCcBccEmail TemplateNote To change the recipient and channel, refer to Configure Output Management. |  |
| 10 | Check Log (Optional) | In the Log column, choose Display Message Log. | The log displays any errors or other information. |  |

#### Accept or Reject Repair Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Customer Service Manager - In-House Repair accepts the repair quotation. The system then creates a repair order for the repair object if a repair order has not been created for diagnosis. If you have already created a repair order, then only the status of the repair object is changed.

Alternatively, the Customer Service Manager - In-House Repair can reject the repair quotations that do not match customer expectations or that have expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager - In-House Repair |  |  |
| 2 | Access App | Open Process Repair Quotations (F4580). | The Process Repair Quotations screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | Choose your repair quotation. | The Process Repair Quotation Details screen is displayed. |  |
| 5 | Display Quotation | Under Transaction History, choose the Repair Quotation | The Display Repair Quotation screen is displayed. |  |
| 6 | Accept Quotation | Choose Accept.Note Alternatively, you can choose Reject.Note If there is no repair order and the repair quotation is in status Accepted, the system automatically creates a new repair order in status Open.The items of the repair quotation can be partially accepted and the total repair quotation amount is adjusted according to the total items accepted. | The status of the repair quotation is set to Accepted.Note If you choose Reject, the status of the repair quotation is set to Rejected and the repair objects status changes to "Rejected at Quotation" at the In-house repair level. The repair quotation can no longer be changed.If you are using accelerated customer returns, the system creates an outbound delivery.For quotations that contain a repair object, a repair order (resource-related or fixed price) is created as a follow-up transaction for the repair object.For quotations that contain multiple repair objects, you must decide which follow-up transaction (repair order or fixed price repair order) is created for each repair object. |  |

|  |
| --- |
| Note If you choose Accept, proceed to chapter [Create Repair Order or Create Fixed Price Repair Order](#unique_39) [page ] 59. If you selected Reject, proceed to chapter [Return to Customer (Optional)](#unique_52) [page ] 81. |

### Create Repair Order or Create Fixed Price Repair Order selected in Follow-Up Steps

#### Create Repair Order or Create Fixed Price Repair Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you decide to start the repair or perform a diagnosis to estimate the repair effort, you can choose Create Repair Order or Create Fixed Price Repair Order.

If you choose Create Repair Order, the system creates a repair order for the repair object to document the actual, resource-related consumption. So, you can bill the repair confirmation items to your customer based on the consumption of time and material.

|  |
| --- |
| Note You do not need to create a repair order manually if you completed the step Create Quotation (Optional). When the repair quotation is accetpted, a repair order with the status Open is created automatically. |

If you choose Create Fixed Price Repair Order, the system creates a repair order with a fixed price that has been agreed with the customer. You can bill the repair order items to your customer based on the agreed fixed price when the repair order has been set to Completed.

Optionally, you can use service bundles to offer customers service products, service parts, and expense items as a package.

The following service bundle scenarios are supported:

- Repair order with time and material service bundle that can contain time and material or fixed price subitems.
- Repair order with fixed price bundle and fixed price partial billing bundle. These bundles can contain fixed price subitems.
- Fixed price repair order with fixed price bundle that can contain fixed price subitems.

Prerequisite

You chose either Create Repair Order or Create Fixed Price Repair Order when you completed Perform Precheck and Decide Follow-Up Steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Perform Prechecks (F4050). | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID>Status: Precheck: Order | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Precheck Details screen is displayed. |  |
| 5 | Create Repair Order | Under Decide, choose one of the following:Create Repair OrderCreate Fixed Price Repair Order | The repair order or the fixed price repair order is created as a follow-up transaction for the repair object. |  |
| 6 | Check Transaction History | Choose Transaction History. | The repair order appears in the transaction history for the repair object under Perform Repair.The repair order is in status Open. |  |
| 7 | Display Repair Order | Under Transaction History, choose the Repair Order > Display Repair Order. | The Repair Orders screen is displayed. |  |
| 8 | Add Items | Choose Edit.Under Items, make the following entries:Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRItem Category: for example, SVP1 Service Item or SVP2 SrvItm (FxPrc)Note You can also add a service bundle as a main item:Product ID: SRV_BUNDLE_02 (Service Bundle)or SRV_BUNDLE_01 (Fixed Price Service Bundle)In this case, you need to maintain subitems under the service bundle item.Note Select No Assignment in Contract Assignment dialog box if no relevant contract exists.Choose Save. | Items are added to the repair quotation. |  |
| 9 | Add Items (Optional) | If a BOM is created for the equipment, you can add items from the product proposal.Under Items, choose Product Proposal.Note The Product Proposal button is only displayed if the repair order is in edit mode.In the Product Proposal dialog box, select the items to be added.Use Choose to add the selected items. | The product or equipment BOM items that are relevant to manage the repair have been added.Note The product proposal contains the relevant service parts and the bill of materials (BOM) items that have been defined for the equipment. |  |
| 10 | Maintain Fixed Price (Optional) | If you have created a Fixed Price Repair Order, define the the fixed price for this order.On the Price Details tab, choose Add to insert a new Price Element.Make the following entries:Price Element: Manual Doc. AmountPrice: for example, 600Currency: EURIf you created an item with category SVP2 SrvItm (FxPrc), navigate to the details of the item and choose Price Details.Choose Add.Make the following entries:Price Element: Manual Itm AmountPrice: <price>Unit: EUR | A fixed price has been entered for the fixed price repair order.Note The total price for the repair is based on the fixed price entered. Prices that have been defined for the product that have been added under items are automatically adapted to reflect the total price proportionally.This total price of the repair order is relevant for billing. Therefore, repair confirmations are not considered in the billing process. |  |
| 11 | Save | Choose Save. | The repair order is saved. |  |

#### Trigger Diagnosis Planning, Plan Diagnosis, Trigger Diagnosis and Perform Diagnosis in Repair Order (Optional)

##### Trigger Diagnosis Planning in Repair Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you trigger the diagnosis planning in the repair order.

|  |
| --- |
| Note Note The following actions are only available if the process is started without a prior quotation:Plan DiagnosisTrigger DiagnosisPerform DiagnosisTrigger Follow-Up Actions for Diagnosis |

The status of the repair object changes to Plan: Diagnosis and the repair object appears in the Plan Repairs(F4152) app. You can continue to plan the diagnosis of the repair object in the planning step of the in-house repair process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Perform Prechecks(F4050). | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <in-house repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Precheck Details screen is displayed. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order Order > Display Repair Order. | The Repair Orders screen is displayed |  |
| 6 | Choose Action | Choose Edit.Choose Actions.Choose Trigger Diagnosis Planning. | The repair order is set to status In Process. |  |
| 7 | Save | Choose Save. | The repairs order is saved. |  |
| 8 | Navigate Back | Navigate back to the Perform Precheck Details screen. | The Perform Precheck Details screen is displayed. |  |
| 9 | Check Status | Check the status of the Repair Object. | The Status of the repair object (equipment) has changed to Diagnosis: Plan. |  |

##### Plan Diagnosis

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen displays. |  |
| 3 | Make Selection | Make the following entries and choose Go:Repair Order: <repair order> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Plan Repair Details screen displays. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order> Display Repair Order. | The Repair Orders screen displays |  |
| 6 | Edit Repair Order | Choose Edit. |  |  |
| 7 | Check Repair Order | Check the relevant repair order diagnosis planning data. | All planning relevant details are entered. |  |
| 8 | Change Repair Order | Enter the repair order items that are required for diagnosis. | All diagnosis relevant items are entered. |  |
| 9 | Save | Choose Save. | The repairs order is saved. |  |

##### Trigger Diagnosis in Repair Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the repair order or the fixed price repair order is released for diagnosis.

The status of the repair object changes to Perform: Diagnosis and the repair object appears in the Perform Repairs (F4241) app.

You can continue to perform the diagnosis of the repair object and then create repair confirmations of the diagnosis in the repair order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Perform Prechecks (F4050). | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID>p | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Precheck Details screen is displayed. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order > Display Repair Order. | The Repair Orders screen is displayed |  |
| 6 | Choose Action | Choose Edit.Choose Actions.Choose Trigger Diagnosis. | The repair order is set to status Released. |  |
| 7 | Save | Choose Save. | The repairs order is saved. |  |
| 8 | Navigate Back | Navigate back to the Perform Precheck Details screen. | The Perform Precheck Details screen is displayed. |  |
| 9 | Check Status | Check the status of the Repair Object. | The Status of the repair object (equipment) has changed to Diagnosis: Perform. |  |

##### Perform Diagnosis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create repair confirmations for the diagnosis, provide actual consumption data and confirm the finalized diagnosis. You use the Perform Repairs (F4241) app to document the diagnosis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Service Technician - In-House Repair. |  |  |
| 2 | Access App | Open Perform Repairs(F4241). | The Perform Repairs screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:Repair Order: <repair order> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Repair Details screen is displayed. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order. | The Repair Orders screen is displayed |  |
| 6 | Create Confirmation | Choose Create Follow-Up. In the Follow-Up - Select Items, select your items and choose Choose. | The Repair Confirmation: New screen is displayed. |  |
| 7 | Maintain Confirmation | Under Parties Involved, make the following entries and choose Save:Exec. Service Employee: for example Service Technician - In-House RepairCaution If you want to continue with the repair steps, do not select the Final Repair Confirmation checkbox in the Repair Confirmation Details. | A repair confirmation has been created. |  |

##### Trigger Follow-Up Actions for Diagnosis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As soon as you have performed the diagnosis, you change the status of the repair object to Diagnosis: Follow-Up and the repair object appears in the app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Perform Prechecks (F4050) app. | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID>Note If the repair ID is not displayed, adjust the filter for the Status field. | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Precheck Details screen is displayed. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order. | The Repair Orders screen is displayed |  |
| 6 | Choose Action | Choose Edit.Choose Actions.Choose Trigger Follow-Up Actions for Diagnosis . |  |  |
| 7 | Save | Choose Save. | The repairs order is saved. |  |
| 8 | Navigate Back | Navigate back to the Perform Precheck Details screen. | The Perform Precheck Details screen is displayed. |  |
| 9 | Check Status | Check the status of the Repair Object. | The Status of the repair object (equipment) has changed to Diagnosis: Follow-Up. |  |

##### Create Diagnosis Follow-Up

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a follow-up based on the diagnosis result to prepare the repair order to plan the repair.

You could also submit a repair quotation to the customer based on your diagnosis results.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Perform Prechecks (F4050) app. | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Precheck Details screen is displayed. |  |
| 5 | Decide Follow-Up | Choose Actions, choose Trigger Repair Planning. | The repair object status changes to Repair: Plan and it appears in the Plan Repairs(F4152) app. |  |

### Trigger Repair Planning in Repair Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process you trigger the repair planning, the status of the repair object changes to Repair: Plan and the repair object appears in the Plan Repairs app. You can continue to plan the repair of the object in the planning step of the in-house repair process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Perform Prechecks (F4050). | The Perform Prechecks screen is displayed. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Precheck Details screen is displayed. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order. | The Repair Orders screen is displayed |  |
| 6 | Choose Action | Choose Edit.Choose Actions.Choose Trigger Repair Planning. |  |  |
| 7 | Save | Choose Save. | The repairs order is saved. |  |
| 8 | Navigate Back | Navigate back to the Perform Precheck Details screen. | The Perform Precheck Details screen is displayed. |  |
| 9 | Check Status | Check the status of the Repair Object. | The Status of the repair object (equipment) has changed to Repair: Plan. |  |

#### Plan Repairs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you plan the repairs based on the available resources and according to agreements with customers to ensure efficient and cost optimized operation.

You plan the repair of the repair objects, for example, assign start and end dates and a technician who carries out the repair.

In this procedure, you can also select multiple repair objects and trigger the Create Returns Order action to manage the return of the repair objects by the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager - In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen displays. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Plan Repair Details screen displays. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order. | The Repair Orders screen displays. |  |
| 6 | Add Product Proposal Items (Optional) | Choose Edit.Under Items, choose Product Proposal.Note The Product Proposal button is only displayed if the repair order is in edit mode.In the Product Proposal dialog box, select the items to be added.Use Choose to add the selected items. | The product or equipment BOM items that are relevant to manage the repair have been added.Note The product proposal contains the relevant service parts and the bill of materials (BOM) items that have been defined for the equipment. |  |
| 7 | Add Items (Optional) | Check the relevant repair order items.Maintain the following items in the repair order (in addition or if required):Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRIn addition, you can choose between fixed price, time and material and service bundle use cases by selecting the respective product and item category combination. | If a service part item is used and the delivery address differs from the standard plant, you can maintain an additional partner function Service Part Recipient in the item details. Once the item and the order have been set to Released, the reservation is created as per the quantity.Note By default, if a user other than the creator of the repair order adds an item to the repair order, the current user is automatically added as the employee responsible to the repair order item. |  |
| 8 | Check Profit Center (Optional) | Under Items, check the profit center for each item. | The profit center is determined automatically.Note The system determines a profit center for each repair order item of a repair order. The system first determines the cost center of the employee responsible for the item and then the profit center that is defined for this cost center. You can also manually change the profit center assigned to a repair order item. |  |
| 9 | Check Planning Data | On the Repair Orders screen, check the following:Equipment IDRequested StartRequested EndNoteItemsUnder Repair Order Details, make the following entries:Requested Start: <date>Requested End: <date> | All planning relevant details are entered. |  |
| 10 | Check Service Team (Optional) | Under Organizational Data, check the service team.Note This is only relevant if you use service teams. | The service team is determined based on the country/region and postal code of the sold-to party.Note You can also manually change the service team assigned to a repair order. If the executing service employee belongs to more than one service teams or doesn't belong to any service team, the system displays an error message. |  |
| 11 | Add Service Employee | Under Parties Involved, make the following entries:Partner Function: Exec. Service EmployeePartner ID: <employee> | An employee is added who will perform the repair. |  |
| 12 | Check Repair Order | If the system displays a message, correct the entries in the repair order.If no message occurs, the repair order has been finalized. | The data of the repair order have been updated. The planning has been finalized. |  |
| 13 | Save | Choose Save. | The repair order is saved. |  |

##### Trigger Repair

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The status of the repair object changes to Repair: Perform and the repair object appears in the Perform Repairs (F4241) app. You can continue to perform the repair of the object and create repair confirmations for the repair order.

Repair confirmations that have been created as a follow-up to repair orders are used for controlling and billing the actual consumed labor and materials in the repair process.

Repair confirmations that have been created as a follow-up to fixed-price repair orders are not used for billing (they are used for controlling only to capture actual costs). In this case, the fixed-price repair order is used as the basis for billing and billing does not rely on confirmed items and quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager – In-House Repair. |  |  |
| 2 | Access App | Open Plan Repairs (F4152). | The Plan Repairs screen displays. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Plan Repairs Details screen displays. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repair Order. | The Repair Orders screen displays. |  |
| 6 | Choose Action | Choose Edit.Choose Actions.Choose Trigger Repair. |  |  |
| 7 | Save | Choose Save. | The status of the repair order changes to Released.The status of the repair object changes to Repair: Perform and the object appears in the worklist of the service technician. This status allows you to perform the repair.Caution You can only release repair orders that do not contain errors. If there are errors, you must correct the data in the repair order before releasing it.Note Releasing a repair order also releases all items. Depending on the product used, an automatic purchase requisition can be triggered. If this applies to your use case, complete the following activities from the Procurement for Service Management (3NI) test script:Convert Purchase Requisitions to Purchase Order for Consumption MaterialsorPost Goods Receipt of Material Items for Consumption MaterialsIf you have enabled credit management for repair orders, the system performs a credit check and updates the credit status.If you activated the simulative ATP check for SRV_05, you will see the availability and quantity of the required stock item when creating the repair order.If you configured the reservation status for SRV_05, you will see the reservation quantity while creating and releasing the repair order. |  |

#### Perform Repairs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create repair confirmations, provide actual consumption data and confirm finalized repairs.

The shipment can be triggered in order to ensure that customers receive repaired objects according to agreements.

You maintain the actual working hours and spare parts.

##### Create Repair Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a follow-up repair confirmation for a repair order or fixed price repair order is created. It includes setting the confirmation to Completed or setting the final confirmation flag.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Service Technician - In-House Repair. |  |  |
| 2 | Access App | Open Perform Repairs (F4241) app. | The Perform Repairs screen displays. |  |
| 3 | Make Selection | Make the following entries and choose Go:Repair Order: <repair order> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Repairs Details screen displays. |  |
| 5 | Check Details of Repair Object | On the Perform Repair Details view, check the following details of the repair object:EquipmentSerial NumberProductSold-To PartyShip-To Party | The repair object details are correct. |  |
| 6 | Display Repair Order | Under Transaction History, choose the Repair Order.The following information displays:EquipmentSold-To PartyStatusRequested StartRequested EndExec. Service EmployeeNoteItems | The Repair Orders screen displays. |  |
| 7 | Create Repair Confirmation | If the repair of the equipment is (partly) complete, you can create the repair confirmation to enter the working time, all expenses and used service parts.Choose Create Follow-Up.In the Follow-Up - Select Items, select your items and choose Choose. | The repair is (partly) performed. |  |
| 8 | Create Repair Confirmation | Check and adapt the entries copied from the repair order.Under Parties Involved, make the following entries:Exec. Service Employee: <employee>Choose Save. | The repair confirmation can be modified until it is set to status Completed.A repair confirmation is created.NoteBy default, the confirmed items are set for complete billing (SCP1, SCE1, SCS1). You can bill an item only if all items of the repair order have been confirmed and the status in the repair order items has been set to Completed.You can also change the item category to partial billing (SCP3, SCE3, or SCS3). Partial billing allows you to bill an item if it has been confirmed and completed in the repair order, even if other items have not yet been finalized.For fixed price repair orders, billing does not rely on the confirmed items and quantities.In the Exec. Service Employee, add Service Technician - In-House Repair user. |  |
| 9 | Edit Items | Under Items on the Repair Confirmations screen, choose Edit for Product ID SRV_02.Make the following entries:Amount: <amount>Choose Save. |  |  |
| 10 | Define Overtime Category (Optional) | Under Items, choose Edit for Product ID SRV_01.Under General Data, make the following entries:Overtime Category: Overtime WeekendChoose Back. | Under Price Details, the price element Overtime displays a price.By maintaining the Overtime Category, the price for the service item increases. |  |
| 11 | Complete Repair | Select the Final Repair Confirmation checkbox (if applicable).Choose Save. | The repair confirmation displays.Note If you want to create further repair confirmations, do not set the final confirmation to Completed and do not select the Final Repair Confirmation checkbox. |  |
| 12 | Set Status | Choose Edit.Under Processing Data, make the following entries:Life Cycle Status: CompletedChoose Save. | The status of the repair confirmation is set to Completed.As soon as all repair confirmations have been set to Completed and one is marked as the final confirmation, the repair order or fixed price repair order status is set to Completed and the status of the related repair object is set to Bill.This is the prerequisite for the repair objects to be released for billing.If there are no related repair order or repair confirmation items that must be billed, the repair object is directly set to Completed automatically.Note This repair confirmation cannot be changed anymore.Caution You can only set repair confirmations to Completed that do not contain errors. You must first correct the data in the repair confirmation. |  |

##### Cancel Repair Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Service Technician - In-House Repair views the available repair confirmations and the repair confirmation details.

In this step, you cancel the repair confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Service Technician - In-House Repair. |  |  |
| 2 | Access App | Open Perform Repairs (F4241) app. | The Perform Repairs screen displays. |  |
| 3 | Make Selection | Make the following entries and choose Go:Repair Order: <repair order> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Perform Repairs Details screen displays. |  |
| 5 | Display Repair Confirmation | Under Transaction History, choose the Repair Confirmation. | The Display Repair Confirmation screen displays. |  |
| 6 | Cancel Repair Confirmation | Choose Cancel Confirmation. | The status of the repair confirmation is set to Completed and the field Canceled Internally is set. |  |

### Prepare and Release for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You finalize the in-house repair process for the repair object.

You can create an outbound delivery. This option is only available if a returns order has been created and the availability status of the repair object is Received by Customer Repair Center.

The Customer Service Representative - In-House Repair reviews the available repair confirmation items (complete billing or partial billing) or the repair order items (fixed price) to be released for billing. In this procedure, you check the assignment of the internal cost and billing relevant repair costs including working time, product, and equipment time. You close the in-house repair from commercial perspective and release the items for billing. Then billing document requests can be created.

For chargeable items such as services and spare parts, you ensure cost covering in accordance with customer agreements.

|  |
| --- |
| Note For time and material items in the repair confirmation, the time-sheet entry, spares cost, and expenses are posted to finance and controlling. For fixed price items, the corresponding item in the repair confirmation is used for controlling purposes only, for capturing actual costs, and the fixed-price items in the repair order are posted to finance.Once the repair is done, the recorded effort in the repair confirmation (for time and material items), and in the repair order (for fixed price items) is released for billing, and a billing document request is created to invoice the customer. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Prepare for Billing (F4263). | The Prepare for Billing screen displays.Note This app only displays repair objects with the status Bill or Repair. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Create Outbound Delivery (Optional) | Select the checkbox for the repair objects to be processed.Choose Decide.In the Decide dialog box, choose Create Outbound Delivery.Note If you have created a returns order for the repair object, you must first create an outbound delivery. An outbound delivery can only be triggered when the availability status of the repair object is set to Received In Repair Center. | The outbound delivery (return to customer) is created and the availability of the repair object is changed to Sent Back by Repair Center. |  |
| 5 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Prepare for Billing Details screen displays. |  |
| 6 | Check Billing Items | Check the items listed under To Be Released for Billing. | Items to be released for billing are listed.Note A fixed price repair order item or a repair confirmation item is only displayed in this list if the repair order status has been set to Completed.A repair confirmation item that has been defined for partial billing is only displayed, if it has been completed and the repair order lifecycle status is Released or Completed.The To Be Returned tab contains repair objects for which an outbound delivery has not yet been created (only relevant if you are using customer returns). |  |
| 7 | Release Items | Select an item or all items choose Release for Billing. | The selected items are released for billing.The items disappear from the list. |  |
| 8 | Check Transaction History | Choose Transaction History. | The Billing Document Request is displayed and has the status To be Invoiced.An Outbound Delivery is displayed and has the status Not Yet Started. |  |

### Return to Customer (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You pick and post goods issue for the outbound delivery to send the repair object back to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Enter Data | Choose For Picking.Make the following entries and choose Execute:Shipping Point/Receiving Pt: 331R | The Outbound Deliveries for Picking screen displays. |  |
| 4 | Change Outbound Delivery | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 5 | Enter Picked Quantity | On the Picking tab, enter the quantity equal to the delivery quantity in the Picked Qty field. |  |  |
| 6 | Save | Choose Save. | The delivery is picked. |  |
| 7 | Enter Data | Navigate to the Manage Outbound Deliveries screen.Choose For Goods Issue.Make the following entries and choose Execute:Shipping Point/Receiving Pt: 331R | The Outbound Deliveries for Goods Issue screen displays. |  |
| 8 | Post Goods Receipt | On the Goods Issue for Outbound Delivery to be Posted screen, select your delivery and choose Post Goods Issue.Make the following entries and choose Continue:Act. Gds Mvmnt Date: for example, <today's date> | The goods receipt is posted. |  |

### Complete Repair Object and Finalize In-House Repair (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you finalize the in-house repair process.

|  |
| --- |
| Note If the repair object is the last repair object to be processed within an in-house repair, the in-house repair is set to Completed as well. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Prepare for Billing (F4263). | The Prepare for Billing screen displays. |  |
| 3 | Make Selection | Make the following entries and choose Go:In-House Repair: <repair ID> | The repair objects are displayed in the result list. |  |
| 4 | Display Details for Repair Object | To display the details of a repair object, choose the table row containing the repair object or the equipment. | The Prepare for Billing Details screen displays. |  |
| 5 | Complete Repair Object | When all related items that are relevant for billing have been released, choose Complete. | The status of the repair object is set to Completed. |  |

### Create Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the billing document requests.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define the Billing Settings | Choose Billing Settings.In the Billing Settings dialog Box, make the following entries:Set billing date and type before billing: ON.Create separate billing document for each item of billing due list: OFF.Automatically post billing documents: ON.Display billing documents after creation: ONChoose OK. | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following search criteria:SD Document Category: Billing Document RequestIn order to better find your items to be billed, choose the Settings icon.In View Settings select the BDR Source Document field for display.Choose OK and search for your items in the list by identifying your service confirmation in the BDR Source Document field.Find your items in the list by identifying your service confirmation in the field BDR Source Document.Select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-To Party or Billing Date. | The Create Billing Documents dialog box is displayed. |  |
| 5 | Select Billing Type and Date | In the Create Billing Documents dialog box, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date>Choose OK. | The Invoice view is displayed. |  |
| 6 | Save | Choose Save. | The billing document is created.Note down the billing document number for future reference. |  |

### Create Repair Template (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Repair templates are used to define reusable sets of service and repair related data that minimize the amount of time required to create a repair order. Repair template items can then be copied as set to repair orders.

You can create a repair template or fixed price repair template with all required service items, expense items, or service parts.

Once the repair template is released, you can copy the line items from the applicable repair template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |  |
| 3 | Create Template | Choose Create: | The Create Service Order Template screen displays . |  |
| 4 | Enter Data | Make the following entries:Template Type: Repair TemplateDescription: <your description>Employee Responsible: <employee>Life Cycle Status: OpenProduct: for example, SRV_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new repair template or fixed price repair template is created and saved.The repair template is opened in edit mode. |  |
| 5 | Enter Reference Objects (Optional) | Under Reference Objects, enter a Product ID, a Functional Location ID, or an Equipment ID.Note You can only enter one of these values. |  |  |
| 6 | Enter Organizational Data (Optional) | Under Organizational Data, make the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 7 | Save and Release Template | Choose Save.Choose Release. | The repair template is saved and released.. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can precede this process.

| Process | Business Condition |
| --- | --- |
| 3MO - Service Contract Management | Optional |
| BD9 - Sell from Stock | Optional |
| BKP - Customer Returns | Optional |
| BDD - Lean Customer Returns | Optional |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3NI - Procurement for Service Management |  |
| J58 - Accounting and Financial Close |  |
| J59 - Accounts Receivable |  |
| 4GG - Credit and Debit Memo Processing for Service Management | Optional |
| 53Y - Intercompany Billing for Service Documents | Optional |
| BKP - Customer Returns | Optional |
| 49X - Service Order Processing with SAP Field Service Management | Optional |

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
> Flagged while digesting this document, not verified: Outbound delivery availability prerequisite is worded inconsistently: 'Received by Repair Center', 'Received by Customer Repair Center' and 'Received In Repair Center' appear in different sections.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample org data conflicts within the script: configuration/master data use plant/shipping point 3310/331R while customer returns steps use 1010/101R and customer 10100001.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3XK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 148,670 chars in the whole document
