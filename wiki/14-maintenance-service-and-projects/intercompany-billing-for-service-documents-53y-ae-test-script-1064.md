---
id: 14-maintenance-service-and-projects/intercompany-billing-for-service-documents-53y-ae-test-script-1064
title: Intercompany Billing for Service Documents (53Y_AE) - Test Script (53Y_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 53Y_AE: intercompany billing of service and repair orders, from order to intercompany invoice."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-order-management-and-billing]
aliases: [53Y_S4CLD2608_BPD_EN_AE]
keywords: [Service Order Management and Billing, intercompany billing, service orders, in-house repair, service confirmation, repair confirmation, intercompany billing request, intercompany invoice, intercompany cost rates, intercompany sales order]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53Y_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1064
topic: 14-maintenance-service-and-projects/service-order-management-and-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intercompany Billing for Service Documents (53Y_AE) - Test Script (53Y_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53Y_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Order Management and Billing** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Intercompany Billing for Service Documents (53Y_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Intercompany Billing for Service Documents (53Y_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855682)

[2 Prerequisites 4](#_Toc232855683)

[2.1 System Access 4](#_Toc232855684)

[2.2 Roles 4](#_Toc232855685)

[2.3 Master Data, Organizational Data, and other Data 6](#_Toc232855686)

[2.3.1 Business Partner 6](#_Toc232855687)

[2.3.2 Master Data 6](#_Toc232855688)

[2.4 Business Conditions 6](#_Toc232855689)

[2.5 Preliminary Steps 7](#_Toc232855690)

[2.5.1 Check Intercompany Sales Order 7](#_Toc232855691)

[2.5.2 Maintain Intercompany Cost Rates 8](#_Toc232855692)

[2.5.3 Maintain Cost Element Group for Intercompany 10](#_Toc232855693)

[2.5.4 Block Intercompany Postings (Optional) 12](#_Toc232855694)

[3 Overview Table 14](#_Toc232855695)

[4 Test Procedures 15](#_Toc232855696)

[4.1 Create Order 15](#_Toc232855697)

[4.1.1 Create Service Order 15](#_Toc232855698)

[4.1.2 Create In-House Repair and Repair Order 16](#_Toc232855699)

[4.2 Create Confirmation 18](#_Toc232855700)

[4.2.1 Create Service Confirmation 19](#_Toc232855701)

[4.2.2 Create Repair Confirmation 20](#_Toc232855702)

[4.3 Generate Intercompany Billing Request 21](#_Toc232855703)

[4.4 Create Intercompany Invoice 23](#_Toc232855704)

## Purpose

Overview

A company has an affiliate company. The affiliate company delivers a service to the ordering company while delivering a service to a customer. The affiliate company posts expenses and records time on the service order or repair order. These expenses are transformed into debit memo requests. An intercompany invoice with reference to the debit memo request is created by the delivering company.

|  |
| --- |
| Note The intercompany process described in this test script uses sample data with the following considerations:The ordering company is a German company.The delivering company is a U.S. company.The scenario is unidirectional: A U.S. company delivers services to a German company. |

If you want to use the intercompany process for another country/region, adapt the master data sample values. You can also refer to scope item Intercompany Billing for Cross-Company Cost Accounting Postings (4AN).

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
| Internal Sales Representative - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Internal Sales Representative - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Your system administrator provides the user and password information. |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Your system administrator provides the user and password information. |
| Service Technician - Customer Service | SAP_BR_CUSTOMER_SRVC_TEC | Service Technician - Customer Service | SAP_BR_CUSTOMER_SRVC_TEC | Your system administrator provides the user and password information. |
| Billing Clerk | SAP_BR_BILLING_CLERK _BR | Billing Clerk | SAP_BR_BILLING_CLERK _BR | Your system administrator provides the user and password information. |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Your system administrator provides the user and password information. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Your system administrator provides the user and password information. |
| Customer Service Representative - In-House Repair | SAP_BR_CUST_SRVC_REP_REPA | Customer Service Representative - In-House Repair | SAP_BR_CUST_SRVC_REP_REPA | Your system administrator provides the user and password information. |
| Service Technician - In-House Repair | SAP_BR_CUST_SRVC_TEC_REPA | Service Technician - In-House Repair | SAP_BR_CUST_SRVC_TEC_REPA | Your system administrator provides the user and password information. |

We recommend that you assign the business roles listed above to the test user. Alternatively, your administrator can create a custom role that contains the following apps and business catalogs to assign to the test user.

|  |
| --- |
| Note The Configuration Expert - Business Process Configuration role should only be used by an administrator. |

| App/Transaction | ID (Role Template) | Business Catalog ID |
| --- | --- | --- |
| List Sales Orders - Intercompany (VA05_AUART) | SAP_BR_INTERNAL_SALES_REP_PRSV | SAP_SD_BC_SO_PROC_INTCO |
| Create Sales Orders - Intercompany (VA01) | SAP_BR_INTERNAL_SALES_REP_PRSV | SAP_SD_BC_SO_PROC_INTCO |
| Manage Cost Rates - Services (F3161) | SAP_BR_OVERHEAD_ACCOUNTANT | SAP_FIN_BC_OH_MD_CCA_PC |
| Manage Cost Element Groups (F5373) | SAP_BR_OVERHEAD_ACCOUNTANT | SAP_FIN_BC_OH_MD_CCA_PC |
| Manage Service Orders - To-Do List (F3571A) | SAP_BR_CUSTOMER_SRVC_MGR | SAP_S4CRM_BC_SERV_MGR_PC |
| Manage In-House Repairs (F4025) | SAP_BR_CUST_SRVC_REP_REPA | SAP_S4CRM_BC_REPA_REP_PC |
| Perform Prechecks (F4050) | SAP_BR_CUST_SRVC_REP_REPA | SAP_S4CRM_BC_REPA_REP_PC |
| Process Service Orders - To-Do List (F4230) | SAP_BR_CUSTOMER_SRVC_TEC | SAP_S4CRM_BC_CUST_SRVC_TEC_PC |
| Perform Repairs (F4241) | SAP_BR_CUST_SRVC_TEC_REPA | SAP_S4CRM_BC_REPA_TEC_PC |
| Generate Intercompany Billing Request (F1829) | SAP_BR_INTERNAL_SALES_REP_PRSV | SAP_PS_BC_INTERCOMPBILLING_PC |
| Create Billing Documents (F0798) Create Billing Documents - VF01 (VF01) | SAP_BR_BILLING_CLERK | SAP_SD_BC_BIL_DOC_PC |

### Master Data, Organizational Data, and other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents products, equipment, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

1. External Tax Calculation Partner Solution makes use of tax attributes from Business Place, Business Partner, Material and Service master data, as well as other attributes automatically determined by the system when the appropriate configuration is done.

Information related to External Tax Calculation attributes is available in the master data script Nota Fiscal Brazil (JD0) and in the scope item Invoice, Taxes and Complementary Postings (1J5).

1. Please inform a valid EAN Code in material master data via app Change Material (MM02) using the role SAP_BR_PRODMASTER_SPECIALIST.

This field is found in the Basic Data 1 view in Dimension/EANs session. It is mandatory to have an EAN to authorize a NF-e in tax authority.

#### Business Partner

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sold-To Party | 33403310 | For this scenario, the company which orders the executing service employee is a German company. It is represented by the German sold-to party 33403310. | This is sample data. You can adapt the value for your country/region if needed. |

#### Master Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | P002 | Project Based Service: Time & Expenses | This material is used to describe different services being provided to the customer. |

### Business Conditions

Before this scenario can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 4AN - Intercompany Billing for Cross-Company Cost Accounting Postings | You must first complete Intercompany Processes – Project-Based Services (16T).To complete the intercompany billing process for service orders, the scope tiem Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) must be activated and you must complete the set-up instructions. |
| 3D2 - Service Order Management and Monitoring | Note The content for both company codes should be activated in order for the intercompany billing to work, as pricing procedures are required for both companies. |

### Preliminary Steps

#### Check Intercompany Sales Order

Purpose

The intercompany billing scenario can be understood as a trading of affiliated companies within a corporate group. The prerequisite for that trading is an intercompany sales order.

In this step, you check whether a proper intercompany sales order is already in place or you can create one.

|  |
| --- |
| Example A U.S. company sells services to a German company. |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. |  |  |
| 2 | Access App | Open List Sales Orders - Intercompany (VA05_AUART). | The List of Sales Orders screen displays. |  |
| 3 | Check for Intercompany Sales Order | Make the following entries and choose Execute:Sold-To Party: for example, 33403310Sales Organization: for example, 3310Material: for example, P002 | If a sales order exists, note down the sales order document number. |  |
| If the intercompany sales order does not exist, proceed with the following steps to create an order. |  |  |  |  |
| 4 | Access App | Open Create Sales Orders - Intercompany (VA01). | The Create Intercompany Order: Overview screen displays. |  |
| 5 | Create Intercompany Sales Order | Make the following entries and press Enter:Sold-to Party: for example, 33403310Ship-to Party: for example, 33403310In the Sales area for customer dialog box, choose 3310 and press Enter.Make the following entries and choose Save:Material: P002Amount: for example, 1000For Brazil-specific data, choose Menu > Goto > Item > Country .Tip You can also double click on the item and navigate to the Country Tab.The Complementary Business Transaction feature is activated in your system, then select the Additional Fiscal Data button and enter the country specific attributes and confirm:● Business Transaction: <S001> Service Rendering ISSQN● Customer Usage:● Usage Purpose:The Complementary Business Transaction Attributes must be filled in accordance with the Internal Tax Department guidance for this sales scenario. | An intercompany sales order is created (order type SO03).Note down the sales order document number. |  |

#### Maintain Intercompany Cost Rates

Purpose

In this step, you check whether actual intercompany cost rates are maintained. If they are not, you define your own actual intercompany cost rates.

|  |
| --- |
| Example A U.S. company sells services to a German company. |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access App | Open Manage Cost Rates - Services (F3161). | The Manage Cost Rates - Services screen displays. |  |
| 3 | Check Cost Rates | Make the following entries and choose Go:Company Code: for example, 3310Valid On: for example, <current date>Receiving Company: for example, 1010Cost Center: for example,33101902Note This is the cost center to which the service executing employee belongs and against which the activity cost allocation will be done. | The actual cost rates for the specified cost center, receiving company, and period are display.There should be at least one entry with the following values:Receiving Company: 1010ICO Rate: YesActivity Type: SVO1 (Service Time)Rate: for example, 100 AEDPer: 1Activity Unit: H |  |
| 4 | Maintain Additional Cost Rates | If the actual intercompany cost rates are not defined, or you want to add additional actual intercompany cost rates, choose Add.In the Create Cost Rates dialog box, make the following entries:Receiving Company: for example, 1010ICO Rate: SelectedCost Center: for example,3310 1902Activity Type: SVO1From FY: <current fiscal year>From Period: <current period>Rate: for example, 100Currency: for example, AEDPer: for example, 1Activity Unit: HChoose Save. | The additional cost rates are created. |  |
| 5 | Check Internal Cost Rates | Make the following entries and choose Go:Company Code: for example, 3310Valid On: <current date>Receiving Company: <empty>Cost Center: for example,33101902Note This is the cost center to which the service executing employee belongs and against which the activity cost allocation will be done. | The actual cost rates for the specified cost center and period display.There should be at least one entry. with the following values:Receiving Company: <empty>ICO Rate: NoActivity Type: SVO1 (Service Time)Rate: for example, 75 USDPer: 1Activity Unit: H |  |
| 6 | Maintain Additional Internal Cost Rates | If the actual internal cost rate is not defined, or you want to add additional actual intercompany cost rates, choose Add.In the Create Cost Rates dialog box, choose Show Details.Make the following entries:Receiving Company: <empty>ICO Rate: DeselectedCost Center: for example, 17101902Activity Type: SVO1From FY: <current fiscal year>From Period: <current period>Rate: for example, 75Currency: for example, AEDPer: 1Activity Unit: HChoose Save. | The additional cost rates are created. |  |

#### Maintain Cost Element Group for Intercompany

Purpose

In order for the correct cost elements to be considered in the intercompany billing, cost elements are added to cost element groups.

If you changed any accounts that are used for the service or expense product, these accounts should be added to the groups accordingly.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access App | Open Manage Cost Element Groups (F5373). | The Manage Cost Element Groups screen displays. |  |
| 3 | Enter Cost Element Group | Make the following entries and shoose Go:Chart of Accounts: for example, YCOACost Element Group: YBPS_ICONode Type: All Nodes |  |  |
| 4 | Check Cost Elements | Under the node YBPS_ICO, the following cost elements should be assigned:94308100 (Service Time)97777700 (ICO Margin)If they are not assigned, select the YBPS_ICO node and choose Edit.On the Change Cost element group: Structure screen, select YBPS_ICO and choose Cost Element.Maintain the cost elements and choose Save. | The required cost elements are assigned to the cost element group YBPS_ICO. |  |
| 5 | Enter Cost Element Group | On the Manage Cost Element Group screen, make the following entries and choose Go:Chart of Accounts: for example, YCOACost Element Group: YBPS_E004Node Type: All Nodes |  |  |
| 6 | Check Cost Element | Under the node YBPS_E004, the following cost elements shoud be assigned:61008000 (Trav.Expense Misc.)If they are not assigned, select the YBPS_E004 node and choose Edit.On the Change Cost element group: Structure screen, select YBPS_E004 and choose Cost Element.Maintain the cost elements and choose Save. | The required cost element is assigned to the cost element group YBPS_E004. |  |

#### Block Intercompany Postings (Optional)

Purpose

In this step, you configure which intercompany postings are allowed. You can block all postings or allow only postings between certain companies.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: Overhead Cost Management |  |  |
| 5 | Open | Open Actual Postings. |  |  |
| 6 | Select Configuration Step | For the Block Intercompany Postings step, choose Configure. | The Block Intercompany Postings: Change: Details screen displays. |  |
| 7 | Maintain General Settings | If an Information dialog box displays, choose Continue.By default, all ICO postings are allowed. To change this setting, make a selection under General Settings and choose Save. | The changes are saved. |  |
| 8 | Maintain Allowlist | In the Dialog Structure on the left, double-click Allowlist Configuration.Maintain the list of sender and receiver companies which should be allowed for ICO postings and choose Save. | The changes are saved. |  |

Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Block Intercompany Postings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Block Intercompany Postings: Change: Details screen is displayed. |  |
| 3 | Maintain General Settings | If an Information dialog box displays, choose Continue.By default, all ICO postings are allowed. To change this setting, select an option under General Settings and choose Save. | The changes are saved. |  |
| 4 | Maintain Allowlist | In the Dialog Structure on the left, double-click Allowlist Configuration.Maintain the list of sender and receiver companies which should be allowed for ICO postings and choose Save. | The changes are saved. |  |

## Overview Table

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_14) [page ] 15 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A service order is created. |
| [Create In-House Repair and Repair Order](#unique_15) [page ] 16 | Customer Service Representative - In-House Repair | Manage In-House Repairs (F4025)Perform Prechecks (F4050) | A repair order is created. |
| [Create Service Confirmation](#unique_16) [page ] 19 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A follow-up service confirmation is created. |
| [Create Repair Confirmation](#unique_17) [page ] 20 | Service Technician - In-House Repair | Perform Repairs (F4241) | If the repair object is repaired, the performed services are released, confirmed and completed. |
| [Generate Intercompany Billing Request](#unique_18) [page ] 21 | Internal Sales Representative - Professional Services | Generate Intercompany Billing Request (F1829) | A debit memo request is created. |
| [Create Intercompany Invoice](#unique_19) [page ] 23 | Billing Clerk | Create Billing Documents - VF01 (VF01) Create Billing Documents (F0798) | An intercompany invoice is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Order

#### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a simple service order in an intercompany scenario.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order > Quick Create . | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Service OrderSold-To Party: for example, 33403310Description: <description>Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EAChoose Save and Edit. | A new service order is created.Note Only service products like SRV_01 and service expense items like SRV_02 are supported in intercompany billing.Note If your sold-to party is associated with one or more service contracts, a dialog box will appear and ask you to select a contract per item. Select No Assignment. |  |
| 5 | Enter Expense Amount | Under Items, choose Edit for the line item which contains the expense item SRV_02.Make the following entries:Amount: for example, 80 USDChoose Apply.Choose Save. | You have entered an amount for the expense item. |  |
| 6 | Release Service Order Item | To release the service items and service order, navigate to the Items view.Choose Release All Items.Choose Save. | The respective order item is released. |  |

#### Create In-House Repair and Repair Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a simple in-house repair and a repair order in an intercompany scenario. The delivery of this service order will be done by another company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Representative - In-House Repair. |  |  |
| 2 | Access App | Open Manage In-House Repairs (F4025). | The Manage In-House Repairs screen displays. |  |
| 3 | Create New In-House Repair | Choose Create. | The New In-House Repair screen displays. |  |
| 4 | Maintain Data for In-House Repair | Make the following entries and choose Create:Transaction Type: In-House RepairSold-To Party: for example, 33403310Sales Organization: for example, Dom. Sales Org DEDistrubition Channel: for example, Direct SalesDivision: for example, Product Division 00Employee Responsible: <employee> | The in-house repair is created and saved.Note If you do not enter the Employee Responsible, the system adds the current user. |  |
| 5 | Add Repair Objects | Under Repair Objects , choose Add.Make the following entries:Equipment: for example, Printer Professional IHR1911Select the Equipment of an item and choose ADD. | Note If no equipment is found for the customer, remove the Current Customer filter.An additional row under Repair Objects is added. |  |
| 6 | Confirm In-House Repair | Choose Confirm. | The in-house repair is set to status In Process and the repair objects are set to status Precheck: Decision Pending.Note You cannot add further repair objects. |  |
| 7 | Access App | Open Perform Prechecks (F4050). | The Perform Prechecks screen displays. |  |
| 8 | Search for Repair Object | Make the following entries and choose Go:In-House Repair: <repair number> | The repair objects are displayed according to your search criteria. |  |
| 9 | Display Repair Object | Choose your repair object. | The Perform Precheck Details screen displays. |  |
| 10 | Start Repair | Under Decide, choose Create Repair Order. | The repair order is created as a follow-up transaction for the repair object.The repair order appears in the transaction history for the repair object under Perform Repair.The Decide options are no longer displayed. |  |
| 11 | Display Repair Order | Under Transaction History, choose Repiar Order > Display Repair Order. | The Repair Orders screen displays. |  |
| 12 | Edit Repair Order | On the Repair Orders screen, choose Edit. |  |  |
| 13 | Add Item | Under Items, make the following entries:Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HR | The repair order item is added. |  |
| 14 | Release Repair Order | Choose Actions > Trigger Repair. | The repair order status changes to Released.The repair order appears in the worklist of the service technician.This status allows you to perform the repair. |  |
| 15 | Save Repair Order | Choose Save. | The repair order is saved. |  |

### Create Confirmation

Purpose

In the following step, you create a follow-up service confirmation or repair confirmation for the intercompany billing scenario. You must choose a service executing employee from a country/region that differs from the customer/company of the order.

|  |
| --- |
| Example The customer of the service order or repair order is from Germany. The service executing employee in the confirmation is from the U.S. |

#### Create Service Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a service confirmation. You set the confirmation to completed.

|  |
| --- |
| Example The customer of the service order is from Germany. The service executing employee in the confirmation is from the U.S. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <service order> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Create Service Confirmation | Choose Create Follow-Up > Create Service Confirmation . | The Create Service Confirmation window displays. |  |
| 6 | Maintain Data | Make the following entries:Final Confirmation: YesExec. Service Employee : for example, 9980000xxxNote Use an employee that is assigned to a U.S. cost center.Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EAChoose Save and Edit. | A new confirmation is created.Note It is mandatory that the executing service employee is assigned to a cost center for which intercompany cost rates are maintained.Note If you did not enter an amount for the expense item in the service order, you must enter it in the service confirmation.This is mandatory. |  |
| 7 | Complete Service Confirmation | Make the following entries and choose Save:Status: Completed | The confirmation is set to Completed.Note Once the status Completed is set, it can no longer be changed; it is only possible to cancel.Since the final confirmation is set, the life cycle status of the service order is automatically set to Completed. This is the prerequisite for the items to be released for billing. |  |

#### Create Repair Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step a follow-up repair confirmation will be created for the intercompany billing scenario.

|  |
| --- |
| Example The customer of the repair order is from Germany. The service executing employee in the confirmation is from the U.S. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Service Technician - In-House Repair. |  |  |
| 2 | Access App | Open Perform Repairs (F4241). | The Perform Repairs screen displays. |  |
| 3 | Search for Repair Object | Make the following entries and choose Go:Repair Order: <repair order> |  |  |
| 4 | Select Repair Order for Confirmation | Choose your repair object. | The Perform Repair Details screen displays. |  |
| 5 | Display Repair Order | Under Transaction History, choose the Repiar Order. | The Repair Orders screen displays. |  |
| 6 | Create Repair Confirmation | Choose Create Follow-Up.In the Follow-Up - Select Items dialog box, select your items.Choose Choose. | The Repair Confirmation: New screen displays. |  |
| 7 | Maintain Data | Make the following entries:Final Confirmation: SelectedExec. Service Employee: for example, 9980000xxxNote Use an employee that is assigned to a U.S. cost center. | A repair confirmation is created. |  |
| 8 | Complete Repair Confirmation | Under Processing Data, make the following entries and choose Save:Life Cycle Status: Completed | The confirmation is set to Completed. |  |

### Generate Intercompany Billing Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you generate an intercompany billing request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. |  |  |
| 2 | Access App | Open Generate Intercompany Billing Request (F1829). | The Application Jobs screen displays. |  |
| 3 | Schedule Job | Choose Create. | The New Job screen displays. |  |
| 4 | Maintain Data | Make the following entries:Job Template: Resource Related Billing between Company CodesJob Name: for example, Resource Related Billing between Company CodesChoose Step 2.Make the following entries:Start Immediately: SelectedChoose Step 3.Make the following entries:Intercompany Sales Document: <sales document>Service Document: <service order number>Choose Schedule. | The job is scheduled. |  |
| 5 | Check Status | On the Application Jobs screen, check that the status of your job changes to Finished.Choose the icon in the Log column of your job. | The Job Log screen displays.Under Log Details, you can find the billing document request number.Note down the request number. |  |

### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an intercompany invoice based on the billing document request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . |  |  |
| 2 | Access App | Open Create Billing Documents (F0798) Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document Request |  |  |
| 4 | Create Intercompany Invoice | In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.If you need to select a document type, use CI02 (Intercompany Invoice). | The Create Billing Documents dialog box displays. |  |
| 5 | Save Invoice | Choose Save. | The invoice is saved.Note The currency of the sending company will be used in the intercompany invoice.Example The currency is USD for the U.S. service executing employee. |  |
| 6 | Preview Intercompany Invoice | On the Billing Document screen, choose Preview to generate and print a PDF. | A PDF of the billing document displays. |  |

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
- related-to :: [[14-maintenance-service-and-projects/test-script-credit-and-debit-memo-processing-for-service-management-4g]]
- related-to :: [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964]]
- related-to :: [[14-maintenance-service-and-projects/test-script-service-order-management-and-monitoring-3d2-ae-927]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53Y_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 37,074 chars in the whole document
