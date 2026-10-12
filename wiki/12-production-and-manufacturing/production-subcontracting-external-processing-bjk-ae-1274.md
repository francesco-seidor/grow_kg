---
id: 12-production-and-manufacturing/production-subcontracting-external-processing-bjk-ae-1274
title: Production Subcontracting – External Processing (BJK_AE) (BJK_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script (BJK_AE, UAE) for production subcontracting: external-operation production order, PO, goods receipt, supplier invoice, payment."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/subcontracting-external-processing]
aliases: [BJK_S4CLD2608_BPD_EN_AE]
keywords: [Production Subcontracting and External Processing, production subcontracting, external processing, production orders, subcontract purchase orders, goods receipt, supplier invoices, purchasing info records, periodic payment, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1274
topic: 12-production-and-manufacturing/subcontracting-external-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Production Subcontracting – External Processing (BJK_AE) (BJK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Production Subcontracting and External Processing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Production Subcontracting – External Processing (BJK_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Production Subcontracting – External Processing (BJK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232861870)

[2 Prerequisites 3](#_Toc232861871)

[2.1 System Access 3](#_Toc232861872)

[2.2 Roles 3](#_Toc232861873)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861874)

[2.4 Business Condition 5](#_Toc232861875)

[2.5 Preliminary Steps 5](#_Toc232861876)

[2.5.1 Create Info Record 5](#_Toc232861877)

[3 Overview Table 8](#_Toc232861878)

[4 Test Procedures 9](#_Toc232861879)

[4.1 Create Production Order with Subcontract Operation 9](#_Toc232861880)

[4.2 Create Purchase Order for External Processing 10](#_Toc232861881)

[4.3 Post Goods Receipt for Subcontract Purchase Order 11](#_Toc232861882)

[4.4 Enter Incoming Supplier Invoice 13](#_Toc232861883)

[4.5 Periodic Payment 14](#_Toc232861884)

[4.6 Review Manufacturing Object Pages 15](#_Toc232861885)

[5 Appendix 16](#_Toc232861886)

[5.1 Succeeding Processes 16](#_Toc232861887)

## Purpose

Overview

This scope item demonstrates the option to execute an operation externally within a production order, which is crucial when in-house capacity is limited. When a planned order for production is converted to a production order during the manufacturing process, the system checks for routing or work center operations that require external processing. When the order is processed and the operation to be handled externally is reached, the system creates a purchase requisition. After generating a purchase order for the operation, the production step is processed by the external subcontractor. The external service is captured with a goods receipt posting. The process is finalized by receiving the subcontractor’s invoice for the service and posting the payment accordingly.

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
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG126 | FIN126,MTS-DI,PD,Batch-Fifo,SerialNo |  |
| Plant | 3310 | Plant 1 AE |  |
| Bill of Material | FG126 | FIN126,MTS-DI,PD,Batch-Fifo,SerialNo |  |
| Routing Group Counter 1 | 43310000 |  |  |
| Routing Group Counter 2 | 43310001 |  |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Info record | 55000000XX | Supplier: 33300001Material Group: L004Info Category: StandardPrice per 100: 5.35 AED |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |
| BNL | Create Routing - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BLD | Create Production Version - MDS |

### Business Condition

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the step described in the Create Costing Run - MDS (BNU) master data script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up-to-date. |

### Preliminary Steps

#### Create Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create info record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Search Purchasing Info Record | Search the info record by following filters.Material Group: L004Supplier: 33300001If the info record with description Shrink Wrapping displays, then note down the info record number and skip the following steps.If no such info record, then proceed to create it. |  |  |
| 4 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen displays. |  |
| 5 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Plant: 3310Purchasing Group: 001Material Group: L004Info Record Description: Shrink Wrapping | Header data is added. |  |
| 6 | Enter General Information | Make the following entries:Salesperson: Sales nameSupplier Telephone Number: 0172595959 | General Information is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: 100Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose the Create button. Enter the following data:Valid From: <Today’s Date>Amount: 2Pricing Unit: 1Valid To: 12/31/9999Currency: AEDChoose the Apply button. | Condition Data is added |  |
| 9 | Save Your Data | Choose Create. | A purchasing info record is saved.Note down the purchasing info record number. |  |

## Overview Table

The Production Subcontracting – External Processing scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Production Order with Subcontract Operation](#unique_9) [page ] 9 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) | Order Operations have been changed to subcontract. Production order is released and PR is created |
| [Create Purchase Order for External Processing](#unique_10) [page ] 10 | Purchaser | Process Purchase Requisitions (F1048A) | Assigned PR is converted to Purchase Order |
| [Post Goods Receipt for Subcontract Purchase Order](#unique_11) [page ] 11 | Warehouse Clerk | Post Goods Movement (MIGO) | GR is done in the system. |
| [Enter Incoming Supplier Invoice](#unique_12) [page ] 13 | Accounts Payable Accountant - Procurement | Create Supplier Invoice (F0859). | The invoice is entered. |
| [Periodic Payment](#unique_13) [page ] 14 | Role dependent upon procedure | App dependent upon procedure | The outgoing payment is processed. |
| [Review Manufacturing Object Pages](#unique_14) [page ] 15 | Production Planner | Search |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Production Order with Subcontract Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This scenario is used when subcontracting production. Normally, the plant handles the production. Sometimes, in order to meet schedule demands, a business partner is used to process an order. When you save the production order, a subcontracting purchase requisition is generated for operation 0030. This process step shows you how to create production order with subcontract operation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Define Production Order: Initial Screen | Enter the following data for production order:Material: FG126Production Plant: 3310Order Type: YBM1Then press Enter. | The Production Order Create: Header screen displays. |  |
| 4 | Define the Production Create: Header data | Enter the following data for production order header:Total Qty: for example, 10 PCEnd: for example, Today + 7 daysOn the tab General, press Enter.Production Version: If a dialog box is displayed for selecting production version, choose 0001. | If the dialog boxOrder has missing parts(see log)displays, choose Continue.In order to avoid triggerring workflow for approval of purchase requisition with total amount more than 500.00 AED, please do not enter high quantity for production order. |  |
| 5 | Change Operation 0030 | Choose Operations.On the Production Order Create: Operation Overview screen, enter the following data for production order in the Operation Overv. section:Op: 0030Control Key: YBP2And press Enter twice. | Change Production Operation Data. |  |
| 6 | Enter External Service Procurement Information | From the Ext. Processing tab, enter the following data for external service procurement:Purch Info Record: use the info record number you noted down in preliminary stepPurchasing Org: 3310Note Use Material Group L004 to find the Purch Info Record for your purchase organization. |  |  |
| 7 | Create the Production Order and PR | Choose Back twice, from the menu, to return to the Production Order header screen.Choose Release Order.Choose Save. | Production Order is created and PR is created.To view the PR, choose Operation Overview, select the operation and scroll to the right of your screen.You can record the PR you created in this step using display the Production order and go to the Ex. Processing tab to review the purchase requisition number. |  |

### Create Purchase Order for External Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you save the production order, a subcontracting purchase requisition is generated for operation 0030. A firm supplier was assigned to the purchase requisition using the outline agreement (value contract) maintained in the routing of Finished Good MTS (FG126). This means that the responsible person is able to convert the purchase order request directly into a purchase order.

This process step shows you how to convert assigned purchase requisitions to purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A). | A list of requisitions is displayed. |  |
| 3 | Select Purchase Requisition | Search for a Purchase Requisition with assigned Source of Supply, and select one using the link of the sources. Change the filter settings as follows and choose Go:Material Group: L004Plant: 3310 |  |  |
| 4 | Prepare the Purchase Order | Select the checkbox of the relevant Purchase Requisition item and choose Create Purchase Order. | The Purchase Order Preview screen displays.If the total amount of PR is more than 500.00 AED, then it could trigger workflow for approval of purchase requisition. And the purchase requisition could be missing here. |  |
| 5 | Create the Purchase Order | Select Standard PO in the Order Type field and choose Save. | The purchase order is created. |  |
| 6 | Return to Manage Purchase Requisition | In the dialog box, choose OK. | The Purchase Requisition list is displayed again. |  |

### Post Goods Receipt for Subcontract Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the warehouse clerk receives a subcontract Purchase Order. The clerk then generates a goods receipt.

The goods receipt ignores the Stock type (quality, blocked). Upon goods receipt, the subcontract Purchase Order Costs are posted to the Production Order. There is no financial document trail other than the goods receipt document and a controlling document. The controlling document can be viewed on the Production Order header by choosing Goto > Documented Goods Movements and the operation does not influence the Purchase Order open quantity; only MIGO (goods receipt) changes the quantity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Purchase Order screen displays. |  |
| 3 | Enter Purchase Order Information | Select Goods Receipt from the executable action menu, and verify or select Purchase Order from the reference document menu.Make the following entries:Purchase Order : <Your PO number>Movement Type : 101 |  |  |
| 4 | Enter Data on Item to be Received | Locate the item to be received, verify the quantity and them choose item OKNote If you don't see item OK, scroll down in the window until it appears. |  |  |
| 5 | Post | Choose Check when the system responds with message Document is OK, and then choose Post. | Goods receipt is posted for Purchase Order. |  |

### Enter Incoming Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to enter the supplier’s invoice for the goods received.

Ensure that the top right of the screen displays a green light. If there is no green light, choose Messages to review and resolve any errors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | Enter the following:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <enter value>Currency: AEDInvoice Date: TodayPosting Date: TodayInvoicing Party: for example, 33300001Reference: <your PO number> |  |  |
| 4 | Enter Purchase Order References | In Purchasing Document References review the references.Make the following entries, using the Purchase Order you created previously:References Document Category: Purchase Order/Scheduling AgreementPurchase Order: <PO number>Then press Enter. |  |  |
| 5 | Select Purchase Order Items | Review the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Invoice Items table. |  |
| 6 | Review the Purchase Order Items Data | In the Invoice Items area, review the Amount, Quantity, Tax Code, and Tax Jurisdiction (if applicable).Note Ensure that the amount and the quantity correspond to the values of the Goods Receipts. |  |  |
| 7 | Review the Tax Code and Payment | In the Tax section, verify the tax code information and enter the tax amount:Tax Code: When no tax code is specified, use <Input Tax Code>In the Payment section, review the payment information and remain Payment Method as blank.Note The tax code is included in the simulation. |  |  |
| 8 | Simulate Supplier Invoice and Review the Messages | Choose Simulate.If there are no differences, a new screen, Simulation, appears. You can review the simulation results in the Simulation Overview and Simulation Details area. The Supplier Invoice is complete to post.Verify the Gross Invoice Amount against the items, plus tax, (when your tax code is <Input Tax Code> there is no tax amount. | The Supplier Invoice is complete to post. |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message:Documents have been created. Supplier invoice: XXX |  |

### Periodic Payment

|  |
| --- |
| Note External Process |

For this activity, use the Master Data from this test script and execute the following steps from the Accounts Payable (J60) test script document:

- Manage Payment Blocks

Payment Run:

- Payment Approval

or

- Manual Payment Online

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the different objects pages available for different roles in the area of manufacturing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in the Roles section above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. | An input field displays. |  |
| 3 | Search Criteria | Make the following entries and choose Search:Products: Material (see the Master Data section) | The system displays a list of objects that use the selected material. |  |
| 4 | Display Object | In the All field, choose Down arrow.Select an object and choose Search. | The list of objects is limited to the object type selected. If no object is selected, a message is displayed instead. |  |
| 5 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort) to filter the results list. | The results list is filtered according to your selections. |  |
| 6 | Repeat Steps | Repeat steps 1-5 for any other role in this test script and any other object offered in the search function. | The list of objects offered for search differs by the role you used to log on. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Make-to-Stock Production – Discrete Manufacturing (BJ5) - (Optional) | Complete the following activities using the data you created in this test script:Create Initial Material StockMaterial StagingPick ComponentsReview Order OperationsConfirm Assembly ActivitiesFinal Confirmation of ProductionPost Goods Receipt for Production Order |

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
- see-also :: [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 26,810 chars in the whole document
