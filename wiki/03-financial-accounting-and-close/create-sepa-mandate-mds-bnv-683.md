---
id: 03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683
title: Create SEPA Mandate - MDS (BNV) (BNV_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition master data script (BNV) with test steps to create, display, list and manage SEPA direct debit mandates for customers."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/direct-debit-and-sepa-mandates]
aliases: [BNV_S4CLD2608_Master_Data_EN_XX]
keywords: [Direct Debit and SEPA Mandates, sepa mandates, sepa direct debit, create sepa mandates, display sepa mandates, manage sepa mandates, business roles, organizational units, customer master data, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-683
topic: 03-financial-accounting-and-close/direct-debit-and-sepa-mandates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create SEPA Mandate - MDS (BNV) (BNV_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Direct Debit and SEPA Mandates** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create SEPA Mandate - MDS (BNV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905026)

[2 Prerequisites 3](#_Toc233905027)

[2.1 System Access 3](#_Toc233905028)

[2.2 Roles 3](#_Toc233905029)

[2.3 Required Organizational Units 3](#_Toc233905030)

[2.4 Mandatory and Optional Master Data 4](#_Toc233905031)

[2.5 Main Parameters for Data Creation 4](#_Toc233905032)

[3 Overview Table 5](#_Toc233905033)

[4 Test Procedures 6](#_Toc233905034)

[4.1 Create SEPA Mandates 6](#_Toc233905035)

[4.2 Display SEPA Mandates 7](#_Toc233905036)

[4.3 Display SEPA Mandate Lists 8](#_Toc233905037)

[4.4 Manage SEPA Mandates 9](#_Toc233905038)

## Purpose

In this document you find a description of how to create Single Euro Payments Area (SEPA) mandate for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the SAP S/4HANA Cloud Public Edition appliance. Fields that are not relevant for the scope of SAP S/4HANA Cloud Public Edition as delivered by SAP Best Practices are not described in this document.

A SEPA mandate is completed by the debtor (a customer purchasing goods or services) to authorize the creditor (a retailer or service provider) to collect payments via SEPA Direct Debit. At the same time, the SEPA mandate includes the authorization of the debtor bank to pay these collections.

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
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |

### Required Organizational Units

Some segments of customer master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Mandate | Business partner | Customer number, IBAN and SWIFT/BIC | Only valid for European customers with SEPA direct debit. | Customer number: <your number |
| Mandate | Company Code | Company Code | Company code data can exist for every company code ID of your enterprise structure for which the SEPA mandate is used. | Company Code: your code |

### Mandatory and Optional Master Data

The following table gives an overview of optional and mandatory master data objects to be used in a profit center master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Customer number | Initial screen | Mandatory |  |
| Company Code | Initial screen | Mandatory |  |

### Main Parameters for Data Creation

This section describes some basic parameters that have impact on the behavior of a master record and are always required to create a SEPA mandate:

Company Code:

For example, XX10.

Business Partner - Customer:

For example, Customer number XX100003.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | SAP Fiori App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create SEPA Mandates](#unique_9) [page ] 6 | Accounts Receivable Accountant | Create SEPA Mandates (FSEPA_M1) | SEPA Mandate is created. |
| [Display SEPA Mandates](#unique_10) [page ] 7 | Accounts Receivable Accountant | Display SEPA Mandates (FSEPA_M3) | SEPA Mandate is displayed. |
| [Display SEPA Mandate Lists](#unique_11) [page ] 8 | Accounts Receivable Accountant | Display SEPA Mandate Lists (FSEPA_M4) | SEPA Mandate List is displayed. |
| [Manage SEPA Mandates](#unique_12) [page ] 9 | Accounts Receivable Accountant | Manage SEPA Mandates (F5158) | SEPA Mandate is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create SEPA Mandates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create SEPA Mandates (FSEPA_M1). | The app opens. |  |
| 3 | Switch Application | On the Create Mandate: Initial Screen screen, choose Switch Application. Select Financial Accounting in the Select Application dialog box and choose Continue. |  |  |
| 4 | Payer ID | In the Customer field, enter XX100003. |  |  |
| 5 | Payee ID | In the Paying Company Code field, enter XX10 and press Enter to continue.Note If a screen of mandates with an activated status displays, it means that those mandates are already created. Select a mandate and choose Continue to check and change the mandate. | The Create Mandate: Detail Screen screen displays. |  |
| 6 | Supplement Data | Choose Supplement Data. | Fields are automatically populated. |  |
| 7 | Basic Data | On the Basic Data tab, make the following entries:Status: EnteredB2B Mandate checkbox: SelectLocation of Sig: <Location>Signature Date: <Date> |  |  |
| 8 | Payer | On the Payer tab, in the Bank Data of Payer section, verify that the IBAN and SWIFT/BIC fields are populated.Note This data is part of your customer master data and should already be created and available. |  |  |
| 9 | Payment Recipient | On the Payment Recipient tab, make the following entry:Creditor ID: <Creditor ID> |  |  |
| 10 | Save Your Data | Save your entries. | The system message Mandate 0000000000## created displays. |  |

### Display SEPA Mandates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

A mandate already exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display SEPA Mandates (FSEPA_M3). | The app opens. |  |
| 3 | Payer ID | In the Customer field, enter XX100003. |  |  |
| 4 | Payee ID | In the Paying Company Code field, enter XX10 and press Enter to continue. | The Display Mandate: Detail Screen screen displays. |  |
| 5 | Navigation | Select the different tabs:Basic Data, Payer, and/or Payment Recipient. | The information displays. |  |
| 6 | Go Back | Choose Exit. |  |  |

### Display SEPA Mandate Lists

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

A mandate already exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display SEPA Mandate Lists (FSEPA_M4). | The app opens. |  |
| 3 | Choose Execute | If a dialog box displays, select Financial Accounting in the Select Application dialog box, and then choose Continue.If no dialog box displays, check the Technical Selections tab and verify that the Application field is set to Financial Accounting.Choose Execute. | The Mandates screen opens, displaying a list of existing mandates. |  |
| 4 | Select a Mandate | Select a Mandate Reference number. | The Change Mandates screen displays, listing details of the selected mandate. |  |
| 5 | Review | Although it is possible to change the mandate data when required, do not change any data, and just review the mandate data. |  |  |
| 6 | Exit | Choose Continue twice, or choose Cancel to exit. |  |  |

### Manage SEPA Mandates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

A mandate already exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage SEPA Mandates (F5158). | The app opens. |  |
| 3 | Choose Mandate | In the Application field, select Financial Accounting. |  |  |
| 4 | Choose Mandate | In the Paying Company Code field, enter XX10.Choose Go.Select the line you want to edit, and choose Edit. | The Change Mandate: Detail screen displays. |  |
| 5 | Review and Edit | Review and edit any of the available fields of the following tabs:Basic DataPayerPayment Recipient |  |  |
| 6 | Save Your Entries | Choose Save to save your entries. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684]]
- related-to :: [[03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686]]
- related-to :: [[03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682]]
- related-to :: [[03-financial-accounting-and-close/sepa-mds-bnv-685]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 14,031 chars in the whole document
