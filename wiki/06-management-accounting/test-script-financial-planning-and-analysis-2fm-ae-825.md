---
id: 06-management-accounting/test-script-financial-planning-and-analysis-2fm-ae-825
title: "Test Script: Financial Planning and Analysis (2FM_AE) (2FM_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2FM (AE): maintaining the predefined Financial Statement Version FPA1 and its semantic tags."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/financial-planning-statement-version]
aliases: [2FM_S4CLD2608_BPD_EN_AE]
keywords: [Financial Planning and Analysis Statement Version, financial statement version, semantic tags, financial planning and analysis, test scripts, business roles, master data, demo data, q system restrictions, 2FM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FM_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-825
topic: 06-management-accounting/financial-planning-statement-version
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Financial Planning and Analysis (2FM_AE) (2FM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Financial Planning and Analysis Statement Version** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Financial Planning and Analysis (2FM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849520)

[2 Prerequisites 3](#_Toc232849521)

[2.1 System Access 3](#_Toc232849522)

[2.2 Roles 3](#_Toc232849523)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232849524)

[3 Overview Table 5](#_Toc232849525)

[4 Test Procedures 6](#_Toc232849526)

[4.1 Maintain Financial Statement Version 6](#_Toc232849527)

[4.2 Maintain Semantic Tags for Financial Statement Version 7](#_Toc232849528)

## Purpose

Overview

This scope item allows SAP S/4HANA Cloud Public Edition customers to leverage a predefined Financial Statement Version (FSV) that supports financial planning and analysis across the enterprise.

The FSV supports financial planning and analysis within SAP Analytics Cloud and can be used within embedded analytics in SAP S/4HANA Cloud Public Edition.

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
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with this organization-specific master data, examples are provided in the following section.

Additional Default Values

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP ERP Central Component (ECC) system to find out which other material master data exists.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Financial Statement Version | FPA1 |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101001 |  |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

## Overview Table

The Financial Planning and Analysis scope item consists of one process step provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Financial Statement Version](#unique_7) [page ] 6 | Configuration Expert - Business Process Configuration | Manage Financial Statement Versions (OB58) | You maintained the financial statement version. |
| [Maintain Semantic Tags for Financial Statement Version](#unique_8) [page ] 7 | General Ledger Accountant | Assign Semantic Tags to Financial Statement Versions (FINSC_FAGL2SEMTA) | Semantic tags are maintained for the financial statement version. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Maintain Financial Statement Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you maintain the financial statement version.

|  |
| --- |
| Caution You can't save changes to the Financial Statement Version in a Q system with the Manage Financial Statement Version app. If you require to save changes to the Financial Statement Version in the Q system, open an incident to the service center using the component XX-S4C-SRV-CON. It's possible to change and save the changes to the Financial Statement Version in the P System. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Statement Versions (OB58). | The Change View "Financial Statement Versions": Overview view is displayed. |  |
| 3 | Select Financial Statement Version | Select the following financial statement version and choose Financial Statement Items:Financial Statement Version: FPA1 | The Change Financial Statement Version view is displayed. |  |
| 4 | Assign Accounts | Select the item where the account should be added and choose Assign Accounts.Note The account can't be in multiple items. | The Change Accounts entry view displays. |  |
| 5 | Enter Account | Make the following entries and choose Continue:Note The account can't be in multiple rows.From Acct: <your account>To Acct: <your account>D: SelectedC: Selected | The account is assigned to the financial statement. |  |
| 6 | Save | Save your entries. |  |  |
| 7 | Delete Accounts | Expand to the item to be maintained, select the account, and choose the Delete button. | The account is deleted from the financial statement. |  |
| 8 | Save | Save your entries. |  |  |

### Maintain Semantic Tags for Financial Statement Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you maintain semantic tags for the financial statement version.

|  |
| --- |
| Caution You can't save changes to the Financial Statement Version in a Q system with the Assign Semantic Tags to FSV app. If you require to save changes to the Financial Statement Version in the Q system, open an incident to the service center using the component XX-S4C-SRV-CON. It's possible to change and save the changes to the Financial Statement Version in the P System. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Assign Semantic Tags to Financial Statement Versions (FINSC_FAGL2SEMTA). | The Change View "Mapping of Financial Statement Versions to Semantic Tag" view is displayed. |  |
| 3 | Add Semantic Tag | Choose New Entries. |  |  |
| 4 | Select Semantic Tag Type | Select Assign Semantic Tag to FS Item and choose Continue. | The New Entries: Details of Added Entries view is displayed. |  |
| 5 | Assign Semantic Tag | Make the following entries and choose Save:FS Version: FPA1FS Item: 68Semantic Tag: OPEREXP | The system displays the message Data was saved. |  |
| 66 | Cancel | Choose Cancel. | The Change View "Mapping of Financial Statement Version to S..": Overview view displays the list of semantic tags. |  |
| 7 | Select Semantic Tag for FSV | Scroll and select a semantic tag relevant to your FSV.FS Vers: FPA1FS Item: 68 |  |  |
| 8 | Delete Semantic Tag | Choose Delete. | The semantic tag is deleted from the FSV. |  |
| 9 | Save | Save your entries. |  |  |

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
- see-also :: [[06-management-accounting/test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 13,837 chars in the whole document
