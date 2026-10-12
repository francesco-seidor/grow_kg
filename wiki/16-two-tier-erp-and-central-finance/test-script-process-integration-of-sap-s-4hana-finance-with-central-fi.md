---
id: 16-two-tier-erp-and-central-finance/test-script-process-integration-of-sap-s-4hana-finance-with-central-fi
title: "Test Script: Process Integration of SAP S/4HANA Finance with Central Finance (88K) (88K_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for 88K: replicating supplier invoices, reversals, changes and billing documents to Central Finance and verifying them."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/central-finance-replication]
aliases: [88K_S4CLD2608_BPD_EN_XX]
keywords: [Central Finance Replication from Subsidiaries, central finance, financial data replication, supplier invoices, invoice reversal, document change, billing documents, business roles, demo data, process integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/88K_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1247
topic: 16-two-tier-erp-and-central-finance/central-finance-replication
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Process Integration of SAP S/4HANA Finance with Central Finance (88K) (88K_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/88K_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Finance Replication from Subsidiaries** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Process Integration of SAP S/4HANA Finance with Central Finance (88K) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232792944)

[2 Prerequisites 3](#_Toc232792945)

[2.1 System Access 3](#_Toc232792946)

[2.2 Additional Manual Configuration 3](#_Toc232792947)

[2.3 Roles 3](#_Toc232792948)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232792949)

[3 Overview Table 5](#_Toc232792950)

[4 Test Procedures 6](#_Toc232792951)

[4.1 Post Supplier Invoice and check successful transfer to CFin system 6](#_Toc232792952)

[4.2 Reverse Supplier Invoice and check successful transfer to CFin system 7](#_Toc232792953)

[4.3 Document Change and check successful transfer to CFin system 9](#_Toc232792954)

[4.4 Processing of Existing Billing Document Requests 10](#_Toc232792955)

[5 Process Integration 12](#_Toc232792956)

[5.1 Preceding Processes 12](#_Toc232792957)

[5.2 Succeeding Processes 12](#_Toc232792958)

## Purpose

Overview

This scope item establishes an integration between SAP S/4HANA Cloud Public Edition and Central Finance, enabling you to replicate financial transaction data from SAP S/4HANA Cloud Public Edition to Central Finance. Data replication can be activated at the company code level in the SAP S/4HANA Cloud Public Edition system.

The integration uses Cloud Integration technologies (SAP Business Connector, Cloud Connector, WebSocket Remote Function Call) and the SAP Landscape Transformation Replication Server.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This document contains the basic testcases for the integration scenario: Central Finance Subsidiary Integration (cFin = Central Finance)

### System Access

|  |  |
| --- | --- |
|  | Details |
| Source System CC8/100 | DLAB landscape: Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SLT Server S6Q/000 | Test S/4 on Premise |
| Target System (cFin) QM7/822 | S/4 Corre Test system 2027 |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/7abddb9333e1916c20ec16ce2ea9d4e0)

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

To Author: Use this section if your scope item is for the On-Premise delivery. Remove the preceding section.After the migration to the DITA Content Management System, your user assistance developer will replace this section with a variable and tag it for the intended delivery.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log OnThe Log-on section is filled by the test administrator. Leave blank. |
| SAP_BR_AP_ACCOUNTANT |  | Accounts payable functions, including invoice processing, payment approvals, and vendor communications |  |  |
| SAP_BR_AR_ACCOUNTANT |  |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | CFP1 |  | The company code must be relevant for cFin and for the last test case relevant for cPay |
| Plant | CFP1 |  |  |
| Supplier | CFINSUPPL |  |  |
| Customer | CFINTEST1 |  |  |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |  |  |  |
| --- | --- | --- | --- |
| <Choose the appropriate entity: Process Step, Report or Item> | Business Role | App/Transaction | Expected Results |
| Post supplier invoice and check successful transfer to CFin system | SAP_BR_AP_ACCOUNTANT | App: Create Supplier Invoice | Documents replicated in cFin |
| Reverse supplier Invoice and check successful transfer to CFin system | SAP_BR_AP_ACCOUNTANT | App: Supplier Invoices List | Documents replicated in cFin |
| Document change and check successful transfer to CFin system | SAP_BR_AP_ACCOUNTANT | App: Create Supplier Invoice | Documents replicated in cFin |
| Processing of existing billing document requests | SAP_BR_AR_ACCOUNTANT | App: Create Billing Documents | Document replicated in cFin |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Supplier Invoice and check successful transfer to CFin system

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Post of supplier invoice and check the replication posting in the cFin system.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / CommentTo Author: Always leave empty. Column is only intended to be used by tester. |
| 1 | Log On | Log on to the source SAP Fiori launchpad as an AP_ACCOUNTANT. |  |  |
| 2 | Access App | Open the [Create Incoming Invoices](https://my300470.s4hana.ondemand.com/sap/bc/ui2/flp?sap-language=EN&sap-client=100#SupplierInvoice-createAdvanced?sap-ui-tech-hint=GUI) app. | Create Supplier Invoice app should be displayed |  |
| 3 | Create simple supplier invoice | Enter data likeTax data, for example, I0Cost center, for example, CPAY_CO1Incoming invoice, for example, G/L account 63001000Reference | Invoice document number |  |
| 4 | Get GL document number | Open tile: [Manage Journal Entries](https://my300470.s4hana.ondemand.com/sap/bc/ui2/flp?sap-language=EN&sap-client=100#AccountingDocument-manageV2&/?sap-iapp-state=ASV5YB69N14JCHLHJBDFMSQD42R0WMFQC8P6GZUR&sap-iapp-state--history=TASVYACMYDIFFY80EA0RVKU4H0FLCLQ8COP1F0OVO) and search via reference number | GL document number. The corresponding GL document is technically cleared. |  |
| 5 | Logon | Log on to the target SAP System |  |  |
| 6 | Start transaction FB03 | Press button ‘Document list’ |  |  |
| 7 | Choose “Dynamic Selections (Shift+F4) | Make the field “Document No in Sender System” available in the selection criteria and select via:Company CodePosting DateDocument No in Sender System | Get the replicated document related to step 3 |  |
| 8 | Compare the replicated document | Check that the “Sender*” fields in the document header contain the correct information from the source systemSenderLogSystemSender CoCodeSender Doc.NoSender FiscalYr | The sender fields shall contain the GL document number of step 4 |  |

### Reverse Supplier Invoice and check successful transfer to CFin system

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Reversal of supplier invoice and check the replication posting in the cFin system.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / CommentTo Author: Always leave empty. Column is only intended to be used by tester. |
| 1 | Log On | Log on to the source SAP Fiori launchpad as an AP_ACCOUNTANT. |  |  |
| 2 | Access App | Open the [Supplier Invoices List](https://my300470.s4hana.ondemand.com/sap/bc/ui2/flp?sap-language=EN&sap-client=100#SupplierInvoice-list1&/?sap-iapp-state--history=TAS8LUZFEORO659RS8S3R78NBRWPJ4OOUEA1EVTIH&sap-iapp-state=ASO6XA37RFUKAHA3DWUKRIZ3KZJ4O8WLVNS2X4RQ) app. |  |  |
| 3 | Search for a supplier invoice | Enter data such as the following:Document numberReference | The invoice should be displayed. |  |
| 4 | Press “Reverse” Button | Fill a reversal reason and confirm | The invoice document number should be reversed. |  |
| 5 | Logon | Log on to the target SAP System |  |  |
| 6 | Start transaction FB03 | Press button ‘Document list’ |  |  |
| 7 | Choose “Dynamic Selections (Shift+F4) | Make the field “Document No in Sender System” available in the selection criteria and select via:Company CodePosting DateDocument No in Sender System | Get the replicated document related to step 3 |  |
| 8 | Compare the replicated document | Check that the “Sender*” fields in the document header contain the correct information from the source systemSenderLogSystemSender CoCodeSender Doc.NoSender FiscalYr | The sender fields shall contain the GL document number of step 4 |  |
| 9 | Check reversal fields | Compare the “reversal” fields in the document header contain the correct information from the source systemReversal RefReversal Org.Reversal Doc.Reversed |  |  |

### Document Change and check successful transfer to CFin system

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Update of supplier invoice and check the replication posting in the cFin system.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / CommentTo Author: Always leave empty. Column is only intended to be used by tester. |
| 1 | Log On | Log on to the source SAP Fiori launchpad as an AP_ACCOUNTANT. |  |  |
| 2 | Access App | Open the [Create Incoming Invoices](https://my300470.s4hana.ondemand.com/sap/bc/ui2/flp?sap-language=EN&sap-client=100#SupplierInvoice-createAdvanced?sap-ui-tech-hint=GUI) app. | The app should open. |  |
| 3 | Create simple supplier invoice | Enter data like:Tax data, for example, I0Cost center, for example, CPAY_CO1Incoming invoice, for example, G/L account 63001000Reference | Invoice document number. The corresponding GL document is technically cleared. |  |
| 4 | Access App | Open tile: [Manage Journal Entries](https://my300470.s4hana.ondemand.com/sap/bc/ui2/flp?sap-language=EN&sap-client=100#AccountingDocument-manageV2&/?sap-iapp-state=ASV5YB69N14JCHLHJBDFMSQD42R0WMFQC8P6GZUR&sap-iapp-state--history=TASVYACMYDIFFY80EA0RVKU4H0FLCLQ8COP1F0OVO) and search for the invoice created in step 3 |  |  |
| 5 | Edit invoice | Press “Edit”, fill the ”Reference” information with some data and save the invoice |  |  |
| 6 | Logon | Log on to the target SAP System |  |  |
| 7 | Start transaction FB03 | Press button ‘Document list’ |  |  |
| 8 | Choose “Dynamic Selections (Shift+F4) | Make the field “Document No in Sender System” available in the selection criteria and select via:Company CodePosting DateDocument No in Sender System | Get the replicated document related to step 3/5 |  |
| 9 | Compare the replicated document | Check whether the reference information contain the correct information from the source system | The sender fields shall contain the same reference information of step 5 |  |

### Processing of Existing Billing Document Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Payment of customer invoice and check the replication posting in the cFin system.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / CommentTo Author: Always leave empty. Column is only intended to be used by tester. |
| 1 | Log On | Log on to the source SAP Fiori launchpad as an AR_ACCOUNTANT. |  |  |
| 2 | Access App | Open the [Create Outgoing Invoices](https://my300470.s4hana.ondemand.com/sap/bc/ui2/flp?sap-language=EN&sap-client=100#Customer-createOutgoingInvoice?sap-ui-tech-hint=GUI) app. | The Create Outgoing Invoices app opens. |  |
| 3 | Define Billing Settings | Enter data likeCustomerTax data, for example, 00Tax jurisdiction code, for example State CAOutgoing invoice, for example, G/L account 41090000Cost center, for example, CPAY_CO1 |  |  |
| 4 | Get document number | Check the document number and the reference text and note it down. | The system should have generated an invoice for billing. |  |
| 5 | Logon | Log on to the target SAP System |  |  |
| 6 | Start transaction FB03 | Press button Document List |  |  |
| 7 | Choose Dynamic Selections (Shift+F4) | Make the field Document No in Sender System available in the selection criteria and select via the Reference. | Get the replicated document related to step 4. |  |
| 8 | Compare replicated document | Check that the Sender fields in the document header contain the correct information from the source system:SenderLogSystemSender CoCodeSender Doc.NoSender FiscalYr | The sender fields shall contain the GL document number of step 7 |  |

## Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 1W4 - Subsidiary Integration of SAP S/4HANA Cloud to Central Finance | n/a |

### Succeeding Processes

No subsequent processes are required after completing the activities in this test script.

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
> Flagged while digesting this document, not verified: Template placeholders remain (e.g. 'To Author' notes, <choose the appropriate entity>); roles table lists role template names only, and system access lists customer-specific test systems.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-project-data-replication-to-central-finance-3w1-978]]
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-subsidiary-integration-of-sap-s-4hana-cloud-to-central-fin]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/88K_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 19,791 chars in the whole document
