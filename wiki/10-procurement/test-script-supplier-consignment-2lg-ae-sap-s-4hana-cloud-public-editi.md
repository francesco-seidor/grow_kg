---
id: 10-procurement/test-script-supplier-consignment-2lg-ae-sap-s-4hana-cloud-public-editi
title: "Test Script: Supplier Consignment (2LG_AE) - SAP S/4HANA Cloud Public Edition (2LG_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item Supplier Consignment (2LG): info record, PO, goods receipt, stock transfer, consignment settlement."
cluster: 10-procurement
tags: [kb/procurement, topic/supplier-consignment]
aliases: [2LG_S4CLD2608_BPD_EN_AE]
keywords: [Supplier Consignment, consignment info record, purchase orders, goods receipt, stock transfer, consignment settlement, supplier invoice jobs, purchase order approval, supplier invoice list, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LG_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-830
topic: 10-procurement/supplier-consignment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Supplier Consignment (2LG_AE) - SAP S/4HANA Cloud Public Edition (2LG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supplier Consignment** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Supplier Consignment (2LG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849553)

[2 Prerequisites 3](#_Toc232849554)

[2.1 System Access 3](#_Toc232849555)

[2.2 Roles 3](#_Toc232849556)

[2.3 Master Data and Organizational Data 4](#_Toc232849557)

[2.4 Business Conditions 5](#_Toc232849558)

[2.5 Preliminary Steps 5](#_Toc232849559)

[2.5.1 Create Consignment Info Record 5](#_Toc232849560)

[3 Overview Table 7](#_Toc232849561)

[4 Test Procedures 8](#_Toc232849562)

[4.1 Create Purchase Order 8](#_Toc232849563)

[4.2 Approve Purchase Order (Optional) 9](#_Toc232849564)

[4.3 Post Goods Receipt 10](#_Toc232849565)

[4.4 Transfer Stock 11](#_Toc232849566)

[4.5 Invoice Receipt from Consignment Withdrawal 12](#_Toc232849567)

[4.5.1 Option 1: Create Consignment Settlement 12](#_Toc232849568)

[4.5.2 Option 2: Schedule Supplier Invoice Jobs 14](#_Toc232849569)

[4.6 Check Supplier Invoice List (Optional) 15](#_Toc232849570)

## Purpose

Overview

By using the consignment process for procurement, the supplier provides the material and stores it at site of the procuring party. The supplier maintains the legal owner of the material until it is withdrawn from the consignment stores. Payment for consignment stock is only required in case the material is withdrawn. For this reason, the supplier is informed of withdrawals of consignment stock on a regular basis.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data and Organizational Data

The organizational structure and master data of your company was created in your SAP S/4HANA Cloud Public Edition system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM128 | RAW128,PD,Consignment |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 | Group 001 |  |
| Purchasing group | 003 | Group 003 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS– MDS |
| BNE | Create Supplier Master - MDS– MDS |
| BHD | Create Purchasing Info Record - MDS – MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BHD - Create Purchasing Info Record - MDS | You have completed the step described in the chapter Create Purchasing Info Record for Consigned Procurement. |

### Preliminary Steps

#### Create Consignment Info Record

Purpose

In this procedure, you create consignment info records for procure process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Consignment>Supplier: 33300001Material: RM128Purchasing Organization: 3310Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Enter the following values:Delivery Time in Days: <XX Days> , for example, 5Under Delivery Tolerance in %: <Tol. Underdl.>, for example, 10Over Delivery Tolerance in %: <Tol. Overdl.> , for example, 10Standard Order Quantity: <Standard order quantity>, for example, 1Order Unit: <Order Unit>, for example, PCTax Code: <Input Tax Code>Choose Enter. |  |  |
| 6 | Enter Condition Data | In the Condition section, choose Create and make the following entries:Valid From: <Valid from Date>Amount: <Amount>, for example, 165Pricing Unit: <Pricing Unit>Valid To: <Valid to Date>Currency: <Currency>Choose Apply. | Condition Data is added. |  |
| 7 | Create Consignment Infor Record | Choose Create. | A purchasing info record for consigned procurement is saved. |  |

Result

The Consignment info records are created.

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_9) [page ] 8 | Purchaser | Manage Purchase Orders (F0842A) | The Purchase Order is created. |
| [Approve Purchase Order (Optional)](#unique_10) [page ] 9 | Purchasing Manager | My Inbox - All Items (F5331) | Purchase Order is approved. |
| [Post Goods Receipt](#unique_11) [page ] 10 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted against the purchase order. |
| [Transfer Stock](#unique_12) [page ] 11 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | The goods are transferred from the supplier consigned stock to own stock . |
| Invoice Receipt from Consignment Withdrawal |  |  |  |
| [Option 1: Create Consignment Settlement](#unique_13) [page ] 12 | Accounts Payable Accountant | Create Logistics Consignment and Pipeline Settlement (MRKON) |  |
| [Option 2: Schedule Supplier Invoice Jobs](#unique_14) [page ] 14 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs - Advanced (F1683) |  |
| [Check Supplier Invoice List (Optional)](#unique_15) [page ] 15 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Supplier Invoice List is checked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to formalize a specific requirement for a material from the supplier by creating a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order data | Choose Create.On the Purchase Order Screen, make the following entries and choose Enter:In the General Information area:Supplier: 33300001Currency: AEDPurchasing Group:001Purchasing Organization: 3310Company Code: 3310In the Items area, choose Create and make the following entries:Item Category: Consignment(K)Material: RM128Order Quantity: X PCPlant: 3310Choose the item and go to the Purchase Order Item screen.Under the General Information tab, make the following entry:Storage Location:331CChoose Apply to go back to Purchase Order screen. |  |  |
| 4 | Save Purchase Order | Choose Order and when the purchase order number is displayed, write it down for further use. | The Purchase Order is created. |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, the Purchasing Manager releases a purchase order.

A prerequisite is the existence of a purchase order that can be released and Purchasing Group is 003.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | A list of already created purchase orders is displayed. |  |
| 3 | Search for Purchase Order Status | Enter the Purchase order number in the search area, then choose Search. |  |  |
| 4 | Open Approve Purchase Orders | On the My Inbox screen, select the Purchase Order from the left screen. | The My Inbox screen is displayed. |  |
| 5 | Approve Purchase Order | On the Release of Purchase Order screen, confirm your created purchase Order information.Choose Approve.On the Submit Decision screen, add note if necessary and choose Submit. | Purchase Order is approved. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Enter detail data | On the Post Goods Receipt for Purchasing Document screen, make the following entry and then choose Enter.Purchasing Document: Enter the purchase order number created in the first step. | The system displays the data for the goods receipt on the Post Goods Receipt for Purchase Order screen. |  |
| 4 | Enter General Information | Go to General Information area and check the following entries.Document Date: <Today>Posting Date: <Today> |  |  |
| 5 | Enter Quantity | Go to Items area and check the quantity.Delivered: X PC |  |  |
| 6 | Enter Storage Location | Go to Items area and check the storage location.Storage Location: Raw mat. stoloc.(331C) |  |  |
| 7 | Select Items | Select the items for which a goods receipt is to be posted. | The Post button is activated. |  |
| 8 | Post | Choose Post. | The system message material document(s) posted: 500xxxxxxx 20XX is displayed. |  |

### Transfer Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, stock is transferred from the vendor consignment stock to the own inventory by transfer posting.

|  |
| --- |
| Note Please confirm there is enough quantity in the vendor consignment stock. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App. | Open Transfer Stock - In-Plant (F1061). | The Transfer Stock – In-Plant screen is displayed. |  |
| 3 | Open Stock Overview | Make the following entries in the fields and choose Enter:Material: RM128Plant: 3310 | The Transfer Stock- In-Plant screen is displayed. |  |
| 4 | Select stock | Choose the icon beside the stock that you want to transfer (Unrestricted-Use Stock, Storage location 331C). | A dialog box opens with Special Stocks, Stock Type, and current Quantity. |  |
| 5 | Select Special Stock | In dialog box, choose item Supplier Consignment XX PC. |  |  |
| 6 | Select stock | Choose the icon beside the stock that you want to transfer (Unrestricted-Use Stock, Storage location 331C) again. | A dialog box containing Special Stocks, Stock Type, and current Quantity is displayed. |  |
| 7 | Select Special Stock | In dialog box choose Unrestricted-Use Stock XX PC. | A dialog box appears. The Storage Location, Stock Type, current Quantity, Special Stock Type and Supplier are displayed according to your entries in the previous steps. |  |
| 8 | Transfer Items | In dialog box, make the following entries in the fields and choose Post.For example:Supplier: 33300001Document Date: TodayPosting Date: TodayQuantity: x PC | The system displays Material document xxx created.The stock has been transferred from the vendor consignment stock to the own inventory. |  |

### Invoice Receipt from Consignment Withdrawal

#### Option 1: Create Consignment Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The liabilities should be cleared regularly towards the supplier because of goods issues from the vendor consignment stock. The consignment goods are settled with invoice receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Logistics Consignment and Pipeline Settlement (MRKON). | The Consignment and Pipeline Settlement screen displays. |  |
| 3 | Enter Parameter | On the selection screen, enter the following values then choose Enter:Company Code: 3310Supplier: 33300001Plant: 3310Material Document: （optional） Enter the material document number created from the last stepConsignment: SelectedPipeline: DeselectedSettle: SelectedWithdrawals Not Settled: Selected |  |  |
| 4 | Post Invoices | Choose Run. | The invoice is posted. |  |
| 5 | View Settlement Document | On the Logistic Consignment and Pipeline Settlement screen, you can see the invoice document number under column Doc. No.. | The settlement document is created. |  |

#### Option 2: Schedule Supplier Invoice Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Scheduling supplier invoice jobs is especially effective if you create settlement documents periodically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Supplier Invoice Jobs - Advanced (F1683). | The Application Jobs screen is displayed. |  |
| 3 | Create Application Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Execute Consignment Settlement | Make the following entries:In the 1. Template Selection section, from the drop-down box of job template, choose Logistic Consignment and Pipeline Settlement.Click Step 2. In the Scheduling Options section, make sure that Start Immediately checkbox is checked. You can also set the start date and start time.Click Step 3, in the Parameter section, make the following entries:Company Code: for example, 3310Supplier: 33300001Plant: for example, 3310Material Document: Enter the material document number created from the last step.Consignment: SelectedPipeline: DeselectedDisplay: SelectedTax Date: <Today>Note The value in Tax Date is the key date for calculating tax, please maintain it carefully according to your financial business requirements.Withdrawals Not Settled: SelectedChoose Check. | The system message displays: You can go ahead and schedule the job. |  |
| 5 | Schedule the job without Test Run | Select Settle and then choose Schedule. |  |  |
| 6 | Result Check | In the Application Jobs screen, find the job you created. You may need to wait several minutes and refresh to see the results after the job status is changed to finished.Choose Results. | The detailed log is displayed in the Document (ID, XXXXX) screen. You can find the corresponding document number and FI document number created. |  |

### Check Supplier Invoice List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can review the document created in the last step and get the generated consignment settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Fiori Launchpad tile | Open the Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the document | On the Supplier Invoices List screen, enter the following values, then choose Go:Invoicing Party : 33300001Company Code: 3310 | Invoices list is displayed. |  |
| 4 | Go to the invoice detailed page | Choose the invoice you created, whose Entry Type is Consignment. | The screen will be navigated to the Supplier Invoice detailed page. |  |
| 5 | Display the document | On the Supplier Invoice screen, go to the Output tab. In the Output Details table, find the line with Output Type of CONSIGNMENT_SETTLEMENT. Choose Display Document in the Preview column. | The document (in this case, Consignment Stock Accounting) is displayed. |  |
| 6 | Download the document | Download the document. | The document is downloaded to your local workspace. |  |
| 7 | Send Documents to Supplier | Send the downloaded document to the supplier as printed document, or by fax or by e-mail or via the Internet.The step is executed offline. | The document is sent to the supplier. |  |

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
> Flagged while digesting this document, not verified: Approve Purchase Order step cites app My Inbox - All Items as F5331 in the Overview Table but F0862 in the test procedure.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 25,684 chars in the whole document
