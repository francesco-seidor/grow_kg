---
id: 14-maintenance-service-and-projects/solution-order-management-with-advanced-variant-configuration-6hy-ae-t
title: "Solution Order Management with Advanced Variant Configuration (6HY_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6HY_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6HY_AE (AE): create, release, print solution orders with configurable items, then follow-on orders and billing."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [6HY_S4CLD2608_BPD_EN_AE]
keywords: [Solution Orders and SAP CPQ Quotations, solution order management, variant configuration, solution order creation, solution order release, solution order output, billing documents, business conditions, business roles, sample master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6HY_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1170
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Solution Order Management with Advanced Variant Configuration (6HY_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6HY_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6HY_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Solution Order Management with Advanced Variant Configuration (6HY_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Solution Order Management with Advanced Variant Configuration (6HY_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858616)

[2 Prerequisite 4](#_Toc232858617)

[2.1 System Access 4](#_Toc232858618)

[2.2 Roles 4](#_Toc232858619)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232858620)

[2.3.1 Additional Manual Configuration 6](#_Toc232858621)

[2.4 Business Conditions 6](#_Toc232858622)

[2.5 Preliminary Steps 7](#_Toc232858623)

[2.5.1 Set default item category for solution order items (Optional) 7](#_Toc232858624)

[3 Overview Table 9](#_Toc232858625)

[4 Test Procedures 10](#_Toc232858626)

[4.1 Create Solution Order 10](#_Toc232858627)

[4.2 Release Solution Order Line Items 14](#_Toc232858628)

[4.3 Print Solution Order 16](#_Toc232858629)

[4.4 Manage Sales Order 17](#_Toc232858630)

[4.5 Manage Service Order 18](#_Toc232858631)

[4.6 Manage Service Contract 18](#_Toc232858632)

[4.7 Manage Billing Document 19](#_Toc232858633)

[4.7.1 Create Billing Document 19](#_Toc232858634)

[4.7.2 Display Billing Document 20](#_Toc232858635)

[5 Appendix 22](#_Toc232858636)

## Purpose

Overview

Solution Order Management helps customers to evolve their business from selling single products to offering holistic solutions: they can manage complex solutions of physical goods, services, projects, and subscriptions in an integrated end-to-end order. With an intuitive progress view, situation handling, and cross object navigation, customers always have an overview of the fulfillment status of the different solution order items. Solution Order Management also comes with embedded pricing, omnichannel convergent billing, and seamless integration into revenue recognition and controlling. This gives customers a consolidated financial view of their solution portfolio. Solution Order Management is supported by a built-in analytics dashboard.

This scope item is a variant of the standard solution order management process in the Solution Order (4GT) scope item, which also supports configurable sales, service, and service contract items. It can be used with 4GT.

## Prerequisite

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test should be conducted with the following system:

Note For system details contact your System Administrator.

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Use the following standard test users or assign roles to testers, respectively for S/4 HANA Cloud System:

Table 1:

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Solution Order Specialist | SAP_BR_SOLN_ORDER_SPCLST | Your system administrator provides the user and password information. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Your system administrator provides the user and password information. |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Your system administrator provides the user and password information. |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Your system administrator provides the user and password information. |
| >Billing Clerk | conkeyref="roles/SAP_BR_BILLING_CLERK_id"/> | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Sample Value | Details | Comments |
| --- | --- | --- | --- | --- | --- |
| Customer |  |  | 33100001 | Domestic UAE Customer 1 | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure.to check the assignment, use Business Role SAP_BR_BUPA_MASTER_SPECIALIST - tile Manage Customer Master Data in the Sales Area Data. |
| Self Services / Self Services / Employee Overview Space |  |  | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Material |  |  | CM-FL-V00 | Configurable Forklifter | Single-level structure |
| Material |  |  | CM-MLFL-KM-VXX | Configurable Forklifter | Multi-level structure |
| Material |  |  | CM-FL-V00-3P | Forklift for 3rd Party | Material can be used to create 3rd party configurable items with or without charge. |
| Material |  |  | CAR-WASH_CONF | Service Order Configurable Product |  |
| Material |  |  | SRV_CONTR_CONFIG | Service Contr.Configurable Product |  |
| Sales Organization |  |  | 3310 | Dom. Sales Org |  |
| Plant |  |  | Domestic UAE Customer 1 | Plant 1 AE |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 2T7 | Create Product Master of Type "Configurable Material" |
| 5BE | Create Configurable Service Product |

#### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/8463ac36c9a9aef9b9f9c5cf6efec22b)

### Business Conditions

Before this test script can be tested, the following business conditions must be met. Ensure the below scope items are activated.

| Scope Item | Business Condition |
| --- | --- |
| 1YT - Make-to-Order Production with Variant Configuration | Must be run before this test script. |
| 6GS - Service Management with Advanced Variant Configuration | Must be run before this test script. |
| 6GU - Service Contract Management with Advanced Variant Configuration | Must be run before this test script. |
| 4R6- Sales Processing using Third-Party with Variant Configuration | Must be run before this test script. |
| 4GT - Solution Order Management | Must be run before this test script. |

### Preliminary Steps

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
| [Create Solution Order](#unique_11) [page ] 10 | Solution Order Specialist | Manage Solution Order | A solution order has been created |
| [Release Solution Order Line Items](#unique_12) [page ] 14 | Solution Order Specialist | Manage Solution Order | Items of the solution order has been released |
| [Print Solution Order](#unique_13) [page ] 16 | Solution Order Specialist | Manage Solution Order | Solution order PDF is displayed |
| [Manage Sales Order](#unique_14) [page ] 17 | Internal Sales Representative | Manage Sales Orders | Sales Order is displayed |
| [Manage Service Order](#unique_15) [page ] 18 | Customer Service Manager | Manage Service Orders | Service Order is displayed |
| [Manage Service Contract](#unique_16) [page ] 18 | Customer Service Manager | Manage Service Contracts | Service Contract is displayed |
| [Create Billing Document](#unique_17) [page ] 19 | Billing Clerk | Create Billing Document | Invoice is created for Solution Order |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new solution order and add line items (for example configurable sales item, configurable service item and configurable service contract item) to solution order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Choose Manage Solution Orders application tile. | The list report page is displayed. |  |
| 3 | Create Solution Order | Choose Create button from the solution order list page | Create Solution Order window will be displayed |  |
| 4 | Maintain Solution Order data | Enter the following data to create a solution order:Description: <your description>External Reference: <your reference>Sold-To Party: e.g. 33100001for US (Domestic UAE Customer 1)Note: Select the sales organization ( e.g. 3310) and Contact person from the popup appears | Required header data for the Solution order has been maintained. |  |
| 5 | Add Sales Item | Maintain the following Sales Items in the solution order:Product ID: for example, CM-FL-V00 (Forklift)Quantity: for example, 1Unit: for example, PCChoose Enter.Note For free of charge sales item change the item category to Conf. Sales Item FoC. Then follow Manage Sales Order chapter. | The Sales Order items for a single-level configurable product are now added to Solution Order. |  |
| 6 | Configure Characteristics | In the Actions column, choose Configure Product to navigate to the Solution Order New Variant Configuration view in edit mode.In the Default Group section, select the following variants using the input help:Lifter Model: StandardCounterweight: 1.000kgFork Size: SmallChoose Done. | All variants for the characteristics are maintained. The Net Value field is automatically calculated according to the prices for the selected variants.The configuration is set to Released. |  |
| 7 | Add Sales Item | Maintain the following Sales Items in the solution order:Product ID: for example, CM-MLFL-KM-VXX (Forklift)Quantity: for example, 1Unit: for example, PCChoose Enter.Note For free of charge sales item change the item category to Conf. Sales Item FoC. Then follow Manage Sales Order chapter. | The Sales Order items for a multi-level configurable product are now added to Solution Order. |  |
| 8 | Configure Characteristics | On the Variant Configuration screen, choose Default Group. Select value for characteristics below:Lifter Mode: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Choose Technical and select value for other characteristics.Wheel Type: <Cushion Tires, Pneumatic Tires>Font Size: <Small, Normal, Large>Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity(Ah): <50, 80, 140>The combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automatically.Wheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Medium or LargeCombination Two:Lifter Model: StandardPower Source: CombustionCounterweight (KG): 1.000or 2.000Wheel Type: Cushion Tires is filled automaticallyFork Size: Small or Normal or LargeCombination Three:Lifter Model: StandardPower Source: electricalCounterweight (KG): 1.000or 2.000Wheel Type: Cushion Tires is filled automaticallyFork Size: Small or Normal or LargeBattery Capacity(Ah): 50 or 80 or 140 (140 only available when fork size is L)Choose Done. | All variants for the characteristics are maintained. The Net Value field is automatically calculated according to the prices for the selected variants.The configuration is set to Released. |  |
| 9 | Add Configurable 3rd party Sales Item | Maintain the following Sales Items in the solution order:Product ID: for example, CM-FL-V00-3P (Forklift for 3rd Party)Quantity: for example, 1Unit: for example, PCChoose Enter.Note For free of charge item, change the item category in solution order to 3rd Pty VC w/o SN FoC. Alternatively, to process the entered 3rd party configurable items as a milestone billing item, change the determined item category to 3P VC w SN Milest or 3P VC w/o SN Milest. | The Sales Order items for 3rd party configurable product are now added to Solution Order. |  |
| 10 | Configure Characteristics | In the Actions column, choose Configure Product to navigate to the Solution Order New Variant Configuration view in edit mode.In the Default Group section, select the following variants using the input help:Lifter Mode: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Choose Technical and select value for other characteristics.Wheel Type: <Cushion Tires, Pneumatic Tires>Fork Size: <Small, Normal, Large>Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity(Ah): <50, 80, 140>Choose Done. | All variants for the characteristics are maintained. The Net Value field is automatically calculated according to the prices for the selected variants.The configuration is set to Released. |  |
| 11 | Add Service Items | Maintain the following Service Items in the solution orderProduct ID: for example, CAR-WASH_CONF (Car Wash Configurable)Quantity: for example, 1Unit: for example, AUChoose Enter.In the appearing contract assignment popup select No Assignment | The Service Order items are added to the Solution Order. |  |
| 12 | Configure Characteristics | In the Actions column, choose Configure Product to navigate to the Solution Order New Variant Configuration view in edit mode.In the Default Group section, select the following variants using the input help:CAR SIZE: LargeCAR WASH TYPE: Premium WashEXTRA POLISH: YesChoose Done. | All variants for the characteristics are maintained. The Net Value field is automatically calculated according to the prices for the selected variants.The configuration is set to Released. |  |
| 13 | Add Service Contract Items | Maintain the following Service Contract Item in the solution orderProduct ID: for example, SRV_CONTR_CONFIG (Configurable Service Contract)Quantity: for example, 1Unit: for example, AUChoose Enter. | The Service Contract Item is added to the Solution Order. |  |
| 14 | Configure Characteristics | In the column Actions choose Configure Product to navigate to the Solution Order New Variant Configuration view in edit mode.In section Default Group:Select the following variants using the value help:Preventive Maintenance: Half-YearlyService Channel: Telephone supportChoose Done. | All variants for the characteristics are maintained. The field Net Value is automatically calculated according to the prices for the selected variants.Configuration status is Released. |  |
| 15 | Save the Solution Order | Choose SaveNote down the ID of the Solution Order you have just created. | Solution Order with all the line items is saved |  |

### Release Solution Order Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the line items of the previously created solution order will be released. It is a prerequisite for a follow-up confirmation of that line items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Order application is displayed. |  |
| 2. | Open Manage Solution Order application | Choose Manage Solution Order application tile. | The list report page is displayed. |  |
| 3. | Find Solution Order | In the search area on the top,enter the ID of your solution order in the ID field.Press the button Go. | Your solution order is displayed in the report list within Manage Solution Orders. |  |
| 4. | Open Solution Order in the Edit mode | Choose the Solution Order and click Edit in the Solution Order Details tab | The edit view of the Solution Order will be opened. |  |
| 5. | Sales Order Simulation | The Sales Items view in tab area Items choose Simulate Sales Order Creation to verify the sales order.Note: In case of error or incompletion a warning would be shown in the Solution Order. In addition to that temporary ATP information can be seen in the Confirmed Quantity and Last Confirmed Delivery Date. | Sales order creation simulated successfully. |  |
| 6. | Release line items in Solution Order | In the tab area Items, change the Status for the individual item (choose Show:All Items).Example-For Sales item: In sales item line change the Status from Open to ReleasedClick on the Save buttonFor Service Order items (service, expense & spare part): In service order item line change the Status from Open to ReleasedClick on the Save buttonFor Service Contract item: In service contract item line change the Status from Open to ReleasedClick on the Save buttonNote: It is also possible to release all the items in the solution order at the same time with the action Release All Items in the All Items view of the Items tab area. | Line item in solution order has been released |  |
| 7. | Verify Distribution Status | In the tab areaItems, under the field Distribution Status verify the status changed to Distribution Started.Choose Refresh to verify the Distribution Status changed to Distribution Success.Note: If theDistribution Status shows as Distribution error then verify if there is any issue in creation of solution order.Once the issue is resolved then chooseRedistributeand chooseRefreshto view the updated status. | Distribution Status for all line items are verified |  |
| 8. | Verify follow-up transaction data in transaction history | Note: choose Refresh to view the updated solution order with the follow-up transaction data. The follow-up transactions are created asynchronously, that’s why it can take some time till the document flow is displayed.In the tab area Transaction History,Forsales item click on Transaction: Sales Order to navigate Sales Orderdetails viewandverify the following dataItems: <Same as sales Items added in solution order>Note: Only one sales order will be created for all sales itemsFor service item click on Transaction: Service Order to navigate Service Orderdetails view and verify the following dataItems: <Same as service Items added in solution order>For service contract item click on Transaction: Service Contract to navigate Service Contractdetails view and verify the following dataItems: <Same as service contract Items added in solution order>Note down all the IDs of the follow-up transactions. | Line item in solution order has been verified |  |

### Print Solution Order

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

### Manage Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the sales order previously created in solution order will be processed for Production Order, refer to section Manufacturing Steps Production Order Processing from chapter Make to Order Production with Single Level Configurable Material in 1YT test script

Note: Once the Production Order is created execute the following steps using the master data from this document (see also the following table).

Sell from Stock (BD9)

| Test Procedure No.of BD9 | Test Procedure | Note |
| --- | --- | --- |
| 4.9 | Create Delivery |  |
| 4.11 | Execute Picking |  |
| 4.16 | Post Goods Issue |  |

### Manage Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State the Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this step the service order previously created in solution order will be processed for service conformation. Refer to sections Create Service Confirmation and Release Confirmation for Billing in 6GS test script

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

Refer to Schedule Billing Document Request Creation, Manage Billing Document Request in 6GU test script

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | >Open Create Billing Documents(F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Search for billing due list | In the search condition, adapt the filter to use the Solution Order ID as search criteria. | All billing due list items belonging to the Solution Order should be displayed:DeliveryBilling Document Requests (from Service Order and Service Contract) |  |
| 5 | Select item(s) for billing | Select row(s) in the Billing Due List created previously and choose button Create.Note: It is possible to combine all the items in the solution order and create a single invoice, at the same time individual invoice can be created for different items in solution order by choosing the individual billing due list items. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.Note: In case the Billing Due List cannot be combined into a single invoice a Split Analysis button will be displayed. In that case you will have to create individual billing documents. | The system generates an invoice for billing.Billing status of the individual items in the Solution Order is updated. |  |

#### Display Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step displays the sales order billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Billing Documents (VF03). | The Display Billing Documents screen is displayed. |  |
| 3 | Search the Billing Document Created in Previous Step | Enter <the Billing document number recorded in Create Billing Document step>.Choose Continue. | The billing document is displayed. |  |
| 4 | Display Output | On the Invoice XXXXXXXX(F2) Display: Overview of Billing Items screen, choose More > Goto > Header > Output. | The Invoice XXXXXXXX(F2) Display: Output screen is displayed. |  |
| 5 | Display Print Preview | Select the output line and choose Display Document. | Print preview for PDF file is displayed. The Solution Order is available on the print form. |  |

## Appendix

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6HY_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 33,410 chars in the whole document
