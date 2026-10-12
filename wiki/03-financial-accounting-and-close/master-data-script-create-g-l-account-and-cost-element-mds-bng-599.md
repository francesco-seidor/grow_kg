---
id: 03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599
title: "Master Data Script: Create G/L Account and Cost Element - MDS (BNG) (BNG_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (BNG) for creating a G/L account and cost element by copying an account, with prerequisites and test steps."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/chart-of-accounts-and-gl-accounts]
aliases: [BNG_S4CLD2608_Master_Data_EN_XX]
keywords: [Chart of Accounts YCOA and G/L Account Creation, g/l account master data, create g/l account, mandatory master data fields, account types and groups, cost elements, business roles, organizational units, sap central business configuration, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-599
topic: 03-financial-accounting-and-close/chart-of-accounts-and-gl-accounts
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create G/L Account and Cost Element - MDS (BNG) (BNG_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Chart of Accounts YCOA and G/L Account Creation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create G/L Account and Cost Element - MDS (BNG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904964)

[2 Prerequisites 3](#_Toc233904965)

[2.1 System Access 3](#_Toc233904966)

[2.2 Roles 3](#_Toc233904967)

[2.3 Required Organizational Units 3](#_Toc233904968)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904969)

[2.5 Main Parameters for Data Creation 6](#_Toc233904970)

[3 Overview Table 7](#_Toc233904971)

[4 Test Procedures 8](#_Toc233904972)

[4.1 Create G/L Account 8](#_Toc233904973)

## Purpose

A general ledger account master record contains information about the account that controls how business transactions are posted to it and how it is managed.

The general ledger in SAP provides a comprehensive and entirely up-to-date view of all assets, payables and receivables accounts, and is fully integrated with the other SAP modules.

Since all the SAP modules are integrated, some GL postings are generated automatically by the system in the background, for example the GR/IR account posting (Goods Received/Invoices Received) and inventory movement GL postings.

Some accounts are ‘open-item-managed’. They are used as a clearing account, so individual items can be cleared when, for example, incoming and outgoing payments and materials are processed.

Other accounts, for example the customer and vendor reconciliation accounts cannot be posted to directly, since they are only a reflection of the business partners in the sub-ledgers.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Required Organizational Units

Some segments of customer master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| G/L Account | Company CodeChart of AccountsControlling Area | See [Mandatory and Optional Master Data](#unique_6) [page ] 4 | Company code data can exist for every company code ID of your enterprise structure for which the GL account and cost element master record is used. | Company Code:____________Chart of Accounts____________Controlling Area____________ |

### Mandatory and Optional Master Data

Customer master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a customer master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Chart of Accounts | On the G/L account UI, you find the entry on the General tab, in the Control section. | Mandatory |  |
| G/L Account | On the G/L account UI, you find the entry on the Copy Account screen. | Mandatory |  |
| Description | On the G/L account UI, you find the entry on the Copy Account screen. | Mandatory |  |
| Account type | On the G/L account UI, you find the entry on the General tab, in the Control section. | Mandatory |  |
| Account Group | On the G/L account UI, you find the entry on the General tab, in the Control section. | Mandatory |  |
| Functional Area | On the G/L account UI, you find the entry on the General tab, in the Control section. | Optional | Use for P&amp;L accounts. |
| G/L Account Long Text | On the G/L account UI, you find the entry on the General tab, in the Description section. | Optional |  |
| Company Code checkbox | On the G/L account UI, you find the entry on the General tab, in the Definition in Company Code section. | Mandatory | Assign to one or several company codes. |
| Blocked for creation | On the G/L account UI, you find the entry on the General tab, in the Administration section. | Optional |  |
| Blocked for Posting | On the G/L account UI, you find the entry on the General tab, in the Administration section. | Optional |  |
| Blocked for planning | On the G/L account UI, you find the entry on the General tab, in the Administration section. | Optional |  |
| Marked for deletion | On the G/L account UI, you find the entry on the General tab, in the Administration section. | Optional |  |
| Account Currency | After creating a new G/L account, you find the details of Company Code in the Control Data > Account Control section. |  |  |
| Only Balance in Local Currency | After creating a new G/L account, you find the details of Company Code in the Control Data > Account Control section. | Optional |  |
| Tax Category | After creating a new G/L account, you find the details of Company Code in the Control Data > Account Control section. | Optional |  |
| Posting Without Tax Allowed | After creating a new G/L account, you find the details of Company Code in the Control Data > Account Control section. | Optional |  |
| Alternative Account Number | After creating a new G/L account, you find the details of Company Code in the Control Data > Account Control section. | Optional |  |
| Sort Key | After creating a new G/L account, you find the details of Company Code in the Control Data > Account Management section. | Optional |  |
| Controlling Area | After creating a new G/L account, you find the details of Company Code in the Control Data > Accounting Settings on Controlling Area section. | Mandatory | Optional for account type Balance Sheet Account |
| Cost Element Category | After creating a new G/L account, you find the details of Company Code in the Control Data > Accounting Settings on Controlling Area section. | Mandatory | Optional for account type Balance Sheet Account |
| Record Quantity | After creating a new G/L account, you find the details of Company Code in the Control Data > Accounting Settings on Controlling Area section. | Optional |  |
| Field Status Group | After creating a new G/L account, you find the details of Company Code in the Create/Bank/Interest > Control of Document Creation section. | Optional |  |
| Post Automatically Only | After creating a new G/L account, you find the details of Company Code in the Create/Bank/Interest > Control of Document Creation section. | Optional |  |
| Supplement Auto. Postings | After creating a new G/L account, you find the details of Company Code in the Create/Bank/Interest > Control of Document Creation section. | Optional |  |
| Planning Level | After creating a new G/L account, you find the details of Company Code in the Create/Bank/Interest > Bank/Financial Details section. | Optional |  |
| Relevant to Cash Flow | After creating a new G/L account, you find the details of Company Code in the Create/Bank/Interest > Bank/Financial Details section. | Optional |  |
| Blocked for Posting | After creating a new G/L account, you find the details of Company Code in the Administration. | Optional |  |
| Marked for Deletion | After creating a new G/L account, you find the details of Company Code in the Administration. | Optional |  |
| Translation text | On the G/L account UI, you find the entry in the Translation tab, Language Key section. | Optional | Translate descriptions into the required languages. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a customer master data record:

Account Type

- Balance sheet accounts
- Nonoperating expense or income
- Primary costs or revenue
- Secondary costs

Account Groups

- Reconciliation account ready for input
- Fixed assets accounts
- Income statement accounts
- Liquid funds accounts
- Materials management accounts
- G/L accounts (general)

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create G/L Account](#unique_9) [page ] 8 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create G/L Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When creating new G/L accounts, it is advisable to use an existing number range as a reference for new G/L accounts.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Open | Choose the arrow at the right of the column with the Chart of Accounts item. |  |  |
| 6 | Select Configuration Step | For the Manage G/L Account Master Data step, choose Configure. |  |  |
| 7 | Search for Your Account | Make the following entries and choose Go:View: Chart of Accounts ViewChart of Accounts: YCOA | The system displays a list of matching G/L accounts. |  |
| 8 | Choose G/L Account | Choose the G/L Account from the search results.Note Click the blue account number link. | The G/L Account Master Data screen appears. |  |
| 9 | Copy Account | Choose Copy. | The Copy of <G/L account number> screen displays. |  |
| 10 | Create Account | Make the following entries and choose OK:Account Number: <account number>Description in Maintenance Language (EN): <description>Group Account Number: <account number>Note This field is visible only when Consolidation is in the scope. | Data entered on the screen G/L Account Master Data displays. |  |
| 11 | Add Description | In the Basic Information section, make the following entries:Chart of Accounts: YCOAG/L Account Long Text:<description> |  |  |
| 12 | Assign Company Code | In the Company Code Assignment section, select a Company Code to assign it to the account. |  |  |
| 13 | Add Translations | In the Translation section, enter the short and long texts for all required languages. |  |  |
| 14 | Save Your Data | Choose Save. | The system confirms that account has been saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | Open Active Flexible Workflow |  |
| 2 | Access the SAP Fiori App | Go to the Business Processes Configuration app and search for the following activity: Manage G/L Account Master Data.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Search for Your Account | Make the following entries and choose Go:View: Chart of Accounts ViewChart of Accounts: YCOA | The system displays a list of matching G/L accounts. |  |
| 4 | Choose G/L Account | Choose the G/L Account from the search results.Note Click the blue account number link. | The G/L Account Master Data screen appears. |  |
| 5 | Copy Account | Choose Copy. | The Copy of <G/L account number> screen displays. |  |
| 6 | Create Account | Make the following entries and choose OK:Account Number: <account number>Description in Maintenance Language (EN): <description>Group Account Number: <account number>Note This field is visible only when Consolidation is in the scope. | Data entered on the screen G/L Account Master Data displays. |  |
| 7 | Add Description | In the Basic Information section, make the following entries:Chart of Accounts: YCOAG/L Account Long Text:<description> |  |  |
| 8 | Assign Company Code | In the Company Code Assignment section, select a Company Code to assign it to the account. |  |  |
| 9 | Add Translations | In the Translation section, enter the short and long texts for all required languages. |  |  |
| 10 | Save Your Data | Choose Save. | The system confirms that account has been saved successfully. |  |

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
- related-to :: [[03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602]]
- related-to :: [[03-financial-accounting-and-close/g-l-mds-bng-601]]
- related-to :: [[03-financial-accounting-and-close/mds-bng-603]]
- related-to :: [[03-financial-accounting-and-close/sachkonto-und-kostenart-anlegen-sds-bng-598]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 17,813 chars in the whole document
