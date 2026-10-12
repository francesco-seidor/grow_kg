---
id: 08-sales-order-management/test-script-digital-payments-foundation-53v-1062
title: "Test Script: Digital Payments Foundation (53V) (53V_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 53V: adding and registering credit card data on a customer business partner via SAP digital payments in S/4HANA Cloud Public Edition 2608."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/digital-payments]
aliases: [53V_S4CLD2608_BPD_EN_XX]
keywords: [Digital Payments and Card Payments in Sales, digital payments, payment cards, business partner, customer master data, payment service provider, business roles, setup instructions, test scripts, 53V]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53V_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1062
topic: 08-sales-order-management/digital-payments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Digital Payments Foundation (53V) (53V_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53V_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Digital Payments and Card Payments in Sales** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Digital Payments Foundation (53V) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232840387)

[2 Prerequisites 3](#_Toc232840388)

[2.1 System Access 3](#_Toc232840389)

[2.2 Roles 3](#_Toc232840390)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232840391)

[2.4 Additional Manual Configuration 4](#_Toc232840392)

[3 Overview Table 5](#_Toc232840393)

[4 Test Procedures 6](#_Toc232840394)

[4.1 Add and Register Credit Card Data in Business Partner 6](#_Toc232840395)

## Purpose

Overview

SAP digital payments is a payment hub between payment service providers and SAP components, solutions, or applications that process incoming payment cards.

The scope item enables the integration between SAP S/4HANA Foundation and SAP digital payments, which allows you to maintain payment card master data in SAP S/4HANA Cloud.

Various payment service providers are supported.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, user, master data, organizational data, and other test data and business conditions.

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Additional Default Values

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP ECC system to find out which other material master data exists.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Customer | xx100010 |  | Replace xx with the two-digit value for your country (for example, 10 for DE, 17 for US, and so on) |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/fba2c4f533757bdfe902b19726f6a79d)

## Overview Table

This scope item consists of process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Add and Register Credit Card Data in Business Partner](#unique_8) [page ] 6 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) or Maintain Business Partner (BP) | You added a credit card to the customer. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Add and Register Credit Card Data in Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you add and register credit card data for an existing customer.

There are two procedure options presented below. Consult the following table to determine when you should use which procedure.

| Procedure Table | When to Use It | Comments |
| --- | --- | --- |
| Manage Customer Master Data | Cloud (Germany and U.S.) |  |
| Maintain Business Partner | Cloud (all other countries)On-Premise (all countries) |  |

Procedure – Manage Customer Master Data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A). | The Manage Customer Master Data view is displayed. |  |
| 3 | Search | Make the following entries and choose Go:Role: CustomerBusiness Partner: <customer number>, for example, xx100010Note Replace xx in the field above with the two-digit code for your country. | The customer is displayed in the Customers pane. |  |
| 4 | Customer Details | In the row for the customer, choose Details (>) at the right of the row. | The Customer view is displayed. The details of the customer are shown. |  |
| 5 | Edit Mode | Choose Edit. |  |  |
| 6 | Payment Cards | Choose the Payment Cards tab. |  |  |
| 7 | Add Payment Card | Choose Create.Note If you want to delete a card instead, select the card and choose Delete. | The Register New Payment Card dialog box is displayed. |  |
| 8 | Register New Payment Card | Make the following entries and choose Register:Card ID: <card ID> | The system displays a webpage where you enter the credit card data. |  |
| 9 | Enter Payment Card Information | On the webpage, make the following entries and choose Submit:Credit Card Type: <type of credit card>Card Number: <credit card number>Name on Card: <name on credit card>Valid to: <month and year of credit card validity>CVC: <credit card validation code; usually located on back of card> | The payment hub verifies the validity of the card details provided via a third-party payment service provider (PSP). The webpage displays a message that the payment card was successfully registered.The card details are added to the Customer Master. |  |
| 10 | Close Webpage | Choose Close. | You are returned to the Customer view. |  |
| 11 | Verify Payment Card | Verify the details added in the Payment Card pane.Make any additional entries as needed (for example, select Standard Card to set this card as the default). |  |  |
| 12 | Save | Choose Save. |  |  |

Procedure – Maintain Business Partner

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view is displayed. |  |
| 3 | Enter Details | In the left pane, make the following entries and choose Start:Find: Business PartnerBy: Customer NumberCustomer Number: <customer number>, for example, xx100010Note Replace xx in the field above with the two-digit code for your country. | The partner number is shown in the table below the fields. |  |
| 4 | Customer | Double-click the customer number in the Partner column. | The right pane displays the customer details. |  |
| 5 | Payment Transactions | Choose the Payment Transactions tab. |  |  |
| 6 | Payment Cards | In the Payment Cards pane, select the radio button for a blank row, enter a value in the Card ID field, and choose the Card Details button.Note If you want to delete a card, select the radio button for the card and choose the Delete button. | A new browser window opens to the payment service provider |  |
| 7 | Enter Payment Card Information | On the web page, make the following entries and choose Submit:Credit Card Type: <type of credit card>Card Number: <credit card number>Name on Card: <name on credit card>Valid to: <month and year of credit card validity>CVC: <credit card validation code; usually located on back of card> | The payment hub verifies the validity of the card details provided via a third-party payment service provider (PSP). The web page displays a message that the payment card was successfully registered.The card details are added to the Customer Master. |  |
| 8 | Close Web Page | Choose Close. | The Credit Card Create: Details dialog box is displayed. |  |
| 9 | Verify Payment Card | Verify the details in the dialog box.Make any additional entries as needed. If you want to set a card as the default card, select the Standard checkbox for the card.When done, choose Continue. |  |  |
| 10 | Save | Choose Save. |  |  |

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
- related-to :: [[08-sales-order-management/external-digital-payments-2lz-ae-test-script-833]]
- related-to :: [[08-sales-order-management/test-script-digital-payments-sales-1z1-ae-sap-s-4hana-cloud-public-edi]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-digital-payments-1s2-ae-7]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53V_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 14,074 chars in the whole document
