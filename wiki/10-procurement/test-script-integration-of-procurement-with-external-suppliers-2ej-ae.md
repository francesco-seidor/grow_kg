---
id: 10-procurement/test-script-integration-of-procurement-with-external-suppliers-2ej-ae
title: "Test Script: Integration of Procurement with External Suppliers (2EJ_AE) - SAP S/4HANA Cloud Public Edition (2EJ_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 2EJ_AE (UAE): API-based procurement and return exchange with external suppliers, S/4HANA-to-S/4HANA and third-party via Postman."
cluster: 10-procurement
tags: [kb/procurement, topic/business-network-purchase-to-pay]
aliases: [2EJ_S4CLD2608_BPD_EN_AE]
keywords: [Purchase-to-Pay Automation with SAP Business Network, external supplier integration, test prerequisites, purchase order creation, return purchase orders, supplier master data, supplier confirmation, third-party integration, supplier invoices, order confirmation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EJ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-814
topic: 10-procurement/business-network-purchase-to-pay
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Integration of Procurement with External Suppliers (2EJ_AE) - SAP S/4HANA Cloud Public Edition (2EJ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EJ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchase-to-Pay Automation with SAP Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integration of Procurement with External Suppliers (2EJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849290)

[2 Prerequisites 4](#_Toc232849291)

[2.1 Additional Manual Configuration 4](#_Toc232849292)

[2.2 System Access 4](#_Toc232849293)

[2.3 Roles 4](#_Toc232849294)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232849295)

[2.5 Business Conditions 6](#_Toc232849296)

[2.6 Preliminary Steps 6](#_Toc232849297)

[2.6.1 Opening New MM Period 6](#_Toc232849298)

[2.6.2 Enabling Supplier Master Data for Return and Shipping Processing 7](#_Toc232849299)

[3 Overview Table 9](#_Toc232849300)

[4 Test Procedures 10](#_Toc232849301)

[4.1 SAP S/4HANA Cloud Public Edition to SAP S/4HANA Cloud Public Edition Integration 10](#_Toc232849302)

[4.1.1 Create Purchase Order Manually 10](#_Toc232849303)

[4.1.2 Review Purchase Order 11](#_Toc232849304)

[4.1.3 Change Purchase Order (Optional) 12](#_Toc232849305)

[4.1.4 Review Order Confirmation (Optional) 13](#_Toc232849306)

[4.1.5 Review Shipping Notification (Optional) 14](#_Toc232849307)

[4.1.6 Review Supplier Invoice 15](#_Toc232849308)

[4.1.7 Create Return Purchase Order (Optional) 16](#_Toc232849309)

[4.1.8 Review Return Order Confirmation (Optional) 17](#_Toc232849310)

[4.1.9 Return Goods to Supplier (Optional) 18](#_Toc232849311)

[4.1.10 Display Credit Memo (Optional) 18](#_Toc232849312)

[4.2 SAP S/4HANA Cloud Public Edition to Third-Party Integration (Optional) 19](#_Toc232849313)

[4.2.1 Create Purchase Order Manually 19](#_Toc232849314)

[4.2.2 Review Purchase Order 20](#_Toc232849315)

[4.2.3 Change Purchase Order (Optional) 21](#_Toc232849316)

[4.2.4 Send Supplier Confirmation 22](#_Toc232849317)

[4.2.5 Review the Supplier Confirmation 23](#_Toc232849318)

## Purpose

Overview

For purchasing organizations whose suppliers use traditional data exchange protocols like electronic data interchange (EDI), or in Two-Tier scenarios, where subsidiaries are on SAP S/4HANA Cloud Public Edition, this scope item provides a set of robust application programming interfaces (APIs) to simplify and automate exchanging procurement documents and their follow-on messages.

The following documents and functions are supported:

Procurement Process:

- Create, change, or cancel purchase order (outbound message)
- Receive purchase order confirmation (inbound message)
- Receive Advance Shipping Notification (ASN, inbound delivery message)
- Receive supplier invoice (inbound message)

Return Process:

- Create return purchase order (outbound message)
- Receive return purchase order confirmation (inbound message)
- Receive supplier invoice: Credit Memo (inbound message)

The Simple Object Access Protocol (SOAP) messaging protocol is supported.

You can enable B2B integration with the corresponding Integration of Sales with External Buyers (2EL) scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b20a5b9688168baeb48b973b8fef7457)

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and supplier, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master Data | Value | Master Data Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Supplier | 33300084 | Domestic UAE Supplier 84 |  |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. |  |
| No Serial no.; no batch no. | See [Business Conditions](#unique_7) [page ] 6 and [Opening New MM Period](#unique_8) [page ] 6 sections. |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions need to be met:

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. The posting period is up-to-date. |
|  | If you want to go through the steps described in chapter SAP S/4HANA Cloud Public Edition to Third Party Integration of this test script, you mandatorily need to install the Postman API client. |

### Preliminary Steps

#### Opening New MM Period

External Process

For this activity, run the following steps from the test script Create New Open MM Posting Period - MDS (BNZ) to close the MM period and open a new posting period.

#### Enabling Supplier Master Data for Return and Shipping Processing

For return order and shipping processing, the supplier master data must be configured. This activity describes how to enable the supplier.

|  |
| --- |
| Note The role SAP_BR_BUPA_MASTER_SPECIALIST is required to perform this activity. |

Procedure

1. Log on to the SAP Fiori launchpad using the role SAP_BR_BUPA_MASTER_SPECIALIST.
2. Open Maintain Business Partner.
3. Choose the Find tab.
4. Enter the following information and choose Start to search for the supplier:

| Field | Value |
| --- | --- |
| Find | Business Partner |
| By | Number |
| BusinessPartner | Enter your supplier number |

1. In the results list displayed in the table, double-click the row with your supplier number to maintain the corresponding master data.
2. Select the Customer role from the dropdown list Change in BP role at the top of the page.
3. Go to the tab Customer: General Data.
4. In section General Data, enter your supplier number in the Supplier field.
5. Save your changes.
6. If a warning message appears, close it by choosing No.
7. Go to the Sales and Distribution tab at the top of the page.
8. In the Sales Area section, enter the corresponding value for the field Sales Org.
9. In the field Distr. Channel, enter 10 and in the field Division, enter 00.
10. Navigate to the Shipping tab.
11. In section Shipping, in the Shipping Condition field, enter the value 01.
12. Go to the Billing tab and scroll down to the Output Tax table.
13. In the column Tax Classific., enter the value 1. Do this for all rows in the table.
14. Save your changes.
15. In the dropdown list Change in BP role at the top of the page, choose the role Supplier (defined).
16. Go to the Vendor: General Data tab.
17. In the General Data section, enter your supplier number in the field Customer.
18. Save your changes.
19. Navigate to the Purchasing tab at the top of the page.
20. In the Purchasing Data tab, scroll down to the section Additional Purchasing Data.
21. Activate the checkbox Returns Supplier.
22. If a small window with the title Customer Default Data pops up, confirm your action by choosing Okay.
23. Save your changes.
24. Exit the app.

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order Manually](#unique_11) [page ] 10 | Purchaser | Create Purchase Order - Advanced (ME21N) |  |
| [Review Purchase Order](#unique_12) [page ] 11 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Change Purchase Order (Optional)](#unique_13) [page ] 12 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Review Order Confirmation (Optional)](#unique_14) [page ] 13 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Review Shipping Notification (Optional)](#unique_15) [page ] 14 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Review Supplier Invoice](#unique_16) [page ] 15 | Accounts Payable Accountant | Supplier Invoices List (F1060A) |  |
| [Create Return Purchase Order (Optional)](#unique_17) [page ] 16 | Purchaser | Create Purchase Order - Advanced (ME21N) | Return purchase order is created and sent to the supplier system aytomatically. |
| [Review Return Order Confirmation (Optional)](#unique_18) [page ] 17 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Return Goods to Supplier (Optional)](#unique_19) [page ] 18 |  |  | Goods are physically transferred to the supplier. |
| [Display Credit Memo (Optional)](#unique_20) [page ] 18 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Supplier invoice is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Caution Before you start with the test, make sure that all activities mentioned in the section Preliminary Steps have been executed. |

### SAP S/4HANA Cloud Public Edition to SAP S/4HANA Cloud Public Edition Integration

#### Create Purchase Order Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you create a purchase order with Confirmation Control Key for inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser (Retail) role. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). |  |  |
| 3 | Enter Purchase Order Data | Enter the necessary data:Order type: NB Standard POSupplier: 33300084In the Header section, on the Org. Data tab:Purch. Org.:3310Purch. Group:001Company Code:3310In the Item Overview section:Material:TG0011Plant:3310Storage Location:331AQuantity:xNet Price:xIn the Item Detail section, on the Confirmations tab:Conf. Control:Confirmations |  |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | Your purchase order is created and the PO number is displayed. |  |

#### Review Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can review an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Open Manage Purchase Orders App | Open Manage Purchase Orders (F0842A). | A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Enter the purchase order number you want to review and choose Go.Select the row with the purchase order to open it. |  |  |

#### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Open the App | Open Manage Purchase Orders (F0842A). | A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Enter the purchase order number and choose Go.Select the row with the purchase order you want to change. |  |  |
| 4 | Change Purchase Order | Choose the Display/Change tab.Change certain field values of the purchase order. |  |  |
| 5 | Save Purchase Order | Choose Save to save the purchase order. | The purchase order is saved and the system displays a confirmation message. |  |

#### Review Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can review the order confirmation.

|  |
| --- |
| Note The following test steps can be processed only after the corresponding supplier system has sent an order confirmation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Open the App | Open Manage Purchase Orders (F0842A). | A list of already created purchase orders is displayed. |  |
| 3 | Open the Purchase Order | Enter the purchase order number and choose Go.Select the row with the purchase order to open it. |  |  |
| 4 | Review Order Confirmation | In the Item Detail section, choose the Confirmation tab.When the external confirmation from your supplier has been sent, you see an additional line in the table showing following information:CC (Confirm. Cat.): ABQuantity: xDelivery Date: x | The order confirmation is displayed. |  |

#### Review Shipping Notification (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can review the shipping notification.

|  |
| --- |
| Note The following test steps can be processed only after the supplier system has sent a shipping notification. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Open the App | Open Manage Purchase Orders (F0842A). | A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Enter the purchase order number and choose Go.Select the row with purchase order to open it. |  |  |
| 4 | Review Shipping Notification | In the Item Detail section, choose the Confirmation tab.When the external shipping notification from your supplier has been sent, you see an additional line in the table showing following information:CC (Confirm. Cat.): LAQuantity: xDelivery Date: x | The shipping notification is displayed. |  |

#### Review Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can review the supplier invoice.

|  |
| --- |
| Note The following test steps can be processed only after the corresponding supplier system has sent an invoice. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Accounts Payable Accountant role. |  |  |
| 2 | Open the App | Open Supplier Invoices List (F1060A). |  |  |
| 3 | Search for Supplier Invoice | On the Supplier Invoice List, search for your invoice and select it to open it. |  |  |

#### Create Return Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how to create a return purchase order for the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) |  |  |
| 3 | Enter Required Data for Return Order | Enter the necessary data:Order type: Enh.Ret.to SupplierSupplier:33300084In the Header section, on the Org. Data tab:Purch. Org.: 3310Purch. Group: 001Company Code: 3310In the Item Overview section:Material: TG0011Plant: 3310Storage Location: 331AQuantity: x |  |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | The return purchase order is created and automatically sent to the supplier system. |  |

#### Review Return Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you can review the return order confirmation.

|  |
| --- |
| Note The following test steps can be processed ONLY after the corresponding supplier system has sent an order confirmation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders (F0842A) screen is displayed.A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Search for purchase order xxx and choose Go.Select the row with purchase order xxx. |  |  |
| 4 | Review Order Confirmation | In the Item Detail section, choose the Returns tab.When the return order gets approved from your supplier and an external confirmation from your supplier has been sent, the field Supplier RMA Number should be updated with a value. | Supplier RMA Number has been updated with a value. |  |

#### Return Goods to Supplier (Optional)

Use

In this procedure, the goods to return are physically transferred to the supplier.

Prerequisites

The return order must have been approved by the supplier.

Procedure

Goods should be physically transferred, no message communication required.

#### Display Credit Memo (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, a supplier invoice is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Accounts Payable Accountant role. |  |  |
| 2 | Open Supplier Invoices List | Open Supplier Invoices List (F1060A). |  |  |
| 3 | Search for Supplier Invoice | On the Supplier Invoices List (F1060A), search for your invoice and select it to open it. |  |  |

### SAP S/4HANA Cloud Public Edition to Third-Party Integration (Optional)

#### Create Purchase Order Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you create a purchase order with Confirmation Control Key for inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser (Retail) role. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). |  |  |
| 3 | Enter Purchase Order Data | Enter the necessary data:Order type: NB Standard POSupplier: 33300084In the Header section, on the Org. Data tab:Purch. Org.:3310Purch. Group:001Company Code:3310In the Item Overview section:Material:TG0011Plant:3310Storage Location:331AQuantity:xNet Price:xIn the Item Detail section, on the Confirmations tab:Conf. Control:Confirmations |  |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | Your purchase order is created and the PO number is displayed. |  |

#### Review Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can review an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Open Manage Purchase Orders App | Open Manage Purchase Orders (F0842A). | A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Enter the purchase order number you want to review and choose Go.Select the row with the purchase order to open it. |  |  |

#### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. |  |  |
| 2 | Open the App | Open Manage Purchase Orders (F0842A). | A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Enter the purchase order number and choose Go.Select the row with the purchase order you want to change. |  |  |
| 4 | Change Purchase Order | Choose the Display/Change tab.Change certain field values of the purchase order. |  |  |
| 5 | Save Purchase Order | Choose Save to save the purchase order. | The purchase order is saved and the system displays a confirmation message. |  |

#### Send Supplier Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can send a supplier confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Open Postman Tool | Open the Postman API client. |  |  |
| 2 | Upload the Payload | Choose Import.Choose the JSON Payload from your local folder. | The payload file is opened. |  |
| 3 | Change the URL | Enter the new URL into the POST field.Note Use the URL from the Buyer System communication arrangement. |  |  |
| 4 | Change Value in Body | In the Message Header, change the following:Unique Message ID: Change the existing entryTime stamp: CurrentDate: According to purchase orderChoose Save.Select the row with the purchase order that you want to change. |  |  |
| 5 | Change the Field in Supplier Confirmation | In the Supplier Confirmation, change the following:SuplrConfExternalReference: Change the existing entryPurchaseOrderID: PO numberDate: According to POPurchaseOrderItem: Same as POSupplierConfirmationPrice: Same as POChoose Save. |  |  |
| 6 | Send the Supplier Confirmation | Note Before sending the confirmation, check all the files.Choose Save. |  |  |

#### Review the Supplier Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This step explains how you can review an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Open Manage Purchase Orders App | Open Manage Supplier Confirmation. |  |  |
| 3 | Select Purchase Order | Enter the purchase order number that you want to check and choose Go.Select the row with the purchase order to open it. |  |  |
| 4 | Supplier Confirmation | On the supplier confirmation screen, check the Confirmation Item. |  |  |
| 5 | Check the Status | Check that the status value is Accepted. |  |  |

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
- related-to :: [[10-procurement/test-script-automated-purchase-to-pay-with-sap-ariba-commerce-automati]]
- related-to :: [[10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business]]
- related-to :: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]
- related-to :: [[10-procurement/test-script-automation-of-source-to-pay-with-sap-business-network-42k]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EJ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 33,670 chars in the whole document
