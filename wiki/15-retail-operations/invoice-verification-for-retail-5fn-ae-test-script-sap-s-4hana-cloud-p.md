---
id: 15-retail-operations/invoice-verification-for-retail-5fn-ae-test-script-sap-s-4hana-cloud-p
title: "Invoice Verification for Retail (5FN_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FN_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP S/4HANA Cloud scope item 5FN_AE: retail supplier invoice verification (three-way matching), incl. blocked, freight, background, API cases."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/retail-procurement-and-invoice-verification]
aliases: [5FN_S4CLD2608_BPD_EN_AE]
keywords: ["Retail Procurement, Invoice Verification and Supplier…", supplier invoice verification, three-way matching, test procedures, blocked invoices, freight condition, background invoice verification, supplier invoice api, purchase order creation, inbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FN_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1083
topic: 15-retail-operations/retail-procurement-and-invoice-verification
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Invoice Verification for Retail (5FN_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Retail Procurement, Invoice Verification and Supplier Returns** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Invoice Verification for Retail (5FN_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Invoice Verification for Retail (5FN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856677)

[2 Prerequisites 4](#_Toc232856678)

[2.1 System Access 4](#_Toc232856679)

[2.2 Roles 4](#_Toc232856680)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856681)

[2.4 Additional Manual Configuration 5](#_Toc232856682)

[2.5 Business Conditions 6](#_Toc232856683)

[2.6 Preliminary Steps 6](#_Toc232856684)

[2.6.1 Create Purchase Order (Without Freight Condition) 6](#_Toc232856685)

[2.6.2 Create Purchase Order (With Freight Condition) 8](#_Toc232856686)

[2.6.3 Create Inbound Delivery 9](#_Toc232856687)

[2.6.4 Confirm Quantities for Putaway 10](#_Toc232856688)

[2.6.5 Post Goods Receipt for Inbound Delivery 11](#_Toc232856689)

[3 Overview Table 12](#_Toc232856690)

[4 Test Procedures 14](#_Toc232856691)

[4.1 Create Supplier Invoice using Purchase Order 14](#_Toc232856692)

[4.2 Display Supplier Invoice 16](#_Toc232856693)

[4.3 Create Supplier Invoice using Purchase Order (Where Amount is Incorrect in Purchase Order) (Optional) 16](#_Toc232856694)

[4.4 Release Blocked Invoice (Optional) 18](#_Toc232856695)

[4.5 Display Supplier Invoice (Optional) 19](#_Toc232856696)

[4.6 Create Supplier Invoice Using Purchase Order (where Amount is Incorrect in Supplier Invoice) (Optional) 20](#_Toc232856697)

[4.7 Display Supplier Invoice (Optional) 22](#_Toc232856698)

[4.8 Create Supplier Invoice using Purchase Order with Freight Condition 22](#_Toc232856699)

[4.9 Display Supplier Invoice 24](#_Toc232856700)

[4.10 Create Invoice Verification in Background 25](#_Toc232856701)

[4.10.1 Enter Supplier Invoice for Background Verification 25](#_Toc232856702)

[4.10.2 Schedule Supplier Invoice Jobs 27](#_Toc232856703)

[4.11 Create Supplier Invoice Using API 28](#_Toc232856704)

[4.11.1 Create Supplier Invoice with reference to Purchase Order using API 28](#_Toc232856705)

[5 Appendix 31](#_Toc232856706)

[5.1 Process Integration 31](#_Toc232856707)

[5.1.1 Preceding Processes 31](#_Toc232856708)

[5.1.2 Succeeding Processes 31](#_Toc232856709)

[5.1.3 Create Supplier Invoice (Sample Payload) 31](#_Toc232856710)

## Purpose

Overview

Once goods are procured from a supplier and placed on the company’s premises through goods receipt, the retailer (recipient) must pay the supplier for the acquired goods. The amount to be paid and the material details are provided by the supplier in the form of an invoice document. Before paying to the supplier, the retailer must verify the invoice. This scope item covers the verification of the invoice before making a payment.

Before the procurement from external suppliers, the retailer carries out a logistics invoice verification. The content of invoice sent from the supplier is compared with the content of the two preceding main documents (the purchase order and the goods receipt). This process is also called three-way matching. The values of the articles and the quantities from the invoice are compared with those of the actual goods receipts. Prices and other conditions from the invoice are compared with those of the purchase order. When the values match, the invoice can be posted directly or after an optional release step. As a result, the respective financial accounts are posted to and handed over for payment. If there are discrepancies, you can decide either to accept or reject them, triggering the corresponding communication to the supplier.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This chapter summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable |  |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing |  |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Materials Management –Warehouse Execution |  |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Materials Management –Warehouse Execution |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Article (Material or Product) | R_1006 | My Best Frozen Strawberries | Single article |
| Article (Material or Product) | R_1003 | Chocolate | Generic article |
| Article (Material or Product) | R_1052 | My Best Blond Shampoo & Conditioner | Sales set |
| Article (Material or Product) | R_2007 | Chocolate Bar Display | Display article |
| Supplier | 33213002 | Retail Food Supplier AE |  |
| Supplier | 33213001 | Retail Non-Food Supplier AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC |  |
| Shipping Point | 3350 | SP DC 3350 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 50 | Distribution |  |
| Division | 00 | Product Division 00 |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/5d226b94ab33ec34dcb3ecf15e0ef0cc)

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 5FM - Procurement for Retail | To run through this scope item, purchase order must exist. |
| 5FU - Inbound Logistics for Distribution Centers | To run through this scope item, Inbound Delivery must exist. |
| 3I4 - Sales Pricing for Retail | Access Sequence for MM Pricing Condition type PPR0 should be switched to 0002 before creating purchase orders in the system, for details please refer to chapter in scope item (). |

### Preliminary Steps

|  |
| --- |
| Note In total five different business scenarios (four without freight condition and one with freight condition) are described in this document.To test this scope item, you need to create five purchase orders and inbound deliveries.You can find steps below to create purchase orders and inbound deliveries. Same data can be used to create multiple documents as well. |

#### Create Purchase Order (Without Freight Condition)

Use

To execute this scope item, you must create a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Purchaser (Retail). |  |  |
| 2 | Open Manage Purchase Orders App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order screen is displayed. |  |
| 3 | Navigate to Create Order Screen | In Create Purchase Order screen, select Create. | Purchase Orders screen is displayed. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data:Order type: NB Standard POSupplier: 33213002In Header section, on the Org. Data tab:Purch. Org.: 3310Purch. Group: 001Company Code: 3310In Item Overview section:Material: R_1006Plant: 3350Storage Location: 995AQuantity: xIn Item Detail section, on Confirmations tab:Conf. Control: Inbound DeliverySelect Enter |  |  |
| 5 | Delete Freight Condition | In case there is a value maintained for freight/Value 1 (FVA1) , you must delete the condition type FVA1.Go to purchase order Item Detail > Conditions Check if FVA1 exist.Select the FVA1 checkbox and select Delete. | Freight condition is deleted. |  |
| 6 | Note different Values | Go to purchase order Item Detail > Conditions > TTX1 > Tax .Go to purchase order Item Detail > Conditions > Total Value . | Make a note of tax amount and total value which will be used during invoice verification. |  |
| 7 | Note Tax Code | Go to purchase order Item Detail > Invoice > Tax Code . | Make a note of the tax code value which will be used during invoice verification. |  |
| 8 | Save Purchase Order | Select Save and when the purchase order number is displayed, make a note of it for further use. | Purchase order is created.Purchase order number is displayed. |  |

Result

Purchase order is created and purchase order number is generated.

|  |
| --- |
| Note Create five purchase orders using above data and use in steps [Create Supplier Invoice using Purchase Order](#unique_10) [page ] 14, [Create Supplier Invoice using Purchase Order (Where Amount is Incorrect in Purchase Order) (Optional)](#unique_11) [page ] 16, [Create Supplier Invoice Using Purchase Order (where Amount is Incorrect in Supplier Invoice) (Optional)](#unique_12) [page ] 20, and 6.1 respectively. |

#### Create Purchase Order (With Freight Condition)

Use

To execute this scope item, you must create a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Purchaser (Retail). |  |  |
| 2 | Open Manage Purchase Orders App | Open Create Purchase Order - Advanced (ME21N) app. | The Create Purchase Order - Advanced (ME21N) screen is displayed. |  |
| 3 | Navigate to Create Order Screen | On the Create Purchase Order screen, select Create. | Purchase Orders screen is displayed. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data:Order type: NB Standard POSupplier: 33213002In Header section, on the Org. Data tab:Purch. Org.: 3310Purch. Group: 3310Company Code: 3310In Item Overview section:Material: R_1006Plant: 3350Storage Location: 995AQuantity: xIn Item Detail section, on Confirmations tab:Conf. Control: Inbound DeliverySelectENTER |  |  |
| 5 | Add Freight conditon | Goto purchase order Item Details > Conditions, enter the following values:Condition Type :<FVA1>Amount: <Amount>Select Enter |  |  |
| 6 | Note different values | Goto purchase order Item Details > Conditions > FVA1Goto purchase order Item Details > Conditions > TTX1 > TaxGoto purchase order Item Details > Conditions > Total Value | Make a note of FVA1, tax amount and total value which will be used during invoice verification. |  |
| 7 | Note Tax Code | Goto purchase order Item Details > Invoice > Tax Code | Make a note of tax code value which will be used during invoice verification. |  |
| 8 | Save Purchase Order | Select Save and when the purchase order number is displayed, write it down for further use. | A new purchase order is created.Purchase order number is displayed. |  |

Result

Purchase order is created and purchase order number is generated.

|  |
| --- |
| Note This purchase order will be used in step [Create Supplier Invoice using Purchase Order with Freight Condition](#unique_14) [page ] 22. |

#### Create Inbound Delivery

Use

To execute this scope item, you must create inbound delivery using purchase order.

|  |
| --- |
| Note Repeat this step for all purchase orders one by one. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Receiving Specialist |  |  |
| 2 | Access the SAP Fiori App | Open Create Inbound Delivery (VL31N) app. | The Generation of Inbound Deliveries screen is displayed. |  |
| 3 | Create Inbound Delivery | On the Create Inbound Delivery (VL31N) app screen, enter the following:Supplier: 33213002Purchase Order: <Your purchase order document number>Select Continue. | Inbound Delivery Overview screen is displayed |  |
| 4 | Save Inbound Delivery document | Select Save. | Inbound delivery |  |

Result

Inbound delivery is created and inbound delivery number is generated.

#### Confirm Quantities for Putaway

Use

In this procedure, you confirm putaway quantity for inbound delivery based on the physical check of the goods arrived at distribution center.

|  |
| --- |
| Note Repeat this step for all inbound deliveries one by one. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Receiving Specialist |  |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery (VL32N) screen is displayed. |  |
| 3 | Enter Inbound Delivery | On the Change Inbound Delivery (VL32N) screen, enter the respective Inbound delivery number created in previous step and select Continue. |  |  |
| 4 | Enter Putaway Quantity | Specify or adjust the Putaway Quantity, if there is any difference in the delivery quantity and the quantity that arrived. |  |  |
| 5 | Save Inbound Delivery | Select Save. | Inbound delivery document with putaway quantity updated is saved. |  |

#### Post Goods Receipt for Inbound Delivery

Use

To execute this scope item, inbound delivery must exist.

|  |
| --- |
| Note Repeat this step for all purchase orders one by one. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Receiving Specialist |  |  |
| 2 | Access the SAP Fiori App | Open Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery (VL32N) screen is displayed. |  |
| 3 | Enter Inbound Delivery | On the Change Inbound Delivery (VL32N) screen, enter the respective Inbound delivery number created in previous step and select Continue. |  |  |
| 4 | Post Goods Receipt | Select Post Goods Receipt. | Goods Receipt is posted.A success message is displayed. |  |

Result

Goods receipt for inbound delivery is posted.

## Overview Table

This scope item consists of a process step that is listed in the table below:

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Supplier Invoice using Purchase Order](#unique_10) [page ] 14 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is generated. |
| [Display Supplier Invoice](#unique_19) [page ] 16 | Accounts Payable Accountant | Display Supplier Invoice - Advanced (MIR4) | Invoice and follow on documents are displayed. |
| [Create Supplier Invoice using Purchase Order (Where Amount is Incorrect in Purchase Order) (Optional)](#unique_11) [page ] 16 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is generated after correcting purchase order amount. |
| [Release Blocked Invoice (Optional)](#unique_20) [page ] 18 | Accounts Payable Accountant | Release Blocked Invoices (MRBR) | Blocked invoice is released. |
| [Display Supplier Invoice (Optional)](#unique_21) [page ] 19 | Accounts Payable Accountant | Display Supplier Invoice - Advanced (MIR4) | Invoice and follow on documents are displayed |
| [Create Supplier Invoice Using Purchase Order (where Amount is Incorrect in Supplier Invoice) (Optional)](#unique_12) [page ] 20 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is generated after correcting gross amount. |
| [Display Supplier Invoice (Optional)](#unique_22) [page ] 22 | Accounts Payable Accountant | Display Supplier Invoice - Advanced (MIR4) | Invoice and follow on documents is displayed |
| [Create Supplier Invoice using Purchase Order with Freight Condition](#unique_14) [page ] 22 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is generated |
| [Display Supplier Invoice](#unique_23) [page ] 24 | Accounts Payable Accountant | Display Supplier Invoice - Advanced (MIR4) | Invoice and follow on documents are displayed |
| [Enter Supplier Invoice for Background Verification](#unique_24) [page ] 25 | Accounts Payable Accountant | Enter Supplier Invoice for Background Verification (MIRA) | Invoice documents for verification in the background is created. |
| [Schedule Supplier Invoice Jobs](#unique_25) [page ] 27 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs (F1683) | Supplier invoice in background job is scheduled |
| [Create Supplier Invoice with reference to Purchase Order using API](#unique_26) [page ] 28 | Administrator (Retail) | Postman (Third-party testing tool) | Invoice is generated |

## Test Procedures

This chapter describes the procedure for the process step that belongs to this scope item.

When invoices are verified, there could be three possible outcomes:

- Verify invoice using purchase order
- Verify invoice using purchase order where invoice amount greater than purchase order amount (optional)
- Verify invoice using purchase order where invoice amount sent by supplier is higher (optional)
- Verify invoice using purchase order with freight condition

### Create Supplier Invoice using Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you verify invoice using purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO) app. | The Create Supplier Invoice - Advanced (MIRO) screen is displayed. |  |
| 3 | Navigate to Create Supplier Invoice - Advanced Screen | In the initial screen, enter Company Code as 3310Select Continue. |  |  |
| 4 | Provide Invoice Details | Select Invoice as TransactionNavigate to Basic Data and enter the values for the following fields:Invoice Date: <enter date>Reference: <enter reference>Amount: <enter amount>(Total value you had noted down while creating purchase order. Item Details > Conditions > Total Value)Tax Code : <enter tax code>(Tax code you have noted down in purchase order. Item Details > Invoice > Tax Code)Tax Amount: <enter tax amount>(Total value you had noted down while creating purchase order. Item Details > Conditions > TTX1 > Tax)Under the Details tab, select the corresponding document type in the Doc. Types field.In the current tab, select PO Reference tab, enter values for the following fields:Ref Document category : 1 Purchase Order/ Scheduling AgreementPurchasing Document : <enter purchase order number>Item type: <1 Goods/service items>Select Enter. |  |  |
| 5 | Check Balance | Look at Balance amount . | Balance in green indicates there is no issue between the purchase order and respective invoice. |  |
| 6 | Post Supplier Invoice | Select Post.Supplier invoice number displays. Make a note of it for further use. | Message is displayed as: Document number XXXXXXX created.Invoice verification is completed. |  |

|  |
| --- |
| Note In this example there is only one item available in purchase order. If there is more than one item exists in purchase order and supplier sends invoice for all the item with complete quantity, then total value and tax details can be retrieved by navigating through Purchase Order > Header > Conditions > Total Value and Purchase Order > Header > Conditions > TTX1 . |

### Display Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you display supplier invoice and follow on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Display Supplier Invoice - Advanced (MIR4) app. | The Display Supplier Invoice - Advanced (MIR4) screen is displayed. |  |
| 3 | Provide Invoice Details | Enter the values for the following fields:Invoice D ocument No. : < Enter invoice document number >Fiscal Year : <Enter year>Select Display Document | Invoice details is displayed. |  |
| 4 | Check Follow On Document | Select Follow-On Documents. | You can view the accounting document. |  |

### Create Supplier Invoice using Purchase Order (Where Amount is Incorrect in Purchase Order) (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step describes how to verify invoice when the amount in the invoice is not in sync (inaccuracy in the purchase order) with the amount in the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO) app. | The Create Supplier Invoice - Advanced (MIRO) screen is displayed. |  |
| 3 | Navigate to Create Supplier invoice – Advanced screen | In the initial screen, enter Company Code as 3310Select Continue. |  |  |
| 4 | Enter Invoice Data | Select Invoice as TransactionNavigate to Basic Data and enter values for the following fields:Invoice Date: <enter date>Reference: <enter reference>Under the Details tab, select the corresponding document type in the Doc. Types field.In the current tab, select PO Reference and enter values for the following fields:Ref Document category: 1 Purchase Order/ Scheduling AgreementPurchasing Document: <enter purchase order number>Item type: <1 Goods/service items>Select Enter.Amount: <enter amount in purchase order item > (higher amount then it is displayed, for example 10%)Select EnterNavigate to Basic Data and enter values for the following fields:Tax Code : <enter tax code>(Tax code you have noted down in purchase order. Item Details > Invoice> Tax Code)Calculate Tax: <Select checkbox>Tax amount field will be updated after selecting calculate tax field.Amount: <enter amount>Amount = Amount in Purchase Order line item + Tax AmountSelect Enter.Note Once you adjust the prices as mentioned above that is balance appears yellow. System will establish that the value invoiced exceeds the expected price by more than the tolerance for price variance.Select Messages to view this information. | Balance amount is displayed at the top of the screen. |  |
| 6 | Post Supplier Invoice | Select Post.When the supplier invoice number displays, note it for further use. | The system message is displayed with creation of document number for blocked payment. |  |

### Release Blocked Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can release blocked invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Release Blocked Invoices (MRBR) app. | The Release Blocked Invoices (MRBR) screen is displayed. |  |
| 3 | Selection of Blocked Invoice | Under Selection of Blocked Invoices, enter the necessary data in the following fields:Company Code: 3310Invoice Document : <enter invoice document number>Navigate to Processing, select Release ManuallyNavigate to Blocking Procedures, select Blocked Due to VariancesSelect Execute. |  |  |
| 4 | Release Blocked Invoice | Select invoice number, release invoice and save changes. | Invoice verification is complete. |  |

### Display Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you display supplier invoice and follow on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the App | Open Display Supplier Invoice - Advanced (MIR4) app. | The Display Supplier Invoice - Advanced (MIR4) screen is displayed. |  |
| 3 | Provide Invoice Details | Enter the values for the following fields:Invoice Document No.: <enter invoice document number>Fiscal Year: <Enter Year>Select Display Document. | Invoice details are displayed. |  |
| 4 | Check Follow On Document | Select Follow-On Documents. | A pop-up is opened and subsequent document is displayed. You can view the accounting document. |  |

### Create Supplier Invoice Using Purchase Order (where Amount is Incorrect in Supplier Invoice) (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step describes how to verify invoice when the amount in the invoice is not in sync (inaccuracies from the supplier) with the amount in the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859) app. | The Create Supplier Invoice (F0859) screen is displayed. |  |
| 3 | Enter General Data | Make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <enter amount>(Total value you had noted down while creating purchase order. Item Details > Conditions > Total Value > )Currency: EURInvoice Date: <Today>Posting Date: <Today>Reference:<enter reference>Invoicing Party:33213002 | The New Supplier Invoice screen is displayed. |  |
| 4 | Enter Purchase Order References | In Purchasing Document Reference section, add the references.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <enter purchase order number> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Reduce Invoice | Choose the item to navigate to the details screen.Choose the Reduce Invoice button in the bottom.On the Reduce Invoice dialog box, make the following entries:Amount from Supplier:<enter amount>the net amount is proposed- overwrite with the gross invoice amount entered beforeChoose OK to close the dialog box and choose Back to Supplier Invoice. | Supplier Invoice amount is reduced |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate .You can check the simulation results in the Simulation Overview and Simulation Details area. | The supplier invoice is simulated. |  |
| 9 | Post Invoice | Choose Post . | A pop-up appears indicating document number is created.Invoice verification is complete. |  |

### Display Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you display supplier invoice and follow on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the App | Open Display Supplier Invoice - Advanced (MIR4) app. | The Display Supplier Invoice - Advanced (MIR4) screen is displayed. |  |
| 3 | Provide Invoice Details | Enter the values for the following fields:Invoice Document No.: <enter invoice document number>Fiscal Year: <Enter Year>Select Display Document. | Invoice details are displayed. |  |
| 4 | Check Follow On Document | Select Follow-On Documents. | A list of documents is displayed. |  |

### Create Supplier Invoice using Purchase Order with Freight Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you verify invoice using purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO) app. | The Create Supplier Invoice - Advanced (MIRO) screen is displayed. |  |
| 3 | Navigate to Create Supplier Invoice - Advanced Screen | In the initial screen, enter Company Code as 3310.Select Continue. |  |  |
| 4 | Provide Invoice Details | Select Invoice as TransactionNavigate to Basic Data and enter the values for the following fields:Invoice Date: <enter date>Reference: <enter reference>Amount: <enter amount>(Total value you had noted down while creating purchase order. Item Details > Conditions > Total Value)Tax Code: <enter tax code>(Tax code you have noted down in purchase order. Item Details > Invoice > Tax Code)Tax Amount: <enter tax amount>(Total value you had noted down while creating purchase order. Item Details > Conditions > TTX1 > Tax)Under Details tab, select the corresponding document type in the Doc. Types field.In the current tab, select PO Reference and enter values for the following fields:Ref Document category: 1 Purchase Order/ Scheduling AgreementPurchasing Document: <enter purchase order number>Item type: <3 Goods/service items + planned delivery cost>Select Enter. |  |  |
| 5 | Check Balance | Look at Balance amount | Balance in green indicates there is no issue between the purchase order and respective invoice. |  |
| 6 | Post Supplier Invoice | Select PostWhen the supplier invoice number displays, make a note of it for further use. | A message appears indicating document number is created.Invoice verification is complete. |  |

|  |
| --- |
| Note In current example there is only one item available in purchase order, if there is more than one item exist in purchase order and supplier sends invoice for all the item with complete quantity then total value and tax details can be fetched from Purchase Order > Header > Conditions > FVA1 and Purchase Order > Header > Conditions > Total Value and Purchase Order > Header > Conditions > TTX1 . |

### Display Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you display supplier invoice and follow on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Display Supplier Invoice - Advanced (MIR4) app. | The Display Supplier Invoice - Advanced (MIR4) screen is displayed. |  |
| 3 | Provide Invoice Details | Enter the values for the following fields:Invoice Document No.: < enter invoice document number >Fiscal Year: <Enter Year>Select Display Document | Invoice details is displayed. |  |
| 4 | Check Follow On Document | Select Follow-On Documents. | You can view the accounting document. |  |

### Create Invoice Verification in Background

#### Enter Supplier Invoice for Background Verification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you enter header data such as the invoice amount, currency, tax information, and assignment for an invoice.

When you save the invoice, system creates invoice documents for verification in the background.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Enter Supplier Invoice for Background Verification (MIRA) app. | The Enter Supplier Invoice for Background Verification (MIRA) screen is displayed. |  |
| 3 | Navigate to Create Supplier Invoice - Adavcned Screen | In the initial screen, enter:Company Code: 3310Select Continue. |  |  |
| 4 | Provide Invoice Details | Select Invoice as TransactionNavigate to Basic Data and enter the values for the following fields:Invoice Date: <enter date>Reference: <enter reference>Amount: <enter amount>(Total value you had noted down while creating purchase order. Item Details > Conditions > Total Value)Tax Code : <enter tax code>(Tax code you have noted down in purchase order. Item Details > Invoice> Tax Code)Tax Amount: <enter tax amount>(Total value you had noted down while creating purchase order. Item Details > Conditions > TTX1> Tax).Under the Details tab, select the corresponding document type in the Doc. Types field.Ref Document category: 1 Purchase Order/ Scheduling AgreementFS Item type: <1 Goods/service items>Purchasing Document: <enter purchase order number>Select Enter. |  |  |
| 5 | Schedule Background Verification | Select Schedule Background Verification .When the supplier invoice number displays, note it for further use. | Message is displayed as: Document number XXXXXXX saved. |  |

|  |
| --- |
| Note In current example there is only one item available in purchase order, if there is more than one item exist in purchase order and supplier sends invoice for all the item with complete quantity then total value and tax details can be fetched from Purchase Order > Header > Conditions > Total Value and Purchase Order > > Header > Conditions > TTX1 . |

#### Schedule Supplier Invoice Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can schedule supplier invoice in a background job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant |  |  |
| 2 | Access the App | Open Schedule Supplier Invoice Jobs (F1683) app. | The Schedule Supplier Invoice Jobs (F1683) screen is displayed. |  |
| 3 | Navigate to Schedule Supplier Invoice Jos - Advanced Screen | In the initial screen, Select Create |  |  |
| 4 | Provide Details for Verification in Background | Under Template Selection enter the values for the following fields:Job Template: <Verification in Background>If some other job template is selected then select F4 and select verification in backgroundJob Name: <enter Job Name>Select Step 2 and under Scheduling Options enter the values for the following fields:Start Immediately : <Select>Recurrence Pattern: <Single Run>By default recurrence pattern is selected as single run, If you want to make to make any change select on Define Recurrence Pattern and change accordingly.Select Step 3 and under Parameters enter the values for the following fields:Invoice Document Number : <enter invoice document number noted in above step>Fiscal Year : <Fiscal year>Company Code: <Company code>Supplier: <Supplier>Posting Date: <Posting date>Posting Date Determination: <Only use posting date entered>Select Schedule, you will be navigated to Application log. |  |  |
| 5 | Check Log | Once status is Finished for the job name you mentioned above.Select Results and you can view further details.Under Result of Verified Invoices check if invoice posted correctly. | Check result. |  |

### Create Supplier Invoice Using API

#### Create Supplier Invoice with reference to Purchase Order using API

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can create supplier invoice using API in POSTMAN tool.

API Name : API_SUPPLIERINVOICE_PROCESS_SRV_0001

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Get the test tool Postman | Refer to Set Up Instructions if postman is not installed already. |  |  |
| 2 | Create Collection | Choose New > Collection at the top left of the screen and make the following entry:Name: <Enter the name for your identification>Choose Create. |  |  |
| 3 | Create Request | Find the collection just created on the left side of the screen. Choose three dots to see more options.Choose Add Request from the list and make the following entry:Request Name: <Enter the name for your identification> |  |  |
| 4 | Maintain Request | Choose the request just created on the left side of the screen under the collection and make the following entry for the details display on the right side of the screen.Select GET in Action dropdown listEnter Request URL: <Service URL>Choose Authorization tab, select TYPE: Basic Auth, maintain Username and Password.Choose Headers tab and add one line entry with the followings:Key: X-CSRF-TOKENValue: FetchChoose Send.In bottom section, go to Headers section and copy the Value generated against key X-CSRF-TOKEN.Go to top section again, choose Headers make below entry:Key: X-CSRF-TOKENValue: <Paste the value copied above>Choose Body tab, select the radio button of Raw and select JSON in the dropdown list.Fill in payload details, as described in the chapter [Create Supplier Invoice (Sample Payload)](#unique_28) [page ] 31.Choose Send. | <Service URL> can get after following setting up instruction guide for 5FN Technical User to be maintained for the Basic Auth. Please refer to setting up scope item 5FN for how to create communication user. | If there is timeout, you need to fetch CSRF-TOKEN again. |
| 5 | Post Request | Change the action from GET to POST.Choose Send on the upper right of the screen. | After successful posting, check the Status 201 Created in POSTMAN tool and in response Supplier Invoice document number is generated. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 5FU - Inbound Logistics for Distribution Centers | Purchase Order must be created and Inbound delivery to be posted. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Not applicable |  |

#### Create Supplier Invoice (Sample Payload)

{
  "CompanyCode": "1010",
  "DocumentDate": "2022-01-05T00:00",
  "PostingDate": "2022-01-05T00:00",
  "SupplierInvoiceIDByInvcgParty": "<ID>",
  "InvoicingParty": "33213002",
  "DocumentCurrency": "AED",
  "InvoiceGrossAmount": "<Amount>",//(Total value you had noted down while creating purchase order. Item Details > Conditions > Total Value)
  "TaxDeterminationDate": "2022-01-05T00:00",
  "TaxIsCalculatedAutomatically": true,
  "SupplierInvoiceIsCreditMemo": "",
  "to_SuplrInvcItemPurOrdRef": {
    "results": [
      {
        "SupplierInvoiceItem": "1",
        "PurchaseOrder": "<Purchase Order Number>",
        "PurchaseOrderItem": "10",
        "Plant": "3350",
        "DocumentCurrency": "AED",
        "ReferenceDocument": "<Goods Reciept Number>",
        "ReferenceDocumentFiscalYear": "<Year>",
        "ReferenceDocumentItem": "1",
        "SupplierInvoiceItemAmount": "<Amount in Purchase Order>",
        "PurchaseOrderQuantityUnit": "PC",
        "QuantityInPurchaseOrderUnit": "10",
        "QtyInPurchaseOrderPriceUnit": "10",
        "TaxCode": "V2"
      }
    ]
  }
}

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
> Flagged while digesting this document, not verified: Internal data inconsistency: master data and UI steps use company code 3310 and currency EUR (F0859 step), while the sample API payload uses CompanyCode 1010 and DocumentCurrency AED; plant 3350 and supplier 33213002 are the same in both.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[15-retail-operations/test-script-procurement-for-retail-5fm-ae-sap-s-4hana-cloud-public-edi]]
- related-to :: [[15-retail-operations/test-script-returns-to-supplier-for-retail-5fo-ae-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 48,617 chars in the whole document
