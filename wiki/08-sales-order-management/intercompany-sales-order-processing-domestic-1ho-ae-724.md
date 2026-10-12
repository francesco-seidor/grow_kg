---
id: 08-sales-order-management/intercompany-sales-order-processing-domestic-1ho-ae-724
title: Intercompany Sales Order Processing – Domestic (1HO_AE) (1HO_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1HO_AE: domestic intercompany trading-goods sales order to AP journal entry, UAE sample data."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/intercompany-sales-domestic-and-international]
aliases: [1HO_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Sales Order Processing (Domestic and…, intercompany sales order, test script, sales order creation, outbound delivery, customer invoice, intercompany billing, picking, goods issue, ap journal entry]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1HO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-724
topic: 08-sales-order-management/intercompany-sales-domestic-and-international
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intercompany Sales Order Processing – Domestic (1HO_AE) (1HO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1HO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Sales Order Processing (Domestic and International)** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Sales Order Processing – Domestic (1HO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847149)

[2 Prerequisites 3](#_Toc232847150)

[2.1 System Access 3](#_Toc232847151)

[2.2 Roles 3](#_Toc232847152)

[2.3 Master Data and Organizational Data, and Other Data 4](#_Toc232847153)

[2.4 Additional Manual Configuration 5](#_Toc232847154)

[2.5 Business Conditions 5](#_Toc232847155)

[2.6 Preliminary Steps 5](#_Toc232847156)

[2.6.1 Create Condition Records (Optional) 7](#_Toc232847157)

[3 Overview Table 8](#_Toc232847158)

[4 Test Procedures 9](#_Toc232847159)

[4.1 Create Sales Order 9](#_Toc232847160)

[4.2 Process Sales Order Approval (Optional) 10](#_Toc232847161)

[4.3 Create Delivery 10](#_Toc232847162)

[4.4 Packing (Optional) 11](#_Toc232847163)

[4.5 Perform Picking 12](#_Toc232847164)

[4.6 Post Goods Issue 13](#_Toc232847165)

[4.7 Create F2 Invoice 14](#_Toc232847166)

[4.8 Create Intercompany Invoice 15](#_Toc232847167)

[4.9 Display AP Journal Entry 16](#_Toc232847168)

## Purpose

Overview

This scope item describes the entire process sequence for the intercompany process for trading goods. The intercompany process described here is only applicable to the following scenario: Both ordering and delivering company are in the same country/region.

A company has an affiliate company that delivers trading goods directly to a customer in intercompany sales. The affiliate company posts the intercompany billing document to the ordering company. The intercompany invoice is also posted automatically to the accounts payables of the ordering company.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data and Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Material which is used in order to be provided to the customer. |
| Customer | 33100001 | Domestic UAE Customer 1 |  |
| Inter-company Payer | 33403310 | Customer in company code 3320 AE representing the ordering United Arab Emirates company (company code 3310) |  |
| Supplier | 33403320 | Supplier in company code 3310 AE representing the delivering AE company (company code 3320) |  |
| Sales Organization | 3310 | Sales organization in company 3310 |  |
| Sales Organization | 3330 | Dom. Sales Org | Flex.Org App or Set Up Organizational (CBC) extension |
| Distribution Channel | 10 | Direct Sales |  |
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

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/aeb43f844eddc7036979d28f89fc6742)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in company codes 3310 and 3320 respectively. |

|  |
| --- |
| Note Before you start the testing, please make sure the setup in the scope item-specific workaround document [1HO Set-Up Instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/1HO_Set-Up_EN_XX.pdf) has been completed. |

### Preliminary Steps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Please refer to test script Create New Open MM Posting Period - MDS (BNZ) to open new posting period in company codes 3310 and 3320.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material: TG12Plant: <Supply Plant in affiliate company>, for example, 3310 | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select an initial stock to add, for example:Storage Location: <Storage Location in the affiliate supply plant>, for example, 331A | A dialog displays.The Storage Location, Stock Type and Current Quantity display according to the previous step entries. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: for example, <today's date>Posting Date: <today's date>Stock Change: Initial EntryQuantity: enter a number, for example, <100> | Material document XXX created. The stock is added. |  |
| 6 | Post Initial Stock in the Plant 3330 | Repeat above steps to post initial stock in the plant 3330 for material TG12:Material: TG12Plant: Supply Plant in the affiliate company, for example, 3330Storage Location: Storage Location in the affiliate supply plant, for example: 333ADocument Date: <today's date>Posting Date: <today's date>Stock Change: Initial EntryQuantity: enter a number, for example, <100> |  |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

The scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction\App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_11) [page ] 9 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Process Sales Order Approval (Optional)](#unique_12) [page ] 10 |  |  | Sales order is approved. |
| [Create Delivery](#unique_13) [page ] 10 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Perform Picking](#unique_14) [page ] 12 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Material is picked. |
| [Post Goods Issue](#unique_15) [page ] 13 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | The goods issue is posted. |
| [Create F2 Invoice](#unique_16) [page ] 14 | Billing Clerk | Create Billing Documents (F0798) | Billing with F2 type is created. |
| [Create Intercompany Invoice](#unique_17) [page ] 15 | Billing Clerk | Create Billing Documents (F0798) | Billing with IV type is created. |
| [Display AP Journal Entry](#unique_18) [page ] 16 | General Ledger Accountant | Manage Journal Entries (F0717A) | AP journal entry displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales order in ordering company, then goods will be directly delivered to the customer from affiliate company/plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order VA01 . | The Sales Order screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 630Choose Continue. | The Create Sales Order: Overview screen displays. |  |
| 5 | Enter Order Details | Sold-to Party: 33100001Cust. Reference: PO numberDeliver. Plant: <Delivery Plant in delivering company code>, for example, 3330Material: <material number>, for example, TG12Order Quantity : <quantity>, for example, 10 |  |  |
| 6 | Check Intercompany Pricing Condition Type | Select the line item and choose the Item Conditions icon.Check intercompany pricing condition type exists, for example, PI02 Inter-company %. |  |  |
| 7 | Save | Choose Save. | A sales order is created.Make a note of the sales order number. |  |

### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This process step shows you how to review the sales orders that might be approved.

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

This process step shows you how to create the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries-From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3330Planned Creation Date: <delivery selection date>Order: <sales order number created previously> | The Create Delivery: Overview screen displays. |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

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

This process step shows you how to take goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Delivery Monitor screen, choose For Picking. |  |  |
| 4 | Enter Shipping Point | On the Manage Outbound Deliveries screen, make the following entry:Shipping Point: 3330 |  |  |
| 5 | Select the Only Picking without WM Checkbox and Choose Execute | Choose Only Picking without WM.Choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Enter Picked Quantity | On the Outbound Delivery xxx Change: Overview screen, choose Picking and enter quantity in the Picked Qty field.Picking status is set to Completely processed if picked quantity and delivery quantity are equal.Deviations in quantity can be solved by the Copy Picked Quantity as Delivery Quantity function. |  |  |
| 8 | Save Document | Choose Save. |  |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entries and choose Execute.Shipping Point: 3330 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue.Select today’s date in the dialog box.Choose Continue. | The goods issue is posted. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen is displayed. |  |
| 3 | Issue Delivery Output | Choose For Goods Issue.Make the following entries and choose Execute.Shipping Point: 3330On the Display Outbound Delivery, enter the Delivery number, and choose Continue.On the Delivery xxxxxxxxxxx Display: Overview:choose More > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_NOTE, and choose Display PDF Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Create F2 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to creater customer invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example, current date.Enter Delivery Number.Choose Enter. |  |  |
| 4 | Save | Choose Save. | The F2 billing document is created. |  |
| 5 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

Financial Posting

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Domestic AE Customer 1 | 41000000 Revenue Domestic – Product22000000 Output Tax (MWS) | none |

### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create intercompany invoice in delivery company code. In background, AP journaleEntry is generated in ordering company via IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Create Intercompany Billing Document | Choose billing type Invoice (IV) and maintain billing date, for example, the current date.Input Delivery Number.Choose Enter. |  |  |
| 4 | Save | Choose Save. | The IV billing document is created. Note down the billing document number for further use.Note To check the details of the IDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the customer facing document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). |  |

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 company code 3310 as a business partner | 41001500 Revenue Affiliate - Product22000000 Output Tax (MWS) | none |

### Display AP Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the account payable journal entries generated by IV invoice IDOC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP journal Entry by Referencing IV Invoice | Make the following entry and choose Go:Original Reference Document: 00 + <Intercompany invoice number generated in previous step> | AP journal entry number displays. |  |
| 5 | Display AP Journal Entry | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP journal entry displays. |  |

|  |
| --- |
| Note Besides the scenario described in the [Post Goods Issue](#unique_15) [page ] 13 section, opposite-direction transactions can be supported: The customer orders goods from company code 3320. Company code 3310 directly delivers goods to the customer as a supplier of 3320. Two invoices are generated: one is the customer invoice to company code 3320, the other is the intercompany invoice that company code 3320 pays to company code 3310. |

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
- related-to :: [[08-sales-order-management/intercompany-sales-order-processing-international-1mx-ae-741]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1HO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,671 chars in the whole document
