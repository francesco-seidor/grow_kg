---
id: 08-sales-order-management/intercompany-sales-order-processing-international-1mx-ae-741
title: Intercompany Sales Order Processing – International (1MX_AE) (1MX_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script for scope item 1MX_AE: intercompany international sales from order through delivery, F2 and IV invoices to AP document (UAE)."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/intercompany-sales-domestic-and-international]
aliases: [1MX_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Sales Order Processing (Domestic and…, intercompany sales order processing, sales order creation, outbound delivery, picking, goods issue, intercompany billing, customer invoice, ap accounting document, initial stock]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MX_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-741
topic: 08-sales-order-management/intercompany-sales-domestic-and-international
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intercompany Sales Order Processing – International (1MX_AE) (1MX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Sales Order Processing (Domestic and International)** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Sales Order Processing – International (1MX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847406)

[2 Prerequisites 4](#_Toc232847407)

[2.1 System Access 4](#_Toc232847408)

[2.2 Roles 4](#_Toc232847409)

[2.3 Master Data and Organizational Data and Other Data 5](#_Toc232847410)

[2.4 Additional Manual Configuration 6](#_Toc232847411)

[2.5 Business Conditions 6](#_Toc232847412)

[2.6 Preliminary Steps 6](#_Toc232847413)

[2.6.1 Create Initial Stock 6](#_Toc232847414)

[2.6.2 Create Condition Records (Optional) 7](#_Toc232847415)

[3 Overview Table 8](#_Toc232847416)

[4 Test Procedures 9](#_Toc232847417)

[4.1 Create Sales Orders 9](#_Toc232847418)

[4.2 Process Sales Order Approval (Optional) 10](#_Toc232847419)

[4.3 Create Delivery 11](#_Toc232847420)

[4.4 Packing (Optional) 12](#_Toc232847421)

[4.5 Perform Picking 12](#_Toc232847422)

[4.6 Post Goods Issue 13](#_Toc232847423)

[4.7 Create F2 Invoice 14](#_Toc232847424)

[4.8 Create Intercompany Invoice 15](#_Toc232847425)

[4.9 Display AP Accounting Document 16](#_Toc232847426)

## Purpose

Overview

This scope item enables intercompany international transactions. As an example, the functionality is leveraged when a company (located in a specific country) sells products to a customer in a different country. The products are shipped from a separate location belonging to a company located in a different country.

This scope item provides capabilities to record the sale, define the pricing to apply to the transaction, and generate the Accounts Payable posting required.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data and Organizational Data and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Material which is used to be provided to the customer |
| End-Customer | 33100002 | Domestic UAE Customer 2 |  |
| Sales organization | 3310 | Company Code 3310Sales organization in ordering company |  |
| Sales organization | 1710 | Sales organization in supplying company |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e01614b98359049a6295c44af7945ebb)

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in company codes 1010, 1020, 1710, and 1720 respectively. |

### Preliminary Steps

#### Create Initial Stock

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entry and choose Enter:Material:TG12Supply Plant: <Supply Plant in the affiliate/foreign company> | The Stock overview for the material is displayed. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: <Storage Location in the affiliate/foreign supply plant>Unrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: todayPosting Date: todayStock Change: Initial EntryQuantity: enter a number | The system displays Material document XXX created. The stock has been added. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Orders](#unique_11) [page ] 9 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Process Sales Order Approval (Optional)](#unique_12) [page ] 10 |  |  | Sales order is approved. |
| [Create Delivery](#unique_13) [page ] 11 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries screen displays. |
| [Perform Picking](#unique_14) [page ] 12 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Material is picked. |
| [Post Goods Issue](#unique_15) [page ] 13 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | The Manage Outbound Deliveries screen displays. |
| [Create F2 Invoice](#unique_16) [page ] 14 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |
| [Create Intercompany Invoice](#unique_17) [page ] 15 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays |
| [Display AP Accounting Document](#unique_18) [page ] 16 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Manage Journal Entries screen displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order | Choose Create > Create Sales Order VA01 . | The Create Sales Documents screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries：Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330Choose Continue. | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Order Details | Make the following entries:Sold-to-Party: 33100002Cust. Reference: PO numberDeliver.Plant: <Delivery Plant in another company code>For example, 1710Material: Material Number, for example TG12Order Quantity : quantity, for example 10Choose Save. |  |  |
| 6 | Enter Tax Departure Country | On the top menu, choose Menu > Goto > Header > Billing . |  |  |
| 7 | Tax Country/Region | In the Billing section, input:Tax Departure Ctry/R:AE |  |  |
| 8 | Go Back | Choose Back. | The Create Standard Order: Overview screen displays. |  |
| 9 | Check Intercompany Pricing Condition Type | Select the line item and choose Conditions, check intercompany pricing condition type exists, for example PI02 Intercompany. |  |  |
| 10 | Save | Choose Save. | An intercompany sales order is created.Make a note of the sales order document number: ___________ |  |

### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the scope item Sell from Stock (BD9).

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveriesscreen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: <Shipping point of intercompany delivery plant>for example, 1710Planned Creation Date:Delivery selection dateOrder: <Sales order number created previously> | The Delivery Creation: Overviewscreen displays. |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5. | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on Deliveries tab. |  |

### Packing (Optional)

Purpose

You can execute packing for delivery items right in an outbound delivery.

Procedure

Complete all the activities described in the test script of Handling Unit Management (4MM) scope item.

### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3. | Open Outbound Delivery Monitor | Choose For Picking. |  |  |
| 4. | Enter Shipping Point | From the Outbound Deliveries for Picking screen, make the following entry:Shipping point: <Shipping point of intercompany delivery plant>for example, 1710 |  |  |
| 5. | Select the Only Picking without WM Checkbox | Select Only Picking without WM and choose Execute. |  |  |
| 6. | Select the Outbound Delivery | Select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7. | Input Picked Quantity | On the Outbound Delivery xxx Change: Overview screen, choose Picking, input quantity in field Picked Qty. | Picking status is set to Completely processed if picked quantity and delivery quantity is equal.Deviations in quantity can be solved by the function Copy Picked Quantity as Delivery Quantity. |  |
| 8. | Save Document | Choose Save. |  |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping point: <Shipping point of intercompany delivery plant>for example, 1710 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. | The goods issue is posted. |  |
| 5 | Choose Current Date | Choose current date from the dialog box. |  |  |
| 6 | Choose Continue | Choose Continue. |  |  |

### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you handle billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, input delivery number, then choose Enter. |  |  |
| 4 | Save | Choose Save. | F2 billing document is created. |  |

Financial Postings

| Material | Debit Accounts | Credit Accouts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33100002 Domestic customer 02 | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Document screen displays. |  |
| 3 | Create Intercompany Billing Document | Select IV Intercompany Billing as Billing Type, maintain Billing Date, for example current date, and input delivery number. |  |  |
| 4 | Press Enter | Press Enter. |  |  |
| 5 | Save | Choose Save.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitoring of the customer facing document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). | IV billing document is created. |  |

Financial Postings

| Material | Debit Accounts | Credit Accouts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 33403310 Company Code 3310 as Business | 41001500 Rev Affiliate- Prod | none |

### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you displays account payable journal entries generated by IV invoice IDoc.

Procedure

| Test Step | Test Step Name | Instruction | Expected Results | Pass/ Fail/ Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.Note If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00+ Intercompany invoice number generated in previous step>.Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

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
- related-to :: [[08-sales-order-management/extended-intercompany-processes-for-sales-1wo-ae-test-script-sap-s-4ha]]
- related-to :: [[08-sales-order-management/intercompany-sales-order-processing-domestic-1ho-ae-724]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 24,889 chars in the whole document
