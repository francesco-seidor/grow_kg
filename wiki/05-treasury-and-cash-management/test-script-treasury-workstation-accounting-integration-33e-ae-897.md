---
id: 05-treasury-and-cash-management/test-script-treasury-workstation-accounting-integration-33e-ae-897
title: "Test Script: Treasury Workstation Accounting Integration (33E_AE) (33E_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for 33E: replicating Treasury (TRM) accounting postings to a central accounting system (ECC or Private Edition) and verifying them."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-accounting-integration]
aliases: [33E_S4CLD2608_BPD_EN_AE]
keywords: [Treasury Workstation Accounting Integration, treasury accounting integration, treasury and risk management, accounting document replication, outbound message monitoring, communication connection, field mapping rules, business roles, demo data, test script]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33E_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-897
topic: 05-treasury-and-cash-management/treasury-accounting-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Treasury Workstation Accounting Integration (33E_AE) (33E_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33E_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Treasury Workstation Accounting Integration** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Treasury Workstation Accounting Integration (33E_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232851406)

[2 Prerequisites 3](#_Toc232851407)

[2.1 Additional Manual Configuration 3](#_Toc232851408)

[2.2 System Access 3](#_Toc232851409)

[2.3 Roles 3](#_Toc232851410)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232851411)

[2.5 Preliminary Steps 5](#_Toc232851412)

[2.5.1 Set up the Communication Connection 5](#_Toc232851413)

[2.5.2 Maintain Mapping Rule in the Central Accounting System 5](#_Toc232851414)

[3 Overview Table 6](#_Toc232851415)

[4 Test Procedures 7](#_Toc232851416)

[4.1 Process TRM Financial Transaction and Generate Accounting Document in Sending System 7](#_Toc232851417)

[4.2 Monitor Outbound Message in Sending System 7](#_Toc232851418)

[4.3 Monitor Inbound Message in Receiving System 9](#_Toc232851419)

[4.4 Check Accounting Document in Receiving System 10](#_Toc232851420)

## Purpose

Overview

This scenario fulfills the requirements for deploying Treasury and Risk Management in SAP S/4HANA Cloud Public Edition, while keeping the other Finance modules in an existing ERP environment. In such cases, Treasury and Risk Management manages the financial transactions and generates the posting in SAP S/4HANA Cloud Public Edition and then transfers the treasury accounting posting to the central accounting system.

Currently, the scenario only supports the SAP ECC system and the SAP S/4HANA Cloud Private Edition system as the central accounting system.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/553b53e7591460390b7e05ee0306ea16)

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP ECC system or SAP S/4HANA Cloud Public Edition system | As the central accounting system maintained by customer |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For the SAP ECC system, the test users with necessary authorization should be provided by customer during implementation project:

| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- | --- |
| Configuration Expert - Business Network Integration |  | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |

### Preliminary Steps

#### Set up the Communication Connection

Purpose

You need to set up the connection between SAP S/4HANA Cloud Public Edition system and the central accounting system for accounting documents replication.

Procedure

Please follow the steps in the Set-up instructions of communication scenario SAP_COM_0277 to enable the connectivity in SAP S/4HANA Cloud Public Edition system. Correspondingly, the central accounting system needs to be configured for inbound message.

Result

#### Maintain Mapping Rule in the Central Accounting System

Purpose

In this step, you set up the field mapping for accounting documents between SAP S/4HANA Cloud Public Edition system and the central accounting system if necessary.

For example, for the accounting document in SAP S/4HANA Cloud Public Edition system, the fields of G/L Account, Cost Center and Profit Center might be different from the central accounting system. You need to specify how the fields in the sender structure are mapped to fields in a receiver structure.

Procedure

SAP delivers the Converting Data Between Sender and Receiver tool, which enables you to convert and map field content from a sender fields to a receiver field. In this way, you can map organizational units, units of measurement, or yours and the customer-specific field content from one system to another. Please initialize and maintain the mapping rule for accounting document according to customer requirements.

To do this, you must perform the following steps in SAP ECC system, or the SAP S/4HANA Cloud Public Edition system:

1. Create the rule: The rules are defined by segment.
2. Maintain the rule: When you maintain rules, the conversion at the field level is determined according to defined rules.
3. Assign the rule to a message type: The assignment defines when the rule is used. This can be sender-specific, receiver-specific, and message type-specific.

Result

All the fields in transported structure mappings between SAP S/4HANA Cloud Public Edition system and the central accounting system are maintained.

## Overview Table

The scope item consists of several process steps in the table below.

| Process Step, Report or Item | Business Role | Transaction /APP | Expected Results |
| --- | --- | --- | --- |
| [Process TRM Financial Transaction and Generate Accounting Document in Sending System](#unique_10) [page ] 7 |  |  | The TRM financial transaction and the relevant posting is generated in S/4HANA Cloud |
| [Monitor Outbound Message in Sending System](#unique_11) [page ] 7 |  |  | The outbound message is generated and sent out correctly in Sending system |
| [Monitor Inbound Message in Receiving System](#unique_12) [page ] 9 |  |  | The inbound message carrying accounting document is imported in Receiving system |
| [Check Accounting Document in Receiving System](#unique_13) [page ] 10 |  |  | The accounting document is generated according to inbound message in receiving system |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Process TRM Financial Transaction and Generate Accounting Document in Sending System

Purpose

You process the TRM financial transactions and generate the relevant posting in S/4HANA Cloud, then the Treasury accounting documents would be transferred to the central accounting system automatically as replication.

Procedure

For TRM financial transaction creation and posting, please refer to the following test scripts for detail instructions. For testing purpose, you can follow one type of financial transaction.

- 1WV Debt and Investment Management
- 1X1 Foreign Currency Risk Management
- 1X3 Interest Rate Derivatives Management
- 2NZ Bank Guarantee Management
- 2UN Money Market Mutual Fund Management

To generate accounting documents, you can process the following steps in the above test scripts:

- Create TRM Contract; you only need to process one type of transaction for testing.
- Set the transaction settlement
- Generate and process payment request for principal payment, then post flows to the general ledger. For the incoming cash flow, you can directly post it to general ledger.

|  |
| --- |
| Note Please note down the generated FI document number for accounting document tracking. |

### Monitor Outbound Message in Sending System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, after assigning recipients to your user, you can use the Message Dashboard to monitor messages from related interface, analyze the causes of errors, and restart outbound messages.

Procedure

Step 1: Assign Recipients to You User

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Network Integration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Assign Recipients to Users (F2949). | The Assign Recipients to User screen is displayed. |  |
| 3 | Assign Recipients to User | On the left pane Users assigned to recipients, choose icon  , then enter the following data in the pop-up search bar and choose Add.Name/ID: for example, CONF_EXPERT_BUS_NET_INTThen enter the following data in the Assign Recipients dialog box, and choose Assign:Namespace: for example, /FINACRecipient Name: for example, FINAC_RECT_FIDCCP02_OUTMessage Type: for example, Application Error or Technical ErrorOverview: <select>Technical User: <select> | The recipient is assigned to user. |  |

Step 2: Message Monitor through Message Dashboard

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Network Integration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Message Dashboard - SAP AIF. | The Interface Monitor screen is displayed. |  |
| 3 | Select Interface | On the Interface Monitor screen, under Calendar Monitor, enter the date information in the search bar, and choose SearchThen under Result List, you can find the line item IDoc Accounting Document Outbound - FIDC.FID02/00001 under the AIF for Accounting - /FINAC. namespaceThe figures representing message in related status in the All Message, Warnings, Errors, and Successfully Processed columns. Choose one figure to investigate. | The Monitoring and Error Handling screen is displayed. |  |
| 4 | Check Message Detail and Error Handing | On the Monitoring and Error Handling screen, under Data Messages, expand the folder and select message item, then navigate to the details of the message under Details. |  |  |

### Monitor Inbound Message in Receiving System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the transferred inbound message in the receiving system. If the message is sent out successfully and the relevant configurations are maintained correctly, you should find the inbound message carrying TRM accounting document in the message list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the central accounting system via user with necessary authorization. |  |  |
| 2 | Access the IDoc list | Enter the transaction code in the Command field, and choose Enter.Transaction Code: WE02 | The IDoc List screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | On the IDoc List screen, enter the following data and choose Execute:Created On: <The message creation date in the previous step>> | The IDoc List is displayed. |  |
| 4 | Display the Message Details | On the Selected IDocs label, select the message item.Select the line item of message then choose the IDoc icon above. On the IDoc Display: 000000000000XXXX screen, you can browse detail through the segment page in the Data records folder. | If the selected message status is green, check the details below. Note down the Doc. No. and company code for the following accounting document check.If the selected message status is red, check the error message. Once the error is fixed, the other message needs to be re-created. |  |

### Check Accounting Document in Receiving System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the accounting document generated through transferred message in the receiving system, ensure the accounting document is identical to the sending system. If the mapping rule is maintained, the data of header and line item would be converted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the central accounting system via user with necessary authorization. |  |  |
| 2 | Access the IDoc list | Enter transaction code in the command field, and choose Enter.Transaction Code: FB03 | The Display Document: Initial Screen screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Display Document: Initial Screen screen, enter the following data and , choose Enter:Document Number: <the accounting document number noted in the previous step>Company Code: <the company code noted in the previous step> | The Display Document: Data Entry View is displayed. |  |
| 4 | Display the Accounting Document details | On the Display Document: Data Entry View screen, double click the line item of accounting document, you can find the details of the line item; Choose the Display Document Header icon, you can find the details of the document header. | From Header of Document Header, you can find the original accounting document info in the Reference Key field and the sending system information in the Log. System system. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-treasury-workstation-paym]]
- related-to :: [[05-treasury-and-cash-management/test-script-treasury-workstation-cash-integration-34p-ae-sap-s-4hana-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33E_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 19,875 chars in the whole document
