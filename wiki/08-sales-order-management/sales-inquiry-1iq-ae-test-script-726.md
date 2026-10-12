---
id: 08-sales-order-management/sales-inquiry-1iq-ae-test-script-726
title: Sales Inquiry (1IQ_AE) Test Script (1IQ_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1IQ (AE): create, change and reject a sales inquiry in Manage Sales Inquiries (F2370)."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-inquiry]
aliases: [1IQ_S4CLD2608_BPD_EN_AE]
keywords: [Sales Inquiries, sales inquiry changes, sales inquiry rejection, test scripts, sample master data, business roles, demo data, condition records, sales quotation, sell from stock]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-726
topic: 08-sales-order-management/sales-inquiry
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Inquiry (1IQ_AE) Test Script (1IQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Inquiries** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Inquiry (1IQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847202)

[2 Prerequisites 3](#_Toc232847203)

[2.1 System Access 3](#_Toc232847204)

[2.2 Roles 3](#_Toc232847205)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232847206)

[3 Preliminary Steps 6](#_Toc232847207)

[3.1 Create Condition Records (Optional) 6](#_Toc232847208)

[4 Overview Table 7](#_Toc232847209)

[5 Test Procedures 8](#_Toc232847210)

[5.1 Create Sales Inquiry 8](#_Toc232847211)

[5.2 Change Sales Inquiry 9](#_Toc232847212)

[5.3 Reject Sales Inquiry 10](#_Toc232847213)

[6 Appendix 11](#_Toc232847214)

[6.1 Process Integration 11](#_Toc232847215)

[6.1.1 Succeeding Processes 11](#_Toc232847216)

## Purpose

Overview

This scope item describes the process for a standard sales inquiry. It allows you to create, edit, and reject an inquiry. You can then create a quotation or sales order based on the inquiry.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpD | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ)(2EG)(BLP).See sections Business Conditions and Preliminary Steps. |
| Sold-to party | 33100003 | Domestic UAE Customer 3 | You can test the scope item using another domestic customer. |
| Ship-to party | 33100003 | Domestic UAE Customer 3 | Customer domestic 03 |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Material | SM0001 | Service Material 01 |  |
| Material | NS0002 | Non-Stock Material 02 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

## Preliminary Steps

### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

This scope item consists of the several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Inquiry](#unique_8) [page ] 8 | Internal Sales Representative | Manage Sales Inquiries (F2370) | The sales inquiry is created and printed. |
| [Change Sales Inquiry](#unique_9) [page ] 9 | Internal Sales Representative | Manage Sales Inquiries (F2370) | The sales inquiry is changed. |
| [Reject Sales Inquiry](#unique_10) [page ] 10 | Internal Sales Representative | Manage Sales Inquiries (F2370) | The sales inquiry is rejected. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Inquiry

Purpose

This activity enables you to enter a sales inquiry after a customer has requested one.

|  |
| --- |
| Note Once you have completed this activity:Option A: If the customer requests to change the sales inquiry, go to [Change Sales Inquiry](#unique_9) [page ] 9.Option B: If the customer accepts the sales inquiry, go to step Appendix [Process Integration](#unique_12) [page ] 11. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Inquiries (F2370). | The Manage Sales Inquires Initial screen displays. |  |
| 3 | Choose Create Inquiry | Choose Create Inquiry . | The Create Inquiry screen displays. |  |
| 4 | Enter Inquiry type | On the Create Inquiry screen, enter the following data and choose Continue:Inquiry Type: IN |  |  |
| 5 | Enter Inquiry Details | On the Create Inquiry: Overview screen, make the following entries and choose Enter:Sold-to party: 33100003Ship-to party: 33100003Customer Reference: <Reference Text>Material: TG11Order Quantity: 10 PC |  |  |
| 8 | Save | Choose Save. Take note of the inquiry number. |  |  |

### Change Sales Inquiry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity enables you to change sales inquiries field values to suit customers' needs, for example, to change the quantity listed in the inquiry.

|  |
| --- |
| Note Once you have completed this activity:Option A: If the customer rejects the sales inquiry, go to step [Reject Sales Inquiry](#unique_10) [page ] 10.Option B: If the customer accepts the sales inquiry, go to step Appendix - [Process Integration](#unique_12) [page ] 11. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Inquiries (F2370). | The Manage Sales Inquires Initial Screen displays. |  |
| 3 | Search for Sales Inquiry | Enter search term(s) in filter bar and choose Go. | Inquiry is displayed in result list. |  |
| 4 | Navigate to Sales Inquiry Screen | Click Inquiry number and choose Change Sales Inquiries. | The Change Inquiry xxx: Overview screen displays. |  |
| 5 | Change Inquiry | Make the following entry and choose Enter:Order Quantity: <Quantity> , for example: 5 PC |  |  |
| 6 | Save | Choose Save. | The quantity changes in the inquiry document. |  |

### Reject Sales Inquiry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity enables the customer to reject the sales inquiry. You can enter the reason for rejection in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Inquiries (F2370). | The Manage Sales Inquiries (F2370) initial screen displays. |  |
| 3 | Search For Sales Inquiry | Enter search term(s) in filter bar and choose Go. | Inquiry is displayed in result list. |  |
| 4 | Reject the Inquiry | Choose the Inquiry and choose Reject All Items. | Reject All Items dialog box displays. |  |
| 5 | Select Reason | Select an appropriate reason in the Reason for Rejection. And choose OK. | The sales inquiry updates with a reason for the rejection. You have now finished the activities in this document. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BDG – Sales Quotation (optional) | This scope item describes the sequence for a standard quotation process with a customer.Using the master data from this document, complete the following activities described in the Test Script:Sales Quotation (BDG).Create a sales order with reference using the sales inquiry number. |
| BD9- Sell from Stock (optional) | This scope item describes the sequence for a standard sales process (sell from stock) with a customer.Using the master data from this document, complete the following activities described in The test Script:Sell from Stock (BD9).Create a sales order with reference using the sales inquiry number. |

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
- see-also :: [[08-sales-order-management/verkaufspreiskondition-anlegen-sds-bet-538]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 15,909 chars in the whole document
